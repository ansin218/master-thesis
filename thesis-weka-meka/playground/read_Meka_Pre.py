_author_ = 'Rana'


import xlrd
import pymysql

# Open the workbook and define the worksheet
book = xlrd.open_workbook("/Users/Rana/Desktop/Experiments/fine_grained.xlsx")
sheet = book.sheet_by_index(0)


# connect to the database

db = pymysql.connect(host='localhost', user='', password='', db='IRC_Main_Study')

cursor = db.cursor()


id=1
for r in range(1, sheet.nrows):
    print(id)
    prediction_issue = sheet.cell(r, 9).value
    prediction_alternative = sheet.cell(r, 10).value
    prediction_pro = sheet.cell(r, 11).value
    prediction_con = sheet.cell(r, 12).value
    prediction_decision = sheet.cell(r, 13).value
    query = ("UPDATE fine_grained_predictions SET isIssue=%s,isAlternative=%s, isPro=%s ,isCon=%s, isDecision=%s WHERE index_id=%s")
    query_data = (prediction_issue, prediction_alternative, prediction_pro, prediction_con,prediction_decision, id)
    cursor.execute(query, query_data)
    id=id+1





db.commit()
cursor.close()
db.close()