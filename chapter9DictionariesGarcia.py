def show_menu():
    print("a. Add Data")
    print("b. Delete Data")
    print("c. End")


def main():
    r = {}

    print("==== Record Keeping App ====")

    while True:
        show_menu()
        choice = input("Select action: ").strip().lower()

        if choice == "a":
            key = input("Enter a key: ").strip().upper()
            value = input("Enter value: ").strip()
            r[key] = value
            print(r)

        elif choice == "b":
            key = input("Enter a key: ").strip().upper()
            if key in r:
                del r[key]
                print()
            else:
                print("=== Key does not exists! ===")
                print()

        elif choice == "c":
            print("THANK YOU. Program will now end")
            break

        else:
            print("=== Invalid choice! Please select a, b, or c. ===")
            print()
main()