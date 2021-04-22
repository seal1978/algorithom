def similar(W,L):
    words = L.split(" ")
    total = 0
    for word in words:
        i = 0
        for c in word:
            if c in W:
                i = 1
            else:
                i = 0
                break
        total = total + i        
                
    print(total)    
    
W="love"
L="velo low vole lovee volvell lowly lower lover levo loved love lovee lowe lowes lovey lowan lowa evolve loves volvelle lowed love"
similar(W,L) 
