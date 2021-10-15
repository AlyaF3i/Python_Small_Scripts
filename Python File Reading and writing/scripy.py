
myFile=open('Chat.txt','r',errors='ignore')
#text=myFile.read().split('\n')

#outputFile=open('output.txt','w')
word="computer organization"
counter=0
for a in myFile.readlines():
    if word in str(a).lower():
        counter+=1

print(f"{word} aquired {counter} times in the chat")