import os
import GenericDAL
import yaml


config=open('Config.yaml')
conf=yaml.load(config)


query="select * from Movie"
movies=GenericDAL.QueryResult(query,conf)


for movie in movies:
	id=movie[0]
	directorid=movie[4]
	producerid=movie[5]
	writerid=movie[6]

	try:
		query="insert into  %s (id) values('%s')"%(conf['DirectorTable'],directorid)
		GenericDAL.ExecuteQuery(query,conf)
	except Exception as e:
		print(query)
		print(e)

	try:
		query="insert into  %s (id) values('%s')"%(conf['ProducerTable'],producerid)
		GenericDAL.ExecuteQuery(query,conf)
	except Exception as e:
		print(e)	

	try:
		query="insert into  %s (id) values('%s')"%(conf['WriterTable'],writerid)
		GenericDAL.ExecuteQuery(query,conf)
	except Exception as e:
		print(e)