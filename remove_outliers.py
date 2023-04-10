import copy
numbers_list = []

def populate_list(numbers_list):
    more_numbers = True
    while more_numbers:
        number = input("Please type in a number or type in a blank line to stop: ")
        if number == " ":
            more_numbers = False
        else:
            number = int(number)
            numbers_list.append(number)

def remove_outliers(numbers_list):
    if len(numbers_list) < 4:
        print("You did not enter enough numbers.")
    else:
        original_list = copy.deepcopy(numbers_list)
        numbers_list.sort()
        final_sorted_list = numbers_list[2:-2]
        print(final_sorted_list)
        print(original_list)

def main() -> None:
    populate_list(numbers_list)
    remove_outliers(numbers_list)

if __name__ == "__main__":
    main()