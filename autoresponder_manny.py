
# coding: utf-8

# In[3]:

questions_when = []
answers_when = []
questions_where = []
answers_where = []


# In[8]:

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
                #print('im here')
                print(rdat)
                answer = answers_where[i]

                print(answers_where[i])
            
                ans = answers-where[i]
                i = len(questions_where)-1
            elif i == len(questions_where)-1:
                answer = input()
                i = len(questions_where)-1
        questions_where.append(quest)
        answers_where.append(answer)     

else:
    print('CONGRADULATIONS!!!!! :DD YOU ARE TODAY WINNER!!! You are selected to claim the sum of $500000000000 in the 2017 AI lottery! to claim your prize send 300000 dollars to UCSD')
# print(whend) 


# In[ ]:

print(answers_when)
print(questions_when)
print(answers_where)
print(questions_where)


# In[4]:

def similarsimians(q1,qX):
    
    import httplib, urllib, base64

    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': '41689ab0590c4c15b25498ed85819575',
    }

    params = urllib.urlencode({
        # Request parameters
        's1': q1,
        's2': qX,
    })

    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("GET", "/academic/v1.0/similarity?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    dat = float(str(data)[2:5])
    rdat = round(dat*100)
    return rdat
    
    
    

#     import http.client, urllib.request, urllib.parse, urllib.error, base64

#     headers = {
#     # Request headers
#         'Ocp-Apim-Subscription-Key': '41689ab0590c4c15b25498ed85819575',
#     }

#     params = urllib.parse.urlencode({
#     # Request parameters
#         's1': q1,
#         's2': qX,
#     })

#     try:
#         conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
#         conn.request("GET", "/academic/v1.0/similarity?%s" % params, "{body}", headers)
#         response = conn.getresponse()
#         data = response.read()
# #         print(data)
#         conn.close()
#     except Exception as e:
#         print("[Errno {0}] {1}".format(e.errno, e.strerror))


    


# In[ ]:




# In[ ]:




# In[ ]:



