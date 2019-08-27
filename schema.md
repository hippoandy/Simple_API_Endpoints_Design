
# Database Schema

## Create Database

```sql
CREATE DATABASE simple_e_commerce CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## Category Table

```sql
CREATE TABLE IF NOT EXISTS Category (
    cate_id         VARCHAR( 20 ),
    cate_name       VARCHAR( 50 ),
    PRIMARY KEY( cate_id )
);
```

## Product Table

```sql
CREATE TABLE IF NOT EXISTS Product (
    prod_id         VARCHAR( 20 ),
    prod_name       VARCHAR( 200 ),
    PRIMARY KEY( prod_id )
);
```

## ProductCategory Table

```sql
CREATE TABLE IF NOT EXISTS ProductCategory (
    prod_id         VARCHAR( 20 ),
    cate_id         VARCHAR( 20 ),
    PRIMARY KEY( prod_id, cate_id ),
    FOREIGN KEY( prod_id ) REFERENCES Product( prod_id )
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY( cate_id ) REFERENCES Category( cate_id )
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
```

## Customer Table

```sql
CREATE TABLE IF NOT EXISTS Customer (
    cust_id             VARCHAR( 20 ),
    cust_first_name     VARCHAR( 200 ),
    cust_last_name      VARCHAR( 200 ),
    PRIMARY KEY( cust_id )
);
```

## ShoppingOrder Table

```sql
CREATE TABLE IF NOT EXISTS ShoppingOrder (
    ord_id          INT NOT NULL AUTO_INCREMENT,
    cust_id         VARCHAR( 20 ),
    timestamp       TIMESTAMP,
    status          VARCHAR( 20 ),
    PRIMARY KEY( ord_id ),
    FOREIGN KEY( cust_id ) REFERENCES Customer( cust_id )
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
```

## OrderDetail Table

```sql
CREATE TABLE IF NOT EXISTS OrderDetail (
    ord_id              INT,
    prod_id             VARCHAR( 200 ),
    amount              INT,
    PRIMARY KEY( ord_id, prod_id ),
    FOREIGN KEY( ord_id ) REFERENCES ShoppingOrder( ord_id )
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY( prod_id ) REFERENCES Product( prod_id )
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
```