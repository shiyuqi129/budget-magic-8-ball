import random

yes=["You're right","Hurray!","I'm proud of you","Close enough","Fair enough","Do it","Let's go!","True","Approved","Absolutely","Yes","YES!!!","Of course","HELL YEAH!","Just do it","I'll allow it","Great idea!","I like that","Yeah","Sure","Nice","Cool","Sounds good to me","Positive","Correct"]
no=["False","Rejected","That's why you need to stay in school","HELL NAH!","PLEASE NO","No","NOOOO!!!","Never","Stop","F*ck off","That's so dumb","What were you thinking","I'm not a lawyer, but I'll advise you to not do it","I'm impressed by how horrible that idea is","Negative","You can do that after you find the cure for cancer"]
huh=["I'll never talk",  "Go outside", "Touch some grass", "Get a job", "Look behind you", "You need therapy", "Stay hydrated","You have surpassed the secondly free question limit, please try again later","Look behind you","I see","Not available","To see is to believe","Response failed to load","Ask Google","Ask ChatGPT","Use your brain","Go back to work","¡Viva la revolución!","Meow","Not important","To be or not to be, that is the question","Your question is shit","Ask a better question","Whatever","Follow your heart","Yes and no","No and yes","I don't care","None of my business","Try again","Knowledge is power","Hmmmmmm...","Ask your friend (if you have any)","What","Uhm... USA! USA! USA!","Asparagus","Wait and see","What will the Pope do?"]

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
    