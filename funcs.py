# imports 
import pandas as pd
import re
import numpy as np
from rich import  print as rprint
from streamlit import success
from  conf import InputFilePath, OutPutFileName, EMAIL_COLUMNS ,DATE_COLUMNS,FILE_EXPORT_TYPE
from dataclasses import dataclass


# Email regex expression for email validation
EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# Email regex expression for email validation


# Representation func
def repr(df:pd.DataFrame):
    """Prints out to the console some information of whats happening 

    Args:
        df (pd.DataFrame): pd.DataFrame 
    """
    print()
    print("Below are the column names and their data types in the file".upper())
    print(df.dtypes)
    print()
    print("Below is the overview of the first five entries of the file")
    print(df.head())

@dataclass    
class ReadData:
    """ Contains all methods that are applied when you read in data

    Returns:
        _type_: _description_
    """
    file_path:str
    # read data in func
    def read_data(self):
        """ uses pandas to read in data from an excel or csv file

        Args:
            file_path (str): path to excel or csv file 

        Returns:
            pd.DataFrame | None
        """
        try:
            file_type = self.file_path.split(".")[-1].lower()
            if file_type in ['xlsx', 'xlsm', 'xlsb', 'xls']:
                # Read Excel files using the appropriate engine if needed
                df =  pd.read_excel(self.file_path, engine='openpyxl' if file_type == 'xlsx' else None)
                read_status(df)
                fill_nans(df)
                repr(df)
                return df
            elif file_type == 'csv':
                # Read CSV files
                df = pd.read_csv(self.file_path)
                read_status(df)
                fill_nans(df)
                repr(df)
                return df
            elif file_type == 'txt':
                # Read tab-delimited files
                df =  pd.read_csv(self.file_path, delimiter='\t')
                read_status(df)
                fill_nans(df)
                repr(df)
                return df
            elif file_type == 'ods':
                # Read OpenDocument Spreadsheet
                df = pd.read_excel(self.file_path, engine='odf')
                read_status(df)
                fill_nans(df)
                repr(df)
                return df
            elif file_type == 'xml':
                # Read XML-based spreadsheets (if compatible)
                df =  pd.read_xml(self.file_path)
                read_status(df)
                fill_nans(df)
                repr(df)
                return df
            elif file_type in ['htm', 'html']:
                # Read HTML tables into DataFrame
                df =  pd.read_html(self.file_path)[0]  # Select the first table found
                read_status(df)
                fill_nans(df)
                repr(df)
                return df
            else:
                raise ValueError(f"Unsupported file format: {file_type}")
        except FileNotFoundError as e:
            print(f">>[Read failed]: The file doesn't exist. Check the input file path. Error:{e}")
        


def read_status(df:pd.DataFrame):
    """ prints out the read Status 

    Args:
        df (pd.DataFrame): Data frame we are reading 
    """
    print(">>[Read Successful]:", "Data had been read successfully")

# fills in any empty values
def fill_nans(df):
    """ Fills up any empty entries with np.nan
    Args:
        df (_type_): pandas Data frame its to fill 
    """
    df = df.fillna(np.nan)
    

# fix names func in df
def fix_names(df:pd.DataFrame):
    """Removes any extra spaces in the column/variable names and replaces them with underscores to keep them nice and nea.

    Args:
        df (pd.DataFrame):pd.Dataframe whose columns names/ variables are to be changed

    Returns:
        pd.Dataframe with modified names 
    """
    columns = df.columns
    new_names_list = []
    for name in columns:
        new_name  = name.strip()
        new_name = "_".join(re.findall(r"\w+",new_name))
        new_names_list.append(new_name.capitalize())
    
    df.columns = new_names_list
    rprint(f">>[Name conversion success]: Variable names have been fixed successfully:{df.columns.tolist()}")
    return df

# export data out func
def export(df:pd.DataFrame, file_name:str=OutPutFileName , export_file_type:str|None=FILE_EXPORT_TYPE): # type: ignore
    """ Exports your dataFrame to a csv the working directory of your choice

    Args:
        df (pd.DataFrame):pd.DataFrame to export
        file_name (str, optional): File name or pathfile to where to save the file 
        eg data.csv or directory/of.my/choice/data.csv
    """
    success_message = f">>[Save Successful]: The data has been saved in file name '{OutPutFileName}.csv' on your pc.."
    try:
        if export_file_type is not None:
            match export_file_type.strip().lower():
                case "csv":
                    df.to_csv(f"{file_name}.csv", index=False)
                    rprint(success_message)
                case "excel":
                    df.to_excel(f"{file_name}.xlsx", engine="openpyxl", index=False) 
                    rprint(f">>[Save Successful]: The data has been saved in file name '{OutPutFileName}.xlsx' on your pc..")
                case _ :
                    df.to_csv(f"{file_name}.csv", index=False)
                    rprint(success_message)
        else:
            df.to_csv(f"{file_name}.csv", index=False)
            rprint(f">>[Save Successful]: The data has been saved in file name '{OutPutFileName}' on your pc..")
            
    except (FileExistsError, Exception) as e:
            rprint(f">>[Save UnSuccessful]: There is an issue with the file your trying to save '{OutPutFileName}'. Check if the File already exists.")
            rprint(f">>[Save UnSuccessful Error]: {e}")
        
# fix emails vars func 
def fix_emails(x:str):
    """This method validates and fixes email addresses in an email column

    Args:
        x (_type_): Takes a str 

    Returns:
        str email
"""
    if is_valid_email(x):
        return x.strip()
    elif is_valid_email("".join(x.split(" "))):
        return "".join(x.split(" "))
    else:
        return np.nan
    

# fix strings func
def fix_words(x):
        if x != np.nan:
                new_name  = str(x).strip()
                new_name = " ".join(re.findall(r"\w+",new_name))
                return new_name.capitalize()
        else:
                return x


# fix numbers func 
def fix_numbers(x):
    if isinstance(x,(int,float)):
        return x
    elif x != np.nan:
        new_name = re.findall(r"\d+",x)
        new_number = int("".join([i for  i  in new_name]))
        return new_number
    else:
        return x


# emails validator func
def is_valid_email(email):
    """Checks the email str against a regex email string 

    Args:
        email (_type_):str from the dataframe column 

    Returns:
        _type_: bool True or False
    """
    return bool(re.match(EMAIL_PATTERN, email))

# indexer func
def indexing_df_columns(store_list, columns ,df:pd.DataFrame):
    """
        Gets the index of the given column in the dataframe 
    Args:
        store_list (_type_): list to store the index of the column 
        columns (_type_): name of the column whose index am storing 
        df (pd.DataFrame): pd.dataframe where am indexing the above 
    """
    try:
        for column in columns:
            column_index = df.columns.tolist()
            column_index = column_index.index(column)# type: ignore
            store_list.append(column_index)
    except Exception as e:
        print(f"Exception {e} has occured ")


# name tracker func         
def track_names(EMAIL_COLUMNS:list[str]|None, DATE_COLUMNS:list[str]|None , df:pd.DataFrame):
    """_summary_

    Args:
        EMAIL_COLUMNS (_type_): Email column names in the dataframe set in the conf.py file 
        DATE_COLUMNS (_type_): Date column names in the dataframe set in the conf.py file 
        df (pd.DataFrame): Dataframe which holds the above variables
    Returns:
        _type_: _description_
    """
    try:
        if df is not  None:
            email_column_indexes = []
            date_column_indexes=[]
            if EMAIL_COLUMNS is not None:
                indexing_df_columns(email_column_indexes,EMAIL_COLUMNS,df)
            
            if DATE_COLUMNS is not None:
                indexing_df_columns(date_column_indexes,DATE_COLUMNS,df)
            print(f"Tracked names indexes")
            rprint(email_column_indexes)
            rprint(date_column_indexes)
            return email_column_indexes, date_column_indexes
    except Exception as e:
            print(f"Error has occured")
            print()
            print(f"Error is :{e}")
            print(">>[DataFrame Error]: DataFrame cant be None. Check your dataframe or input_file_path...")
        
        


# date fixer func 
def fix_dates(x):
    raise NotImplementedError

# string column fixer func 
def fix_str_columns(df:pd.DataFrame, email_column_indexes, date_column_indexes):
    """This handles all the str manipulations to emails, dates, 

    Args:
        df (pd.DataFrame): _description_
        email_column_indexes (_type_): _description_
        date_column_indexes (_type_): _description_

    Returns:
        _type_: _description_
    """
    columns = df.select_dtypes(include="object").columns.to_list()
    emails = [df.columns.tolist()[index] for index in email_column_indexes]
    dates = [df.columns.tolist()[index] for index in date_column_indexes]
    print(f"list of all object dtype columns: {columns}")
    for column in columns:
        # print(f"List to compare emails:{emails} ---> current column:{column}")
        # print(f"List to compare dates:{dates} ---> current column:{column}")
        if column in emails: # type: ignore
            df[f"{column}"] = df[f"{column}"].apply(lambda x:fix_emails(x) ) 
            print(f"{column}:has been fixed successfully")
        elif column in dates:  # type: ignore
            df[f"{column}"] = df[f"{column}"].apply(lambda x:fix_dates(x) ) 
            print(f"{column}:has been fixed successfully")
        else:
            df[f"{column}"] = df[f"{column}"].apply(lambda x:fix_words(x) ) 
            print(f"{column}:has been fixed successfully")
            
    return df


def fix_number_columns(df:pd.DataFrame):
    for column in df.select_dtypes(include="number").columns:
        df[f"{column}"] = df[f"{column}"].apply(lambda x:fix_numbers(x)) 
    return df

if __name__ == "__main__":
    print(">>[INFO]: Running Funcs.py... The wrong file. Run Main.py...")