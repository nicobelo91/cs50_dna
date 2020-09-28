from cs50 import get_int
import sys
import csv
import re

# Check if command line is complete
if len(sys.argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    sys.exit(1)
# Open csv file and read into memory
csvfile = open("small.csv","r")
# Open dna sequence txt file, read into memory
dnasequence = open()

# For each STR compute the longest run of consecutive repeats


# Save STR counts into a data structure
writer = csv.writer(file)
# Compare the STR counts against each row in CSV file
if match:
    print("Lavender")
else:
    print("No Match")

"""
s = "AASDASDDAAAAAAAAERQREQREQRAAAAREWQRWERAAA"

groups = re.findall(r'(?:AA)+', s)
print(groups)
# ['AA', 'AAAAAAAA', 'AAAA', 'AA']

largest = max(groups, key=len)
print(len(largest) // 2)
# 4
"""
csvfile.close()
dnasequence.close()