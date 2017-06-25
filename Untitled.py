
# coding: utf-8

# In[317]:

questions_when = []
answers_when = []
questions_where = []
answers_where = []


# In[327]:

import luis
l = luis.Luis(url='https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/6dc24e47-4be6-4a17-bad5-11cf23a1f1b0?subscription-key=2c52009f6dfc4ef4af55e12fb680b68f&timezoneOffset=0&verbose=true&q=')
question = input()
r = l.analyze(question)
best = r.best_intent()
print (best.intent)
quest = ''

for i in range (0,len(r.entities)):
    quest = quest + ' '+ r.entities[i][0]
print(quest)    


# In[328]:

if best.intent == 'When':
    if len(answers_when) == 0 and len(questions_when) == 0:
        answer = input()
        answers_when.append(answer)
        questions_when.append(quest)
    else:
        for i in range(0,len(questions_when)):
            rdat = similarsimians(quest,questions_when[i])
            if rdat > 75:
                print(rdat)
                answer = answers_when[i]
                print(answers_when[i])
                i = len(questions_when)-1
            elif i == len(questions_when)-1:
                answer = input()
                i = len(questions_when)-1
        questions_when.append(quest)
        answers_when.append(answer)           
                
elif best.intent == 'Where':
    if len(answers_where) == 0 and len(questions_where) == 0:
        answer = input()
        answers_where.append(answer)
        questions_where.append(quest)
    else:
        for i in range(0,len(questions_where)):
            rdat = similarsimians(quest,questions_where[i])
            if rdat > 75:
                print(rdat)
                answer = answers_where[i]
                print(answers_where[i])
                i = len(questions_where)-1
            elif i == len(questions_where)-1:
                answer = input()
                i = len(questions_where)-1
        questions_where.append(quest)
        answers_where.append(answer)     
        
else:
    print('CONGRADULATIONS!!!!! :DD YOU ARE TODAY WINNER!!! You are selected to claim the sum of $500000000000 in the 2017 AI lottery! to claim your prize send 300000 dollars to UCSD')
# print(whend) 


# In[329]:

print(answers_when)
print(questions_when)
print(answers_where)
print(questions_where)


# In[321]:

def similarsimians(q1,qX):

    import http.client, urllib.request, urllib.parse, urllib.error, base64

    headers = {
    # Request headers
        'Ocp-Apim-Subscription-Key': '41689ab0590c4c15b25498ed85819575',
    }

    params = urllib.parse.urlencode({
    # Request parameters
        's1': q1,
        's2': qX,
    })

    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("GET", "/academic/v1.0/similarity?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
#         print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    dat = float(str(data)[2:10])
    rdat = round(dat*100)
    
    return rdat


# In[313]:




# In[139]:

import requests
mydata=[('one','1'),('two','2')]#The first is the var name the second is the value
resp = requests.post('http://localhost/SDAIhack.php',params=mydata)

# mydata=urllib.urlencode(mydata)
# path='http://localhost/SDAIhack.php'    #the url you want to POST to
# req=urllib2.Request(path, mydata)
# req.add_header("Content-type", "application/x-www-form-urlencoded")
# page=urllib2.urlopen(req).read()
print (resp)


# In[ ]:



