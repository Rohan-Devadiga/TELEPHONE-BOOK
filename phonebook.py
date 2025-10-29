import os

FILE_NAME = "phonebook.txt"


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone}\n")

    print(f"✅ Contact '{name}' added successfully.\n")


def view_contacts():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("📭 No contacts found.\n")
        return

    print("\n📒 All Contacts:")
    with open(FILE_NAME, "r") as file:
        for line in file:
            name, phone = line.strip().split(",")
            print(f"👤 {name} - 📞 {phone}")
    print()


def search_contact():
    term = input("Enter name or phone number to search: ").strip().lower()

    found = False
    with open(FILE_NAME, "r") as file:
        for line in file:
            name, phone = line.strip().split(",")
            if term in name.lower() or term in phone:
                print(f"✅ Found: {name} - {phone}")
                found = True

    if not found:
        print("❌ No matching contact found.\n")


def delete_contact():
    term = input("Enter name or phone number to delete: ").strip().lower()

    if not os.path.exists(FILE_NAME):
        print("❌ Phonebook is empty.\n")
        return

    lines = []
    deleted = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            name, phone = line.strip().split(",")
            if term in name.lower() or term in phone:
                print(f"🗑️ Deleting: {name} - {phone}")
                deleted = True
                continue
            lines.append(line)

    with open(FILE_NAME, "w") as file:
        file.writelines(lines)

    if deleted:
        print("✅ Contact deleted successfully.\n")
    else:
        print("❌ Contact not found.\n")


def main():
    while True:
        print("===== 📞 Telephone Book =====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
