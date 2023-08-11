from memori import Memori
from code import Code
from qpuc import QPUC

if __name__ == "__main__":
    while True:
        game = QPUC()
        if not game.run():
            continue
        game.cleanup()
        game = Code()
        if not game.run():
            continue
        game.cleanup()
        game = Memori()
        if not game.run():
            continue
        game.cleanup()
        # TODO: Open the door
        break
