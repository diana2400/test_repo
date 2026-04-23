import random

def greeting():
    print('\nПривет, команда! Сегодня будем работать вместе!')

def motivation_quote():
    quotes = [
        'Команда - это сила!',
        'Каждый коммит приближает нас к успеху!',
        'Git сохраняет все, что мы делаем',
        'Вместе мы - команда мечты!'
    ]
    print('Цитата дня:', random.choice(quotes))

def coin_flip():
    coin = random.randint(0, 1)
    if coin == 0:
        print('Выпала РЕШКА')
    else:
        print('Выпал ОРЕЛ')

def guess_number():
    secret = random.randint(1, 3)
    print("Угадай число от 1 до 3")
    guess = int(input('Твой ответ: '))
    if guess == secret:
        print("Круто! Ты угадал.")
    else:
        print(f'Не угадал. Было число {secret}')

tasks = []

def add_tasks():
    task = input('Что нужно сделать? ')
    tasks.append(task)
    print(f'Задача добавлена: {task}')

def menu():
    while True:
        print('\n=== Меню проекта ===')
        print('1. Приветствие')
        print('2. Цитата дня')
        print('3. Орел/Решка')
        print('4. Угадай число')
        print('5. Добавить задачу')
        print('6. Выход')
        choice = input('Выбери номер: ')
        if choice == '1': greeting()
        elif choice == '2': motivation_quote()
        elif choice == '3': coin_flip()
        elif choice == '4': guess_number()
        elif choice == '5': add_tasks()
        elif choice == '6':
            print('Пока, команда!')
            break

menu()