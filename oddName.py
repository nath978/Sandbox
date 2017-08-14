# """Nathan Reavell"""

def main():

    Name = input("What is your name? ")

    while not is_valid(Name):
        print("Name is invalid")
        Name = input(">>> ")

    for char in range(1,len(Name),2):
        print(Name[char])

def is_valid(Name):
    if Name == "":
        return False

    return True

main()