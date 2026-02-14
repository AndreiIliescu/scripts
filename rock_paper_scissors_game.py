""" Acest proiect simulează jocul rock, paper, scissors, jucat între un user și calculator. """

import random
# Import modulul „random” pentru calculator, să aleagă ce va juca în fiecare tură.

choices = ['ROCK', 'PAPER', 'SCISSORS']
# Creez o listă cu cele 3 opțiuni posibile

user_choice = int(input('Make a choice: 1 for ROCK, 2 for PAPERS or 3 for SCISSORS: '))
# Creez o variabilă și îi cer utilizatorului să introducă o cifră între 0 și 2, ce reprezintă alegerile disponibile.

if user_choice < 1 or user_choice > 3:
    print('Invalide choice')
elif user_choice == 1:
    print(f'You chose: {choices[0]}')
elif user_choice == 2:
    print(f'You chose: {choices[1]}')
else:
    print(f'You chose: {choices[2]}')
# Creez condiții:
# dacă utilizatorul introduce orice cifră mai mică decât 0 sau mai mare decât 3, i se va afișa mesajul de opțiune invalidă.
# dacă alege una dintre cele 3 opțiuni valide i se va afișa ceea ce a ales.

print() # print pentru spațiiere în consolă

computer_choice = random.randint(1, 3)
# Folosind „random.randint” aleg un interval (între 1 și 3, în cazul de față) în care calculatorul să aleagă.

if computer_choice == 1:
    print(f'Computer chose: {choices[0]}')
elif computer_choice == 2:
    print(f'Computer chose: {choices[1]}')
else:
    print(f'Computer chose: {choices[2]}')
# Creez condiții pentru opțiunile calculatorului:
# dacă alege una dintre cele 3 opțiuni valide i se va afișa ceea ce a ales.

print() # print pentru spațiiere în consolă

if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == 3 and computer_choice == 1:
    print('You lose!')
elif user_choice == 1 and computer_choice == 3:
    print('You win!')
elif user_choice > computer_choice:
    print('You win!')
elif user_choice < computer_choice:
    print('You lose!')
# Creez condiții pentru logica jocului:
# dacă utilizatorul și calculatorul aleg același număr - este egalitate.
# dacă utilizatorul alege „3” și calculatorul „1” - utilizatorul pierde.
# dacă utilizatorul alege „1” și calculatorul „3” - utilizatorul câștigă.
# daca utilizatorul alege un număr mai mare decât calculatorul - utilizatorul câștigă
# daca utilizatorul alege un număr mai mic decât calculatorul - utilizatorul pierde
