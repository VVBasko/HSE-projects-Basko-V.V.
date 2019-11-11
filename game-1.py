print('Собрался Иван-царевич на бой со Змеем Горынычем, трехглавым и треххвостым.')
print('"Вот тебе меч-кладенец, - говорит ему Баба-яга.')
print('- Одним ударом ты можешь срубить Змею либо 1 голову, либо 2 головы, либо 1 хвост, либо 2 хвоста.')
print('Запомни: срубишь голову - новая вырастет, срубишь хвост - 2 новых вырастут, срубишь 2 хвоста - голова вырастет, ')
print('срубишь 2 головы - ничего не вырастет".')
print('Попробуй отрубить Змею Горынычу все головы и хвосты, иначе ты проиграешь!')
heads = 3
tails = 3
while tails >= 0:
    while heads >= 0:
        if heads == 1 and tails == 0:
            print('Ты проиграл!')
            heads = -1
            tails = -1
            break
        else:
            print('Что будем рубить (одну голову, две головы, один хвост или два хвоста)?')
            n = str(input())
            if n == 'одну голову':
                heads = heads
                tails = tails
                print('Осталось голов - ', heads, ', хвостов - ', tails, '.', sep='')
            elif n == 'две головы':
                if heads >= 2:
                    heads = heads - 2
                    tails = tails
                    if heads == 0 and tails == 0:
                        print('Ты победил!')
                        tails = -1
                        break
                    else:
                        print('Осталось голов - ', heads, ', хвостов - ', tails, '.', sep='')
                else:
                    print('Нельзя срубить больше голов, чем осталось у Змея.')
            elif n == 'один хвост':
                if tails >= 1:
                    heads = heads
                    tails = tails + 1
                    if heads == 0 and tails == 0:
                        print('Ты победил!')
                        tails = -1
                        break
                    else:
                        print('Осталось голов - ', heads, ', хвостов - ', tails, '.', sep='')
                else:
                    print('Нельзя срубить больше хвостов, чем осталось у Змея.')
            elif n == 'два хвоста':
                if tails >= 2:
                    heads = heads + 1
                    tails = tails - 2
                    if heads == 0 and tails == 0:
                        print('Ты победил!')
                        tails = -1
                        break
                    else:
                        print('Осталось голов - ', heads, ', хвостов - ', tails, '.', sep='')
                else:
                    print('Нельзя срубить больше хвостов, чем осталось у Змея.')
            else:
                print('Так дело не пойдёт... Попробуй ещё раз!')
