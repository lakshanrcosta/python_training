def get_user_input_numbers():
    numbers = []

    while True:
        try:
            user_input = input("Enter a number: (Type done when you finish): ")
            
            if user_input.lower() == 'done':
                break

            numbers.append(int(user_input))
        except ValueError:
            print("Invalid input! Please enter a valid number")

    return numbers

user_input_numbers = get_user_input_numbers()
print("List of user input numbers", user_input_numbers)

