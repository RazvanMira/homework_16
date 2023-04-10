list_one = ["apples"]
list_two = ["apples", "and", "oranges"]
list_three = ["apples", "oranges", "and", "bananas", "apples"]
list_four = ["oranges", "bananas", "and", "lemons"]

list_total = list_one + list_two + list_three + list_four
set_list = set(list_total)
final_list = list(set_list)
final_list.remove("and")
final_list.insert(-1, "and")
print(final_list)
final_string = final_list[0] + ", " + final_list[1] + ", " + final_list[2] + ", " + final_list[3] + " " + final_list[4]
print(final_string)