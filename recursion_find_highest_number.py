# Designed by Ryan Brewer
# Programming Challenge (Chp. 12.3, Tony Gaddis textbook)
# Largest List Item
# Design a function that accepts a list as an argument and
# returns the largest value in the list. The function should use
# recursion to find the largest item.n

def main():
    # Declare local vareiables and initialize an empty list
    # Default value is a sentinel; value replaced when a higher value is found in list.
    numbers_list = []
    new_number = int(
        input("Let's create a list of numbers. Enter the first number:\n"))
    numbers_list.append(new_number)

    while new_number != -1:
        new_number = int(
            input('Enter the next number in the list, or enter -1 to complete the list.\n'))
        numbers_list.append(new_number)

  # Display number list entered by user
    print('\nYou entered the following list of numbers:')
    print(numbers_list)

    # Find highest number in the list
    starting_index = 0
    last_index = len(numbers_list) - 1
    print('\nThe highest number in this list is:',
          find_highest(numbers_list, starting_index, last_index))

# Define recursive function to determine highest number in list (number list from main functin is passed as an argument)


def find_highest(num_list, start_index, end_index):
  # Base case reviews last  last two numbers in a list and returns the higher value.
  # Recursive case compares the following and recursively returns the highest value between:
  # 1) the value at the start_index in the numbers list; 2) the highest of all subsequent numbers in the list
    if start_index == len(num_list) - 2:
        highest_num = greater_of(num_list[start_index], num_list[end_index])
        return highest_num

    else:
        current_number = num_list[start_index]
        # Recursive case
        highest_subsequent_number = find_highest(
            num_list, (start_index + 1), end_index)
        return greater_of(current_number, highest_subsequent_number)


def greater_of(num_1, num_2):
    if num_1 >= num_2:
        return num_1
    else:
        return num_2


main()
