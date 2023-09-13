from game import Game


def test() -> bool:

    test = Game()

    try:
        test.intro()
    except:
        return False

    try:
        test.run()
    except:
        return False

    return True
