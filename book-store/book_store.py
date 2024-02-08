from collections import Counter

def total(basket):
    counts = []
    for x in [1, 2, 3, 4, 5]:
        if x in Counter(basket).keys():
            counts.append(Counter(basket)[x])
        else:
            counts.append(0)
    counts.sort(reverse = True)
    for i in range(4): counts[i] -= counts[i + 1]
    pairs3and5 = counts[2] if counts[2] <= counts[4] else counts[4]
    counts[2] -= pairs3and5
    counts[4] -= pairs3and5 
    counts[3] += 2 * pairs3and5
    discounts, final_price = [0, 5, 10, 20, 25], 0
    for i in range(5):
        books = counts[i]
        discount = discounts[i]
        final_price += (i + 1) * books * 8 * (100 - discount)
    return final_price