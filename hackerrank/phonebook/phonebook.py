# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

# read an integer to get the number of entries into the phonebook
numRecords=None
for line in sys.stdin:
    entry = line.rstrip()
    try:
        numRecords = int(entry.split(' ')[0])
        break
    except:
        # try again to get _only_ an integer input
        pass

# loop the records count and add the phone numbers
phoneBook = {}
for line in sys.stdin:
    entry = line.rstrip()
    if not re.match("^\w+\s+\d{8}$", entry):
        # input does not match '<name> <phonenumber - 8 digit> so try again
        print("try again")
        continue
    phoneBook[entry.split(' ')[0]] = entry.split(' ')[1]
    if len(phoneBook) >= numRecords:
        break

# read forever queries to the phonebook
for line in sys.stdin:
    if line == "\n":
        break
    entry = line.rstrip()
    number = phoneBook.get(entry.split(' ')[0], None)
    if not number:
        print("Not found")
    else:
        print(f"{entry.split(' ')[0]}={number}")
