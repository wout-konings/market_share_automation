# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 08:57:50 2021

@author: WoutKonings
"""


#!/usr/bin/env python
import snowflake.connector
from snowflake.connector import ProgrammingError
from snowflake.connector.pandas_tools import write_pandas
import time
import os
from creds import sf_username, sf_password

# sf_username = os.environ.get('SF_USERNAME_ENV')
# sf_password = os.environ.get('SF_PASSWORD_ENV')


class Snowflake():
    
    
    def __init__(self):
        
        self.connect()
        
    
    def connect(self):
        
        self.conn = snowflake.connector.connect(
            user=sf_username,
            password=sf_password,
            account='wmg-datalab',
            authenticator='https://wmg.okta.com'
            )
        self.cursor = self.conn.cursor()
        #Gets the version
        try:
            self.cursor.execute("SELECT current_version()")
            one_row = self.cursor.fetchone()
            print("Connection established. Version= " +  str(one_row[0]))
        except:
            pass
        # self.ctx.close()
    
    def close(self):
        self.conn.close()
    
    def set_cursor(self, warehouse, database, schema):
        self.cursor.execute(f"USE WAREHOUSE {warehouse}")
        self.cursor.execute(f"USE DATABASE {database}")
        self.cursor.execute(f"USE SCHEMA {schema}")
        
    
    def query(self, query):
        self.cursor.execute(query)
        try:
            query_id = self.cursor.sfqid
            print('start query')
            print(self.conn.is_still_running(self.conn.get_query_status_throw_if_error(query_id)))
            while self.conn.is_still_running(self.conn.get_query_status_throw_if_error(query_id)):
                print('Still querying')
                print(self.conn.get_query_status_throw_if_error(query_id))
                time.sleep(1)
            print('Query ready')
        except ProgrammingError as err:
            print('Programming Error: {0}'.format(err))
    
    def query_pandas(self, query):
        self.query(query)
        df = self.cursor.fetch_pandas_all()
        return df
    
    def query_table(self, table_name):
        
        query = 'SELECT * FROM ' + table_name
        return self.query_pandas(query)
        
    
    def write_data(self, 
                            df, 
                            warehouse,
                            database,
                            schema,
                            table_name,
                            steps = 1000):
        
        self.set_cursor(warehouse=warehouse, 
                        database=database,
                        schema=schema
                        )
        
        for i in range(0, len(df), steps):
            check = write_pandas(conn=self.conn, 
                             df=df.iloc[i:i+steps, :], 
                             table_name=table_name,
                             database=database,
                             schema=schema)
            print(str(i) + ": " + str(check))
        
    
if __name__ == "__main__":
    
    sf = Snowflake()
    sf.set_cursor(warehouse="WM_BENELUX_SANDBOX_WH_M", 
                  database="WM_BENELUX_SANDBOX",
                  schema="WOUT_K"
                  )
    
    sf.close()
    
    
    
    
