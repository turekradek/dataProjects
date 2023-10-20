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

folders_tree = {}
# where = os.getcwd() 
# ################
# def check_json_keys(file_path):
#     with open(file_path) as f:
#         data = json.load(f)
#     if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
#         keys = data[0].keys()
#         return keys
#     else:
#         return None

# def insert_data_to_table(cur, conn, data, keys_in_json):
#     try:
#         placeholders = ', '.join(['%s'] * len(keys_in_json))
#         columns = ', '.join(keys_in_json)
        
#         for item in data:
#             values = [item[key] for key in keys_in_json]
#             print(f'Inserting: {", ".join(map(str, values))}')
            
#             query = f"INSERT INTO wyniki ({columns}) VALUES ({placeholders})"
#             cur.execute(query, values)
#         conn.commit()
#     except Exception as e:
#         print("Error occurred while inserting data:", e)


# # connection to postgres database
# conn = psycopg2.connect(
#         host = "localhost",
#         port = "5432" ,
#         dbname = "postgres",
#         user='postgres' ,
#         password = "radek" 
#         )
# cur = conn.cursor()

# # create table if it doesn't exists
# cur.execute("""
#             CREATE TABLE IF NOT EXESTS xxxxxx(
#                 columna1 TEXT,
#                 COLUMN2 INTEGER,
#                 COLUMN3 TEXT
#             )
#             """)
# conn.commit()

# # Open the JSON file and load the data
# with open('data3.json') as f:
#     data = json.load(f) 
# # Usage example
# json_file_path = 'data3.json'
# keys_in_json = check_json_keys(json_file_path)

# if keys_in_json:
#     with open(json_file_path) as f:
#         data = json.load(f)
#     insert_data_to_table(cur, conn, data, keys_in_json)

# # Select and print first 5 rows in the table
# try:
#     cur.execute("SELECT * FROM wyniki  LIMIT 5")
#     rows = cur.fetchall()
#     print("First 5 rows in the table:")
#     for row in rows:
#         print(row)
# except Exception as e:
#     print("Error occurred while selecting data:", e)

# conn.commit()
# conn.close()
# ####################
dict_pattern_files = '{{}}:{{}}'
folders_tree = {
    
}
def find_folders( path: str ) -> bool:
        folders_list = os.listdir( path )
        if 'rekrutacjazuza' in folders_list  :
            gdzie = folders_list.index("rekrutacjazuza")
            folders_list.pop(gdzie)
        print( f'11111 folders_list: %s' % folders_list )
        folders_list = choose_folders(folders_list, path) ROZLACZ SCIEZKI WEZ TYLKO NAZWY FOLDEROW
        print( f'11111 folders_list: %s' % folders_list )
        for folder in folders_list:
            if os.access( folder, os.W_OK ) and os.path.isdir(folder) and (not folder.startswith(".")):
                print( f'*** folder: %s' % folder )
                # folders_tree[folder] = ''
                content_this_folder = show_folder_content(folder, path)
                print( f'*** content_this_folder: %s' % content_this_folder )
                
                print(f'-->  {folders_tree}   <--')  
                # folders_tree[folder]["content"] = temporary_dict
                folders_regular = choose_folders( folder, path)
                print( f'========folders_regular==={folder}========{folders_regular}    ===================')
                folders_zip = choose_folders_zip( folder, path)
                # print( f'========folders_zip==={folder}========{folders_zip}    ===================')
                # files_list = chose_files( folder, path)
                # print( f'========files_list===={folder}======={files_list}    ===================')
                # files_list_txt = choose_files_txt( folder, path)
                # print( f'========files_list_txt===={folder}======={files_list_txt}    ===================')
                # files_list_json = choose_files_json( folder, path)
                # print( f'========files_list_json==={folder}========{files_list_json}    ===================')
                # files_list_csv = choose_files_csv( folder, path)
                # print( f'========files_list_csv===={folder}======={files_list_csv}    ===================')
                # folder_content = os.listdir( folder )
                # print( f'folder_content: %s' % folder_content )
                # show_folder_content( folder, path )
                temporary_dict = { f"{folder}" : {
                    "content": content_this_folder,
                    "folders_regular": folders_regular,
                    # "folders_zip": folders_zip,
                    # "files_list": files_list,
                    # "files_list_txt": files_list_txt,
                    # "files_list_json": files_list_json,
                    # "files_list_csv": files_list_csv,
                    }
                }
                folders_tree[folder] = temporary_dict
                print( '------folders_tree-----------')                
                print(f'-->  {folders_tree}   <--')                
                print( '-----------------')  
                temporary_dict.clear()
        # folders_tree[folder]["content"] = content_this_folder                
        # folders_tree[folder]["regular"] = folders_regular                
        # folders_tree[folder]["zip"] = folders_zip                
        # folders_tree[folder]["files_all"] = files_list                
        # folders_tree[folder]["files_txt"] = files_list_txt                
        # folders_tree[folder]["files_json"] = files_list_json                
        # folders_tree[folder]["files_csv"] = files_list_csv                
        print( '------folders_tree----------------------------------------------')                
        print( folders_tree)                
        print( '-----------------')                      

def show_folder_content(folder: str, path: str ) -> list:
        print( f'*******show_folder_content****start*****************')
        path = os.path.join( path, folder)
        folder_content = os.listdir( path )
        print( f'path show_folder_content :                 %s ' % path )
        print( f'folder_content : %s' % folder_content)
        # print( f'\t\t\tfolder_content: %s' % folder_content )
        # if 'rekrutacjazuza' in folder_content:
        #         gdzie = folder_content.index("rekrutacjazuza")
        #         folder_content.pop(gdzie)
        # folders = choose_folders( folder_content, path)
        # files = chose_files( folder_content, path)
        # files_txt = choose_files_txt( folder_content, path)
        # files_json = choose_files_json( folder_content, path)
        # files_csv = choose_files_csv( folder_content, path)
        # print( f' folders {folders} ')
        # print( f' files {files} ')
        # print( f' files_txt {files_txt} ')
        # print( f' files_json {files_json} ')
        # print( f' files_csv {files_csv} ')
        print( f'*******show_folder_content****stop*****************')
        return folder_content

def choose_folders(content_folder: list, path: str) -> list:
        print( f'*******choose_folders****start******{content_folder}***********')
        folders_only = []
        for folder in content_folder:
            if os.path.isdir(folder) and (not folder.startswith(".")):
                folder_path = os.path.join(path, folder)
                if os.path.isdir( folder_path) == True  and  (not folder_path.endswith(".zip")):
                        folders_only.append( folder_path )
        print( f'*******choose_folders****STOP*****************')                
        return folders_only

def choose_folders_zip(content_folder: list, path: str) -> list:
        print( f'*******choose_folders_zip****start*****************') 
        folders_zip = []
        for folder in content_folder:
                folder_path = os.path.join(path, folder)
                if os.path.isdir( folder_path) and folder_path.endswith(".zip"):
                        folders_zip.append( folder_path )
        print( f'*******choose_folders_zip****STOP*****************')                 
        return folders_zip

def chose_files(content_folder: list,  path: str) -> list:
        print( f'*******chose_files****start*****************')
        files_only = []
        for object in content_folder:
                path = os.path.join(path,object)
                if os.path.isfile(object):
                        files_only.append( object )
        print( f'chose_files func : {files_only}')
        print( f'*******chose_files****STOP*****************')
        return files_only

def choose_files_txt(files_list: list,  path: str) -> list:
        files_txt = []
        for file in files_list:
                path = os.path.join(path,file)
                if os.path.isfile(file) and file.endswith('.txt'):
                        files_txt.append(file)
        print( f'choose_files_txt func : {files_txt}')                
        return files_txt 

def choose_files_json(files_list: list,  path: str ) -> list:
        files_json = []
        for file in files_list:
                path = os.path.join(path,file)
                if os.path.isfile(file) and file.endswith('.json'):
                        files_json.append(file)
        print( f'choose_files_json func : {files_json}')                 
        return files_json 

def choose_files_csv(files_list: list,  path: str) -> list:
        files_csv = []
        for file in files_list:
                path = os.path.join(path,file)
                if os.path.isfile(file) and file.endswith('.csv'):
                        files_csv.append(file)
        print( f'choose_files_csv func : {files_csv}')                     
        return files_csv 

def csv_to_json(csv_file: str) -> dict:
        pass

def read_columns_from_file( file_name: str, separator:str ) -> list:
        file = open( file_name , 'r' )
        columns = file.readline().strip()
        print(f'1 columns {columns}')
        columns = columns.split( separator )
        print(f'2 columns {columns}')
        return columns 

def create_dictionary(  columns: list ):
        dictionary = {}
        for name in columns:
                dictionary[name] = name
        return dictionary

def create_data( file_name: str, dictionary: dict ):
        file = open( file_name ,  'r' )
        content = [  line. strip() for line in  file.readlines() ]
        content = content[1:]    
        data = []
        keys = list( dictionary.keys() )
        print( f'\n\n\nkeys: {keys}')
        for index, linia in enumerate(content):
                resutl = {}
                linia = linia.split(';')
                print( f'linia : {linia}')
                for element in linia:
                        resutl[keys[0]] = linia[0]
                # print( f'=== 0 resutl {resutl }')
                resutl[keys[1]] = linia[1]
                # print( f'=== 1 resutl {resutl }')
                resutl[keys[2]] = linia[2]
                # print( f'=== 2 resutl {resutl }')
                resutl[keys[3]] = linia[3]
                # print( f'=== 3 resutl {resutl }')
                data.append( resutl ) 
                # print( f' index {index} \n data _+_+_+_+_+ {data}' )
                result = {}
        print( data, f'\n\n {len(data)}' )
        return  data 

def unzip_folder(path: str, folder_name: str):
    path_joined = os.path.join(path, folder_name)
    extracted_dir = folder_name.replace('.zip', '')
    path_extracted_dir = os.path.join(path, extracted_dir)
    with zipfile.ZipFile(path_joined, 'r') as zip_directory:
        zip_directory.extractall( path_extracted_dir )

directory = r'Kierowcy.txt'
# columns = read_columns_from_file( file_to_read, ';')
# print( ' these are columns from txt file {}'.format(columns) )
# dictionary = create_dictionary( columns ) 
# print( f' dictionar {dictionary}')
# data =  create_data(directory, dictionary )

def file_to_json(filename: str, data: dict):
        # Write the data to a JSON file
        with open(f'{filename}.json', 'w') as f:
                json.dump(data, f) 

def csv_to_json_via_df(csv_file: str, separator: str) -> str :
        df_from_csv_file = pd.read_csv(csv_file, delimiter=separator) 
        print( f'11 df_from_csv_file: {type(df_from_csv_file)}')
        df_from_csv_file_json = df_from_csv_file.to_json()
        print( f'22 df_from_csv_file_json: {type(df_from_csv_file_json)}')
        print( f'\n\n\n  {df_from_csv_file_json[:300]}')
        print( f'\n\n\n  {df_from_csv_file_json[-20:]}')
        file_to_write = csv_file.split('.')[0] + '.json'
        print( f'33 file_to_write: {type(file_to_write)} - {file_to_write}')
        result = json.loads(r'{"callno":{"0":"HP160970008","1":"P161000007","2":"P160992496","3":"P160992494","4":"P160992493"}}')
        result = json.loads(df_from_csv_file_json)
        print( f'44 result: {type(result)} ')
        with open(f'{file_to_write}.json', 'w') as f:
                json.dump(result, f) 


                
if __name__ == "__main__":
        print( f"Here you have arguments : \n {sys.argv}")
        where = os.getcwd() 
        # print(f'where : {where}')
        # find_folders( where)
        path_to_folder = sys.argv[1].strip()
        find_folders( path_to_folder )
        # file_to_read = sys.argv[1].strip()
        # print( f"==== file_to_read : {file_to_read}")
        # path_to_write = '/'.join(sys.argv[1].split('/')[:-1])
        # print( f"==== path_to_write : {path_to_write}")
        # columns = read_columns_from_file( file_to_read, ',')
        # print( f"==== columns : {columns}")
        # dictionary = create_dictionary( columns ) 
        # print( f"==== dictionary : {dictionary}")
        # # data =  create_data(file_to_read, dictionary )
        # # print( f"==== data TYPE  : {type(data)}")
        # file_to_write = file_to_read.split('.')[0] + '.json'
        # csv_to_json_via_df(file_to_read, ',')
        # file_to_json( file_to_read, data)
        # unzip_folder( sys.argv[1], sys.argv[2])