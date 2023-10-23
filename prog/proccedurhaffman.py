from readline import write_history_file


k = -1

def index(a):
    global k
    k += 1
    return k
        

def coding(a):
    t = set(a)
    b = [[char, str(index(t))] for char in t]
    cur = "0"
    for i in range(len(b)):
        if (b[i][1] == '0'):
            continue
        elif i == len(b)-1:
            cur = '1' * len(cur)
        else:
            cur = '1' + cur
        b[i][1] = cur
    code = ""
    


def Extractmin(H):
    min = 100

    for i in range(len(H)):
        if min > H[i][1]:
            min = H[i][1]
    for i in range(len(H)):
        if min == H[i][1]:
            H.pop(i)
            break        
    return min

def hoffman(frequencies):
    rez = []
    H = []
    
    for i in range(len(frequencies)):
        H.append([i, frequencies[i]])

    for k in range(len(frequencies), 2*len(frequencies)-1):
        a = Extractmin(H)
        b = Extractmin(H)
        c = a + b
        H.append([k, c])
        rez.append([c, a, b])
    return rez


if __name__ == "__main__":
    a = "abacabad"
    b = "01001100100111"
    coding(a)
    frequencies = [3, 5, 10, 21]
    print(hoffman(frequencies))