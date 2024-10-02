import sys

def circular_massiv(n, m):
    massiv = []
    i = 0

    while True:
        massiv.append(i + 1)
        i = (i + m - 1) % n
        
        if i == 0:
            break

    result = []
    for number in massiv:
        result.append(str(number))
    
    return ''.join(result)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("python task1.py <n> <m>")
    else:
        result = circular_massiv(int(sys.argv[1]), int(sys.argv[2]))
        print(result)
