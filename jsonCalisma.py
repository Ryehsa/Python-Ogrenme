import json

with open("users.json") as users:
    data=json.load(users)
    print(data[0]["address"]["zipcode"])
    #print(data[0])

    #for x in range(5):
        #print(data[x])
       
