sample1 = [x**x for x in range(10)]

sample2 = [[x*n for n in range(5)] for x in range(10)]

sample3 = {x: x**x for x in range(5)}

if __name__ == '__main__':
    print('sample 1:', sample1)
    print('sample 2:', sample2)
    print('sample 3:', sample3)
