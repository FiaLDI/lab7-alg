

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
    frequencies = [3, 5, 10, 21]
    print(hoffman(frequencies))