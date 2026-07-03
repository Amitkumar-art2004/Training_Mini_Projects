ContactBook = {
    "user1": {
        "name": "amit",
        "phone": 1234567890
    },
    "user2": {
        "name": "anish",
        "phone": 61421818421
    },
    "user3": {
        "name": "aditya",
        "phone": 98379697632
    },
    "user4": {
        "name": "anshu",
        "phone": 23486982424
    }
}
phoneSet = set()
for user in ContactBook.values():
    phone = user["phone"]
    if phone in phoneSet:
        print("Duplicate phone number found:", phone)
    else:
        phoneSet.add(phone)
search_name = input("Enter name to search: ")
for user in ContactBook.values():
    if user["name"] == search_name:
        print("Contact Found:")
        print(user)
else:
    print("User not found")
new_name = input("Enter new name: ")
new_phone = int(input("Enter phone number: "))
if new_phone in phoneSet:
    print("Duplicate phone number! Contact not added.")
else:
    ContactBook["user5"] = {
        "name": new_name,
        "phone": new_phone
    }
    phoneSet.add(new_phone)
    print("Contact Added!")
update_name = input("Enter name to update: ")
for user in ContactBook.values():
    if user["name"] == update_name:
        user["phone"] = int(input("Enter new phone number: "))
        print("Contact Updated!")
delete_name = input("Enter name to delete: ")
for key, user in list(ContactBook.items()):
    if user["name"] == delete_name:
        del ContactBook[key]
        print("Contact Deleted!")
print("\nFinal Contact Book:")
for user in ContactBook.values():
    print(user)
