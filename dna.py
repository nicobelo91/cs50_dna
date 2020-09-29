from cs50 import get_int
import sys
import csv
import re

# Check if command line is complete
if len(sys.argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    sys.exit(1)
# Open csv file and read into memory
with open(f"{sys.argv[1]}",'r') as csvfile:
    database = csv.reader(csvfile)    
    #list_of_rows = list(csvfile)
    #print(list_of_rows)
        #for row in range(1,len(text)):
            #print(text)
# Open dna sequence txt file, read into memory
    with open(f"{sys.argv[2]}",'r') as dnasequence:
    
        # For each STR compute the longest run of consecutive repeats
    
        # Search in the database:
        sequence = csv.reader(dnasequence)
        # Save STR counts into a data structure
        str_list = {}
        for dna in sequence:
            # Convert dna list into a string
            listToString = ''.join([str(elem) for elem in dna])
            
            # Search for AGATC
            AGATC = re.findall(r'(?:AGATC)+', listToString)
            #print(AGATC)
        
            largestAGATC = max(AGATC, key=len)
            #print(len(largestAGATC) // 5)
            str_list['AGATC'] = (len(largestAGATC) // 5)
            
            # Search for AATG
            AATG = re.findall(r'(?:AATG)+', listToString)
            #print(AATG)
        
            largestAATG = max(AATG, key=len)
            #print(len(largestAATG) // 4)
            str_list['AATG'] = (len(largestAATG) // 4)
        
            # Search for TATC
            TATC = re.findall(r'(?:TATC)+', listToString)
            #print(TATC)
        
            largestTATC = max(TATC, key=len)
            #print(len(largestTATC) // 4)
            str_list['TATC'] = (len(largestTATC) // 4)
    
    # For each row in the data check if each str count matches
    nameoflist = {}
    for text in csvfile:
        nameoflist["my_list" + str(text)] = text.split(",")
    #list_of_people = list(csvfile)
    #my_list = list_of_people.split(",")
    
    # if so, print the person's name
    """
    # Compare the STR counts against each row in CSV file
    with open(f"{sys.argv[1]}") as csvfile:
        database = csv.reader(csvfile)    
        for row in csvfile:
    
    if match:
        print("Lavender")
    else:
        print("No Match")
    """
