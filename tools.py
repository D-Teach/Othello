import numpy as np
import random
def rng(max):
    return random.randrange(max)







def main():
    a = []
    for i in range(100000):
        a.append(rng(5))

    res = np.zeros((5,), dtype=int)
    for number in a:
        res[number] += 1
    print(res)
    return






if __name__ == '__main__':
    main()
