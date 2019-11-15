# text
import string

alphabet = string.ascii_lowercase
morse = '''.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- 
.--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'''.split()

morse_code_dict = dict(zip(alphabet, morse))


def smorse(word: str) -> str:  # converts the word to morse code
    return "".join([morse_code_dict.get(c, "") for c in word])


def main():
    print(smorse('sos'))
    print(smorse("daily"))
    help(zip)


if __name__ == "__main__":
    main()


