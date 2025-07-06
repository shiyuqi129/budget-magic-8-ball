import random

yes=["Yes","YES!!!","Of course","HELL YEAH!","Just do it","I'll allow it","Great idea!","I like that","Yeah","Sure","Cool","Sounds good to me","Positive","Correct"]
no=["HELL NAH!","PLEASE NO","No","NOOOO!!!","Never","Stop","F*ck off","That's so dumb","What were you thinking","I'm not a lawyer, but I'll advise you to not do it","I'm impressed by how horrible that idea is","Negative","You can do that after you find the cure for cancer"]
huh=["Not important","To be or not to be, that is the question","Your question is shit","Ask a better question","Whatever","Follow your heart","Yes and no","No and yes","I don't care","None of my business","Try again","Knowledge is power","Hmmmmmm...","Ask your friend (if you have any)","What","Uhm... USA! USA! USA!","Asparagus","Wait and see","What will the Pope do?"]

while True:
    _=input("What's your question?")
    a=random.random()
    if(a<0.25):
        print(random.choice(yes))
    elif(a<0.5):
        print(random.choice(no))
    else:
        print(random.choice(huh))
    