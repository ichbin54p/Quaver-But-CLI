from platform import system
from sys import stdin

def map_picker(maps):
    current = 0
    print(f"> {maps[current]} < {maps[current+1]}", end="\r")
    while True:
        if stdin.read(1) == "a":
            current += 1
        elif stdin.read(1) == "d":
            current -= 1
        if current == 0:
            print(f"\r> {maps[current]} < {maps[current+1]}", end="\r")
        elif current == len(maps):
            print(f"\r{maps[current-1]} > {maps[current]} < {maps[current+1]}", end="\r")
        else:
            print(f"\r{maps[current-1]} > {maps[current]} <", end="\r")
        

while True:
    if system().lower() == "linux":
        command = input("> ")
        if command == "play":
            map_picker(
                [
                    {
                        "name": "test"
                    },
                    {
                        "name": "test2"
                    },
                    {
                        "name": "test3"
                    }
                ]
            )
    else:
        print("Support for other operating systems are still being developed...")

