from json import dumps

moves = []

def move(origin, destination):
    # print("Moving disk from {} to {}".format(origin, destination))
    moves.append([origin, destination])


def hanoi(num_of_disks, origin, temporary, destination):
    if num_of_disks == 0:
        pass
    else:
        hanoi(num_of_disks - 1, origin, destination, temporary)
        move(origin, destination)
        hanoi(num_of_disks - 1, temporary, origin, destination)


hanoi(20, 0, 1, 2)
print(len(moves))
with open("moves.json", "w") as file:
    file.write(dumps(moves))
