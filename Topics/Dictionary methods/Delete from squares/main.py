number = int(input())

square = squares.pop(number, None)
if square is None:
    print("There is no such key")
else:
    print(square)
print(squares)
