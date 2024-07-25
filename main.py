from ExtractExcel import *
from WriteToPDF import *

if __name__ == '__main__':
    ids = []
    lNames = []
    fNames = []
    fDay = []
    sDay = []
    tDay = []
    pay = []

    #change based on the class
    pblName = 'Computer Science PM'

    #Change based on the Week
    week = '3'

    #Change based on Facilitator
    facilitator = 'Ngawang Ghongwatsang'

    # Filling in the lists
    getIDS(ids)
    getLNames(lNames)
    getFNames(fNames)
    getFirstDay(fDay)
    getSecondDay(sDay)
    getThirdDay(tDay)
    getPay(pay)


    fillpdf(fNames,lNames, ids, pblName, week, facilitator, fDay, sDay, tDay, pay)


