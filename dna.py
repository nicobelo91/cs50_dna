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
    with open(f"{sys.argv[1]}",'r') as csvfile:
        database = csv.reader(csvfile)
        list_of_headers = next(database)[1:]
        
         # Open dna sequence txt file, read into memory
        with open(f"{sys.argv[2]}",'r') as dnasequence:
        
            # Search in the database:
            sequence = csv.reader(dnasequence)
            # Save STR counts into a data structure
            for dna in sequence:
                # Convert dna list into a string
                listToString = ''.join([str(elem) for elem in dna])
                dnaGroup = [substring_length(listToString, header) for header in list_of_headers]
                
                print_name(database,dnaGroup)

# For each STR compute the longest run of consecutive repeats                
def substring_length(string, substring):        
    # Search for AGATC
    substring = re.findall(r'(?:{substring})+', string) # Doesn't read the value of {substring}
    #print(AGATC)
    print(substring)
    largest = max(substring, key=len)
    #print(len(largestAGATC) // 5)
    return ((len(largest) // len(substring)))
                
def print_name(database,dnaGroup):
    for row in database:
        person = row[0]
        values = [val for val in row[1:]]
        if values == dnaGroup:
            print(person)
            return
        print("No match")
        
main()