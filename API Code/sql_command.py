# sql ----------------------------------------------
sql_list_order = "SELECT * FROM ShoppingOrder"

sql_order_by_id = '''
    SELECT 
        Ord.*,
        OrderDetail.prod_id,
        OrderDetail.amount AS purchased_amount
    FROM
        (
            SELECT
                ord_id, timestamp, status,
                Cust.cust_id, Cust.cust_first_name, Cust.cust_last_name
            FROM
                ShoppingOrder
                INNER JOIN
                    Customer AS Cust
                ON ShoppingOrder.cust_id = Cust.cust_id
        ) AS Ord
        INNER JOIN
            OrderDetail
        ON Ord.ord_id = OrderDetail.ord_id
    WHERE Ord.ord_id = "{}"
'''

sql_list_product = "SELECT * FROM Product"

sql_product_by_id = '''
    SELECT 
        Prod.*,
        Category.cate_name
    FROM
        (
            SELECT
                Product.*,
                ProductCategory.cate_id
            FROM
                Product
                INNER JOIN
                    ProductCategory
                ON Product.prod_id = ProductCategory.prod_id
            ORDER BY Product.prod_id
        ) AS Prod
        INNER JOIN
            Category
        ON Category.cate_id = Prod.cate_id
    WHERE Prod.prod_id = "{}"
'''

sql_num_of_sold_prod_per_cate = '''
    SELECT
        CateProd.cate_id, CateProd.cate_name,
        SUM(amount) AS sold
    FROM
        OrderDetail
        INNER JOIN
            (
                SELECT b.prod_id AS prod_id, a.cate_id, a.cate_name
                FROM Category AS a
                INNER JOIN ProductCategory AS b ON a.cate_id = b.cate_id
                ORDER BY b.prod_id ASC
            ) AS CateProd
        ON OrderDetail.prod_id = CateProd.prod_id
'''

sql_num_of_sold_per_prod = '''
    SELECT
        Product.prod_id, Product.prod_name,
        SUM(amount) AS sold
    FROM
        Product
        LEFT JOIN
            OrderDetail
        ON OrderDetail.prod_id = Product.prod_id
    GROUP BY Product.prod_id
'''

sql_num_of_sold_of_prod = '''
    SELECT
        Product.prod_id, Product.prod_name,
        SUM(amount) AS sold
    FROM
        Product
        INNER JOIN
        (
            SELECT * FROM OrderDetail
            WHERE prod_id = "{}"
        ) AS OrderDetail
        ON OrderDetail.prod_id = Product.prod_id
    GROUP BY Product.prod_id
'''

sql_num_of_sold_per_prod_by_date = '''
    SELECT
        Product.prod_id, Product.prod_name,
        SUM(sold)
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
                WHERE {}
            ) AS AllOrderWithDetail
        ON AllOrderWithDetail.prod_id = Product.prod_id
'''

sql_purchased_by_cust = '''
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
                INNER JOIN
                    ShoppingOrder AS SOrd
                ON Cust.cust_id = SOrd.cust_id
            WHERE Cust.cust_id = "{}"
        ) AS CustOrd
        INNER JOIN
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
    ORDER BY CustOrd.cust_id ASC
'''

sql_order_by_cust = '''
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
'''
# ---------------------------------------------- sql