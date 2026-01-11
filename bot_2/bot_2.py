def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Contact not found."
        except ValueError:
            return "Error: Invalid input."
        except IndexError:
            return "Error: Missing arguments."
        except Exception as e:
            return f"Error: {str(e)}"
    return inner

def parse_input(user_input):
    if not user_input.strip():
        return "", []
    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: Invalid number of arguments for 'add' command. Use: add [name] [phone]"
    
    name, phone = args
    if not phone.isdigit():
        raise ValueError("Phone must contain only digits.")
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Invalid number of arguments for 'change' command. Use: change [name] [phone]"
    
    name, phone = args
    if not phone.isdigit():
        raise ValueError("Phone must contain only digits.")
    contacts[name] = phone 
    return "Contact updated."
    
@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: Invalid number of arguments for 'phone' command. Use: phone [name]"
    
    name = args[0]

    return contacts[name]
    
def show_all_contacts(contacts):
    if not contacts:
        return "No contacts found."
    
    result = "All contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def main():
    contacts = {}
    print("Welcome to the Contact Bot!")
    
    while True:
        user_input = input("enter command: ")
        command, args = parse_input(user_input)
        
        if command == "":
            print("Error: Please enter a command.")
            continue
            
        if command in ["close", "exit", "good bye"]:
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
            print(show_all_contacts(contacts))
        else: 
            print("Error: Unknown command.")

if __name__ == "__main__":
    main()