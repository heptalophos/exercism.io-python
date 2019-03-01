class Luhn(object):
    def __init__(self, card_num):
        self.number = card_num.replace(" ", "")


    def is_valid(self):
        if (not self.number.isdigit()) or (len(self.number) <= 1):
            return False
        else:
            digits = [int(self.number[i]) for i in reversed(range(len(self.number)))]
            for i in range(len(digits)):
                if i % 2 == 1:
                    digits[i] = digits[i] * 2 if digits[i] * 2 < 9 else digits[i] * 2 - 9
            return sum(digits) % 10 == 0