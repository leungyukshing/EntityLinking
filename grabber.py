import os,sys
from urllib import request
from bs4 import BeautifulSoup
import csv
import codecs

#coding:utf8
# create file
path = "list.csv"
with open(path, 'w', newline='', encoding='utf-8-sig') as f:
	csv_write = csv.writer(f)
	csv_head = ["Name_en", "Name_ch", "Rank", "Score", "Region"]
	csv_write.writerow(csv_head)

# get data from website
url = "https://www.cingta.com/detail/11984"
req = request.Request(url)
page = request.urlopen(req)
soup = BeautifulSoup(page, "html.parser")
page.close()

tables = soup.findAll('table')
tab = tables[0]

for tr in tab.tbody.findAll('tr'):
	tds = tr.findAll('td')
	if len(tds) != 11:
		continue
	name_en = tds[0].getText()
	name_ch = tds[1].getText()
	rank = tds[2].getText()
	score = tds[3].getText()
	region = tds[4].getText()
	print(name_en)
	print(name_ch)
	print(rank)
	print(score)
	print(region)

	with open(path, 'a+', newline='', encoding='utf-8-sig') as f:
		csv_write = csv.writer(f)
		data_row = [name_en, name_ch, rank, score, region]
		csv_write.writerow(data_row)