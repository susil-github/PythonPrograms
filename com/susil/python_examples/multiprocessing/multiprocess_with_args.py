from multiprocessing import Process


def calculate_square(n):
    print(f'The square value is-> {n*n}')


def calculate_cube(n):
    print(f'the cube value is-> {n*n*n}')


if __name__ == '__main__':
    p1 = Process(target=calculate_square, args=(5,))
    p2 = Process(target=calculate_cube, args=(4,))

    p1.start()
    p2.start()
    print('here both the process started...')
    p1.join()
    p2.join()
    print('completed the execution for both of them')