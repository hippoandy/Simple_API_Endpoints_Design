## Introduction

This is a simple API server application which depict a customer shopping order management system.
The server provides API endpoints to get information from the database in the format of ***JSON***, **XML**, and ***CSV***.

The API server is implemented using ***Python-Flask*** with **Python 3.7**. A ***MariaDB (MySQL)*** open-source database software is utilized as the data storage. The testing dataset is arbitrarily created and inserted already into the database.

## Database Design

The following is the database schema design:

<img src="{{url_for('simpleapidemo.static', filename='img/schema.png')}}" alt="Database Schema Design" width="800px"/>
<br />

## Implemented API Endpoints

* Current API Version: ***v1***
* API Link: `/api/<API VER>/<API NAME>`
* Supported Output Format: ***JSON***, ***XML***, ***CSV***
* Default Parameters:

| Name     | Type     | Description                    | Default     |
|----------|----------|--------------------------------|-------------|
| `page `| Integer | (***Pagination***) page number | 1 |
| `size `| Integer | (***Pagination***) number of items per page | 10 |
| `format `| Text | Return data format, values in [ "**json**", "**xml**", "**csv**" ] | json |

* API Endpoints Links:

| API NAME     | Extra Parameters          | Description                    |
|--------------|---------------------------|--------------------------------|
| `/order/listOrder` | None | List all the received shopping orders. |
| `/order/showByID` | `ord_id` | Show the detail of an order by ID (`ord_id`). |
| `/order/orderByCustomer` | `cust_id` | Show orders by Customer using Customer ID (`cust_id`). |
| `/product/listProduct` | None | List all the products. |
| `/product/showByID` | `prod_id` | Show the detail of a product by ID (`prod_id`). |
| `/product/numOfSold` | `prod_id` | Show the number of sold per product, if product ID (`prod_id`) is given, return only the result with that ID. |
| `/product/numOfSoldByDate` | `start_date`, `end_date`, `range`, `prod_id` | Show the number of sold amount per product specified by a date range and grouping by `day`, `week`, or `month`. Parameter `start_date` and `end_date` are for the time filtering and `range` values in [ "**day**", "**week**", "**month**" ] to determine the grouping. If `range` is not specified, grouping by `date` is default. If a product Id (`prod_id`) is given, return the result only with that ID. |
| `category/numOfSold` | `cate_id` | Show the number of sold per category, if category ID (`cate_id`) is given, return only the result with that ID. |
| `/category/purchasedByCustomer` | `cust_id` | Show the number of purchased amount in a certain category by a customer with ID (`cust_id`). |

## Try it Out!

To try the API endpoints, please use the following format:
```
http://<SERVER ADDR>/api/<API Ver>/<ENDPOINT LINK>
```

To add parameters, please use the following format:
```
http://<SERVER ADDR>:5000/api/<API Ver>/<ENDPOINT LINK>?<PARA 1>=<VALUE>&<PARA 2>=<VALUE>&...
```