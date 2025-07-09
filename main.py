import random

def load_responses(path) -> list[str]:
    with open(path, encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

yes = load_responses("responses/yes.txt")
no = load_responses("responses/no.txt")
huh = load_responses("responses/huh.txt")

print("DISCLAIMER: THIS PROGRAM IS FOR ENTERTAINMENT PURPOSES ONLY\nDO NOT TAKE THE RESULT SERIOUSLY\nTHE RESPONSES ARE RANDOMLY GENERATED\nTHEY DO NOT REFLECT THE VIEW OR BELIEF OF THE AUTHOR\nTHE AUTHOR SHALL NOT BE LIABLE FOR ANY DIRECT OR INDIRECT CONSEQUENCES OF ANYONE FOLLOWING ITS ADVICE\nYOU HAVE BEEN WARNED\n")

while True:
    _=input("What's your question?")
    a=random.random()
    if(a<0.25):
        print(random.choice(yes))
    elif(a<0.5):
        print(random.choice(no))
    else:
        print(random.choice(huh))
    