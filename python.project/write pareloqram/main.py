def rightslash(number):
    for x in range(int(number)):
        print("/", end="")
def leftslash(number):
    for x in range(int(number)):
        print("\\",end="")
def space(number):
    for x in range(int(number)):
        print(" ",end="")
def bottomline(number):
    for x in range(int(number)):
        print()
def toppart(diametr):
    startspace = diametr/2-1
    for x in range(int(diametr/2)):
        space(startspace-x)
        rightslash(1)
        space(x*2)
        leftslash(1)
        bottomline(1)
def bottompart(diametr):
    startspace = diametr-2
    for x in range(int(diametr/2)):
        space(x)
        leftslash(1)
        space(startspace - x*2)
        rightslash(1)
        bottomline(1)
def pareloqram(diametr):
    toppart(diametr)
    bottompart(diametr)

pareloqram(15)
