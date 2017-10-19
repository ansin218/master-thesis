_author_ = 'Rana'

import pymysql
from xlutils.copy import copy
from xlrd import open_workbook

# Copy the template and create a new sheet

wb = copy(open_workbook('Template.xls', formatting_info=True))
ws=wb.get_sheet(0)
row_num=1
column_num=0


# connect to the database
database = pymysql.connect(host='localhost', user='root', password='password', db='Issue_Trackers')
cursor = database.cursor()


# Read issue information and store them in arrays

issue_id=[]
issue_title=[]
#issue_description=[]
issue_reporter=[]
issue_assignee=[]

cursor.execute("SELECT issue_id, title, reporter, assignee FROM thunderbird_rss_issues")
for row in cursor:
    issue_id.append(row[0])
    issue_title.append(row[1])
    issue_reporter.append(row[2])
    issue_assignee.append(row[3])


# for each issue:
# 1) insert its information into a new row in the excel sheet
# 2) insert all the comments information after that (each sentence in a new row)



issues_len=len(issue_id)
for i in range(0,issues_len):
    # Insert the issue information
    ws.write(row_num, column_num, issue_id[i])
    column_num+=1
    ws.write(row_num, column_num, issue_title[i])
    column_num += 1
    #ws.write(row_num, column_num, issue_description[i])
    #column_num += 1
    ws.write(row_num, column_num, issue_reporter[i])
    column_num += 1
    ws.write(row_num, column_num, issue_assignee[i])
    column_num += 1
    wb.save('First_Trial.xls')



    # Retrieve its comments and insert them into the excel sheet
    cursor.execute("SELECT  author, tagged, comment, sentence FROM thunderbird_rss_comments WHERE issue_id="+str(issue_id[i]))
    for row in cursor:
        column_num=5
        ws.write(row_num, column_num, row[0])
        column_num += 1
        ws.write(row_num, column_num, row[1])
        column_num += 1
        ws.write(row_num, column_num, row[2])
        column_num += 1
        ws.write(row_num, column_num, row[3])
        row_num+=1


    column_num=0
    wb.save('First_Trial.xls')




cursor.close()
database.close()
