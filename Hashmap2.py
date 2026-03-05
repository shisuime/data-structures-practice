wordCount={}

with open("poem.txt","r") as f:
    for line in f:
        # print(line.split(" "))
        tokens=line.split(" ")

        for word in tokens:
            word=word.replace("\n","")
            if word in wordCount:
                wordCount[word]+=1
            else:
                wordCount[word]=1


print(wordCount)