file = open(“reverseme.txt”, “r”)

def list_doubler(lst):
    return [lst[::-1] for _ in lst]

print(list_doubler(file))
