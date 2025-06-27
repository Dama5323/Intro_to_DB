-- Full description of books table without using DESCRIBE/EXPLAIN/ANALYZE
SELECT 
    COLUMN_NAME AS 'Field',
    COLUMN_TYPE AS 'Type',
    IF(IS_NULLABLE = 'YES', 'YES', 'NO') AS 'Null',
    IFNULL(COLUMN_KEY, '') AS 'Key',
    IFNULL(COLUMN_DEFAULT, 'NULL') AS 'Default',
    IFNULL(EXTRA, '') AS 'Extra'
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = 'alx_book_store'
    AND TABLE_NAME = 'books';
