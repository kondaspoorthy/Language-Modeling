def getTopWords(count, words, probs, ignoreList):
    dict={}
    for i in range(0,len(words)):
        dict[words[i]]=probs[i]
    print(dict)
getTopWords(2, [ "hello", "world", "again"], [2/5, 2/5, 1/5], [])