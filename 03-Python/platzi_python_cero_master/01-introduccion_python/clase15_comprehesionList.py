squares = [x ** 2 for x in range(1,11)]
print(squares)
celsius = [0, 10, 15, 20, 25, 30, 35, 40]
fahrenheits = [((9/5) * temp + 32) for temp in celsius]
print("Temperatura en F ",fahrenheits)

events = [x for x in range(1,21) if x % 2 == 0]
print(events)

matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

transposed = [[row[i] for row in matrix] for i in range(3)]

print(matrix)
print(transposed)
