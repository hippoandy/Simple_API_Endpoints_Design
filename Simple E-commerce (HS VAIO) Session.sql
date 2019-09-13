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