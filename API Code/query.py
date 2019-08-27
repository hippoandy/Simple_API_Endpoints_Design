
import mysql.connector

import config

def db_connect():
    conn = mysql.connector.connect(
        host =      config.maria_host,
        port =      config.maria_port,
        user =      config.maria_user,
        passwd =    config.maria_passwd,
        db =        config.maria_db
    )
    cur = conn.cursor()
    return cur, conn


def sql_query( sql, page_num=None, page_size=None ):
    # get the connection
    cur, conn = db_connect()

    if( page_num is not None and page_size is not None ):
        # calculate number of documents to skip
        skips = page_size * (page_num - 1)
        # output data to file
        cur.execute( '''
            {} LIMIT {} OFFSET {}
        '''.format( sql, page_size, skips ) )
    else:
        cur.execute( sql )

    data = cur.fetchall()
    conn.close()

    return { "results": data, "total": cur.rowcount }, cur.description