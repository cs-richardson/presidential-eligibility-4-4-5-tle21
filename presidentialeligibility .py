age = int(input("What is your age?: ")) #Prompts user for age

citizen = input("Are you a citizen of the US? (yes/no): ") #Prompts user whether they are a citizen of the U.S or not

residency = int(input("How long have you been a resident in the U.S? (years): ")) #Promps user for how long they have been a resident

if age <0: #if age is less than zero, it is not true
    print ("Please enter your REAL AGE.") 
    
if citizen != "yes" and citizen != "no": #if citizenship is anything other than 'yes' or 'no' it doesn't make sense
    print ("Please answer with 'yes' or 'no' only.") 
    
if residency <0: #if residency is less than zero, it is not true
    print ("Please enter how long you REALLY have been a resident in the U.S.")

print("  ") #Printing nothing to add more space 

if age >= 35 and citizen == "yes" and residency >= 14: #President eligibility requirement
    print ("You are eligible to run for president!") 
else: #If they do not meet the requirements, they are not eligible to run for president
    print ("You are not eligible to run for president!")

