-- Selecting all columns from the 'ad' table
SELECT * FROM ad;

-- Counting total rows in the 'ad' table
SELECT COUNT(*) FROM ad;

-- Counting by storage for the 256 variant
SELECT COUNT(storage) FROM ad 
WHERE storage LIKE '%256%';

-- Counting by storage for the 128 variant
SELECT COUNT(storage) FROM ad 
WHERE storage LIKE '%128%';

-- Counting by storage for the 64 variant
SELECT COUNT(storage) FROM ad 
WHERE storage LIKE '%64%';

-- Counting the number of 5G phones
SELECT COUNT(model) FROM ad 
WHERE model LIKE '%5G%';

-- Grouping by brand and counting occurrences for model 'c51'
SELECT brand, COUNT(brand) FROM ad 
WHERE model = 'c51'
GROUP BY brand;

-- Counting occurrences of each brand
SELECT brand, COUNT(brand) AS count 
FROM ad 
GROUP BY brand 
ORDER BY count DESC;

-- Grouping by model and brand
SELECT brand, model, COUNT(model) AS count
FROM ad 
GROUP BY model, brand 
ORDER BY count DESC;

-- Grouping by color and brand
SELECT brand, color, COUNT(color) AS count
FROM ad 
GROUP BY color, brand 
ORDER BY count DESC;

-- Knowing the count of 5G phones for a particular brand (e.g., 'Motorola')
SELECT brand, model, COUNT(model) AS model_count
FROM ad 
WHERE brand = 'Motorola' AND model LIKE '%5G%' 
GROUP BY brand, model;
