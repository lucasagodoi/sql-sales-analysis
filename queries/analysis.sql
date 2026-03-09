SELECT Region, SUM(Revenue) as Total_Revenue
FROM sales
GROUP BY Region;

SELECT Category, AVG(Revenue) as Avg_Revenue
FROM sales
GROUP BY Category;

SELECT Month, SUM(Revenue) as Monthly_Revenue
FROM sales
GROUP BY Month;