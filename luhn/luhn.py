class Luhn(object):
    
    def __init__(self, card_num):
        self.num = card_num.replace(" ", "")
    
    def valid(self):
        if (len(self.num) <= 1) or (not self.num.isdigit()):
            return False
        digits = [int(d) for d in str(self.num[::-1])]
        for i in range(1, len(digits), 2):
            digits[i] *= 2
            if (digits[i] > 9):
                digits[i] -= 9 
        return sum(digits) % 10 == 0