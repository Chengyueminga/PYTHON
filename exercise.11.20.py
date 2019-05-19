#1/18/2019
#Game:Connect Four
def main():
    #even for yellow and odd for red
    count = 0
    countColumn = 7 * [0]
    diskPosition = [[0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0]]
    status = "continue"
    while status == "continue":
        if count % 2 == 0:
           red = eval(input("Drop a red disk column(0 - 6):"))
           y = countColumn[red]
           print(red,5 - y)
           diskPosition[5 - y][red] += 1
           countColumn[red] += 1
        else:
            yellow = eval(input("Drop a yellow disk column(0 - 6):"))
            diskPosition[5 - countColumn[yellow]][yellow] += 2
            countColumn[yellow] += 1
        count += 1

        for i in range(6):
            for j in range(7):
                if diskPosition[i][j] == 0:
                    print("| ",end = "")
                elif diskPosition[i][j] == 1:
                    print("|",end = "")
                    print("R",end = "")
                elif diskPosition[i][j] == 2:
                    print("|",end = "")
                    print("Y",end = "")
            print("|")

        for i in range(6):
            for j in range(3):
                countOfConsecutive = 0
                for k in range(1,4):
                    if diskPosition[i][j] == diskPosition[i][j + k] and (diskPosition[i][j] == "Y" or diskPosition[i][j]\
                            == "R"):
                        countOfConsecutive += 1
                    else:
                        break
                if countOfConsecutive == 3:
                    status = "win"

        for i in range(6):
            for j in range(3):
                countOfConsecutive = 0
                for k in range(1,4):
                    if diskPosition[j + k][i] == diskPosition[j][i] and (diskPosition[i][j] == "Y" or diskPosition[i][j]\
                            == "R"):
                        countOfConsecutive += 1
                    else:
                        break
                if countOfConsecutive == 3:
                    status = "win"

        if max(countColumn) > 5:
            status = "draw"

        print(status)
main()
