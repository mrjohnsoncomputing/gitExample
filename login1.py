
for attempt_number in range(3):
    username = input('Username: ')
    if username in ('bob', 'jane', 'sally'):
        print(f'Welcome {username}')
        break
else:
    print(f'no')
