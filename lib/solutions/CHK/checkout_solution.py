

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



    for item in 'ABCD':
        count = skus.count(item)
        if item in offers:
            

            offer_qty, offer_price = offers[item]
            if item == 'A':
            
            total += (count //offer_qty) * offer_price #apply offer here
            total += (count % offer_qty) * prices[item] #remaining 
        else:
            total += count * prices[item]

    return total 






