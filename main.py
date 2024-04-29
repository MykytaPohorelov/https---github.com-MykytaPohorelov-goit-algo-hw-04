from pathlib import Path

file_name = Path('./Temp')

def total_salary(path):

    income = 0
    devs = 0

    try:
        with open(file_name / path, 'r', encoding='utf-8') as file:
            
            for line in file:
                name, salary = line.split(",")
                income += int(salary)
                devs += 1
            
            if devs == 0:
                return 0, 0
            
            avg_salary = int(income / devs)
            return income, avg_salary
    
    except FileNotFoundError:
        print("File not found!")
        return None
    except Exception as e:
        print(f'{e} - try again')
        return None

total, average = total_salary("path.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# ------------

file_name = Path('./Cats')

def get_cats_info(path):

    cat_list = []

    try:
        with open(file_name / path, 'r', encoding='utf-8') as file:
            
            for line in file:

                id, name, age = line.split(",")
                cat_dict = {
                    'id': id,
                    'name': name,
                    'age': int(age)
                }
                cat_list.append(cat_dict)
        
        return cat_list             
                
    except FileNotFoundError:
        print("File not found!")
        return None
    except Exception as e:
        print(f'{e} - try again')
        return None

cats_info = get_cats_info("path.txt")
if cats_info is not None:
    print(cats_info)

# ------------

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Phone number for {name} updated."
    else:
        return f"{name} not found in contacts."
    
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return f"{name} not found in contacts."
    
def show_all(args, contacts):
    contact_list = []
    if contacts:
        result = "All contacts with phone numbers:\n"
        for name, phone in contacts.items():
            contact_list.append(contacts)
            # result += f"{name}: {phone}\n"
            result += f"{contact_list}"
            return result
    else:
        return "No contacts details."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()