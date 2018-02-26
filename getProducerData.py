from lxml import html
import requests
import os
import GenericDAL
import yaml
import csv

config=open('Config.yaml')
conf=yaml.load(config)


query="select * from %s "%(conf['ProducerTable'])
producerList=GenericDAL.QueryResult(query,conf)

for producer in producerList:
	producerId=producer[0]
	query="select imdb from %s where producerid = '%s' "%(conf['MovieTable'],producerId)
	try:
		imdbs=GenericDAL.QueryResult(query,conf)
	except:
		continue
	total=0.0
	count=0
	score=0
	for imdb in imdbs:
		total+=float(imdb[0])
		count+=1
	if count!=0:
		score="%.4f" % (total/count)
	try:
		query="update %s set score= %s where id= '%s'"%(conf['ProducerTable'],score,producerId)
		GenericDAL.ExecuteQuery(query,conf)
	except:
		continue
