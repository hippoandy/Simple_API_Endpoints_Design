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
GROUP BY MONTH(timestamp), Product.prod_id
ORDER BY MONTH(timestamp)
;