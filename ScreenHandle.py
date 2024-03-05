import os

def cls() -> None:
    os.system("cls")

def pause() -> None:
    os.system("pause")

def alert(msg : str) -> None:
    print(msg)
    pause()