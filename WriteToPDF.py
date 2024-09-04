from fillpdf import fillpdfs
import datetime
import os
import shutil

def fillpdf(fNames:list, lNames:list, ids:list, pblName:str, week:str, facilitator:str, fDay:list, sDay:list,\
            tDay:list, pay:list) -> None:
    # Create a new folder named "Week_X_PDFs" (replace X with the week number)
    folder_name = f"Week {week} - {pblName}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

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
            form_fields[9]: fDay[i],
            form_fields[10]: 'NONE' if fDay[i] != 0 else 'Did not show up/Did not complete work',
            form_fields[12]: sDay[i],
            form_fields[13]: 'NONE' if sDay[i] != 0 else 'Did not show up/Did not complete work',
            form_fields[15]: tDay[i],
            form_fields[16]: 'NONE' if tDay[i] != 0 else 'Did not show up/Did not complete work',
            form_fields[18]: 0,
            form_fields[19]: 'NONE' if tDay[i] != 0 else 'Did not show up/Did not complete work',
            form_fields[26]: fNames[i] + ' ' + lNames[i], #signature for online classes
            form_fields[27]: formatted_date,
            form_fields[31]: week,
            form_fields[32]: facilitator,
            form_fields[33]: choice,
        }

        # Change file name based on the week
        pdf_name = f"WEEK {week} {fNames[i]} {lNames[i]}.pdf"
        fillpdfs.write_fillable_pdf('SYEP 2024 YY PBL Attendance Sheet W' + week + '.pdf', pdf_name, data_dict)

        # Move the generated PDF into the new folder
        shutil.move(pdf_name, os.path.join(folder_name, pdf_name))
