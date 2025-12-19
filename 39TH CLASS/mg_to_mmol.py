data="Chol=190mg HDL=45mg LDL=110mg"

chol=int(data[data.index("Chol=")+6 : data.index("mg" , data.index("Chol="))])

Hdl=int(data[data.index("HDL=")+4 : data.index("mg" , data.index("HDL="))])

Ldl=int(data[data.index("LDL=")+4 : data.index( "mg" ,  data.index("LDL="))])

print(chol,Hdl,Ldl)