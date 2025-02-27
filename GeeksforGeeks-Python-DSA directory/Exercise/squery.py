numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
queries = [(1, 5), (3, 8), (6, 10)]  # (start_index, end_index)
for start, end in queries:
sub_list = numbers[start-1:end]
print(f"Sum from index {start} to {end}: {sum(sub_list)}")