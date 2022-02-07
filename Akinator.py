


from multiprocessing.connection import answer_challenge


print('Приветcтвую игрок!!'
'\n Я попытаюсь отгадать твоего загаданного персонажа!')
print('Ваш персонаж женского пола? y/n''\n')
ans = str(input())
if ans == 'y':
    print('Она человек?')
    ans = str(input())
    if ans == 'y':
        print('Она реальна?')
        ans = str(input())
        if
    elif ans == 'n':
        print('Это монстр женского пола?')
        ans = str(input())    
elif ans == 'n':
    print('Он человек?')
    ans = str(input())
    if ans == 'y':
        print('Это реальный человек?')
        ans = str(input())
    elif ans == 'n':
        print('Он летает?')
        ans = str(input())
        if ans == 'y':
            print('Это дракон!')
            ans = str(input())
        elif ans == 'n':
            print('это крокодил')
            



