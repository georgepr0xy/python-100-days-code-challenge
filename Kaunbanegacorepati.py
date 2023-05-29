listofqns=('who is the Pm','who is the president of india?','who is the Tesla CEO')
listofans=('elon musk','Narendra modi','Droupadi murmur')
print(listofqns[0])
print('Your options are:',listofans)
takeans=input()
if(takeans == listofans[1]):
    print("you won 5000rs")
else:
 print('you lost')