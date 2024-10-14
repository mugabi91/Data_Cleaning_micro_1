from funcs import *
def main():
    df: pd.DataFrame | None = read_data(InputFilePath) # type: ignore
    print()
    email_column_indexes , date_column_indexes = track_names(EMAIL_COLUMNS, DATE_COLUMNS, df) # type: ignore
    df = fix_names(df) # type: ignore
    df = fix_str_columns(df,email_column_indexes,date_column_indexes)
    # print()
    # print("Select the columns that are numeric: ")
    # for option, column in enumerate(df.columns,start=1): #type: ignore
    #     print(f"{option}: {column}")
        
    df=fix_number_columns(df) # type: ignore
    print()
    rprint(df.head()) # type: ignore
    export(df)
    print()
    
    
if __name__ =="__main__":
    if (OutPutFileName is None ) or (InputFilePath is None):
        rprint("Go to the conf.py file and Enter the input file name and output file name")
    else:
        main()