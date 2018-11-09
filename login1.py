print('begin')
for attempt_number in range(3):
    username = input('Username: ')
    if username in ('bob', 'jane', 'sally', 'allan','arnold'):
        print(f'Welcome {username}')
        break
    print('Invalid login: go away!')
else:
    print(f'You tried 3 times. Now I hate you')
print('end')
