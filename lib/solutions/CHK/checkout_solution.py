

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A':50, 'B': 30, 'C': 20, 'D': 15}

    #offers
    offers = {'A':(3,130), 'B':(2,45)}
    
    if not isinstance(skus, str) or any(item not in prices for item in skus):
        return -1
    
    total = 0
    for item in 


