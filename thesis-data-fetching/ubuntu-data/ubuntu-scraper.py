#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from time import time
import pymysql
import pymysql.cursors

start_time = time()

db = pymysql.connect(host='localhost', user='root', password='password', db='master_thesis', autocommit=True)
cursor = db.cursor()

x = 0
for x in range(0, 132809, 75):
    link = "https://bugs.launchpad.net/ubuntu/+bugs?orderby=-importance&memo=" + str(x) + "&start=" + str(x)
    print("\nMAIN LINK: Scraping and parsing data from: ", link, "\n")

    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    i = 0
    a_len = len(soup.find_all('span', class_='bugnumber'))

    for i in range(a_len):

        x = soup.find_all('span', class_='bugnumber')[i].get_text()
        str_hash = '#'
        if str_hash in x:
            x = x.split(str_hash, 1)
            bug_number = x[1]

        y = soup.find_all('span', class_='field')[i].get_text()
        str_hash = ' (Ubuntu)'
        if str_hash in y:
            y = y.split(str_hash, 1)
            bug_category = y[0]
            bug_category = bug_category.replace(" ", "")
            bug_category = bug_category.replace("\n", "")

        to_scrape = 'https://bugs.launchpad.net/ubuntu/+source/' + bug_category + '/+bug/' + bug_number
        inner_page = requests.get(to_scrape)
        print("SUB LINK ", i+1, ": Scraping and parsing data from: ", to_scrape)
        inner_soup = BeautifulSoup(inner_page.content, 'html.parser')
        try:
            title = inner_soup.find_all('span', class_='ellipsis')[0].get_text()
        #title = title.replace(" ", "")
        #title = title.replace("\n", "")
        #print("Title: ", title)
        except IndexError:
            title = 'Unknown'
        except:
            title = 'Unknown'
        try:
            reporter = inner_soup.find_all('a', class_='person')[0].get_text()
            reporter = reporter.replace(" ", "")
            reporter = reporter.replace("\n", "")
        except IndexError:
            reporter = 'Unknown'
        except:
            reporter = 'Unknown'
        #print("Reporter: ", reporter)
        try:
            assignee = inner_soup.find_all('span', class_='yui3-activator-data-box')[1].get_text()
            assignee = assignee.replace(" ", "")
            assignee = assignee.replace("\n", "")
        except IndexError:
            assignee = 'Unassigned'
        except:
            assignee = 'Unassigned'
        #print("Assignee: ", assignee)
        try:
            description = inner_soup.find_all('div', class_='yui3-editable_text-text')[0].get_text()
        except IndexError:
            description = 'Unknown'
        except:
            description = 'Unknown'
        #print("Description: ", description)
        comment_len = len(inner_soup.find_all('div', class_='comment-text'))
        j = 0
        for j in range(comment_len):
            comment = inner_soup.find_all('div', class_='comment-text')[j].get_text()
            pre_comment = 'Comment ' + str(j+1) + ': '
            #print(pre_comment, comment)
            to_scrape = 'https://bugs.launchpad.net/ubuntu/+source/' + bug_category + '/+bug/' + bug_number + '/comments/' + str(j+1)
            author_page = requests.get(to_scrape)
            if(author_page.status_code == 404):
                to_scrape = 'https://bugs.launchpad.net/ubuntu/+bug/' + bug_number + '/comments/' + str(j+1)
                author_page = requests.get(to_scrape)
                print("Page Status: ", author_page.status_code)
                print("AUTHOR LINK: Scraping and parsing data from: ", to_scrape)
            else:
                print("Page Status: ", author_page.status_code)
                print("AUTHOR LINK: Scraping and parsing data from: ", to_scrape)
                author_soup = BeautifulSoup(author_page.content, 'html.parser')
                try:
                    author = author_soup.find_all('a', class_='person')[0].get_text()
                except IndexError:
                    author = 'Unknown/Deactivated User'
                except:
                    author = author_soup.find_all('a', class_='person-inactive')[0].get_text()

            #print('Author: ', author)
            refstr = "In reply to comment #"
            if refstr in comment:
                try:
                    tagged = ""
                    x = comment.split(refstr, 1)
                    x = x[1].split(")", 1)
                    tagged = x[0]
                    to_scrape = 'https://bugs.launchpad.net/ubuntu/+source/' + bug_category + '/+bug/' + bug_number + '/comments/' + tagged
                    #print("Scraping and parsing tagged person from: ", to_scrape)
                    tagged_page = requests.get(to_scrape)
                    tagged_soup = BeautifulSoup(tagged_page.content, 'html.parser')
                    tagged = tagged_soup.find_all('a', class_='person')[0].get_text()
                    #print('Tagged: ', tagged)
                except ValueError:
                    tagged = "NULL"
                    #print('Tagged: ', tagged)
                except IndexError:
                    tagged = "NULL"
                    #print('Tagged: ', tagged)
            else:
                tagged = "NULL"
                #print('Tagged: ', tagged)

            try:
                cursor.execute("""INSERT INTO ubuntu_try (title, description, comment, reporter, assignee, author, tagged) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s")""" % (title, description, comment, reporter, assignee, author, tagged))
            except:
                db.rollback()

        print('\n')

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
