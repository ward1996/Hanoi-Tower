import sys
import copy

TOTAL_DISKS = 5

SOLVED_TOWER = list(range(TOTAL_DISKS, 0 ,-1))

def main():
    towers = {"A": copy.copy(SOLVED_TOWER), "B": [], "C": []}

    while True:
        display_towers(towers)

        #user's move
        fromTower, toTower = getPlayerMove(towers)

        #moving disks
        solve(fromTower, toTower, towers)
        
        #check if solved
        if SOLVED_TOWER in (towers['B'], towers['C']):
            display_towers(towers)
            print("SOLVED!!")
            sys.exit()



def getPlayerMove(towers):

    while True:
        print('Enter the letters of "from" and "to" towers, or QUIT.')
        print("(e.g., AB to move a disk from tower A to tower B.)")
        print('***** you can type "slove" to auto solve *****')
        print()

        response = input('> ').upper().strip()
        

        if response == 'QUIT':
            print('well played , GG.')
            sys.exit()
        
        if response == "SOLVE":
            TOH("A","C","B",5,towers)

        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print('Enter one of AB, AC, BA, BC, CA, or CB.')
            continue
        fromTower, toTower = response[0], response[1]

        if len(towers[fromTower]) == 0:
            print('you have selected an empty tower')
            continue
        elif len(towers[toTower]) == 0:
            return fromTower, toTower
        elif (towers[toTower][-1] < towers[fromTower][-1]):
            print('cant put a alrger disk on top of a smaller one')
            continue  
        else:
            return fromTower, toTower



def display_towers(towers):
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                display_disk(0)  # Display the bare pole with no disk.
            else:
                display_disk(tower[level])  # Display the disk.
        print()
    emptySpace = " " * (TOTAL_DISKS)
    print("{0} A{0}{0} B{0}{0} C\n".format(emptySpace))

def display_disk(width):
    emptySpace = " " * (TOTAL_DISKS - width)
    if width == 0 :
        print(f"{emptySpace}||{emptySpace}", end=" ")
    else:
        disk = "@" * width
        numLable = str(width).rjust(2, "_")
        print(f"{emptySpace}{disk}{numLable}{disk}{emptySpace}", end=" ")

def solve(source, destination, towers):
    disk = towers[source].pop()
    towers[destination].append(disk)

def TOH(source, auxiliary, destination, numOfDisk, towers):
    
    if numOfDisk  >= 0:
        TOH(source, destination, auxiliary, numOfDisk-1, towers)

        #Moving the disk from source to destination
        
        display_towers(towers)
        try:
            solve(source, destination, towers)
        except:
            sys.exit(1)
            
        TOH(auxiliary, source, destination, numOfDisk-1, towers)




if __name__ == '__main__':
    main()