from computer import Computer

computer = Computer()
computer.load_file("13.txt")
computer.execute()

count = 0
while True:
    try:
        x = computer.read_from()
        y = computer.read_from()
        tile = computer.read_from()
        if tile == 2:
            count += 1
    except StopIteration:
        break

print(count)
