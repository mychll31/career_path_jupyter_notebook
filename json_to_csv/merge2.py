import glob
import csv


# Open result file
with open('out.csv','wb') as fout:
    wout = csv.writer(fout,delimiter=',') 
    interesting_files = glob.glob("dataset/*.csv") 
    for filename in interesting_files: 
        print 'Processing',filename 
        # Open and process file
        h = True
        with open(filename,'rb') as fin:
            rows = fin.next()
            print(rows)
            if h:
                h = False
            else:
                fin.next()#skip header
            for line in csv.reader(fin,delimiter=','):
                wout.writerow(line)
