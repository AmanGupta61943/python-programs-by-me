num=int(input("Total no. of repository user wants to create: "))
names=[]
contact_numbers=[]
for i in range(num):
    name = input("Enter the Name: ")
    contact_number = input("Enter the Phone Number: ")

    names.append(name)
    contact_numbers.append(contact_number)

print("\n\tName\t\t\tPhone Number\n")

#Creating a list of names & contact in tabular form:

for i in range(num):
    print("\t{}\t\t\t{}".format(names[i], contact_numbers[i]))

#Search:

while True:
    choice=int(input("\n\nPress 1 or 2\n1=To search\n2=To Exit\n"))
    if choice == 1:
        search_name=input("\n Enter the name you want to search: ")
        print("\nSEARCH RESULT :")
        if search_name in names:
            index = names.index(search_name)
            contact_number = contact_numbers[index]
            print("Name: {}, Phone Number: {}".format(search_name, contact_number))
            
        else:
            print("Name not found in repository")
            
    else:
        print("Exit")
        break
