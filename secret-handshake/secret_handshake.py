_actions = ["wink", "double blink", "close your eyes", "jump"]

def commands(code):
    seq = [a for i, a in enumerate(_actions) if code & 1 << i]
    if code & 1 << 4:
        seq = list(reversed(seq))
    return seq


def secret_code(actions):
    seq = actions
    if not set(actions).issubset(set(_actions)):
        seq = []
    code = sum(1 << _actions.index(a) for a in _actions)  
    if commands(code) != seq:
        code += 1 << 4
    return code 