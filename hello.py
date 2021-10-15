
f=open('chatWeb.txt','r',errors='ignore')
number='971 50 974 4722'
w=open(f'{number}.txt','w',errors='ignore')
for line in f.readlines():
    if number in line:
        w.write(str(line.encode(encoding="UTF-8")))
f.close()
w.close()