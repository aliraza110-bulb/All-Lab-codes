record="STU|Steamup|AGE:22|GPA=3.44|DEPT-CS|CGPA-3.51|sem-7|credit_hour =70.00|roll number=40"
name = record.split("|")[1]
age = int(record[record.index("AGE:") + 4 :record.index("|GPA")])
gpa = float(record[record.index("GPA=") +4 : record.index("|DEPT")])
cgpa = float(record[record.index("CGPA-") +5 : record.index("|sem")])
semester = int(record[record.index("sem-") +4 : record.index("|credit")])
credit_hour=float(record[record.index("hour =") +6 : record.index("|roll")])
print("\tname : ",name,
      "\n\tage : ",age,
      "\n\tgpa : ",gpa,
      "\n\tCgpa : ",cgpa,
      "\n\tsemesters : ",semester,
      "\n\tcredit_hour : ",credit_hour)

convert_gpa=gpa/4*100
print("GPA in percent",convert_gpa)