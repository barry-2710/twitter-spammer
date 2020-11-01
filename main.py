import json

file = open('tweets.json')
data = json.load(file)
racial_slurs = ['miserly', 'jew' 'red_savage', 'mongrel', 'half_breed' , 'sambo', 'spook', 'nigger', 'coon', 'kike']
tweet =[]
slur_used = ""
id = 0
for i in data['tweets']:
    tweet.append(i['tweet'])
for word in tweet:
    id += 1
    text = word.split()
    count = 0
    for l in text:
        if(l in racial_slurs):
            count += 1
    pro = (count/len(text))
    print("The profanity of id ",id, "is", pro)