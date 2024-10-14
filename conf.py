########################### Watch the type data types of your input ######################################
## Enter the file_path to the file you want to clean
# The input file path is the path of the file you want to clean on your computer.
# forexample input_file_path = r"C:\Users\M D\Desktop\baby.xlsx"


# [Optional]: Input file export type eg "csv" for a comma seperated file or "Excel" for xlsx,xlms, xls etc.
# returns a csv file by default if not set to anything.

InputFilePath:str  = r"C:\Users\M D\Desktop\Data_Cleaning_micro_1\dirty_data.csv"
OutPutFileName:str= "Cleaned_data"

FILE_EXPORT_TYPE:str|None = None
###############################################################################################################

# // ONLY SET IF YOU HAVE COLUMNS THAT MEET THAT COLUMN TYPE OTHERWISE LEAVE EMPTY
# Add to the list below any email columns in your file 


EMAIL_COLUMNS: list[str|None] = ["email"]
DATE_COLUMNS: list[str|None] =["signup_date"]  
AGE_COLUMNS: list[str|None] =[]   # Not implemented yet
CURRENCY_COLUMNS: list[str|None] =["income"]  
ID_COLUMNS: list[str|None] =[]    # Not implemented yet


###############################################################################################################
"""
Age or Date Fields: Ensure valid ranges (e.g., no negative age).
Currency: Standardize to a specific currency for uniformity.
Percentages: Ensure they fall between 0 and 100.
IDs or Phone Numbers: Check for duplicates or invalid formats.
Timestamps: Ensure proper time zone handling when applicable.
"""

# take care of dates , date validator,different formats
# take care of number cols , currency, age 


if __name__ == "__main__":
    print(f">>[INFO]: Your running Conf.py..")
    print(f">>[INFO]: Your running Conf.py..")
    print(f">>[INFO]: Your running Conf.py..")
    print(f">>[INFO]: Run the main.py NOT Conf.py..")