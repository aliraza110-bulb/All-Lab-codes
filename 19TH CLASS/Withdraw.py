def withdraw(balance,amount):
    if amount> balance:
        raise Exception ('insufficient balance')
    else:
        balance -= amount
        return balance
try:
    currentbalance=500
    withdraw_amount=600
    new_balance=withdraw(currentbalance,withdraw_amount)
    print('withdraw successfull',new_balance)
except Exception as e:  
    print(e)

# yai simple hai jaisai pichle mai yai istemal kiya tha
# except ZeroDivisionError:
#     print('num can not divide by zero')

while True:
    exit_choice=('type exit to stop else enter')
    if exit_choice == 'exit':
        break
    
