print("Welcome to Mini Search Engine!")
print("Enter command to see container id: docker container ls")
print()

while(True):
    var = input("Please enter the address of your file. Enter quit to stop. >")
    print("Enter command: docker cp "+var+" container_id:/" + var)
    print()
    if var == "quit":
        break
