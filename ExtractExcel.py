import datetime
from openpyxl import load_workbook

# Name of Excel File
book = load_workbook('Activity Sheet Participant Info - Week 5.xlsx', data_only=True)

#Change sheet based on which sheet you want the info read from, bottom of the page gives you the name of the sheet
sheet = book['Youth Advocacy Hillcrest SB PM']

def getClass():
    return (sheet['A2']).value
def getIDS(ids: list) -> None:

    first = True
    for cell in sheet['B']:
        if cell.value:
            if first:
                ids.append((cell.value))
                first = False
            else:
                try:
                    ids.append(int(cell.value))
                except ValueError:
                    pass  # Skip non-integer values


def getFNames(fNames: list) -> None:
    for cell in sheet['C']:
        if cell.value:
            fNames.append(cell.value)


def getLNames(lNames: list) -> None:
    for cell in sheet['D']:
        if cell.value:
            lNames.append(cell.value)


def getFirstDay(fDay: list) -> None:
    first = True
    for cell in sheet['E']:
        if cell.value is not None:
            if first:
                fDay.append(cell.value)
                first = False
            elif not first:
                try:
                    fDay.append(float(cell.value))
                except (ValueError):
                    pass  # Skip non-numeric values
def getSecondDay(sDay: list) -> None:
    first = True
    for cell in sheet['F']:
        if cell.value is not None:
            if first:
                sDay.append(cell.value)
                first = False
            elif not first:
                try:
                    sDay.append(float(cell.value))
                except (ValueError):
                    pass  # Skip non-numeric values

def getThirdDay(tDay: list) -> None:
    first = True
    for cell in sheet['G']:
        if cell.value is not None:
            if first:
                tDay.append(cell.value)
                first = False
            elif not first:
                try:
                    tDay.append(float(cell.value))
                except (ValueError):
                    pass  # Skip non-numeric values
def getPay(pay: list) -> None:
    first = True
    for cell in sheet['H']:
        if cell.value != None:
            try:
                if first:
                    pay.append((cell.value))
                    first = False
                else:
                    pay.append(int(cell.value))
            except ValueError:
                pass  # Skip non-numeric values

