import random

yes=["Yes","YES!!!","Of course","HELL YEAH!","Just do it","I'll allow it","Great idea!","I like that","Yeah","Sure","Cool"]
no=["PLEASE NO","No","NOOOO!!!","Never","Stop","F*ck off","That's so dumb","What were you thinking","I'm not a lawyer, but I'll advise you to not do it","I'm impressed by how horrible that idea is"]
huh=["Ask a better question","Whatever","Follow your heart","Yes and no","No and yes","I don't care","Non of my business","Try again","Hmmmmmm...","Ask your friend (if you have any)","What","Uhm... USA! USA! USA!"]

while True:
    _=input("What's your question?")
    a=random.random()
    if(a<0.3):
        print(random.choice(yes))
    elif(a<0.6):
        print(random.choice(no))
    else:
        print(random.choice(huh))
    