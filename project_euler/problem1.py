'''
PROBLEM1: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
#approach: create a function that takes in two arguments: a list of natural numbers, and a another natural number.

import sys

def findMultiplesSumBelowBound(natList, bound):
    '''
    natList     list of nonnegative integer. if an element is greater than the bound arg, then its ignored essentially
    bound       integer that is nonnegative
    '''
    
    #create a list that we will simply sum in the end, which is empty in the beginning
    counterList = []
    
    #iterate through each item in the input list
    for num in natList:
        #skip the trivial case where the natural number is 0 since adding this to our counterList is pointless will not add anything to our sum
        if num == 0:
            continue
        #iterate through each possible multiplicand: obviously bound-1 is the maximum multiplicand for the smallest multiplier - which is 1 (0 is skipped)
        for multiplicand in range(1, bound):
            #check if the product is less than the bound
            if ((multiplicand * num) < bound):
                #if the product is less, then append the product (the multiple) to our counterList
                counterList.append(multiplicand * num)
            #if the product is greater than the bound
            else:
                #then every product after this for this num will also be greater than the bound, so skip on to the next num instead of checking each multiplicand
                break
    
    return sum(counterList)

def main():
    natList = [int(i) for i in sys.argv[2:len(sys.argv)]]
    if not natList:
        print('List of natural numbers is empty. Exiting prematurely.')
        sys.exit()
    print(findMultiplesSumBelowBound(natList, int(sys.argv[1])))

if __name__ == "__main__":
    main()           
