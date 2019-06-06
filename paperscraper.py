# This is an online newspaper scraper that grabs articles en masse from whichever website it is pointed toward.
# Written by Colin Rose (crose@brocku.ca) with help from John Simpson (john.simpson@computecanada.ca) and Jessica Otis
# Written June 4 2019 at DHSI in Victoria, BC
# Written in python 3.6.X using Sublime Text

# Method: GODS

# 1. Get some data
import newspaper
paper_url = "https://www.thestar.com" #insert URL of desired newspaper
# print(paper_url)

# paper = newspaper.build(paper_url, memoize_articles=False) #this prevents python from caching searched results and retrieving entire corpus on every run
# above function is best used for initial scrape of article cache
paper = newspaper.build(paper_url) #use this one if you are doing repeat scraping
print(len(paper.articles)) #will show you number of available articles

# 2. Observe it

# myOutputFile = open("TorStarTitles.csv", "w") #this command rewrites entire file on every instance (w=write)
myOutputFile = open("TorStarTitles.csv", "a") #this command appends new entries to end of existing file (a=append)

for article in paper.articles:
	article.download()
	article.parse()
	#print(article.title)
	myOutputFile.write('"' + article.title + '",' + article.url + "\n")
	#break 

myOutputFile.close()	

# 3. Do something with it

# 4. Save it
