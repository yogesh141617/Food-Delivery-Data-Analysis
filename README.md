# Food Delivery Data Analysis

## Overview
An end-to-end analysis of food delivery order data to understand order trends, delivery performance, customer behavior, and business insights.

## Tools Used
Python (Pandas, Google Colab), MySQL, Power BI

## What I Did
- Cleaned and transformed the raw dataset using Python and Pandas
- Imported the cleaned dataset into MySQL
- Performed data analysis using SQL queries
- Created an interactive Power BI dashboard to visualize key metrics and trends

## Key Insights
-Total number of orders: 50K orders placed by 5K customers, across 250 restaurants and 200 delivery partners.
- Total revenue: 1.91M in total order value (average order value 38.17), plus 79.11K in tips and 70.35K in discounts. The dashboard shows order value rather than platform revenue, so I used “total order value” here.
- Key order and delivery trends:
--The average estimated delivery time is 30.95 min, but the actual average is 35.15 min, so deliveries run about 4 min over the estimate.
--About 37% of deliveries are late (~18K orders), and the cancellation rate is about 2%.
--Delivery time rises with traffic (~31 min Low, ~35 Medium, ~40 High) and with weather (~34 min Clear to ~47 min Storm).
- Top-performing category or location:
--Burger is the top category, with ~16K orders and ~0.55M in order value. Local is second (~12.8K orders, ~0.47M).
--City A is the top location, with ~20K orders (about 40% of the total). City D has the highest average order value (~43) but the fewest orders (~5K).
- Other important findings:
--Regular customers account for 50% of orders and ~1.0M in order value, while Premium customers have the lowest average order value (~34).
--The 20–29 age group places about 48% of all orders.
--Credit card is the leading payment method (~0.95M) and also generates most tips. Cash tips are under 1% of cash order value.
--Storms raise the cancellation rate to ~3.7%, about 2.6x the rate in clear weather.
--Driver experience has almost no effect on delivery time or rating (~35 min and ~4.5 across all experience groups).

## Dashboard Preview
1. Executive Overview
   <img width="926" height="578" alt="image" src="https://github.com/user-attachments/assets/ffa214a6-ff1c-48bc-a3a8-ac0f8bd97121" />
2. Customer Analytics
   <img width="928" height="573" alt="WhatsApp Image 2026-11-16 at 3 29 12 PM" src="https://github.com/user-attachments/assets/7f72ec84-6090-437c-ba9f-f037f37325bc" />
3. Restaurant Analytics
   <img width="930" height="577" alt="image" src="https://github.com/user-attachments/assets/f2c3c8a7-e8e6-44f8-8a6b-9a0f101f406f" />
4. Driver Analytics
   <img width="930" height="574" alt="image" src="https://github.com/user-attachments/assets/2d092d36-4887-49fd-bd57-20db0420e44b" />
5. Logistics & ETA
   <img width="926" height="574" alt="image" src="https://github.com/user-attachments/assets/4876c9b4-8d29-458b-8e4e-0936fe718d6a" />
6. Financial Analysis
   <img width="930" height="580" alt="image" src="https://github.com/user-attachments/assets/157698e1-8d92-4f22-8d76-ce6aef7b60b6" />
7. Overall Data Overview
   <img width="929" height="577" alt="image" src="https://github.com/user-attachments/assets/37fdfc0d-9c26-4463-bdfa-2f40deb0fc61" />


## Files
- Dataset/ : Raw and cleaned datasets
- Python_Analysis/ : Python data cleaning and analysis notebook
- SQL/ : SQL queries and Python-MySQL integration code
- PowerBI/ : Power BI dashboard file
- Images/ : Dashboard screenshots
