#cerner_2^5_2020
c = []
while True:
    c += (lambda d : [(a, b) for a, b in zip(d[:-1], d[1:])])("".join([a for a in __import__("itertools").filterfalse(lambda a : a in ["!", "?", ".", ","], input("> ").lower())]).split(" "))
    e = (lambda f : ([f[0], f[1]] + [((f := (None, None) if  [i for i in c if i[0] == f[1]] == [] else (__import__("random").choice([i for i in c if i[0] == f[1]])))[1]) for n in range(20)]))(__import__("random").choice(c))
    print(" ".join([i for i in e if i != None]))

'''
A really dumb "Markov-ish" chatbot.

EXAMPLE:
PS C:\dev\personal> python .\really_dumb_chat_bot.py
> Hello my new chatbot!
new chatbot
> Yes, you are a robot!
a robot
> Indeed, you are a creature of my own creation that has no free will!
of my new chatbot
> I don't think you have a chatbot?
yes you have a robot
> Indeed, that robot is you
my new chatbot
> What robot is it that you are speaking of?
robot is it that robot is you have a creature of my new chatbot
> I don't understand
has no free will
> Yes, I suppose that is a good explanation of this conversation
'''
