import argparse

from greetpy import hello, goodnight


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('day_or_night', choices=('day', 'night'))
    parsed_args = parser.parse_args()
    day_or_night = parsed_args.day_or_night

    if day_or_night == 'day':
        hello.say_hello()
    else:
        goodnight.say_goodnight()


if __name__ == '__main__':
    main()
