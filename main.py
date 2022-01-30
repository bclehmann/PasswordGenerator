import argparse, random

ALPHANUMERIC_CHARSET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
DEFAULT_CHARSET = ALPHANUMERIC_CHARSET + '!@#$%^&*()-_=+`~[]{}'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--length', '-l', default=32, type=int);
    parser.add_argument('--charset', '-c', default=DEFAULT_CHARSET)
    parser.add_argument('--alphanumeric', default=False, action='store_true')

    args = parser.parse_args()
    charset = ALPHANUMERIC_CHARSET if args.alphanumeric else args.charset

    cryptoRandom = random.SystemRandom()
    print(''.join(map(lambda _: cryptoRandom.choice(charset), range(args.length))))