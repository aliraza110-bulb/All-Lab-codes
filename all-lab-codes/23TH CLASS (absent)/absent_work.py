import re
String = "a quick brown fox jumps over the lazy dog"
pattern = r"brown.fox"

match = re.search(pattern,String)
if match:
    print("Matched!!")
    
else:
    print("Match not found!!!")


import re

String = ['acd','bcd','abcd','xyz']
pattern = r"a|b"

match = [s for s in String if re.match(pattern,s)]
if match:
    print("Match found!!")
else:
    print("Matched not found!!")

import re

string = "A big white leopard ran across the field with its massive motor like speed. no one has ever stopped it." 
pattern = r"Ab*"

match = re.search(pattern,string)
if match:
    print("Match found")
    print(match)
else:
    print("Matched not foundd!!")

import re 


pattern = r"ab?c"
String = ["ac","acb","dabc","abdc"]

match = [s for s in String if re.search(pattern,s)]
if match:
    print(match)
else:
    print("Match not found!!")

import re

pattern = r"ab+c"
String = ["ac","acb","dabc","abdc"]

match = [s for s in String if re.search(pattern,s)]
if match:
    print(match)
else:
    print("Match not found!!")


import re

pattern = r"a{2,4}"
string = ["aaab","aab","Marvelous","accomplished","retarted","adhesive","reactive","Plotonium-230"]

match = [s for s in string if re.search(pattern,s)]
if match:
    print(match)
else:
    print("not matched")



import re

pattern = r'(a|b)cd'
string = ["acd","abcd","gcd","xyz","bcd","efg"]

match = [s for s in string if re.search(pattern,s)]
if match:
    print(match)
else:
    print("Not matched!!")




import re

pattern = r"\d"
string = ["abc","123","a1b2c3"]

match = [s for s in string if re.search(pattern,s)]
if match:
    print(match)
else:
    print("Not matched!!")  

import re

pattern = r"\D"
string = ["abc","123","a1b2c3"]

match = [s for s in string if re.search(pattern,s)]
if match:
    print(match)
else:
    print("Not matched!!")  

import re 

pattern = r"\s"
string =['Hello world','noSPaces','line\nbreak']

matches = [s for s in string if re.search(pattern,s)]
if matches:
    print(matches)
else:
    print("Match not found!!")

import re
p = re.compile('ab*')
print(p.findall("abababbabbbbb"))