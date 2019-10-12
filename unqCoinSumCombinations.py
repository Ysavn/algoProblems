#You have a collection of coins, and you know the values of the coins and the quantity of each type of coin in it. You want to know how many distinct sums you can make from non-empty groupings of these coins.

def possibleSums(coins, quantity):
    
    #main set containing all unique sum combinations
    st = set()
    for coin, q in zip(coins, quantity):
        
        # temporary set 
        t = set()
        for i in range(q):
            val = coin * (i+1)
            for s_val in st: #for all existing values in set 'st', create new values in set t
                tmp = s_val + val
                t.add(tmp)
            t.add(val)
        st.update(t) # add all values of temporary set to the main set  
    return len(st) # return the len showing unique sum combinations 

