class NumberListManager:
    def __init__(self):
        self.numbers = []

    def get_user_input(self):
        while True:
            try:
                user_input = input("Enter a number: (Type done when you finish): ")
                
                if user_input.lower() == 'done':
                    break

                self.numbers.append(int(user_input))
            except ValueError:
                print("Invalid input! Please enter a valid number")
    
    def display_numbers(self):
        print("List of user input numbers: ", self.numbers)


number_list_manager = NumberListManager()
number_list_manager.get_user_input()
number_list_manager.display_numbers()