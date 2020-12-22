def solution(N):

    k = 1
    begin = 0
    point = 0
    maxNum = 0
    while n != 0:
        while k * 2 <= n:
            k = k * 2
            begin = begin + 1
        if point - begin - 1 > maxNum:
            maxNum = point - begin - 1
        point = begin
        n = n - k
        k = 1
        begin = 0
    print (maxNum)
