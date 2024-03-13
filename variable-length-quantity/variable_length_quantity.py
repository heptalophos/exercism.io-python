def encode(numbers: list[int]) -> list[int]:
    encoded = []
    for n in reversed(numbers):
        if n == 0:
            encoded += [0]
        msbit = 0
        while n > 0:
            encoded += [msbit ^ (n & 127)]
            msbit = 128
            n >>= 7
    return encoded[::-1]


def decode(bytes_: list[int]) -> list[int]:
    decoded, n = [], 0
    for idx, byte in enumerate(bytes_):
        n = (n << 7) + (byte & 127)
        if byte & 128 == 0:
            decoded += [n]
            n = 0
        elif idx == len(bytes_) - 1:
            raise ValueError('incomplete sequence')
        else:
            continue
    return decoded 
