data=[10,'20',None,'hello',30]

for i in data:
    try:
        print(int(i))
    except Exception as e:
        print(e)
