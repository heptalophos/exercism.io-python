class PhoneNumber(object):
    def __init__(self, num):
        INVALID = '0' * 10
        digits = [d for d in num if d.isdigit()]
        if len(digits) == 11 and digits[0] != '1':
            raise ValueError("Invalid number")
        if len(digits) != 10:
            raise ValueError("Invalid number")
        
        self.number = ''.join(digits[-10:]) or INVALID

    def area_code(self):
        if self.number[0] < '2' or self.number[3] < '2':
            raise ValueError("Invalid number")
        return self.number[:3]

    def pretty(self):
        return '({}) {}-{}'.format(
            self.area_code,
            self.number[3:6], 
            self.number[6:]
        )
        
