library("rvest")
library("dplyr")

#set variable 
#read url with read_html
imdb <- read_html("http://www.imdb.com/showtimes/cinema/US/ci100180205?ref_=inth_tny_th")

#set up features of data set 
title <- imdb %>% html_nodes(".info span a") %>% html_text
time <- imdb %>% html_nodes("time") %>% html_text

#make data frame to visualize contents
mydf <- data.frame(title, time)

list(mydf)
