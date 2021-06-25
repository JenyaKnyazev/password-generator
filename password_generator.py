import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
matrix = [letters,symbols,numbers]
arr = [nr_letters,nr_symbols,nr_numbers]
matrix_copy = []
matrix_copy.append([])
matrix_copy.append([])
matrix_copy.append([])
matrix_copy[0].extend(letters)
matrix_copy[1].extend(symbols)
matrix_copy[2].extend(numbers)
password = ""
while arr[0] > 0 or arr[1] > 0 or arr[2] > 0:
    word_letter_symbol = random.randint(0,2)
    if arr[word_letter_symbol] > 0:
        index = random.randint(0,len(matrix[word_letter_symbol])-1)
        password+=matrix[word_letter_symbol][index]
        matrix[word_letter_symbol].pop(index)
        if len(matrix[word_letter_symbol]) == 0:
            matrix[word_letter_symbol]=[]
            matrix[word_letter_symbol].extend(matrix_copy[word_letter_symbol])
        arr[word_letter_symbol]-=1
print("here is your password: "password)

