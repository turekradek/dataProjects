import pandas as pd
import numpy as np
import requests
import os
import sys 
import json
import zipfile
import xlsxwriter
import psycopg2
from sqlalchemy import create_engine
import openpyxl

file_name = 'UsedCars/output.xlsx'
excel_file = pd.ExcelFile(file_name)

excel_sheets = excel_file.sheet_names 
print( excel_sheets)
df_excel = pd.read_excel(file_name)
print( df_excel.head(10))
    




if __name__ == '__main__':
    # if len(sys.argv) > 0:
    #     file_name = sys.argv[1]
    # else:
    #     file_name = 'output.xlsx'
    print( 'DONE')