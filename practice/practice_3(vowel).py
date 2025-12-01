text = input("Enter the text: ").lower()

a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

for char in text:
    if char == "a":
        a_count += 1
    elif char == "e":
        e_count += 1
    elif char == "i":
        i_count += 1
    elif char == "o":
        o_count += 1
    elif char == "u":
        u_count += 1

print("A:", a_count)
print("E:", e_count)
print("I:", i_count)
print("O:", o_count)
print("U:", u_count)


        
