#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def calc(firstNum, attrList):
    expectNum = len(attrList)
    if expectNum == 0:
        exit(0)
    secondNumList = []
    compareList = []
    bigData = {
        1: {"name": "leader", "num": [3,16,21,23,24,31,33]},
        2: {"name": "rich", "num": [15,16,24,31,32,33,41,52]},
        3: {"name": "soft", "num": [5,6,11,15,16,24,25,31,32,35,45]},
        4: {"name": "girlful", "num": [5,6,15,16,35]},
        5: {"name": "helpFamily", "num": [3,5,6,11,13,15,16,24,31,32,35]},
        6: {"name": "skill", "num": [13,14,22,26,29,33,36,38,42]},
        7: {"name": "flighty", "num": [15,19,24,25,26,28,32,42]}
    }
    for i in attrList:
        secondNumFor = []
        for num in bigData[i]["num"]:
            if num > (firstNum):
                secondNumFor.append(num - firstNum)
        compareList.append(secondNumFor)
    for i in compareList:
        secondNumList += i
    secondNumList = list(set(secondNumList))
    removeNum = []
    if expectNum > 1:
        for num in secondNumList:
            for i in range(expectNum):
                if num not in compareList[i]:
                    removeNum.append(num)
        for i in removeNum:
            if i in secondNumList:
                secondNumList.remove(i)
    return secondNumList

def sanitate(totalList, unexpect):
    bigData = {
        1: {"name": "bloody", "num": [17,19,20,27,32,34,44,47]},
        2: {"name": "diequick", "num": [4,9,10,19,20,34,44]},
        3: {"name": "swordhurt", "num": [3,4,6,8,9,10,12,14,17,18,19,20,28]},
        4: {"name": "desest", "num": [10,19,20,27,28,34,39,44]},
        5: {"name": "shenjing", "num": [4,34,44,54]},
        6: {"name": "suside", "num": [20,27,34]}
    }
    for idx, num in enumerate(totalList):
        for i in unexpect:
            if num in bigData[i]["num"]:
                totalList[idx] = "%s-%s" % (num, bigData[i]["name"])
    return totalList                
    

def main(fir, expect):
    print(calc(fir, expect))
    secList = calc(fir, expect)
    for i in secList:
        totalNum = []
        secNum = []
        for t in calc(i, expect):
            secNum.append(t+i)
            totalNum.append(t+fir+i)
        totalNum = sanitate(totalNum, [1,2,3,4,5,6])
        print("%s - %s - %s - %s" % (i, calc(i, expect), secNum, totalNum))




if __name__ == '__main__':
    main(12, [1,2,3,5])