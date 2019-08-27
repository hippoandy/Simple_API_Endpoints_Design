''' A Demo Customer Management System

Author: Yu-Chang (Andy) Ho

This is a demo API server of customer management system.
This server is implemented using Python-Flask.
It provides APIs to communicate with the MariaDB (MySQL) database.

'''

from flask import Flask, render_template, request, Response, send_from_directory
from datetime import datetime

import config
import sql_command

import utils
import query

# create the flask application
app = Flask(
    __name__,
    static_url_path='', 
    static_folder='web/static',
    template_folder='web/templates'
)

# server main page, will show part of the documentation
@app.route( "/" )
def index():
    return render_template( 'index.html' )

# assets requests
@app.route( "/documentation.md" )
def manual():
    return render_template( 'documentation.md' )
@app.route( "/<path:filename>" )
def send_img( filename ):
    return send_from_directory( app.static_folder, filename )

## General Funtions -----------------------------------------------
# determine the output format
api_output = {
    "json": utils.sql_to_json,
    "xml":  utils.sql_to_xml,
    "csv":  utils.sql_to_csv
}

# get the default required parameters, will have default value if not specified
def def_para():
    page = 1 if request.args.get( 'page' ) is None else request.args.get( 'page' )
    size = 10 if request.args.get( 'size' ) is None else request.args.get( 'size' )
    try:    # try to convert int
        page = int( page )
        size = int( size )
    except: return None
    # page size and page number should not be less than 1
    if( page < 1 or size < 1 ): return None

    # parameters with default values
    ret_format = "json" if request.args.get( 'format' ) is None else request.args.get( 'format' )
    ret_format = utils.clean_str( ret_format.lower(), strip=True )
    if( ret_format not in config.api_format ): return None
    # return those parameters in a dict
    return { "page": page, "size": size, "format": ret_format }

# query the database and present the result (Q4)
# if something went wrong, output the msg defined in the helper function
def gen_response( sql, para, helper_funct ):
    # send the sql query
    res, desc = query.sql_query(
        sql,
        page_num=para[ "page" ],
        page_size=para[ "size" ]
    )
    if( res is None or desc is None ): return helper_funct()
    return MyResponse( api_output[ para[ "format" ] ]( res, desc ) )

# customized response object
# will determine the mimetype dynamically
class MyResponse( Response ):
    def __init__( self, response, **kwargs ):
        if( 'mimetype' not in kwargs and 'contenttype' not in kwargs ):
            if( response.startswith( '<?xml' ) ):
                kwargs[ 'mimetype' ] = 'application/xml'
            elif( response.startswith( '{' ) ):
                kwargs[ 'mimetype' ] = 'application/json'
            else:
                kwargs[ 'mimetype' ] = 'text/csv'
        return super( MyResponse, self ).__init__( response, **kwargs )
## ----------------------------------------------- General Funtions

## API Endpoints --------------------------------------------------

# list of order
@app.route( "{}/order/listOrder".format( config.api_head ) )
def list_order():
    # obtain the parameters
    ## parameters with default values
    para = def_para()
    if( para is None ): return help_list_order()
    return gen_response( sql_command.sql_list_order, para, helper_funct=help_list_order )

''' Error msg for api endpoint "/order/listOrder" '''
def help_list_order( err="Invalid Query!" ):
    msg = f'''
    {err}

Usage: /order/listOrder

    {config.api_def_para_usage}
    '''
    return msg

# show order by id
@app.route( "{}/order/showByID".format( config.api_head ) )
def ord_show_by_id():
    # obtain the parameters
    ## parameters with default values
    para = def_para()
    if( para is None ): return help_ord_show_by_id()
    ## user given parameters
    ord_id = request.args.get( "ord_id" )
    if( ord_id is None ): return help_ord_show_by_id( "No Order ID given!" )
    ord_id = utils.clean_str( ord_id, strip=True )

    sql = sql_command.sql_order_by_id.format( ord_id )
    return gen_response( sql, para, helper_funct=help_ord_show_by_id )

''' Error msg for api endpoint "/order/listOrder" '''
def help_ord_show_by_id( err="Invalid Query!" ):
    msg = f'''
    {err}

Usage: /order/showByID

    ord_id: Order ID to query
    {config.api_def_para_usage}
    '''
    return msg

# list of order by customer (Q7)
@app.route( "{}/order/orderByCustomer".format( config.api_head ) )
def ord_order_by_customer():
    # obtain the parameters
    ## parameters with default values
    para = def_para()
    if( para is None ): return help_ord_order_by_customer()
    ## user given parameters
    cust_id = request.args.get( "cust_id" )
    if( cust_id is None ): return help_ord_order_by_customer( "No Customer ID given!" )
    cust_id = utils.clean_str( cust_id, strip=True )

    sql = sql_command.sql_order_by_cust
    sql += f' WHERE ShoppingOrder.cust_id = "{cust_id}"'
    return gen_response( sql, para, helper_funct=help_ord_order_by_customer )

''' Error msg for api endpoint "/order/listOrder" '''
def help_ord_order_by_customer( err="Invalid Query!" ):
    msg = f'''
    {err}

Usage: /order/orderByCustomer

    cust_id: Customer ID to query
    {config.api_def_para_usage}
    '''
    return msg

# list of product
@app.route( "{}/product/listProduct".format( config.api_head ) )
def list_product():
    # obtain the parameters
    ## parameters with default values
    para = def_para()
    if( para is None ): return help_list_product()
    return gen_response( sql_command.sql_list_product, para, helper_funct=help_list_product )

''' Error msg for api endpoint "/product/listProduct" '''
def help_list_product( err="Invalid Query!" ):
    msg = f'''
    {err}

Usage: /product/listProduct

    {config.api_def_para_usage}
    '''
    return msg

# show product by id
@app.route( "{}/product/showByID".format( config.api_head ) )
def prod_show_by_id():
    # obtain the parameters
    ## parameters with default values
    para = def_para()
    if( para is None ): return help_prod_show_by_id()
    ## user given parameters
    prod_id = request.args.get( "prod_id" )
    if( prod_id is None ): return help_prod_show_by_id( "No Product ID given!" )
    prod_id = utils.clean_str( prod_id, strip=True )

    sql = sql_command.sql_product_by_id.format( prod_id )
    return gen_response( sql, para, helper_funct=help_prod_show_by_id )

''' Error msg for api endpoint "/order/listOrder" '''
def help_prod_show_by_id( err="Invalid Query!" ):
    msg = f'''
    {err}

Usage: /product/showByID

    prod_id: Product ID to query
    {config.api_def_para_usage}
    '''
    return msg

# number of sold amount per category
@app.route( "{}/product/numOfSold".format( config.api_head ) )
def prod_num_of_sold():
    # obtain the parameters
    ## parameters with default values
    para = def_para()
    if( para is None ): return help_prod_num_of_sold()
    ## user given parameters
    prod_id = None if( request.args.get( "prod_id" ) is None ) else request.args.get( "prod_id" )

    # default to get all the result
    sql = sql_command.sql_num_of_sold_per_prod
    # if specific product id is given......
    if( prod_id is not None ):
        prod_id = utils.clean_str( prod_id, strip=True )
        sql = sql_command.sql_num_of_sold_of_prod.format( prod_id )
    return gen_response( sql, para, helper_funct=help_prod_num_of_sold )

''' Error msg for api endpoint "/product/numOfSold" '''
def help_prod_num_of_sold( err="Invalid Query!" ):
    msg = f'''
    {err}

Usage: /product/numOfSold

    prod_id: Product ID to query, if not given, default to return all the data
    {config.api_def_para_usage}
    '''
    return msg

# number of sold amount per product by date (Q5)
@app.route( "{}/product/numOfSoldByDate".format( config.api_head ) )
def prod_num_of_sold_date():
    # obtain the parameters
    ## parameters with default values
    para = def_para()
    if( para is None ): return help_prod_num_of_sold_date()
    prod_id = None if( request.args.get( "prod_id" ) is None ) else request.args.get( "prod_id" )
    time_range = None if( request.args.get( "range" ) is None ) else request.args.get( "range" )
    ## user given parameters
    start = utils.clean_str( str(request.args.get( "start_date" )), strip=True )
    end = utils.clean_str( str(request.args.get( "end_date" )), strip=True )
    # convert to datetime object
    try:
        start = datetime.strptime( start, "%Y-%m-%d" )
        end = datetime.strptime( end, "%Y-%m-%d" )
    except: return help_prod_num_of_sold_date( err="Invalid date!" )
    # end date is before start date
    if( end < start ): return help_prod_num_of_sold_date( err="End date is berfore start date!" )
    start = start.strftime( "%Y-%m-%d" )
    end = end.strftime( "%Y-%m-%d" )
    if( start == end ):
        start += " 00:00:00"
        end += " 23:59:59"

    # determine the grouping time range
    switcher = {
        "day": "DAY(timestamp)",        # group by day
        "week": "WEEK(timestamp)",      # group by week
        "month": "MONTH(timestamp)"     # group by month
    }
    if( time_range is not None ): time_range = utils.clean_str( time_range.lower(), strip=True )
    time_filter = switcher.get( time_range, "DATE(timestamp)" )
    # append the timestamp filter
    sql = sql_command.sql_num_of_sold_per_prod_by_date.format( f' timestamp BETWEEN "{start}" AND "{end}" ' )
    # if a specific product id is given......
    if( prod_id is not None ):
        prod_id = utils.clean_str( prod_id, strip=True )
        sql += f' WHERE Product.prod_id = "{prod_id}"'
    sql += f" GROUP BY Product.prod_id, {time_filter} ORDER BY {time_filter}"
    return gen_response( sql, para, helper_funct=help_prod_num_of_sold_date )

''' Error msg for api endpoint "/product/numOfSoldByDate" '''
def help_prod_num_of_sold_date( err="Invalid Query!" ):
    msg = f'''
    {err}

Usage: /product/numOfSoldByDate

    start_date: Start date
    end_date: End date
    range: Group result by the given time unit, support {", ".join( config.api_time_range )}
    prod_id: Product ID to query, if not given, default to return all the data
    {config.api_def_para_usage}
    '''
    return msg

# number of sold amount per category
@app.route( "{}/category/numOfSold".format( config.api_head ) )
def cate_num_of_sold():
    # obtain the parameters
    ## parameters with default values
    para = def_para()
    if( para is None ): return help_cate_num_of_sold()
    ## user given paramter
    cate_id = None if( request.args.get( "cate_id" ) is None ) else request.args.get( "cate_id" )

    sql = sql_command.sql_num_of_sold_prod_per_cate
    # if the category id is specificed......
    if( cate_id is not None ):
        cate_id = utils.clean_str( cate_id, strip=True )
        sql += f' WHERE cate_id = "{cate_id}" '
    sql += " GROUP BY cate_id "
    return gen_response( sql, para, helper_funct=help_cate_num_of_sold )

''' Error msg for api endpoint "/category/numOfSold" '''
def help_cate_num_of_sold( err="Invalid Query!" ):
    msg = f'''
    {err}

Usage: /category/numOfSold

    cate_id: Category ID to query
    {config.api_def_para_usage}
    '''
    return msg

# number of purchased amount in category by customer (Q3)
@app.route( "{}/category/purchasedByCustomer".format( config.api_head ) )
def cate_purchased_by_cust():
    # obtain the parameters
    ## parameters with default values
    para = def_para()
    if( para is None ): return help_cate_purchased_by_cust()
    ## user given parameters
    cust_id = request.args.get( 'cust_id' )
    if( cust_id is None ): return help_cate_purchased_by_cust( err="Please enter the cust_id!" )
    cust_id = utils.clean_str( str(cust_id), strip=True )

    sql = sql_command.sql_purchased_by_cust.format( cust_id )
    return gen_response( sql, para, helper_funct=help_cate_purchased_by_cust )

''' Error msg for api endpoint "/category/purchasedByCustomer" '''
def help_cate_purchased_by_cust( err="Invalid Query!" ):
    msg = f'''
    {err}

Usage: /category/purchasedByCustomer

    cust_id: Customer ID to query
    {config.api_def_para_usage}
    '''
    return msg

## -------------------------------------------------- API Endpoints

if __name__ == '__main__':
    app.run( use_reloader=True, debug=True )
