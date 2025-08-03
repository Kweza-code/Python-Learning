demand = int(input("How many contacts do you want to enter? "))

def ask(demand):
    contact_list = []

    for i in range(demand):
        name = input(f"Enter the name of contact {i + 1}: ")
        number = input("Enter a phone number: ")

        contact = {
            "name": name,
            "number": number
        }

        contact_list.append(contact)

    print("\nList of contacts:")
    for contact in contact_list:
        print(f"- {contact['name']} : {contact['number']}")

ask(demand) 