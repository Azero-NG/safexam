import re

#file=input("Please input the directory of html file:")
#html=open(file).read()
html=open('test.html').read()
#print(html)
library=open('ALL.txt').read()

P_CH=re.compile('<dl id="CH(.{1,2})">([\s\S]*?)</dl>')
P_CH_title=re.compile('<dd class="subject">(.*?)</dd>')
answer=''
num=0
error=0
for x in P_CH.findall(html):
    answer=P_CH_title.findall(x[1])[0]
    answer=answer[0:len(answer)]
    P_CH_answer=re.compile(answer+'.*?------(.*?)------')
    num=int(x[0])
    try:
        answer=P_CH_answer.findall(library)[0]
        print(x[0]+answer)
    except:
        print(x[0]+"error")
        error+=1

P_MC=re.compile('<dl id="MC(.{1,2})">([\s\S]*?)</dl>')
P_MC_title=re.compile('<dd class="subject">(.*?)</dd>')
for x in P_MC.findall(html):
    answer=P_MC_title.findall(x[1])[0]
    answer=answer[0:len(answer)-2]
    P_MC_answer=re.compile(answer+'.*?------(.*?)------')
    try:
        answer=P_MC_answer.findall(library)[0]
        print(str(num+int(x[0]))+answer)
    except:
        print(x[0]+"error")
        error+=1

P_TF=re.compile('<dl id="TF(.{1,2})">([\s\S]*?)</dl>')
P_TF_title=re.compile('<dd class="subject">(.*?)</dd>')
for x in P_TF.findall(html):
    answer=P_TF_title.findall(x[1])[0]
    answer=answer[0:len(answer)-2]
    P_TF_answer=re.compile(answer+'.*?------(.*?)------')
    try:
        answer=P_TF_answer.findall(library)[0]
        print(x[0]+answer)
    except:
        print(x[0]+"error")
        error+=1
print(error)
