def verify(isbn):
    digits = list(isbn.replace('-', '').replace('_', ''))
    if digits and digits[-1] == 'X':
        digits[-1] = '10'
    if len(digits) != 10 or any(not d.isdigit() for d in digits):
        return False
    countdown = list(range(10, 0, -1))
    return sum(int(d) * c for d, c in zip(digits, countdown)) % 11 == 0
