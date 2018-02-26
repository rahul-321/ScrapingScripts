import csv
import requests
from lxml import html


urls=[
"http://www.imdb.com/search/title?year=2007,2007&title_type=feature&sort=boxoffice_gross_us,desc&page=2&ref_=adv_nxt",
"http://www.imdb.com/search/title?year=2007,2007&title_type=feature&sort=boxoffice_gross_us,desc&page=1&ref_=adv_prv",
"http://www.imdb.com/search/title?year=2006,2006&title_type=feature&sort=boxoffice_gross_us,desc&page=1&ref_=adv_prv",
"http://www.imdb.com/search/title?year=2006,2006&title_type=feature&sort=boxoffice_gross_us,desc&page=2&ref_=adv_nxt",
"http://www.imdb.com/search/title?year=2005,2005&title_type=feature&sort=boxoffice_gross_us,desc&page=1&ref_=adv_prv",
"http://www.imdb.com/search/title?year=2005,2005&title_type=feature&sort=boxoffice_gross_us,desc&page=2&ref_=adv_nxt",
"http://www.imdb.com/search/title?year=2004,2004&title_type=feature&sort=boxoffice_gross_us,desc&page=1&ref_=adv_prv",
"http://www.imdb.com/search/title?year=2004,2004&title_type=feature&sort=boxoffice_gross_us,desc&page=2&ref_=adv_nxt"]
with open('goodMovies20173.csv', 'a+') as csvfile:
	fieldnames = ['movie']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	#writer.writeheader()
	for url in urls: 
		try:
			start_page1= requests.get(url)
			tree1=html.fromstring(start_page1.text)
			movieList=tree1.xpath('//h3[@class="lister-item-header"]/a/text()')
			print(movieList)
			for movieName in movieList:
				writer.writerow({'movie': movieName})
		except:
			continue

'''
http://www.imdb.com/search/title?year=2015,2015&title_type=feature&sort=boxoffice_gross_us,desc&page=1&ref_=adv_prv	
http://www.imdb.com/search/title?year=2015,2015&title_type=feature&sort=boxoffice_gross_us,desc&page=2&ref_=adv_nxt
http://www.imdb.com/search/title?year=2014,2014&title_type=feature&sort=boxoffice_gross_us,desc&page=1&ref_=adv_prv
http://www.imdb.com/search/title?year=2014,2014&title_type=feature&sort=boxoffice_gross_us,desc&page=2&ref_=adv_nxt
http://www.imdb.com/search/title?year=2013,2013&title_type=feature&sort=boxoffice_gross_us,desc&page=1&ref_=adv_prv
http://www.imdb.com/search/title?year=2013,2013&title_type=feature&sort=boxoffice_gross_us,desc&page=2&ref_=adv_nxt
http://www.imdb.com/search/title?year=2012,2012&title_type=feature&sort=boxoffice_gross_us,desc&page=2&ref_=adv_nxt
http://www.imdb.com/search/title?year=2012,2012&title_type=feature&sort=boxoffice_gross_us,desc&page=1&ref_=adv_prv
http://www.imdb.com/search/title?year=2012,2012&title_type=feature&sort=boxoffice_gross_us,desc&page=1&ref_=adv_prv
"http://www.imdb.com/search/title?year=2012,2012&title_type=feature&sort=boxoffice_gross_us,desc&page=1&ref_=adv_prv",
"http://www.imdb.com/search/title?year=2012,2012&title_type=feature&sort=boxoffice_gross_us,desc&page=2&ref_=adv_nxt",

'''	