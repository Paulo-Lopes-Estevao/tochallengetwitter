
def VerifyState(state: bool):
    if state:
        return AtivarState()
    return DesativarState()


def AtivarState():
    return True


def DesativarState():
    return False
