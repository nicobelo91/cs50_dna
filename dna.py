from cs50 import get_int
import sys
import csv
import re

# Check if command line is complete
if len(sys.argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    sys.exit(1)
# Open csv file and read into memory
#with open("databases/small.csv") as csvfile:
# Open dna sequence txt file, read into memory
with open(f"{sys.argv[2]}") as dnasequence:

    # For each STR compute the longest run of consecutive repeats

    # Search in the database:
    database = csv.reader(dnasequence)
    #database = "AGATCASDASDSAFGFDGGFAGATC"
    for dna in database:
        # Convert dna list into a string
        listToStr = ''.join([str(elem) for elem in dna])
        
        # Search for AGATC
        AGATC = re.findall(r'(?:AGATC)+', listToStr)
        print(AGATC)
    
        largest = max(AGATC, key=len)
        print(len(largest) // 4)
        
        
    """
    # Search for AATG
    AATG = re.findall(r'(?:AATG)+',database)
    print(AATG)

    largest = max(AATG, key=len)
    print(len(largest) // 2)

    # Search for TATC
    TATC = re.findall(r'(?:TATC)+',database)
    print(TATC)

    largest = max(TATC, key=len)
    print(len(largest) // 2)

    # Save STR counts into a data structure
    #writer = csv.writer(file)
    """
    # Compare the STR counts against each row in CSV file
    """
    if match:
        print("Lavender")
    else:
        print("No Match")
    """
