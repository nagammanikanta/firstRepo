import sys
type = sys.argv[1]

if type =="t2.micro":
    print("it will charge 2 dollers a day")
elif type == "t2.medium":
    print("it will charge 4 dollers a day")
    
elif type =="t2.xlarge":
    print("it will charge 8 dollars a day")

else:
    print("please provide a valid instance type")
    
    