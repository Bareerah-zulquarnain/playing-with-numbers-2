numberlargest = int(input("enter a largest number"))
numbersmallest = int(input("enter a smallest  number"))

while (numbersmallest ):
    numberstore=numbersmallest
    numbersmallest = numberlargest%numbersmallest
    numberlargest=numberstore

print("hcf is :" ,numberlargest)