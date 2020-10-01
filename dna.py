from cs50 import get_int
import sys
import csv
import re

def main():
from cs50 import get_int
import sys
import csv
import re


def main():
    # Check if command line is complete
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)
    # Open csv file and read into memory
    csvfile = open(f"{sys.argv[1]}", 'r')
    database = csv.reader(csvfile)
    list_of_headers = next(database)[1:]
        
    # Open dna sequence txt file, read into memory
    with open(f"{sys.argv[2]}", 'r') as dnasequence:
    
        # Search in the database:
        sequence = dnasequence.read()
        #sequence = csv.reader(dnasequence)
        # Save STR counts into a data structure
        dnaGroup = [substring_length(sequence, header) for header in list_of_headers]
            
        print_name(database, dnaGroup)
    csvfile.close()

# For each STR compute the longest run of consecutive repeats     


def substring_length(string, substring):
    count = 0  # Number of times that the substring is repeated
    pattern = substring
    while pattern in string:
        count += 1
        pattern += substring
    return count
                
                
def print_name(database, dnaGroup):
    for row in database:
        person = row[0]
        values = [int(val) for val in row[1:]]
        if values == dnaGroup:
            print(person)
            return
    print("No match")
    
    
main()