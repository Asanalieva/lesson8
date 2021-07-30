file = open("score.txt", "r")
lines = file.readlines() # readlines only 1 used
for i in lines:
    print(i)
file.close()

