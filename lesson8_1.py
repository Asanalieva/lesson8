import datetime
time = datetime.date.today()
file = open("score.txt", "w")
file.write("Hello, World!\n")
file.write("I love Python")
file.close()