import sys

if len(sys.argv) != 2:
    quit()

f = open(sys.argv[1],"r")

dic={}

for word in (f.read().strip().split()):
        if not(word in dic.keys()):
            dic[word] = 1
        else:
            dic[word] += 1

f.close()

print(dic)
