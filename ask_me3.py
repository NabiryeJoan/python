name = (input("what is your name "))
print("Hello", name + "!") 
print("how are u",name)

if name=="jack" or name=="jackie":
    print("hello",name)
    print("goodbye",name)
    
else: 
    print("hello friend")
age = int(input("how old are you ?"))
if age < 18:
    print("you are below the working age.")
elif age <18 and age > 25:
    print("you are of age to look for a job")
elif age >=25 and age <30:
    print("you should be having a job")
elif age >30 and age <60:
    print("you should think of having a family")
elif age <90 and age >=60:
    print("you should retire")
else:
      print("Goodbye,", name)
      print("You are" , age , "years old.")
      print("You are an alien in nature.")
