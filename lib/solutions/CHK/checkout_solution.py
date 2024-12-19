
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A':50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G':20, 'H':10, 'I':35, 'J':60, 'K':80, 'L':90, 'M':15, 'N':40, 'O':10, 'P':50, 'Q':30, 'R':50, 'S':30, 'T':20, 'U':40, 'V':50}

    #offers
    offers = {'A':[(3,130),(5,200)], 'B':[(2,45)], 'E': [(2,'B')], 'F': [(3,20)], 'H': [(5,45),(10,80)], 'K': [(2,150)],'N':([3,'M']), 'P':[(5,200)], 'Q':[(3,80)], 'R':[(3,'Q')],'U':[(3,120)],'V':[(2,90),(3,130)] }
    
    if not isinstance(skus, str) or any(item not in prices for item in skus):
        return -1
    
    #count how many items of each
    counts_of_items = {}
    for item in skus:
        counts_of_items[item] = counts_of_items.get(item, 0) +1


    total = 0

    print(counts_of_items)
    #handle different cases seperately
    #new special offer:
    if 'F' in counts_of_items and counts_of_items['F'] > 2:
        total += (counts_of_items['F'] // 3) * 20 # discounted rate added
        counts_of_items['F'] = (counts_of_items['F'] % 3)
     
    #special offer
    if 'E' in counts_of_items and 'B' in counts_of_items:
        e_count = counts_of_items['E']
        b_count = counts_of_items['B']
        free_b = e_count // 2
        counts_of_items['B'] = max (0, b_count - free_b)
    
    #other usual offers
    for item,count in counts_of_items.items():
        if item in offers:
            item_offers = sorted([offer for offer in offers[item] if isinstance(offer[1], int)], key= lambda x: -x[-1]) 
            for offer_qty, offer_price in item_offers:
                total += (count //offer_qty) * offer_price
                count %= offer_qty
                #then add remaining at usual price 
        total += count * prices[item]
    return total


#Sorry - im not too sure how much you value formatting over timing  - I have assumed timing and speed is more important! thank you


