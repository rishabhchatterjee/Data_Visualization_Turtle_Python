import math, random

################################################################################
#                GET LARGER CALL STACK TO CALC UPTO MANY DIGITS                #
################################################################################

def callWithLargeStack(f,*args):   # Course Notes
    import sys
    import threading
    threading.stack_size(2**27)  # 64MB stack
    sys.setrecursionlimit(2**27) # will hit 64MB stack limit first
    # need new thread to get the redefined stack size
    def wrappedFn(resultWrapper): resultWrapper[0] = f(*args)
    resultWrapper = [None]
    #thread = threading.Thread(target=f, args=args)
    thread = threading.Thread(target=wrappedFn, args=[resultWrapper])
    thread.start()
    thread.join()
    return resultWrapper[0]

################################################################################
#                CALCULATE UPTO N DIGITS AFTER . FOR RATIONAL NUMBERS          #
################################################################################

def division(divident, divisor, digits = 10, count = 0, ans =[]):
    if(count >= digits):
        return []
    else:
        remainder = divident % divisor
        quotient = divident // divisor
        if(quotient >= 10):
            ans.append((quotient // 10))
            ans.append((quotient % 10))
        else:
            ans.append((quotient))
        nextDivident = remainder*10
        return  ans + division(nextDivident, divisor, digits, count + 1, ans=[])

################################################################################
#                 GET RID OF TERMINATING 0'S LEAVING ONE 0                     #
################################################################################

def endingZeroesTerminate(L):
    zeroCount = 0
    if(0 in L):
        first = L.index(0)
        remaining  = len(L) - first 
        for i in range(first, first + remaining):
            if(L[i] == 0):
                zeroCount += 1
        if(zeroCount >= remaining - 1):
            L = L[:first + 1]
        return L
    else:
        return L