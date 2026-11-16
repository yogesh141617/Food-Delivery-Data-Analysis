import pandas as pd
import mysql.connector

# ---------- 1. Load the CLEANED csv ----------
path = r"C:\\Users\\asus tuf  gaming\\Downloads\\food_delivery_orders_cleaned (4).csv"
df = pd.read_csv(path, keep_default_na=False, na_values=[""])
df.columns = df.columns.str.strip().str.lower()

cols = ["order_id", "customer_id", "restaurant_id", "driver_id", "order_date", "order_hour",
        "day_of_week", "is_weekend", "city", "delivery_area", "customer_age", "customer_type",
        "restaurant_type", "restaurant_primary_category", "restaurant_rating", "items_count",
        "subtotal", "discount_percent", "tax_amount", "service_fee", "delivery_fee", "order_total",
        "payment_method", "tip_amount", "distance_km", "weather", "traffic_level",
        "delivery_partner_experience_months", "delivery_partner_rating",
        "restaurant_preparation_time_minutes", "estimated_delivery_time_minutes",
        "actual_delivery_time_minutes", "late_delivery", "order_status",
        "cancellation_reason", "customer_rating", "order_time"]

missing = [c for c in cols if c not in df.columns]
extra = [c for c in df.columns if c not in cols]
print("Missing from file:", missing)
print("Extra in file:", extra)
if "order_time" in missing and len(extra) == 1:
    df = df.rename(columns={extra[0]: "order_time"})

df = df[cols]

# ---------- 2. Fix dates / times ----------
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
date_str = df["order_date"].dt.strftime("%Y-%m-%d")
df["order_time"] = pd.to_datetime(
    date_str.str.cat(df["order_time"].astype(str).str[-8:], sep=" "), errors="coerce")
df["order_date"] = date_str
df["order_time"] = df["order_time"].dt.strftime("%Y-%m-%d %H:%M:%S")

# NaN / NaT -> None so MySQL stores NULL
df = df.astype(object).where(pd.notna(df), None)

# ---------- 3. Connect to MySQL ----------
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="RAM@1234",
    database="Projects",
)
print("mysql connection successfully established")
cursor = connection.cursor()

# ---------- 4. Create table ----------
cursor.execute("DROP TABLE IF EXISTS FOOD_DELIVERY_DETAILS")
cursor.execute("""
CREATE TABLE FOOD_DELIVERY_DETAILS(
    Order_id VARCHAR(300) PRIMARY KEY,
    Customer_id VARCHAR(300),
    Restaurant_id VARCHAR(300),
    Driver_id VARCHAR(300),
    Order_date DATE,
    Order_hour TINYINT UNSIGNED,
    Day_of_week VARCHAR(50),
    Is_weekend VARCHAR(10),
    City VARCHAR(300),
    Delivery_area VARCHAR(300),
    Customer_age TINYINT UNSIGNED,
    Customer_type VARCHAR(300),
    Restaurant_type VARCHAR(300),
    Restaurant_primary_category VARCHAR(300),
    Restaurant_rating DECIMAL(3,2),
    Items_count TINYINT UNSIGNED,
    Subtotal DECIMAL(10,2),
    Discount_percent DECIMAL(5,2),
    Tax_amount DECIMAL(10,2),
    Service_fee DECIMAL(10,2),
    Delivery_fee DECIMAL(10,2),
    Order_total DECIMAL(10,2),
    Payment_method VARCHAR(50),
    Tip_amount DECIMAL(10,2),
    Distance_km DECIMAL(6,2),
    Weather VARCHAR(50),
    Traffic_level VARCHAR(50),
    Delivery_partner_experience_months SMALLINT UNSIGNED,
    Delivery_partner_rating DECIMAL(3,2),
    Restaurant_preparation_time_minutes SMALLINT UNSIGNED,
    Estimated_delivery_time_minutes SMALLINT UNSIGNED,
    Actual_delivery_time_minutes DECIMAL(6,2),
    Late_delivery VARCHAR(20),
    Order_status VARCHAR(50),
    Cancellation_reason VARCHAR(100),
    Customer_rating DECIMAL(3,2),
    Order_time DATETIME
)
""")
print("table is created")

# ---------- 5. Insert data in batches ----------
insert_query = (f"INSERT INTO FOOD_DELIVERY_DETAILS ({', '.join(cols)}) "
                f"VALUES ({', '.join(['%s'] * len(cols))})")
data = list(df.itertuples(index=False, name=None))

i = 0
try:
    for i in range(0, len(data), 1000):
        cursor.executemany(insert_query, data[i:i + 1000])
    connection.commit()
    print(f"{len(data)} rows uploaded successfully")
except mysql.connector.Error as e:
    connection.rollback()
    print("FAILED:", e)
    for row in data[i:i + 1000]:          # pinpoint the bad row in the failing batch
        try:
            cursor.execute(insert_query, row)
        except mysql.connector.Error as e2:
            print("Bad row:", row)
            print(e2)
            break
    connection.rollback()

# ---------- 6. Quick verification ----------
cursor.execute("SELECT COUNT(*) FROM FOOD_DELIVERY_DETAILS")
print("Rows in table:", cursor.fetchone()[0])

cursor.close()
connection.close()