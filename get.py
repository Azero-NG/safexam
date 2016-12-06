import urllib.request
import re
#################define function######################################
def Getone(data):
    pattern = re.compile('<div class="list_text" >([\s\S]*)<div class="page">')
    data=pattern.findall(data)#where all the question is
    pattern = re.compile('<dl>[\s\S]*?</dl>')
    data=pattern.findall(data[0])#where every answer is
    question=[]
    title = re.compile("<dt>(.*)?（ ")
    P_answer = re.compile('<span style="color:red;">(.*?)</span>')
    for x in data:
        try:
            question.append([])
            question[len(question)-1].append(title.findall(x)[0])
            question[len(question)-1].append(P_answer.findall(x)[0])
        except:
            print("error")
            pass
    return question
#############################main###################################



type=['CH','MC','TF']
P_page=re.compile('共 <span>(.*?)</span> 页')



for i in range(1,8):
    for j in type:
       url ="http://121.194.63.3/web_jiaoda/index.php?m=member&c=index&a=examtraining&id=" + str(i) + "&type=" + j
       data = urllib.request.urlopen(url).read().decode("UTF-8")
       page = int(P_page.findall(data)[0])
       question = Getone(data)
       for x in question:
           try:
               print(x[0]+'------'+x[1]+'------')
           except:
               print("error")
               pass


       for k in range(1,page):
           url= "http://121.194.63.3/web_jiaoda/index.php?m=member&c=index&a=examtraining&id=" + str(i) + "&type=" + j + "&page=" + str(k)
           data = urllib.request.urlopen(url).read().decode("UTF-8")
           question = Getone(data)
           for x in question:
               try:
                   print(x[0]+'------'+x[1]+'------')
               except:
                   print("error")
                   pass

