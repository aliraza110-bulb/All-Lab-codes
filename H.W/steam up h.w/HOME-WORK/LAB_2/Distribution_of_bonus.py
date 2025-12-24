employees = {
   "Alice": 5,
   "Bob": 4,
   "Charlie": 3,
   "David": 2,
   "Eve": 5
}


def calculate_bonus(rating):
   if rating == 5:
       print('You got $1000')
   elif rating == 4:
       print('You got $750')
   elif rating == 3:
       print('You got $500')
   else:
       print('No bonus for you')


for name, rating in employees.items():
   print(f"Employee: {name} | Rating: {rating}")
   calculate_bonus(rating)


  
