

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A':50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}

    #offers
    offers = {'A':[(3,130)(5,200)], 'B':[(2,45)], 'E': [(2,'B')]}
    
    if not isinstance(skus, str) or any(item not in prices for item in skus):
        return -1
    
    #count how many items of each
    counts_of_items = {}
    for item in skus:
        counts_of_items[item] = counts_of_items.get(item, 0) +1


    total = 0

    #handle different cases seperately
    #special offer
    if 'E' in counts_of_items and 'B' in counts_of_items:
        e_count = counts_of_items['E']
        b_count = counts_of_items['B']
        free_b = e_count // 2
        counts_of_items['B'] = max (0, b_count - free_b)
    
    #other usual offers
    for item,count in counts_of_items.items():
        if item in offers:
            item_offers = sorted(offers[item], key =lambda x: -x[1]) 
            for offer_qty, offer_price in item_offers:
                total += (count //offer_qty) * offer_price
                count %= offer_qty
                #then add remaining at usual price 
        total += count * prices[item]
    return total



