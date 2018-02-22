from lxml import html
import requests
import os

objectList=[]
hashTable={}

debug=True


def getInfo( mn ):
	movieName=mn.lower()
	movieName=' '.join(movieName.split())
	movieName='+'.join(movieName.split())
	start_page1= requests.get("http://www.imdb.com/find?ref_=nv_sr_fn&q="+movieName+"&s=all")
	tree1=html.fromstring(start_page1.text)

	links=tree1.xpath('//td[@class="result_text"]/a/@href')[0]
	scrapedMovieName=tree1.xpath('//td[@class="result_text"]/a/text()')[0]
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
	else:
		imdb=imdbL[0]
	
	#gener
	genre=tree2.xpath('//div[@itemprop="genre"]/a/text()')	
	Genre=""
	for g in genre:
		Genre+=(g+" ")
	Genre=Genre[1:]
	Genre=Genre	
	
	#duration
	timeL=tree2.xpath('//div[@class="subtext"]/time[@itemprop="duration"]/text()')
	if len(timeL)==0:
		time="Duration of movie is not available"
	else:
		time=timeL[0]
	''.join(time.split())
	time=time[25:]
	time=time
	bsn=time.find('\n')
	duration=time[:bsn]

	#release date
	dateL=tree2.xpath('//div[@class="subtext"]/a[@title="See more release dates"]/text()')
	if len(dateL)==0:
		date="Release date is currently not available"
	else:
		date=dateL[0]
	''.join(date.split())	
	dsn=date.find('(')
	releaseDate=date[:dsn]

	#directorName
	directorName=tree2.xpath('//div[@class="credit_summary_item"]/span[@itemprop="director"]/a[@itemprop="url"]/span[@itemprop="name"]/text()')[0]

	#directorId
	directorId=tree2.xpath('//div[@class="credit_summary_item"]/span[@itemprop="director"]/a[@itemprop="url"]/@href')[0]

	#writerName
	writerName=tree2.xpath('//div[@class="credit_summary_item"]/span[@itemprop="creator"]/a[@itemprop="url"]/span[@itemprop="name"]/text()')[0]

	#writerId
	writerId=tree2.xpath('//div[@class="credit_summary_item"]/span[@itemprop="creator"]/a[@itemprop="url"]/@href')[0]

	#top3ActorsNames
	actorsNamesList=tree2.xpath('//div[@class="credit_summary_item"]/span[@itemprop="actors"]/a[@itemprop="url"]/span[@itemprop="name"]/text()')
	if(len(actorsNamesList)>3):
		actorsNamesList=actorsNamesList[:3]

	#top3ActorsId
	actorsIdList=tree2.xpath('//div[@class="credit_summary_item"]/span[@itemprop="actors"]/a[@itemprop="url"]/@href')
	if(len(actorsIdList)>3):
		actorsIdList=actorsIdList[:3]

	#budget
	budgetNGross=tree2.xpath('//div[@id="titleDetails"]/div[@class="txt-block"]/text()');
	budget=(budgetNGross[26].strip('\n')).strip()

	#openingWeekGross
	openingWeekGross=((budgetNGross[29].strip('\n')).strip())[:-1]	

	#producerName
	producerName=tree2.xpath('//div[@id="titleDetails"]/div[@class="txt-block"]/span[@itemprop="creator"]/a[@itemprop="url"]/span[@itemprop="name"]/text()')[0];

	#producerId
	producerId=tree2.xpath('//div[@id="titleDetails"]/div[@class="txt-block"]/span[@itemprop="creator"]/a[@itemprop="url"]/@href')[0];	


	#certification
	certification=tree2.xpath('//div[@class="txt-block"]/span[@itemprop="contentRating"]/text()')[0]

	'''
	urlForRatings="http://www.imdb.com/title/"+movieId+"/ratings?ref_=tt_ql_op_4"
	print(urlForRatings)
	start_page3=requests.get(urlForRatings)
	tree3=html.fromstring(start_page3.text)
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
	

movieList=["the hangover","deadpool","black panther","avengers"]


for m in movieList:
	if m is not None:
		getInfo(m)
	else:
		print('Movie with name '+copy+' Change the name of the file and try again.')
