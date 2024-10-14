## Enter the file_path to the file you want to clean
# The input file path is the path of the file you want to clean on your computer.
# forexample input_file_path = r"C:\Users\M D\Desktop\baby.xlsx"
InputFilePath  = r"C:\Users\M D\Desktop\df_cleaner\dirty_data.csv"

## Enter the name of the output file after the clean
# forexample output_file_name = "cleaned_data"
OutPutFileName = "cleaned"


## Enter Email columns  // ONLY SET IF YOU HAVE EMAILS COLUMNS OTHERWISE LEAVE EMPTY
# Add to the list below any email columns in your file 
#  MIND THE SPELLING 

EMAIL_COLUMNS = ["email"]

## Enter DATE columns  // ONLY SET IF YOU HAVE  DATE COLUMNS OTHERWISE LEAVE EMPTY
# Add to the list below any date columns in your file 
#  MIND THE SPELLING 
DATE_COLUMNS =[]



# take care of dates , date validator,different formats
# take care of number cols , currency, age 