# (!!!Доп!!!) Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# (0,0,0), (0,0,1) и тд.

for x in [0,1]:
    for y in [0,1]:
        for z in [0,1]:
            print(f'({x},{y},{z})')
            if not(x or y or z)==(not x and not y and not z):
                print('Утверждение верно')
            else:
                print('Утверждение ложно')


