from fillpdf import fillpdfs
import datetime
from cursive import *
from fillpdf import fillpdfs

def fillpdf(fNames:list, lNames:list ,ids:list, pblName:str, week:str, facilitator:str, fDay:list, sDay:list,\
            tDay:list, pay:list) -> None:

    date = datetime.datetime.today()
    formatted_date = date.strftime("%Y-%m-%d")


    form_fields = list(fillpdfs.get_form_fields('SYEP 2024 YY PBL Attendance Sheet.pdf').keys())
    for i in range(1,len(ids)):

        choice = ''
        if pay[i] == 0:
            choice = 'Choice3'
        elif pay[i] == 1:
            choice = 'Choice2'
        else:
            choice = 'Choice1'


        data_dict = {
            form_fields[0]: fNames[i] + ' ' + lNames[i],
            form_fields[1]: ids[i],
            form_fields[2]: pblName,
            form_fields[3]: ' ' + week,
            form_fields[4]: '  7',
            form_fields[5]: '  15',
            form_fields[6]: '  7',
            form_fields[7]: '  19',
            form_fields[9]: fDay[i],
            form_fields[10]: 'NONE' if fDay[i] != 0 else 'Did not show up/Did not complete work',
            form_fields[11]: '3',
            form_fields[12]: sDay[i],
            form_fields[13]: 'NONE' if sDay[i] != 0 else 'Did not show up/Did not complete work',
            form_fields[14]: '3',
            form_fields[15]: tDay[i],
            form_fields[16]: 'NONE' if tDay[i] != 0 else 'Did not show up/Did not complete work',
            form_fields[27]: formatted_date,
            form_fields[28]: '3',
            form_fields[31]: week,
            form_fields[32]: facilitator,
            form_fields[33]: choice,
            form_fields[35]: fDay[0],
            form_fields[36]: sDay[0],
            form_fields[37]: tDay[0]

        }


        fillpdfs.write_fillable_pdf('SYEP 2024 YY PBL Attendance Sheet.pdf', 'WEEK ' + week + ' ' + \
                                    fNames[i] + ' ' + lNames[i] +'.pdf', data_dict)