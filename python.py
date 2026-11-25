'''

------------------------------------------------KEYWORD-----------------------------------------------------------
import keyword
print(keyword.kwlist)
a=None
print(a)


-----------------------------------------------------TYPECASTING----------------------------------------------------------

a=eval(input("enter:"))
print(a,type(a))

 #helps to identify the data type of the input value


 -------------------------------------------------TUPLES---------------------------------------------------------------------

a=10,20,30
print(a)

a=(10,2.3,5j,True,'hi',)


---------------------------------------------------SLICING----------------------------------------------------------------------

a='Hello'
print(a[2:3])      # prints 'l'

print(a[1:4])      # prints 'ell'
print(a[1:])       # prints 'ello'
print(a[:4])       # prints 'Hell'
print(a[:])        # prints 'Hello'
print(a[2:4])      # prints 'll'
print(a[-3:-2:1])   # prints 'l'
print(a[-3:-1:1])   # prints 'll
print(a[3:1-1:-1])   #prints lle
print(a[-2:-4-1:-1])  #prints lle  with negative indexing
print(a[-2:-5-1:-1])   #prints 'lleH'  with negative indexing
print(a[::-1])   #prints 'olleH'  with negative indexing   reverse the string


============================================================================================



a="good Morning"
print(a[0:4])      # prints 'good'
print(a[5:])       # prints 'morning'
print(a[7:11])   
print(a[-2:-5])
print(a[1:5+1:2])  #prints 'odM'  with step indexing
print(a[-2:-5:-1])  #prints 'gno'  with negative indexing
print(a[-2:-5-1:-1])  #prints 'gnoM'  with negative indexing
print(a[::-1])   #prints 'gninroM doog'  with negative indexing   reverse the string
print(a[::2])   #prints 'gdMoin'  with step indexing
print(a[::3])   #prints 'gooi'  with step indexing
print(a[::4])   #prints 'g o'  with step indexing
print(a[::5])   
print(a[5:11+1:3])
print(a[5::3])
print(a[-7::3])
print(a[10::3])
#for 'nr '
print(a[-2:-8-1:-3])

print(len(a[10:4-1:-3]))

a='Happy birthday'
print(a[10:8-1:-1])


------------------------------------------------------------REVERSE-----------------------------------------------------------------------------

n=int(input('enter number:'))
rev=0
while n>0:
    ld=n%10
    n=n//10
    rev=rev*10+ld
    print(rev)


    ----------------------------------------------------OOP'S---------------------------------------------------------------------------------

    class college:
    cname="gopalan"
    cloc="hoodi"
    s1=college()
    college.cname="gopalan college"
    h=college()
    print(s1.cname)


    #object change is only for that object not for class
    #class variable change is for all objects of that class
class college:
s1=college()
s1.name='harish'
s1.phon=9000000000000

s2=college()
s2.name='girish'
s2.phon=333333333333

s1.cloc='kr purum'
print('After changing')
print(s1.cloc)

--------------------------------------------------------LOOPS AND STSTEMENTS-------------------------------------------------------------------


#if
a=int(input('enter:'))
if a%2==0:
    print('even')
else:
    print('odd')

================================

l=eval(input("enter the list"))
if len(l)==5:
    print('yes')
else:
    print('no')

================================
print(chr(65)) #ASCII value of 65 is A
print(ord('A')) #ASCII value of 'A' is 65

================================

#ELIF STATEMENT

ch=input("enter:")
if"A"<=ch<="Z":
    print("uppercase")
elif "a"<=ch<="z":
    print("lowercase")
else:
    print("invalid")
================================

#NESTED IF STATEMENT(for login page)

Un=input('Enter:')
if un=='heroin':
    print('correct username')
    pw=input('Enter:')
    if pw=='hi@123':
        print('login successful')

    else:
        print('incorrect pw')
else:
    print('incorrect un')

================================

#WHILE LOOP

i=1
while i<=100:
    print(i)
    i+=1

================================

i=1
while i<=100:
    if i%2==0:
        print(i,'even')
    i+=1

================================

i=2
while i<=50:
    print(i)
    i+=2

'''

#FOR LOOP

'''for i in range(1,100):
    print(i)'''

'''for i in range(1,49):
    if i%2==0:
        print(i,'even') 



#for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.

l=[10,20,30]
for i in l:  
    print(i)


#CONVERTING UPPERCASE TO LOWERCASE AND LOWERCASE TO UPPERCASE

s=input('enter string:')
for i in s:
    if "A"<=i<="Z":
        out+=chr(ord(i)+32)
    elif 'a'<=i<='z':
        out+=chr(ord(i)-32)
    else:
        out+=i
print(out)


#REVERSE A STRING


s=input('enter string:')
rev=''
for i in s:
    rev=i+rev
    print(rev)


#NESTED FOR LOOP
#(i=row, j=column)
for i in range(1,6):
    for j in range(1,6):
        print('*' , end='')    #PATTERN PRINTING


for i in range(1,6):   #FORWAED SLASH PATTERN
    for j in range(1,6):
        if i+j==6:
            print('*',end='')
        else:
            print(' ',end='')
    print()




for i in range(1,6):    #BACKWARD SLASH PATTERN
    for j in range(1,6):
        if i==j:
            print('1',end='')
        else:
            print('@',end='')
    print()



for i in range(1,6):    #LOWER TRIANGLE PATTERN
    for j in range(1,6):
        if i>j:
            print('1',end='')
        else:
            print('@',end='')
    print()
    


------------------------------------------------------------------LISTS------------------------------------------------------------

a=[10,2.3,5j,True,'hi']
if(len(a)==5):
    print('list is valid')
else:
    print('list is not valid')


-----------------------------------------------------------------FUNCTIONS-----------------------------------------------------------

#function is a block of code which is used to perform a specific task. It can be called multiple times in a program. It helps to reduce the complexity of the program and makes it more readable
# 4.ways to define a function in python
# 1. Function without arguments and without return value
# 2. Function with arguments and without return value
# 3. Function without arguments and with return value
# 4. Function with arguments and with return value

#with arg with return value
def convert(s):
    out=''
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    return out
print(convert(input('enter  a string:')))

#ANOTHER WAY TO DEFINE FUNCTION WITH ARGUMENTS AND WITH RETURN VALUE

def convert(s,out):
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    return out
print(convert(input('enter  a string:'),''))




#WITH ARGUMENT WITHOUT RETURN VALUE

def convert(s,out):
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    print(out)    
convert(input('enter  a string:'),'')


#WITHOUT ARGUMENTS AND WITHOUT RETURN VALUE

def convert():
    s=input('enter  a string:')
    out=''
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    print(out)    
convert()

#without arguments and with return value

def convert():
    s=input('enter  a string:')
    out=''
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    return out
print(convert())


-------------------------------------------------------------------------FLOAT------------------------------------------------------------------

a=10
print(float(1.0))

-----------------------------------------------------DICTONARY----------------------------------------------------------------------

a={'a':10}
print(a['a'])

a={'a':10,'a':20} 
print(a['a'])

a={'a':10,'a':20} 
print(a.keys())

a={'a':[10,20,30],'b':40}
print(a['a'][1])      #to acess only 20 from the list in dictionary


a={'a':[10,20,30],'b':40}
print(a['a'][-2])     #to acess only 20 from the list in dictionary


----------------------------------------------------------------DATA TYPES-------------------------------------------------------


a=10
print(bool(a)) //ture

a=0
print(bool(a)) //false


---------------------------------------------------------------------CONSTRUCTOR-------------------------------------------------------

class college:
    def _init_(self,name,phno,usn):
        self.name=name
        self.phno=phno
        self.usn=usn


s1 = college('Harish', 87878, 'a3h3h')
s2 = college('Girish', 65878, 'a78ghh')
print(s1.name)


-------------------------------------------------------------COMPLEX-----------------------------------------------------------------

a=3+5j
print(a)


'''