-- SQL practice: 2026-10-16
-- Dataset: Chinook (music store). Tables: Artist, Album, Track, Genre,
-- Customer, Invoice, InvoiceLine, Employee, Playlist, PlaylistTrack, MediaType.
--
-- Run all queries:   sqlite3 -header -column ../data/chinook.db < queries.sql
-- Explore a table:   sqlite3 ../data/chinook.db ".schema Invoice"
--
-- Each question lists the expected number of result rows so you can check yourself.


-- Q1 (WHERE)
-- List the first name, last name and city of every customer in Brazil.
-- Expected: 5 rows
SELECT FirstName, LastName, City
FROM Customer
WHERE Country = 'Brazil';


-- Q2 (JOIN)
-- List the titles of all albums by the artist 'AC/DC'.
-- Hint: Album has an ArtistId column.
-- Expected: 2 rows
Select Title
From Album
Where ArtistId = 1;

-- Q3 (JOIN + GROUP BY)
-- For each genre, show the genre name and how many tracks it has,s
-- sorted from most tracks to fewest.
-- Expected: 25 rows (Rock should be first)
SELECT Genre.Name, COUNT(*) AS TrackCount
FROM Track
JOIN Genre ON Track.GenreId = Genre.GenreId
GROUP BY Genre.Name
ORDER BY TrackCount DESC;
-- Q4 (GROUP BY + HAVING)
-- Which billing countries have total sales (sum of Invoice.Total) over 100?
-- Show the country and its total, rounded to 2 decimals, highest first.
-- Expected: 6 rows
-- Q4 (GROUP BY + HAVING)
SELECT BillingCountry, ROUND(SUM(Total), 2) AS TotalSales
FROM Invoice
GROUP BY BillingCountry
HAVING TotalSales > 100
ORDER BY TotalSales DESC;
-- Q5 (subquery / NOT EXISTS)
-- Which customers have never bought a Jazz track?
-- Path: Customer -> Invoice -> InvoiceLine -> Track -> Genre
-- Expected: 27 rows
SELECT FirstName, LastName
FROM Customer
WHERE CustomerId NOT IN (
  SELECT Invoice.CustomerId
  FROM Invoice
  JOIN InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId
  JOIN Track ON InvoiceLine.TrackId = Track.TrackId
  WHERE Track.GenreId = 2
);


-- Q6 (CTE + window function)  -- interview favourite
-- For each country, find the customer who spent the most in total.
-- Show country, customer name and total spent.
-- Hint: WITH totals AS (...) then RANK() OVER (PARTITION BY ... ORDER BY ...)
-- Expected: 26 rows (24 countries, but the UK has a three-way tie)
-- Q6
WITH totals AS (
  SELECT Customer.Country,
         Customer.FirstName || ' ' || Customer.LastName AS Name,
         SUM(Invoice.Total) AS Spent
  FROM Customer
  JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
  GROUP BY Customer.CustomerId
),
ranked AS (
  SELECT Country, Name, Spent,
         RANK() OVER (PARTITION BY Country ORDER BY Spent DESC) AS Rnk
  FROM totals
)
SELECT Country, Name, ROUND(Spent, 2) AS Spent
FROM ranked
WHERE Rnk = 1
ORDER BY Country;