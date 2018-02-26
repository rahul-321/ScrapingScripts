from lxml import html
import requests
import os
import GenericDAL
import yaml
import csv

config=open('Config.yaml')
conf=yaml.load(config)

query="select * from %s "%(conf['WriterTable'])
writerIdList=GenericDAL.QueryResult(query,conf)

#director="name/nm0000095/?ref_=tt_ov_dr"
for writer in writerIdList:
	if float(writer[2])!=0.00:
		print(writer[0])
		continue
	print(writer[2])
	start_page1= requests.get("http://www.imdb.com/"+writer[0])
	tree1=html.fromstring(start_page1.text)

	movies=tree1.xpath('//div[@class="filmo-category-section"]/div[starts-with(@id,"writer")]/b/a/@href')
	dates=tree1.xpath('//div[@class="filmo-category-section"]/div[starts-with(@id,"writer")]/span[@class="year_column"]/text()')
	baseUrl="http://www.imdb.com"

	count=0
	total=0
	for movieId in movies:
		finalUrl=baseUrl+movieId
		start_page2=requests.get(finalUrl)
		tree2=html.fromstring(start_page2.text)
		imdbL=tree2.xpath('//span[@itemprop="ratingValue"]/text()')

		# imdb ratings
		if len(imdbL)==0:
			continue
		else:
			imdb=str(imdbL[0])

		#release date
		try:
			dateL=tree2.xpath('//div[@class="subtext"]/a[@title="See more release dates"]/text()')
			if len(dateL)==0:
				continue
			else:
				date=dateL[0]
			''.join(date.split())	
			dsn=date.find('(')
			releaseDate=date[:dsn]
		except Exception as e:
			continue

		releaseDate=releaseDate.strip()
		releaseDate=releaseDate.split(" ")
		try:
			releaseDate=int(releaseDate[2])
		except:
			continue

		if((releaseDate)<2005):
			break

		#print(imdb,"	",releaseDate)
		total+=float(imdb)
		count+=1
	try:
		print(total/count)
		score="%.4f" % (total/count)
		query="update %s set score= %s where id= '%s'"%(conf['WriterTable'],score,writer[0])
	except:
		continue
	try:
		GenericDAL.ExecuteQuery(query,conf)
	except Exception as e:
		print (e)
		continue
