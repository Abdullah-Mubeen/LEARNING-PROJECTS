import json

def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {"name": name, "age": age, "email": email}
    return person

def display_contact(people):
    for i, person in enumerate(people):
      print(i+1, "-", person["name"], "|", person["age"], "|", person["email"])

def delete_contact(people):
    display_contact(people)

    while True:
        number = input("Enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("invalid number, out of range")
            else:
                 break
        except: 
            print("Invalid number")

    people.pop(number-1)
    print("Person Deleted")

def search_contact(people):
    search_name = input("search for a name: ").lower()
    results = []

    for person in people:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)

    display_contact(results)

print("Hello, welcome to the Save Contact Dairy.")
print()

with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]


while True:
    print("Save Contacts List ", len(people))

    command = input("You can 'Add', 'Delete' or 'Search' or 'Q' to Quit ").lower()
    if command == "add":
        person = add_person()
        people.append(person)
        print("People Added")
    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        search_contact(people)
    elif command == 'q':
        break
    else:
        print("invalid command")
   

with open("contacts.json", "2") as f:
    json.dump({"contacts": people}, f)

print(people)