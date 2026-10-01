-- Sales Analytics Queries

-- Total sales and profit
SELECT
    SUM(Sales) AS total_sales,
    SUM(Profit) AS total_profit
FROM sales_data;

-- Sales by region
SELECT
    Region,
    SUM(Sales) AS total_sales
FROM sales_data
GROUP BY Region
ORDER BY total_sales DESC;

-- Profit by category
SELECT
    Category,
    SUM(Profit) AS total_profit
FROM sales_data
GROUP BY Category
ORDER BY total_profit DESC;

-- Top products by sales
SELECT
    Product,
    SUM(Sales) AS total_sales
FROM sales_data
GROUP BY Product
ORDER BY total_sales DESC;
