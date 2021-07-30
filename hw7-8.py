import datetime

plane = [
    ["*", "*", "*"],  # 0
    ["*", "*", "*"],  # 1
    ["*", "*", "*"]   # 2
]


def print_plane(plane):
    counter = 0
    for i in plane:
        counter += 1
        print(f"| {i[0]} | {i[1]} | {i[2]} |")
        if counter != 3:
            print("|-----------|")


def check_winner(plane):
    for i in range(3):
        if plane[i][0] != "*" and plane[i][0] == plane[i][1] == plane[i][2]:
            return plane[i][0]

    for i in range(3):
        if plane[0][i] != "*" and plane[0][i] == plane[1][i] == plane[2][i]:
            return plane[0][i]

    if plane[0][0] != "*" and plane[0][0] == plane[1][1] == plane[2][2]:
        return plane[0][0]

    if plane[0][2] != "*" and plane[0][2] == plane[1][1] == plane[2][0]:
        return plane[0][2]

    return None


def main():
    print_plane(plane)

    for i in range(9):
        if i % 2 == 0:
            player = "X"
        else:
            player = "0"

        player_x = int(input(f"{player}, введити X координату! "))
        player_y = int(input(f"{player}, введити Y координату! "))
        plane[player_x][player_y] = player
        winner = check_winner(plane)
        if winner:
            print()
            print(f"Winner is {winner}!!!")
            time = datetime.datetime.now()
            file = open("results.txt", "a+")  # append a+
            file.write(f"Winner was: {winner} on ({time})")
            file.close()
            return

        print_plane(plane)
# def txt():



main()


