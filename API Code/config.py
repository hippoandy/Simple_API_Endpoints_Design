

# database connection ------------------------------
maria_host = "127.0.0.1"
maria_port = 3306
maria_user = ""
maria_passwd = ""
maria_db = ""
# ------------------------------ database connection

# api settings -------------------------------------
api_ver = "v1"
api_head = "/api/{}".format( api_ver )
api_format = [ "json", "csv", "xml" ]
api_time_range = [ "day", "week", "month" ]

api_def_para_usage = '''
    page:   (Numeric) page number, value should be larger than 1              [default    1]
    size:   (Numeric) number of items per page, value should be larger than 1 [default   10]
    format: (Text) return data format, support JSON, CSV, and XML                  
                   Input: [ "json", "csv", "xml" ]                            [default json]
'''
# api settings -------------------------------------


encoding_utf8 = 'utf8'