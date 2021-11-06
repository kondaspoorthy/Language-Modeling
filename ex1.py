def loadBook(filename):
    lst=[]
    file=open(filename,"r")
    book=file.read()
    for line in book:
        innerlst=line.split(" ")
        lst.append(innerlst)
    return lst
print(loadBook("data/test1.txt"))
