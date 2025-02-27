my_tuple = (1, 2, 3, 4, 5)
is_distinct = len(set(my_tuple)) == len(my_tuple)
print(is_distinct)  

my_tuple2 = (1, 2, 2, 3)
is_distinct2 = len(set(my_tuple2)) == len(my_tuple2)
print(is_distinct2)  