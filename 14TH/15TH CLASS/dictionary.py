dictionary={1:'python',2:'java'}

print(dictionary)

print(dictionary[2])
print('\n')





dic = {}

dic[0] = 'python'

dic[2] = 'language'

dic[3] = 1

print(dic)
print('\n')




dic['vaue_set']=2,3,

print('dictionary')

print(dic)
print('\n')




dict2='welcome' 

print('updated key value')

print(dict2)
print('\n')





dict5={'nested':{'1':'Life',2:'system'}}

print(dict5)

print(dict5['nested'])

print(dict5['nested']['1'])

print(dict5 ['nested'][2])
print('\n')



dict3=dict(a=1,b=2,c=3,d=4)

print(dict3)
print('\n')





main_dict1={'a':1,'b':2,'c':3}

#deep copy 

dict_deep=dict(main_dict1)

#jab hum deep dict mia change karaiungai to main dict nahi chnage hogi

dict_deep['b']=20

print('after chnage in deep copy,main_dict:',main_dict1)
print('\n')





main_dict2={'a':1,'b':2,'c':3}

#shaloow copy
dict_shallow=main_dict2

#jab hum shaloow copy mai value chaneg karaingai to wo main dict mai bhi change hogi

dict_shallow['a']=10
 
print('after chnage in shallow copy, main dict;',main_dict2)
print('\n')


txt1={1:'student',2:'faculty'}
txt2=txt1
print('\n')

txt1.clear()

print('After Removing items usimng clear()')
print('txt1=',txt1)
print('txt=2',txt2)
print('\n')



txt1={1:'one',2:'two'}
txt2=txt1
print('\n')

#yai text 1 ko empty kadaigi

txt1={}
print('\n')

d1={1:'a',20:[1,2,3],30:'c'}
print('given dicionary:' , d1)
print('\n')


d2=d1.copy()
print('print The copy of d1:',d2)
print('\n')

#updating
d2[10]= 10
d2[20][2] = '45' 

print('updated copy:',d2)
print('\n')
