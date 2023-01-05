# picking

import pickle
s={1:["abc",56],2:["xyz",78]}
fw=open("stud1.data","wb")
pickle.dump(s,fw)
fw.close()
fr=open("stud1.data","rb")
data=pickle.load(fr)        #it will fetch the first record

try:
    while True:
        print(data)
        pickle.load(fr)
except:
    print("file read")
print("chale jaaaaa")