
# Utility to Remove extra Users from Larger directory to match user set with Verizon List

from asyncio.windows_events import NULL
from queue import Empty
import phonenumbers
from pickle import FALSE, TRUE
import csv
from pathlib import Path
import re



def phoneNumFormat(unformattedNum):
    # Sample phone number
    phone_number = unformattedNum

    # Remove any non-digit characters
    digits_only = re.sub(r"\D", "", phone_number)

    # Format the phone number
    formatted_number = re.sub(r"(\d{3})(\d{3})(\d{4})", r"(\1) \2-\3", digits_only)

    # Print the formatted number
    return formatted_number


workingFilePath= 'C:\\Users\\geoffe.elias\\OneDrive - Cephas Services LLC\\Dev\\source\\repos\\CSV_ReformatPhoneNum\\CSV_ReformatPhoneNum\\'

# This is the Verizon List of Mobile Numbers per each User
sourceFileName = "VerizonList.csv"
sourceFile=workingFilePath+sourceFileName

# This is the Current User Directory Information of each User with their listed Work, Home, and Mobile Phone Number (downloaded from Admin.Google)
currentDataFileName = "GoogleDataSet.csv"
currentDataSet=workingFilePath+currentDataFileName

# Working combined directory/file path (OS-Dependent currently)
outputFileName = "report.csv"
outputFile=workingFilePath+outputFileName


# source_DataSet=[]
  
with open(sourceFile, 'r', newline='\r\n') as source, open(outputFile, 'w', newline='') as result: 
    rdr=csv.reader(source)  #
    wtr=csv.writer(result)             
    for row in rdr:
        formattedNum=phoneNumFormat(row[1]) 
        wtr.writerow([row[0],row[1],formattedNum]) # Write the elements of the source file to the output file.

    result.close();

print("Operation completed") 