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

    pblName = 'Pathways'
    week = '2'

    facilitator = 'Alejandra Hernandez'

    # Filling in the lists
    getIDS(ids)
    getLNames(lNames)
    getFNames(fNames)
    getFirstDay(fDay)
    getSecondDay(sDay)
    getThirdDay(tDay)
    getPay(pay)


    fillpdf(fNames,lNames, ids, pblName, week, facilitator, fDay, sDay, tDay, pay)


