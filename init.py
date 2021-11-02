
width = int(input('Input board width: '))
height = int(input('Input board height: '))

def initialize_field(w, h):
    rectangular = []
    if(w > 0 and h > 0):
        for i in range(h):
            rectangular.append([0])
            for j in range(w):
                rectangular[i] = [0] * w
    return rectangular;

field = initialize_field(width, height)

def print_field(field):
    w_str = ""
    print("-- Game board --")
    for i in range(len(field)):
        w_str = ""
        for j in range(len(field[i])):
            w_str += "[" + str(field[i][j]) + "]"
        print(w_str)
        w_str = ""
    return 0;

print_field(field)
