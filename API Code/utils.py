
from io import BytesIO, StringIO
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import json
import csv
import datetime
# import textwrap

import config

def del_space( txt ):
    return txt.strip()

def del_spec_char( txt ):
    return txt.replace( '\n', '' ).replace( '\r', '' ).replace( '\t', '' )

def clean_str( txt, strip=False ):
    txt = txt.replace( "\"", "" ).replace( "'", "" )
    txt = del_spec_char( txt )
    return txt if( strip ) else del_space( txt )

# convert sql result to json
def get_json( res, desc ):
    return [ dict(zip([key[ 0 ] for key in desc], row)) for row in res[ "results" ] ]

# get current timestamp, prevent duplicate program statements
def get_current():
    current_time = datetime.datetime.now()
    return {
        "dt_obj": current_time,
        "date": current_time.strftime( "%Y/%m/%d" ),
        "time": current_time.strftime( "%H:%M:%S" )
    }

# output sql result to json format
def sql_to_json( res, desc ):
    # get the data in json format
    data = get_json( res, desc )
    # get current date, time
    cur_time = get_current()

    return json.dumps(
        {
            "api_version": config.api_ver,
            "encoding": config.encoding_utf8,
            "query_date": cur_time[ "date" ],
            "query_time": cur_time[ "time" ],
            "num_of_results": res[ "total" ],
            "results": data 
        },
        default=str
    )

# output sql result to xml format
def sql_to_xml( res, desc ):
    # sub-funct to create xml section
    def create_sub( parent, name, text ):
        if( ' ' in str(name) ): name = str(name).replace( ' ', '_' )
        if( '(' in str(name) ): name = name.replace( '(', '' )
        if( ')' in str(name) ): name = name.replace( ')', '' )
        SubElement( parent, name ).text = str(text)

    # get current date, time
    cur_time = get_current()

    # get the data in json format
    data = get_json( res, desc )
    # transform to xml format
    top = Element( 'root' )
    top.set( 'api_version', config.api_ver )
    top.set( 'encoding', config.encoding_utf8 )
    top.set( 'query_date', cur_time[ "date" ] )
    top.set( 'query_time', cur_time[ "time" ] )
    create_sub( top, 'num_of_results', res[ "total" ] )
    container = SubElement( top, 'results' )
    for d in data:
        row = SubElement( container, 'row' )
        for k in d.keys(): create_sub( row, k, d[ k ] )
    # include the option "encoding" will create the xml declaration
    # the xml declaration is import for the response to determine the mimetype
    return( ElementTree.tostring( top, encoding=config.encoding_utf8, method='xml' ).decode() )

# output sql result to csv format (Q6)
def sql_to_csv( res, desc ):

    data = get_json( res, desc )

    header = [ x[ 0 ] for x in desc ]

    csv_data = ','.join( header ) + '\n'
    for d in data:
        row = ",".join( [str(v) for v in d.values()] )
        csv_data += row + '\n'
    return csv_data
