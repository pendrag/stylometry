import os
import csv
import requests

def gutenberg_mirror_download(row):
    try:
        num = row['gutenberg_id']
        path = list(num[:len(num)-1])
        path.extend([num, num + ".txt"])
        path = "/".join(path)
        url = "http://mirrors.xmission.com/gutenberg/" + path
        # url = "http://www.gutenberg.org/ebooks/%d.txt.utf-8" % int(row['gutenberg_id'])

        response = requests.get(url)
        print("downloading ") + url
        if not os.path.exists(row['author']):
            os.makedirs(row['author'])
        with open(row['author'] + '/' + row['title'] + '.txt', "wb") as local_file:
            local_file.write(response.content())
    except error:
        print(error)

def gutenberg():
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'gutenberg_mirror.csv'),'rb') as csvfile:
        file_reader = csv.DictReader(csvfile)
        for row in file_reader:
            gutenberg_mirror_download(row)
            print(row)
