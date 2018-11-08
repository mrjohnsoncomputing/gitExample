RETRIES = 3
USERS = (
    'bob',
    'jane',
    'sally',
)

print('Begin')
for attempt_number in range(RETRIES):
    username = input('Username: ')
    if username in USERS:
        print(f'Welcome {username}')
        break
    print(f'Unknown user {username}')
else:
    print(f'{RETRIES} failed attempts - exit')
print('End')
