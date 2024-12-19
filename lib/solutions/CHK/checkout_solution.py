
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A':50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G':20, 'H':10, 'I':35, 'J':60, 'K':80, 'L':90, 'M':15, 'N':40, 'O':10, 'P':50, 'Q':30, 'R':50,
               'S':30, 'T':20, 'U':40, 'V':50, 'W':20, 'X':90, 'Y':10,'Z':50} 

    #offers
    offers = {'A':[(3,130),(5,200)], 'B':[(2,45)], 'E': [(2,'B')], 'F': [(3,20)], 'H': [(5,45),(10,80)], 'K': [(2,150)],'N':([3,'M']), 'P':[(5,200)], 'Q':[(3,80)],
               'R':[(3,'Q')],'U':[(3,120)],'V':[(2,90),(3,130)]}
    
    if not isinstance(skus, str) or any(item not in prices for item in skus):
        return -1
    
    #count how many items of each
    counts_of_items = {}
    for item in skus:
        counts_of_items[item] = counts_of_items.get(item, 0) +1

    total = 0

    #handle special offers
    if 'E' in counts_of_items and 'B' in counts_of_items:
        e_count = counts_of_items['E']
        b_count = counts_of_items['B']
        free_b = e_count // 2
        counts_of_items['B'] = max (0, b_count - free_b)
    
    if 'U' in counts_of_items and counts_of_items['U'] > 3:
        total += (counts_of_items['U'] // 4) * 120 # discounted rate added
        counts_of_items['U'] = (counts_of_items['U'] % 4)

    if 'F' in counts_of_items and counts_of_items['F'] > 2:
        total += (counts_of_items['F'] // 3) * 20 # discounted rate added
        counts_of_items['F'] = (counts_of_items['F'] % 3)
     
    if 'R' in counts_of_items and 'Q' in counts_of_items:
        r_count = counts_of_items['R']
        q_count = counts_of_items['Q']
        free_q = r_count // 3
        counts_of_items['Q'] = max (0, q_count- free_q)

    if 'N' in counts_of_items and 'M' in counts_of_items:
        n_count = counts_of_items['N']
        m_count = counts_of_items['M']
        free_m = n_count // 3
        counts_of_items['M'] = max (0, m_count- free_m)
    
    #handle the rest
    for item,count in counts_of_items.items():
        if item in offers:
            item_offers = sorted([offer for offer in offers[item] if isinstance(offer[1], int)], key= lambda x: -x[-1]) 
            for offer_qty, offer_price in item_offers:
                total += (count //offer_qty) * offer_price
                count %= offer_qty
                #then add remaining at usual price 
        total += count * prices[item]
    return total




