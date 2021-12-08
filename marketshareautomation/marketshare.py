# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 08:20:24 2021

@author: WoutKonings
"""

"""
requirements:
    pygsheets
    pandas
    base64
    datetime
    time
    
"""

from snowflake_module import Snowflake
from queries import  get_data, exist_query
import datetime

def write_sheets():
    
    #log time
    now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    print(f"Start executing marketshareautomation at {now}")
    
    sf = Snowflake()
    
    sf.set_cursor(warehouse='WM_BENELUX_SANDBOX_WH_M', 
                  database='WM_BENELUX_SANDBOX', 
                  schema='WOUT_K')
    
    max_date = sf.query_pandas(exist_query)
    max_date = str(max_date.iloc[0,0])
    get_data_new = get_data.replace('DATE_REPLACE', max_date)
    
    sf.set_cursor(warehouse='WM_BENELUX_SANDBOX_WH_M', 
                  database='DF_PROD', 
                  schema='DAP')
    shares = sf.query_pandas(get_data_new)
    
    
    
    sf.write_data(df=shares, 
                  warehouse = 'WM_BENELUX_SANDBOX_WH_M', 
                  database='WM_BENELUX_SANDBOX', 
                  schema='WOUT_K', 
                  table_name = 'MARKET_SHARE_WM_BENELUX')
    
    now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    print(f"Code executed normally at {now}" )

if __name__ == "__main__":
    
    write_sheets()
    
    
    #Query the data
    
    