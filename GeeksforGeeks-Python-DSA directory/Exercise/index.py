my_list = [10, 20, 30, 40, 50]
element_to_find = 30
try:
                  index = my_list.index(element_to_find)
                  print(f"The index of {element_to_find} is {index}")
except ValueError:
                  print(f"{element_to_find} is not in the list")