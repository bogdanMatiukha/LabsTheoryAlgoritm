while True:
    print("\n1 - Sum of numbers between A and B")
    print("2 - Count symbol in string")
    print("3 - Check three-digit number")
    print("4 - Sum of numbers from 1 to N")
    print("5 - Find longest string")
    print("0 - Exit")

    choice = input("Choose task: ")

    if choice == "1":
        a = int(input("Enter A: "))
        b = int(input("Enter B: "))

        total = 0

        for i in range(min(a, b), max(a, b) + 1):
            total += i

        print("Sum:", total)

    elif choice == "2":
        text = input("Enter a string: ")
        symbol = input("Enter a symbol: ")

        count = text.count(symbol)

        print("Count:", count)

    elif choice == "3":
        number = int(input("Enter a number: "))

        if 100 < number < 999:
            print("three-digit")
        else:
            print("not three-digit")

    elif choice == "4":
        n = int(input("Enter N: "))

        numbers = list(range(1, n + 1))

        print("Sum:", sum(numbers))

    elif choice == "5":
        strings = []

        print("To finish, type “exit”")

        while True:
            text = input("Enter a string: ")

            if text == "exit":
                break

            strings.append(text)

        if strings:
            print("Longest string:", max(strings, key=len))
        else:
            print("No strings entered")

    elif choice == "0":
        print("Program finished")
        break

    else:
        print("Invalid choice")
