_author_ = 'Rana'


import xlrd
import pymysql

# Open the workbook and define the worksheet
book = xlrd.open_workbook("/Users/Rana/Desktop/Experiments/binary_predictions.xlsx")
sheet = book.sheet_by_index(0)


# connect to the database

db = pymysql.connect(host='localhost', user='', password='', db='IRC_Main_Study')

cursor = db.cursor()

for r in range(1, sheet.nrows):
    prediction = sheet.cell(r, 2).value
    prediction = prediction.split(':')[1]
    id = sheet.cell(r,5).value
    cursor.execute("UPDATE Message_Binary SET predicted_class=%s WHERE id=%s ", (prediction, id))




db.commit()
cursor.close()
db.close()