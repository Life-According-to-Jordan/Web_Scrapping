console.log('the bot is starting');

var Twit = require('twit');

//config is in a seperate javascript file and loads in or Twitter App
//security information and log in
var config = require('./config');

//make a new tweet from our log in information
var T = new Twit(config);
//filters tweets that contain '#cat'
var stream = T.stream('statuses/filter', { track: '#travel', language: 'en' })

stream.on('tweet', function (tweet) {
  console.log(tweet)
})
