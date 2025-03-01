def search_matrix(matrix, target):
        for row in matrix:
            for element in row:
                if element == target:
                    return True  
            else:
                continue  

        return False

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(search_matrix(matrix, 5))
print(search_matrix(matrix, 10))  