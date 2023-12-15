'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este numero é par ou impar. Caso o usuário não digite um
inteiro, informe que não foi um numero inteiro.
'''
typed_number = input("Enter an integer: ")

try:
    int_number = int(typed_number)

    if int_number % 2:
        print(f'The {int_number} is a ever number')
    else:
        print(f'The {int_number} is a odd number')
except:
    print(f'The number you typed is not a integer')

'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
'''
current_hours = float(input("Enter the hour now: "))
good_morning = current_hours >= 0 and current_hours <= 11
good_afternoon = current_hours > 11 and current_hours < 18
# good_night = current_hours > 18 and current_hours <= 23

if good_morning:
    print(f'Good Morning, now is {str(current_hours).replace(".", ":")}')
elif good_afternoon:
    print(f'Good Afternoon now is {str(current_hours).replace(".",":")}')
else:
    print(f'Good Night now is {str(current_hours).replace(".",":")}')

'''
Faça um programa que peça o primeiro nome do usuário. 
Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
maior que 6 escreva "Seu nome é muito grande".
'''
user_name = input("Enter your name, please: ")
name_size = len(user_name)
short_name = name_size < 4
normal_name = name_size > 4 and name_size <= 6
# long_name = name_size > 6

if name_size >= 2:
    if short_name:
        print(f'The name {user_name} is too short')
    elif normal_name:
        print(f'The {user_name} is a normal name')
    else:
        print(f'The {user_name} is to large')
else:
    print('Type a big name to test the program')
