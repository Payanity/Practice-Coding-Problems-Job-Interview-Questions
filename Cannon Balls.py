p1Start = 10; p3Start = 20; bottomp1Start = 6; bottomp3Start = 10
#list of pyramids from before p1 to p3
list = [4, 10, 20]

def pyramidCompositeSizeTake6(pSize1, pSize3, bottompSize1, bottompSize3, lister):
    inc1 = 4; inc3 = 5
    while True:
        if (((pSize3 - pSize1) in list) and ((pSize3 - pSize1) != pSize1)): return pSize3
        bottompSize3 += inc3; pSize3 += bottompSize3; inc3 += 1; lister.append(pSize3); bottompSize1 += inc1; pSize1 += bottompSize1; inc1 += 1



def pyramidCompositeSizeTake5(pSize1, pSize3, bottompSize1, bottompSize3, lister):
    inc1 = 4; inc3 = 5
    while True:
        if (((pSize3 - pSize1) in list) and ((pSize3 - pSize1) != pSize1)):
            print(pSize1)
            print(pSize3)
            print(lister)
            return pSize3
        bottompSize3 += inc3;
        pSize3 += bottompSize3;
        inc3 += 1
        lister.append(pSize3)
        bottompSize1 += inc1;
        pSize1 += bottompSize1;
        inc1 += 1
        #print(pSize3)
        #print(lister)

#22 lines of code including print statemnet babeyyyyy and variables above babayyy (would be 19 without print statements in function)
def pyramidCompositeSizeTake4(pSize1, pSize3, bottompSize1, bottompSize3, lister):
    inc1 = 4; inc3 = 5
    while True:
        if (((pSize3 - pSize1) in list) and ((pSize3 - pSize1) != pSize1)):
            print(pSize1)
            print(pSize3)
            print(lister)
            return pSize3
        if (pSize1 >= bottompSize3):
            bottompSize3 += inc3
            pSize3 += bottompSize3
            inc3 += 1
            lister.append(pSize3)
        else:
            bottompSize1 += inc1
            pSize1 += bottompSize1
            inc1 += 1

#wrong algo though (list isn't actually doing anything in this one)... go the right answer with this algo bc of luck; it only factored in
#The bottom layer and pyramid on top being a pyramid combo and not pyramids within, say, possibly the bottom two layers and top three
#or something
"""def pyramidCompositeSizeTake3(pSize1, pSize3, bottompSize1, bottompSize3):
       inc1 = 3
       inc3 = 5
       notFound = True
       while notFound:
            if ((pSize1 == bottompSize3) and ((pSize3 - bottompSize3) != pSize1)) or (((pSize3 - pSize1) in list) and ((pSize3 - pSize1) != pSize1)):
                print(pSize1)
                print(pSize3)
                notFound = False
                return pSize3
            if (pSize1 >= bottompSize3):
               list.append(pSize3)
               bottompSize3+=inc3
               #print(bottompSize3)
               pSize3+=bottompSize3
               inc3+=1
            else:
                bottompSize1 += inc1
                pSize1 += bottompSize1
                #print(bottompSize1)
                inc1+=1


"""

#would only work for seeing if consecutive pyramid sixes add up
"""def pyramidCompositeSize(pSize1, pSize2, pSize3, bottompSize3):
        notFound = True
        while notFound:
            print(pSize3)
            print("\n")
            if pSize1 + pSize2 == pSize3:
                notFound = False
                return pSize3
            else:
                #pSize1 = pSize2
                pSize2 = pSize3
                bottompSize3 += 3
                pSize3 += bottompSize3"""

""" def pyramidCompositeSizeTake2(pSize1, pSize2, pSize3, bottompSize3):
    if pSize1 + pSize2 == pSize3:
        return pSize3
    bottompSize3 +=3
    pyramidCompositeSizeTake2(pSize2, pSize3, pSize3 + bottompSize3, bottompSize3) """



#print(pyramidCompositeSize(3, 10, 19, 9))
#print(pyramidCompositeSizeTake2(p1Start, p2Start, p3Start, bottomp3Start))
#print(pyramidCompositeSizeTake3(p1Start, p3Start, bottomp1Start, bottomp3Start))
print(pyramidCompositeSizeTake4(p1Start, p3Start, bottomp1Start, bottomp3Start, list))
print()
print(pyramidCompositeSizeTake5(p1Start, p3Start, bottomp1Start, bottomp3Start, list))
print()
print(pyramidCompositeSizeTake6(p1Start, p3Start, bottomp1Start, bottomp3Start, list))