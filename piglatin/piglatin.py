def main():
    vowels = 'aeiouy'

    while True:
        word = input('Enter a word: ')
        if word[0].lower() in vowels:
            modified = word + 'way'
        else:
            modified = word[1:] + word[0] + 'ay'
        print('\n' + modified + '\n')

        try_again = input('Try again? enter "y" to go again or "n" to quit: ')
        if try_again.lower() == 'n':
            break


if __name__ == '__main__':
    main()
