def id_generator():
    count = 0
    while True:
        count += 1
        yield count


id_gen = id_generator()
