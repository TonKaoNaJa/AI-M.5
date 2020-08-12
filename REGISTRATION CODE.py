# TEST001 hello world
# This program prints Hello, world!
# This Program name is REGISTRATION NAJA!

count = 0 
print ( ' Hello You! ' )

username = input ( ' insert your username \n ' )
print ('hi there , %s ' % username)

while count < 100 :
    password = input ( ' insert your password \n ' )
    repassword = input ( ' insert your repassword \n ' )

    if password == repassword :
        print ( ' Your Password Correct ' )
        break 
    else :
        print ( ' Type Your Password Again PLS ' )
        repassword = input ( ' insert your repassword \n ' )
        continue 

print ( ' WELCOME ' )
name = input ( ' insert your name \n ' )
lastname = input ( ' insert your last name \n ' )

print (  name + lastname  )
