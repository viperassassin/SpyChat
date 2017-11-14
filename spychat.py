from details import spy_name, spy_age , spy_review
print('name of spy:' + spy_name)
print('age:' + str(spy_age))
print('review of spy:' + str(spy_review))
spy_age = 0
spy_review = 0.0
spy_initial=raw_input("Enter whether are you Mr. and Ms.:")
print('Initial of Spy:' + spy_initial)
name = spy_initial + spy_name
print('your full name:' + name)
if(len(spy_name) > 0):
 print('so your name is valid')
 if(spy_age>10) and (spy_age<50):
     print("You are authenticated User:" + name)
     if(spy_review>4.5) and (spy_review<5.0):
         print('Great Ace')
     elif(spy_review>4.0) and (spy_review<4.5):
         print('excellent')
     elif(spy_review>3.5) and (spy_review<4.0):
         print('perfect')
     elif(spy_review>3.0) and (spy_review<3.5):
         print('average')
     else:
         print('lol spy')
print("!!Congrats you are authenticated user!!")
