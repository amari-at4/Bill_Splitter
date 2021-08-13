email = input()


def check_email(address):
    assert '@' in address, 'Try again!'
    print('Done!')


check_email(email)
