def win(a):
    for i in range(len(a)):
        j = 0
        if a[i][j] == a[i][j + 1]  and a[i][j + 1] == a[i][j + 2] and a[i][j + 2] == a[i][j]:
            return win

    for j in range(len(a)):
        i = 0
        if a[i][j] == a[i + 1][j] and a[i + 1][j] == a[i + 2][j] and a[i + 2][j] == a[i][j]:
            return win
    i, j = 0, 0
    if (a[i][j] == a[i + 1][j + 1] and a[i + 1][j + 1] == a[i + 2][j + 2] and a[i + 2][j + 2] == a[i][j]  ) or (a[i][j+2] == a[i + 1][j + 1] and a[i + 1][j + 1] == a[i+ 2][j] and a[i+ 2][j] ==  a[i][j+2]):
        return win

def SpaceFull(a):
    b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i][j] != b[i][j]:
                count += 1
                if count == 9:
                    return False
    return True


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


for i in range(len(a)):
    for j in range(len(a)):
        if j == len(a)- 1:
            print(a[i][j], end = ' ')
        else:
            print(a[i][j], end = '|')
    print()
    if i == len(a)- 1:
        print(' ')
    else:
        print('-+-+-')
    
choice = input('Choose who goes first, X or O ')


while win(a) != win:
    move = int(input(str(choice) + ' ' + 'turn. Whats your move? '))
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == move:
                a[i][j] = choice
               

    for i in range(len(a)):
        for j in range(len(a)):
            if j == len(a)- 1:
                print(a[i][j], end = ' ')
            else:
                print(a[i][j], end = '|')
        print()
        if i == len(a)- 1:
            print(' ')
        else:
            print('-+-+-')

    if SpaceFull(a) == False:
        print('Tie')
        break
        
    if win(a) == win:
        print(str(choice) + ' ' + 'wins')
        break
    else:
        if choice == 'X':
            choice ='O'
        else:
            choice = 'X'

