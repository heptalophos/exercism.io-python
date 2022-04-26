class PhoneNumber(object):
    def __init__(self, num):
        INVALID = '0' * 10
        digits = [d for d in num if d.isdigit()]
        if len(digits)
        if len(digits) == 11: 
            if digits[0] != '1':
                raise ValueError("11 digits must start with 1")
            else:
                digits = digits[1:]
        if len(digits) != 10:
            raise ValueError("Number over or less than 10 digits")
        self.number = ''.join(digits[-10:]) or INVALID
        if self.number[0] == '0' :
            raise ValueError("exchange code cannot start with zero")
        if self.number[0] < '2' :
            raise ValueError("exchange code cannot start with one")
        if self.number[3] == '0' :
            raise ValueError("area code cannot start with zero")
        if self.number[3] < '2' :
            raise ValueError("area code cannot start with one")
        self.area_code = self.number[:3]

    def pretty(self):
        return '({})-{}-{}'.format(
            self.area_code,
            self.number[-7:-4], 
            self.number[-4:]
        )
        
