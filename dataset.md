# Testing Dataset

## Customer

```sql
INSERT INTO
    Customer( cust_id, cust_first_name, cust_last_name )
VALUES
    ('cust00001', 'Andy', 'Ho' ),
    ('cust00002', 'Roger', 'Lee' ),
    ('cust00003', 'Ethan', 'Hou' ),
    ('cust00004', 'Jesse', 'Hung' ),
    ('cust00005', 'Mike', 'Sun' ),
    ('cust00006', 'Peter', 'Sun' ),
    ('cust00007', 'Yuan', 'Chen' ),
    ('cust00008', 'Kevin', 'Huang' ),
    ('cust00009', 'Cathy', 'Lee' )
;
```

### Result
```
mysql> select * from Customer;
+-----------+-----------------+----------------+
| cust_id   | cust_first_name | cust_last_name |
+-----------+-----------------+----------------+
| cust00001 | Andy            | Ho             |
| cust00002 | Roger           | Lee            |
| cust00003 | Ethan           | Hou            |
| cust00004 | Jesse           | Hung           |
| cust00005 | Mike            | Sun            |
| cust00006 | Peter           | Sun            |
| cust00007 | Yuan            | Chen           |
| cust00008 | Kevin           | Huang          |
| cust00009 | Cathy           | Lee            |
+-----------+-----------------+----------------+
```

## Category

```sql
INSERT INTO
    Category( cate_id, cate_name )
VALUES
    ('cate00001', 'CateA' ),
    ('cate00002', 'CateB' ),
    ('cate00003', 'CateC' ),
    ('cate00004', 'CateD' ),
    ('cate00005', 'CateE' ),
    ('cate00006', 'CateF' ),
    ('cate00007', 'CateG' ),
    ('cate00008', 'CateH' ),
    ('cate00009', 'CateI' ),
    ('cate00010', 'CateJ' )
;
```

### Result
```
mysql> select * from Category;
+-----------+-----------+
| cate_id   | cate_name |
+-----------+-----------+
| cate00001 | CateA     |
| cate00002 | CateB     |
| cate00003 | CateC     |
| cate00004 | CateD     |
| cate00005 | CateE     |
| cate00006 | CateF     |
| cate00007 | CateG     |
| cate00008 | CateH     |
| cate00009 | CateI     |
| cate00010 | CateJ     |
+-----------+-----------+
```

## Product

```sql
INSERT INTO
    Product( prod_id, prod_name )
VALUES
    ('prod00001', 'Product 1' ),
    ('prod00002', 'Product 2' ),
    ('prod00003', 'Product 3' ),
    ('prod00004', 'Product 4' ),
    ('prod00005', 'Product 5' ),
    ('prod00006', 'Product 6' ),
    ('prod00007', 'Product 7' ),
    ('prod00008', 'Product 8' ),
    ('prod00009', 'Product 9' ),
    ('prod00010', 'Product 10' ),
    ('prod00011', 'Product 11' ),
    ('prod00012', 'Product 12' ),
    ('prod00013', 'Product 13' ),
    ('prod00014', 'Product 14' ),
    ('prod00015', 'Product 15' ),
    ('prod00016', 'Product 16' ),
    ('prod00017', 'Product 17' ),
    ('prod00018', 'Product 18' ),
    ('prod00019', 'Product 19' ),
    ('prod00020', 'Product 20' )
;
```

### Result
```
mysql> select * from Product;
+-----------+------------+
| prod_id   | prod_name  |
+-----------+------------+
| prod00001 | Product 1  |
| prod00002 | Product 2  |
| prod00003 | Product 3  |
| prod00004 | Product 4  |
| prod00005 | Product 5  |
| prod00006 | Product 6  |
| prod00007 | Product 7  |
| prod00008 | Product 8  |
| prod00009 | Product 9  |
| prod00010 | Product 10 |
| prod00011 | Product 11 |
| prod00012 | Product 12 |
| prod00013 | Product 13 |
| prod00014 | Product 14 |
| prod00015 | Product 15 |
| prod00016 | Product 16 |
| prod00017 | Product 17 |
| prod00018 | Product 18 |
| prod00019 | Product 19 |
| prod00020 | Product 20 |
+-----------+------------+
```

## ProductCategory

```sql
INSERT INTO
    ProductCategory( prod_id, cate_id )
VALUES
    ('prod00001', 'cate00001' ),
    ('prod00001', 'cate00002' ),
    ('prod00001', 'cate00003' ),
    ('prod00002', 'cate00002' ),
    ('prod00002', 'cate00004' ),
    ('prod00002', 'cate00005' ),
    ('prod00002', 'cate00006' ),
    ('prod00003', 'cate00003' ),
    ('prod00003', 'cate00001' ),
    ('prod00004', 'cate00004' ),
    ('prod00004', 'cate00007' ),
    ('prod00004', 'cate00008' ),
    ('prod00005', 'cate00005' ),
    ('prod00005', 'cate00009' ),
    ('prod00005', 'cate00010' ),
    ('prod00006', 'cate00006' ),
    ('prod00006', 'cate00001' ),
    ('prod00006', 'cate00002' ),
    ('prod00007', 'cate00007' ),
    ('prod00007', 'cate00001' ),
    ('prod00007', 'cate00002' ),
    ('prod00007', 'cate00003' ),
    ('prod00007', 'cate00009' ),
    ('prod00007', 'cate00010' ),
    ('prod00008', 'cate00008' ),
    ('prod00009', 'cate00009' ),
    ('prod00010', 'cate00010' ),
    ('prod00011', 'cate00001' ),
    ('prod00012', 'cate00002' ),
    ('prod00013', 'cate00003' ),
    ('prod00014', 'cate00004' ),
    ('prod00015', 'cate00005' ),
    ('prod00016', 'cate00006' ),
    ('prod00017', 'cate00007' ),
    ('prod00018', 'cate00008' ),
    ('prod00019', 'cate00009' ),
    ('prod00020', 'cate00010' )
;
```

```
A B C D E F G H I  J
1 2 3 4 5 6 7 8 9 10

1 -> A, B, C
2 -> B, D, E, F
3 -> A, C
4 -> D, G, H
5 -> E, I, J
6 -> A, B, F
7 -> A, B, C, G, I, J
```

## Order

```sql
START TRANSACTION;
    INSERT INTO
        ShoppingOrder( cust_id, timestamp, status )
    VALUES
        ( 'cust00001', CURRENT_TIMESTAMP(), 'Waiting for Delivery' )
    ;
    SET @LASTID = LAST_INSERT_ID();
    INSERT INTO
        OrderDetail( ord_id, prod_id, amount )
    VALUES
        ( @LASTID, 'prod00001', 10 ),
        ( @LASTID, 'prod00002', 5 ),
        ( @LASTID, 'prod00003', 2 ),
        ( @LASTID, 'prod00004', 1 )
    ;
COMMIT;

START TRANSACTION;
    INSERT INTO
        ShoppingOrder( cust_id, timestamp, status )
    VALUES
        ( 'cust00002', CURRENT_TIMESTAMP(), 'Waiting for Delivery' )
    ;
    SET @LASTID = LAST_INSERT_ID();
    INSERT INTO
        OrderDetail( ord_id, prod_id, amount )
    VALUES
        ( @LASTID, 'prod00003', 1 ),
        ( @LASTID, 'prod00006', 2 ),
        ( @LASTID, 'prod00008', 3 ),
        ( @LASTID, 'prod00009', 4 )
    ;
COMMIT;

START TRANSACTION;
    INSERT INTO
        ShoppingOrder( cust_id, timestamp, status )
    VALUES
        ( 'cust00003', CURRENT_TIMESTAMP(), 'On It\'s Way' )
    ;
    SET @LASTID = LAST_INSERT_ID();
    INSERT INTO
        OrderDetail( ord_id, prod_id, amount )
    VALUES
        ( @LASTID, 'prod00005', 5 ),
        ( @LASTID, 'prod00010', 5 )
    ;
COMMIT;

START TRANSACTION;
    INSERT INTO
        ShoppingOrder( cust_id, timestamp, status )
    VALUES
        ( 'cust00001', CURRENT_TIMESTAMP(), 'Delivered' )
    ;
    SET @LASTID = LAST_INSERT_ID();
    INSERT INTO
        OrderDetail( ord_id, prod_id, amount )
    VALUES
        ( @LASTID, 'prod00002', 5 ),
        ( @LASTID, 'prod00005', 5 )
    ;
COMMIT;

START TRANSACTION;
    INSERT INTO
        ShoppingOrder( cust_id, timestamp, status )
    VALUES
        ( 'cust00006', CURRENT_TIMESTAMP(), 'On It\'s Way' )
    ;
    SET @LASTID = LAST_INSERT_ID();
    INSERT INTO
        OrderDetail( ord_id, prod_id, amount )
    VALUES
        ( @LASTID, 'prod00001', 8 ),
        ( @LASTID, 'prod00002', 6 ),
        ( @LASTID, 'prod00003', 4 )
    ;
COMMIT;
```

## Number of Items per Category
```sql
SELECT a.cate_id, b.num_of_items
FROM
    Category AS a
    INNER JOIN
    (
        SELECT tmp.cate_id, COUNT( prod_id ) as num_of_items
        FROM ProductCategory AS tmp
        GROUP BY tmp.cate_id
    ) AS b
ON a.cate_id = b.cate_id;
```

## Number of Item Sold per Category
```sql
SELECT
    CateProd.cate_id, CateProd.cate_name,
    SUM(amount) AS sold
FROM
    OrderDetail
    LEFT JOIN
        (
            SELECT b.prod_id AS prod_id, a.cate_id, a.cate_name
            FROM Category AS a
            INNER JOIN ProductCategory AS b ON a.cate_id = b.cate_id
            ORDER BY b.prod_id ASC
        ) AS CateProd
    ON OrderDetail.prod_id = CateProd.prod_id
GROUP BY cate_id;
```

## Number of Item Sold per Product
```sql
SELECT
    Product.prod_id, Product.prod_name,
    SUM(amount) AS sold
FROM
    Product
    LEFT JOIN
        OrderDetail
    ON OrderDetail.prod_id = Product.prod_id
GROUP BY Product.prod_id
;
```

If only want to show product that is sold, use `INNER JOIN`:
```sql
SELECT
    Product.prod_id, Product.prod_name,
    SUM(amount) AS sold
FROM
    Product
    INNER JOIN
        OrderDetail
    ON OrderDetail.prod_id = Product.prod_id
GROUP BY Product.prod_id
;
```

## Number of Item Sold of a Product
```sql
SELECT
    Product.prod_id, Product.prod_name,
    SUM(amount) AS sold
FROM
    Product
    INNER JOIN
    (
        SELECT * FROM OrderDetail
        WHERE prod_id = "prod00001"
    ) AS OrderDetail
    ON OrderDetail.prod_id = Product.prod_id
GROUP BY Product.prod_id
```

## Number of Item Sold per Product by Date, Week, Month, or Year

```sql
SELECT
    Product.prod_id, Product.prod_name,
    SUM(sold) AS sold
FROM
    Product
    INNER JOIN
        (
            SELECT
                OrderDetail.prod_id, ShoppingOrder.timestamp,
                OrderDetail.amount AS sold
            FROM ShoppingOrder
            JOIN
                OrderDetail
            ON ShoppingOrder.ord_id = OrderDetail.ord_id
        ) AS AllOrderWithDetail
    ON AllOrderWithDetail.prod_id = Product.prod_id
GROUP BY DATE(timestamp), Product.prod_id
ORDER BY DATE(timestamp)
;
```

By week, use `WEEK(timestamp)`.
By month, use `MONTH(timestamp)`.
By year, use `YEAR(timestamp)`.

## Orders by Customer

```sql
SELECT
    ShoppingOrder.ord_id,
    ShoppingOrder.timestamp AS order_time,
    ShoppingOrder.status AS order_status,
    Customer.cust_id, Customer.cust_first_name, Customer.cust_last_name
FROM
    ShoppingOrder
    JOIN
        Customer
    ON ShoppingOrder.cust_id = Customer.cust_id
;
```

## Number of Orders per Customer

```sql
SELECT
    Cust.cust_id, Cust.cust_first_name, Cust.cust_last_name,
    SOrd.num_of_orders
FROM
    Customer AS Cust
    LEFT JOIN
    (
        SELECT cust_id, COUNT( ord_id ) as num_of_orders
        FROM ShoppingOrder
        GROUP BY cust_id
    ) AS SOrd
ON Cust.cust_id = SOrd.cust_id;
```

## Number of Sold per Category by Customer
<!-- ```sql
SELECT 
    CustOrd.cust_id, CustOrd.cust_first_name, CustOrd.cust_last_name,
    CateSold.cate_id, CateSold.cate_name, CateSold.amount AS number_purchased
FROM
    (
        SELECT
            Cust.cust_id, Cust.cust_first_name, Cust.cust_last_name,
            SOrd.ord_id
        FROM
            Customer AS Cust
            LEFT JOIN
                ShoppingOrder AS SOrd
            ON Cust.cust_id = SOrd.cust_id
    ) AS CustOrd
    RIGHT JOIN
        (
            SELECT
                ord_id, SUM(amount) AS amount,
                CateProd.cate_id, CateProd.cate_name
            FROM
                OrderDetail
                LEFT JOIN
                    (
                        SELECT b.prod_id AS prod_id, a.cate_id, a.cate_name
                        FROM Category AS a
                        INNER JOIN ProductCategory AS b ON a.cate_id = b.cate_id
                        ORDER BY b.prod_id ASC
                    ) AS CateProd
                ON OrderDetail.prod_id = CateProd.prod_id
            GROUP BY cate_id
        ) AS CateSold
    ON CustOrd.ord_id = CateSold.ord_id
;
``` -->

```sql
SELECT 
    CustOrd.cust_id, CustOrd.cust_first_name, CustOrd.cust_last_name,
    CateSold.cate_id, CateSold.cate_name, SUM(CateSold.amount) AS number_purchased
FROM
    (
        SELECT
            Cust.cust_id, Cust.cust_first_name, Cust.cust_last_name,
            SOrd.ord_id
        FROM
            Customer AS Cust
            LEFT JOIN
                ShoppingOrder AS SOrd
            ON Cust.cust_id = SOrd.cust_id
    ) AS CustOrd
    RIGHT JOIN
        (
            SELECT
                ord_id, SUM(amount) AS amount,
                CateProd.cate_id, CateProd.cate_name
            FROM
                OrderDetail
                LEFT JOIN
                    (
                        SELECT b.prod_id AS prod_id, a.cate_id, a.cate_name
                        FROM Category AS a
                        INNER JOIN ProductCategory AS b ON a.cate_id = b.cate_id
                        ORDER BY b.prod_id ASC
                    ) AS CateProd
                ON OrderDetail.prod_id = CateProd.prod_id
            GROUP BY ord_id, cate_id
        ) AS CateSold
    ON CustOrd.ord_id = CateSold.ord_id
GROUP BY CustOrd.cust_id, CateSold.cate_id
;
```