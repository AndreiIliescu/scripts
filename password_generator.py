""" Acest proiect presupune crearea de parole generate random dintr-o colecție de litere (majuscule și minuscule),
cifre (de la 0 la 9) și simboluri speciale, având orice lungime. """

import random
# Import modulul „random” pentru a selecta elemente aleatorii pentru parolă și pentru a le amesteca între ele.


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
           'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=']
# Creez 3 liste care conțin toate litere alfabetului (minuscule și majuscule), toate cifrele (de la 0 la 9) și cele mai
# uzuale simboluri speciale, acceptate în majoritatea parolelor.

password = [] # Creez o variabilă „password” căreia îi atribui o listă goală.

def password_generator(letters_input, numbers_input, symbols_input):
    """ Funcție care primește 3 parametri, iar pe baza lor determină lungimea range-ului prin care iterează, cu ajutorul
    a 3 „for loop”, prin fiecare dintre cele 3 liste, selectând aleatoriu elemente pe care le adaugă la lista
    „password”. Apoi acestea vor fi amestecare între ele și transformate într-un string. """

    for letter in range(letters_input):
        random_letters = random.choice(letters)
        password.append(random_letters)
    # „for loop” iterează prin toate elementele listei „letters”, conform unui range definit de user. „random.choice”
    # alege aleatoriu elemente din listă și le salvează în variabila „random_letters”, care mai apoi sunt adăugate în
    # lista „password”.

    for number in range(numbers_input):
        random_numbers = random.choice(numbers)
        password.append(random_numbers)
    # „for loop” iterează prin toate elementele listei „numbers”, conform unui range definit de user. „random.choice”
    # alege aleatoriu elemente din listă și le salvează în variabila „random_numbers”, care mai apoi sunt adăugate în
    # lista „password”.

    for symbol in range(symbols_input):
        random_symbols = random.choice(symbols)
        password.append(random_symbols)
    # „for loop” iterează prin toate elementele listei „symbols”, conform unui range definit de user. „random.choice”
    # alege aleatoriu elemente din listă și le salvează în variabila „random_symbols”, care mai apoi sunt adăugate în
    # lista „password”.

    random.shuffle(password) # Amestecă toate elementele din listă.

    randomized_password = "".join(password) # Adaugă și transformă toate elementele listei într-un string.

    return f'Your new randomly generated password is: {randomized_password}' # Returnează un string cu toate elementele
                                                                             # din listă, amestecate.


user_letters_input = int(input("Enter how many letters you would like your password to have: "))
user_numbers_input = int(input("Enter how many numbers you would like your password to have: "))
user_symbols_input = int(input("Enter how many symbols you would like your password to have: "))
# Creez 3 variabile care acceptă input de la utilizator, sub formă de numere întregi, în care îi cer să introducă câte
# elemente din fiecare categorie dorește să conțină parola lui.

print(password_generator(user_letters_input, user_numbers_input, user_symbols_input))
# Apelez funcția, într-un print, pentru a mi se afișa rezultatul final
