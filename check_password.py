import requests
import hashlib
import sys


def api_data(password):

    url = 'https://api.pwnedpasswords.com/range/' + password
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'Error:{ res.status_code}')

    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text)
    for h, count in hashes:

        if h == hash_to_check:
            return count
    return 0


def check_password(password):
    hashed_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
    first5_char, tail = hashed_password[:5], hashed_password[5:]
    response = api_data(first5_char)
    print(response)

    return get_password_leaks_count(response, tail)


def main(*args):
    for password in args:
        count= check_password(password)
        if count :
            print(f'{password} was found {count} times, you should change it')
        else:
            print(f'{password} was not found')
    return 'Done'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
 

