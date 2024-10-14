from funcs import *
def main():
    # read in data frame 
    df: pd.DataFrame | None = ReadData(InputFilePath).read_data() # type: ignore
    print() # create space for print out df column types
    
    # Tracking some column names
    email_column_indexes , date_column_indexes,currency_column_indexes = track_names(EMAIL_COLUMNS, DATE_COLUMNS,CURRENCY_COLUMNS,df) #type: ignore
    
    # Fixing df column names 
    df = fix_names(df) # type: ignore
    
    # fixing columns in the df 
    df = fix_str_columns(df,email_column_indexes,date_column_indexes,currency_column_indexes)
    
    # Clearing tracked columns stores  
    email_column_indexes.clear()
    date_column_indexes.clear()
    currency_column_indexes.clear()
    
    # print()
    # print("Select the columns that are numeric: ")
    # for option, column in enumerate(df.columns,start=1): #type: ignore
    #     print(f"{option}: {column}")

    # df=fix_number_columns(df) # type: ignore
    print()
    
    # displaying the output of the cleaning after text cleaning 
    rprint(df.head()) # type: ignore
    
    # Exporting the dataframe 
    export(df)
    print()
    
    
if __name__ =="__main__":
    if (OutPutFileName is None ) or (InputFilePath is None):
        rprint("Go to the conf.py file and Enter the input file name and output file name")
    else:
        main()