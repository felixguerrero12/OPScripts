file = open(“reverseme.txt”, “r”)

def list_doubler(lst):
    complete_word = []
    for word in lst:
        complete_word.append(lst[::-1])
    return complete_word

print(list_doubler(file))
