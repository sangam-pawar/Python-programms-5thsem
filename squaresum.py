def squareDigitSum(num):
    summ = 0
    num = int (num)

    squareNum = num * num

    while squareNum > 0:
        summ = summ + (squareNum % 10)
        

