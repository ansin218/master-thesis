import nltk
nltk.download('all')


for i in range(len(final_list)):
    current_title = final_list[i]
    query = "SELECT title, comment FROM lucene_try WHERE title = %s"
    cursor.execute(query, final_list[i])
    for row in cursor:
        root_comment = BeautifulSoup(row[1], "lxml").text
        print("Root Title: ", current_title)
        for j in range(len(root_comment)):
            print("Root Comment: ", root_comment[j])
            cleancomment = tokenize.sent_tokenize(root_comment[j])
            for k in range(len(cleancomment)):
                comment = cleancomment[k]
                print("Comment: ", comment)
                #cursor.execute("""INSERT INTO lucene_rs (title, root_comment, comment) VALUES ("%s", "%s", "%s")""" % (current_title, root_comment, comment))

            print("\n")
    print("\n")

cursor.close()
conn.close()
