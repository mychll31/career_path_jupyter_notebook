import csv
import glob
inputs = glob.glob("dataset/*.csv") 

# First determine the field names from the top line of each input file
# Comment 1 below
fieldnames = []
for filename in inputs:
  with open(filename, "r") as f_in:
    reader = csv.reader(f_in)
    headers = next(reader)
    for h in headers:
      if h not in fieldnames:
        fieldnames.append(h)

# Then copy the data    
with open("out2.csv", "a") as f_out:   # Comment 2 below
  writer = csv.DictWriter(f_out, fieldnames=fieldnames)
  writer.writeheader()
  for filename in inputs:
    with open(filename, "r") as f_in:
      reader = csv.DictReader(f_in)  # Uses the field names in this file
      for line in reader:
        # Comment 3 below
        writer.writerow(line)
        

writer = csv.DictWriter(open("out2.csv", 'a' ), fieldnames)
