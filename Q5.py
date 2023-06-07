Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword Art Online","Bleach","Dragon Ball Z","One Piece"]
must_watch = ["Full Metal Alchemist","Code Geass","Death Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack On Titan"]

def f(mainstream,must_watch):

    print(list(set(Mainstream) & set(must_watch)),
    list(set(Mainstream) ^ set(must_watch)))

f(Mainstream,must_watch)