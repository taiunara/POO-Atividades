import random



print("GERADOR DE VALORES ALEATÓRIOS:")
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
x = random.sample(l, 6)
def sort(x):
    for final in range(len(x), 0, -1):
        for current in range(0, final - 1):
            if x[current] > x[current+1]:
                x[current], x[current+1] = x[current+1], x[current]


sort(x)
print(x)