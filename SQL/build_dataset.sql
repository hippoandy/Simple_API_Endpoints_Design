use simple_e_commerce;

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