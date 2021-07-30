def write_to_file(text):
    file = open("score2.txt", "a+") #append a+
    file.write(text)
    file.close()


def read_from_file():
    file = open("score2.txt")
    lines = file.readlines()
    file.close()

    return lines

def main():
    while True:
        print("1 Вывести счет команды")
        print("2 Добавить  новый счет")
        option = int(input("choose"))
        if option == 1:
            scores = read_from_file()
            for i in scores:
                print(i)
        if option == 2:
            commands = input()
            score = input()
            write_to_file(f"{commands}-{score}\n")
main()