create view vw_SaleProduct as 
select color,EnglishProductName, convert(date,OrderDate) OrderDate,SUM(SalesAmount) TotalSale
From [dbo].[dimProduct] A
inner join [dbo].[FactInternetSales] B on A. ProductKey=B.ProductKey Group by color, EnglishProductName, convert(date,OrderDate);