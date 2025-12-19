import csv
fields=['NAME','BRANCH','YEAR','CGPA']
rows=[['Nikhil','COE',2,9.0],
      ['Sanchit','COE',2,9.1],
      ['Aditya','IT',2,9.3],
      ['Sagar','SE',1,9.5],
      ['Prateek','MCE',3,7.8],
      ['Sahil','EP',2,9.1]]
filename="student.csv"
with open(filename,'w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)