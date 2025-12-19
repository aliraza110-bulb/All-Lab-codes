import csv
fields=['NAME','BRANCH','YEAR','CGPA']
rows=[['Nikhil','COE',2,9.0],
      ['Sanchit','COE',2,9.1],
      ['Aditya','IT',2,9.3],
      ['Sagar','SE',1,9.5],
      ['Prateek','MCE',3,7.8],
      ['Sahil','EP',2,9.1]]

filename="/home/steampup-qbh/Desktop/ALI_RAZA_XA/all-lab-codes/student.csv"

with open(filename,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header=next(csvreader)
    for row in csvreader:
        print(row)