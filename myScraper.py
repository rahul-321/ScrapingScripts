from lxml import html
import requests
import os
import GenericDAL
import yaml
import csv

config=open('Config.yaml')
conf=yaml.load(config)

debug=False


def getInfo( mn ):
	movieName=mn.lower()
	movieName=' '.join(movieName.split())
	movieName='+'.join(movieName.split())
	start_page1= requests.get("http://www.imdb.com/find?ref_=nv_sr_fn&q="+movieName+"&s=all")
	tree1=html.fromstring(start_page1.text)

	try:
		links=tree1.xpath('//td[@class="result_text"]/a/@href')[0]
		scrapedMovieName=tree1.xpath('//td[@class="result_text"]/a/text()')[0]
	except Exception as e:
		return

	baseUrl="http://www.imdb.com"
	finalUrl=baseUrl+str(links)

	if debug:
		print(finalUrl)
	

	start_page2=requests.get(finalUrl)
	tree2=html.fromstring(start_page2.text)
	imdbL=tree2.xpath('//span[@itemprop="ratingValue"]/text()')

	#movieId
	movieId=links[7:16]


	# imdb ratings
	if len(imdbL)==0:
		imdb="Imdb is not available"
		return
	else:
		imdb=str(imdbL[0])
	
	#gener
	try:
		genre=tree2.xpath('//div[@itemprop="genre"]/a/text()')	
		Genre=""
		for g in genre:
			Genre+=(g+" ")
		Genre=str(Genre[1:])
	except Exception as e:
		return	
	
	#duration
	try:
		timeL=tree2.xpath('//div[@class="subtext"]/time[@itemprop="duration"]/text()')
		if len(timeL)==0:
			time="Duration of movie is not available"
			return
		else:
			time=timeL[0]
		''.join(time.split())
		time=time[25:]
		time=time
		bsn=time.find('\n')
		duration=str(time[:bsn])
	except Exception as e:
		return

	#release date
	try:
		dateL=tree2.xpath('//div[@class="subtext"]/a[@title="See more release dates"]/text()')
		if len(dateL)==0:
			date="Release date is currently not available"
			return
		else:
			date=dateL[0]
		''.join(date.split())	
		dsn=date.find('(')
		releaseDate=date[:dsn]
	except Exception as e:
		return
	
	'''
	releaseDate=releaseDate.strip()
	if int(releaseDate[:-4])<2007:
		return
	'''

	#directorName
	try:
		directorName=str(tree2.xpath('//div[@class="credit_summary_item"]/span[@itemprop="director"]/a[@itemprop="url"]/span[@itemprop="name"]/text()')[0])
	except Exception as e:
		print(e," director")
		return


	#directorId
	try:
		directorId=str(tree2.xpath('//div[@class="credit_summary_item"]/span[@itemprop="director"]/a[@itemprop="url"]/@href')[0])
	except Exception as e:
		print(e," did")
		return



	#writerName
	try:
		writerName=str(tree2.xpath('//div[@class="credit_summary_item"]/span[@itemprop="creator"]/a[@itemprop="url"]/span[@itemprop="name"]/text()')[0])
	except Exception as e:
		print(e, "writerName")
		return

	#writerId
	try:
		writerId=str(tree2.xpath('//div[@class="credit_summary_item"]/span[@itemprop="creator"]/a[@itemprop="url"]/@href')[0])
	except Exception as e:
		print(e, " writerId")
		return


	#top3ActorsNames
	try:
		actorsNamesList=tree2.xpath('//div[@class="credit_summary_item"]/span[@itemprop="actors"]/a[@itemprop="url"]/span[@itemprop="name"]/text()')
		if(len(actorsNamesList)>3):
			actorsNamesList=actorsNamesList[:3]
	except Exception as e:
		print(e)
		return



	#top3ActorsId
	try:
		actorsIdList=tree2.xpath('//div[@class="credit_summary_item"]/span[@itemprop="actors"]/a[@itemprop="url"]/@href')
		if(len(actorsIdList)>3):
			actorsIdList=actorsIdList[:3]
	except Exception as e:
		print(e)
		return


	#budget
	try:
		budgetNGross=tree2.xpath('//div[@id="titleDetails"]/div[@class="txt-block"]/text()');
		budgetNGross=[s for s in budgetNGross if "$" in s]
		budget=str((budgetNGross[0].strip('\n')).strip())
	except Exception as e:
		print(e)
		return


	#openingWeekGross
	try:
		openingWeekGross=str(((budgetNGross[1].strip('\n')).strip())[:-1])	
	except Exception as e:
		print(e)
		return


	#producerName
	try:
		producerName=str(tree2.xpath('//div[@id="titleDetails"]/div[@class="txt-block"]/span[@itemprop="creator"]/a[@itemprop="url"]/span[@itemprop="name"]/text()')[0]);
	except Exception as e:
		print(e)
		return


	#producerId
	try:
		producerId=str(tree2.xpath('//div[@id="titleDetails"]/div[@class="txt-block"]/span[@itemprop="creator"]/a[@itemprop="url"]/@href')[0]);	
	except Exception as e:
		print(e)
		return


	#certification
	try:
		certification=str(tree2.xpath('//div[@class="txt-block"]/span[@itemprop="contentRating"]/text()')[0])
	except Exception as e:
		print(e)
		return

	'''
	urlForRatings="http://www.imdb.com/title/"+movieId+"/ratings?ref_=tt_ql_op_4"
	print(urlForRatings)
	start_page3=requests.get(urlForRatings)
	tree3=html.fromstring(start_page3.text)
	'''
	'''
	print(movieId)
	print(mn,imdb,Genre,releaseDate,duration)
	print(directorName,directorId)
	print(writerName,writerId)
	print(actorsNamesList,actorsIdList)
	print(budget)
	print(openingWeekGross)
	print(producerName)
	print(producerId)
	print(certification)
	'''

	#query="insert into table Movie values()"
	try:
		query="insert into  %s (id,name,releasedate,duration,directorid,producerid,writerid,imdb,budget,collection,certification) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(conf['MovieTable'],movieId,mn,releaseDate,duration,directorId,producerId,writerId,imdb,budget,openingWeekGross,certification)
		print(query)
		GenericDAL.ExecuteQuery(query,conf)
		query="insert into  %s (id,name) values('%s','%s')"%(conf['DirectorTable'],directorId,directorName)
		GenericDAL.ExecuteQuery(query,conf)
		query="insert into  %s (id,name) values('%s','%s')"%(conf['ProducerTable'],producerId,producerName)
		GenericDAL.ExecuteQuery(query,conf)
		query="insert into  %s (id,name) values('%s','%s')"%(conf['WriterTable'],writerId,writerName)
		GenericDAL.ExecuteQuery(query,conf)
		for i in range(0,len(actorsIdList)):
			query="insert into %s (movieid,actorid,rank) values('%s','%s','%s')"%(conf['MoviesActorTable'],movieId,actorsIdList[i],str(i+1))
			GenericDAL.ExecuteQuery(query,conf)
			query="insert into  %s (id,name) values('%s','%s')"%(conf['ActorTable'],actorsIdList[i],actorsNamesList[i])
			GenericDAL.ExecuteQuery(query,conf)
	except Exception as e:
		pass
		#print(e)





movieList=["logan","beauty and the beast","star wars episode eight","the hangover","deadpool","avengers"]


sagat = ['goodMovies20173.csv']
for sagatList in sagat:
	with open(sagatList, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for movie in reader:
			try:
				# fix up movie names
				movieName = movie[0]
				paren = str.rfind(movie[0], " (")
				if paren > 0:
					movieName = movieName[0:paren]
				print ("Processing movie: " + movieName)
				#for m in movieList:
				try:
					getInfo(movieName)
				except Exception as e:
					continue
			except Exception as e:
				continue

debug= False
if debug:
	try:
		for m in movieList:
			getInfo(m)
	except Exception as e:
		print(e)


