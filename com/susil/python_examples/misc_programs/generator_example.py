def generate():
    for i in range(5):
        yield i

g = generate()

print(next(g))