counter = 0

def increment():
    global counter
    counter += 7

increment()
increment()

print(counter)