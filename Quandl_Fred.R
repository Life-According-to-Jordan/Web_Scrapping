print('Quandl Scraper - Fred/GPA')
library(Quandl)

#quandl user api granted upon enrolling as a user
#quandl web scraping is extremelly easy since they have the data neatly organized
mydata = Quandl("FRED/GDP", start_date="2000-12-31", end_date="2018-12-31", collapse="annual", rows=4)

#data returned as data.frame
class(mydata)

mydata

print('it worked, thank you for running my code!')
