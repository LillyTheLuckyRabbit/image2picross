import sys
import subprocess
from math import ceil
from itertools import groupby
from os.path import exists

def convertImage(fileName):
    assert subprocess.call(["convert", fileName, "-background", "white", "-alpha", "remove", "-alpha", "off", "-compress", "none", "temp.ppm"]) == 0

    imageFile = open("temp.ppm", 'r')
    image = imageFile.read()
    imageFile.close()

    assert "P3" in image

    subprocess.run(["rm", "temp.ppm"])

    return image

def imageToMatrix(image):
    lines = image.splitlines()

    assert lines[0] == "P3"

    if lines[1][0] == '#':
        lines = lines[0:1] + lines[2:]

    res = lines[1].split()
    res= [int(res[0]), int(res[1])]
    padding = [ceil(float(res[0]) / 5.0) * 5 - res[0], ceil(float(res[1]) / 5.0) * 5 - res[1]]

    lines = lines[3:]

    imageMatrix = list()
    for i in range(res[1]):
        imageMatrix.append(list())
        splitLine = list(map(int, lines[i].split()))
        for e in range(res[0]):
            imageMatrix[i].append(splitLine[e * 3 : e * 3 + 3])

    for i in range(int(padding[1] / 2)):
        imageMatrix.insert(0, list())
        for e in range(res[0]):
            imageMatrix[0].append([255, 255, 255])

    for i in range(int(padding[1] / 2) + padding[1] % 2):
        imageMatrix.append(list())
        for e in range(res[0]):
            imageMatrix[-1].append([255, 255, 255])

    for i in imageMatrix:
        for e in range(int(padding[0] / 2)):
            i.insert(0, [255, 255, 255])
        for e in range(int(padding[0] / 2) + padding[0] % 2):
            i.append([255, 255, 255])

    return imageMatrix

def makeLables(imageMatrix):
    rows = list()
    columns = list()

    for i in imageMatrix:
        rows.append(list())
        for color, group in groupby(i):
            if color != [255, 255, 255]:
                rows[-1].append([len(list(group)), color])
        if not len(rows[-1]):
            rows[-1].append([0, [0, 0, 0]])

    for i in range(len(rows)):
        rows[i] = list(reversed(rows[i]))

    imageMatrixRot = [list(reversed(rot)) for rot in zip(*imageMatrix[::-1])]
    imageMatrixRot = list(reversed(imageMatrixRot))

    for i in imageMatrixRot:
        columns.append(list())
        for color, group in groupby(i):
            if color != [255, 255, 255]:
                columns[-1].append([len(list(group)), color])
        if not len(columns[-1]):
            columns[-1].append([0, [0, 0, 0]])

    return rows, columns

def makeGraph(rows, columns, imageMatrix, printSolution):
    print("(* generated with image2picross.py *)")
    print("newgraph")

    print("(* rows *)")
    print("yaxis min 0.5 max " + str(float(len(rows) + 0.5)) + " no_draw_axis")
    print("size " + str(float(len(rows)) * (2.0 / 7.0)) + " no_grid_lines no_draw_hash_marks no_auto_hash_labels")
    for i in range(len(rows)):
        for e in range(len(rows[i])):
            print("newstring hjc vjc x " + str(-0.5 - (0.75 * float(e))) + " y " + str(len(rows) - i))
            print("          fontsize 12 lcolor", end=' ')
            print(float(rows[i][e][1][0]) / 255.0, end=' ')
            print(float(rows[i][e][1][1]) / 255.0, end=' ')
            print(float(rows[i][e][1][2]) / 255.0, end=' ')
            print(":", end=' ')
            print(" " + str(rows[i][e][0]))

    print("(* columns *)")
    print("xaxis min 0.5 max " + str(float(len(columns) + 0.5)) + " no_draw_axis")
    print("size " + str(float(len(columns)) * (2.0 / 7.0)) + " no_grid_lines no_draw_hash_marks no_auto_hash_labels")
    for i in range(len(columns)):
        for e in range(len(columns[i])):
            print("newstring hjc vjc x " + str(len(columns) - i) + " y " + str(len(rows) + 0.5 + (0.75 * float(len(columns[i]) - e))))
            print("          fontsize 12 lcolor", end=' ')
            print(float(columns[i][e][1][0]) / 255.0, end=' ')
            print(float(columns[i][e][1][1]) / 255.0, end=' ')
            print(float(columns[i][e][1][2]) / 255.0, end=' ')
            print(":", end=' ')
            print(" " + str(columns[i][e][0]))

    if printSolution:
        for i in range(len(rows)):
            for e in range(len(columns)):
                colorStr = str(float(imageMatrix[i][e][0]) / 255) + " " + str(float(imageMatrix[i][e][1]) / 255) + " " + str(float(imageMatrix[i][e][2]) / 255)
                print("newline poly pcfill " + colorStr)
                print("   pts", end=' ')
                print(str(e + .5) + " " + str(float(len(rows) - 1 - i + .5)), end=' ')
                print(str(e + .5) + " " + str(float(len(rows) - 1 - i + 1.5)), end=' ')
                print(str(e + + 1.5) + " " + str(float(len(rows) - 1 - i + 1.5)), end=' ')
                print(str(e + + 1.5) + " " + str(float(len(rows) - 1 - i + .5)), end=' ')
                print()
    
    for i in range(len(rows) - 1):
        if (i + 1) % 5 > 0:
            print("newline color 0.75 0.75 0.75")
        else:
            print("newline color 0 0 0")
        print("         pts 0.5 " + str(float(i) + 1.5) + " " + str(float(len(columns)) + 0.5) + " " + str(float(i) + 1.5))

    for i in range(len(columns) - 1):
        if (i + 1) % 5 > 0:
            print("newline color 0.75 0.75 0.75")
        else:
            print("newline color 0 0 0")
        print("         pts " + str(float(i) + 1.5) + " " + str(float(len(rows)) + 0.5) + " " + str(float(i) + 1.5) + " 0.5")

    print("newline pts 0.5 0.5 0.5 " + str(float(len(rows) + 0.5)) + " " + str(float(len(columns) + 0.5)) + " " + str(float(len(rows) + 0.5)) + " " + str(float(len(columns) + 0.5)) + " 0.5 0.5 0.5")


if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Usage: python3 image2picross.py [--solution | -s] image")

printSolution = False
if sys.argv[1] == "-s" or sys.argv[1] == "--solution":
    printSolution = True

image = convertImage(sys.argv[len(sys.argv) - 1])
imageMatrix = imageToMatrix(image)
rows, columns = makeLables(imageMatrix)
makeGraph(rows, columns, imageMatrix, printSolution)
