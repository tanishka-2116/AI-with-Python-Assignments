# Assignment 3: Phonebook using dictionary

phonebook = {}

def add_contact(phonebook, name, phone_number):
    phonebook[name] = phone_number
    print(f"Contact {name} added.")

def delete_contact(phonebook, name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")

def update_contact(phonebook, name, new_phone_number):
    if name in phonebook:
        phonebook[name] = new_phone_number
        print(f"Contact {name} updated.")
    else:
        print("Contact not found.")

def search_contact(phonebook, name):
    if name in phonebook:
        return phonebook[name]
    else:
        return "Contact does not exist."

# Operations
add_contact(phonebook, "Amit", "9876543210")
add_contact(phonebook, "Neha", "9123456789")
add_contact(phonebook, "Rahul", "9988776655")

print("Phonebook:", phonebook)

print("Search Neha:", search_contact(phonebook, "Neha"))

update_contact(phonebook, "Amit", "9000000000")
print("After update:", phonebook)

delete_contact(phonebook, "Rahul")
print("After delete:", phonebook)
