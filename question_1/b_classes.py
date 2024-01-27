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

    def sort_numbers_desc(self):
        number = len(self.numbers)
        for i in range(number -1):
            for j in range(0, (number-i) -1):
                if self.numbers[j] < self.numbers[j +1]:
                    self.numbers[j], self.numbers[j+1] = self.numbers[j+1], self.numbers[j]

number_list_manager = NumberListManager()
number_list_manager.get_user_input()
number_list_manager.sort_numbers_desc()
number_list_manager.display_numbers()