import sys


def otan(word):
    dictionary = {
        'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
        'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India',
        'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November',
        'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra',
        'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey',
        'X': 'Xray', 'Y': 'Yankee', 'Z': 'Zulu', '0': 'Zero', '1': 'One',
        '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six',
        '7': 'Seven', '8': 'Eigh', '9': 'Nine', ' ': ' '}
    phon = [dictionary[w] for w in word]
    return ' '.join(phon)


def main(argv):
    word = argv[1].upper()
    print (otan(word))


if __name__ == "__main__":
    main(sys.argv)
