import praw
import time
import re
import configparser

keyword = 'apples' #keyword you want to match on		 
keyword2 = 'applies'

config = configparser.ConfigParser()
config._interpolation = configparser.ExtendedInterpolation()
config.read('config.ini')

bot = praw.Reddit(user_agent=config.get('applesSection', 'user_agent'),
	              client_id=config.get('applesSection', 'client_id'),
	              client_secret=config.get('applesSection', 'client_secret'),
	              username=config.get('applesSection', 'username'),
	              password=config.get('applesSection', 'password'))
                  
subreddit= bot.subreddit('All') #decide which subs you want to scan for
comments = subreddit.stream.comments() 

for comment in comments:
	text = comment.body #text of the comment you matched on
	author = comment.author #comment author, good if you want to tag the other person
	

	if keyword in text.lower() and author != 'ApplesBot' and author != 'AutoModerator' and author != 'GoodBot_BadBot': #put username here so you dont match on yourself
		message = ''.join(("Hello everyone, my name is the ApplesBot. \n   ",
					"u/{0}".format(author)," you typed ", keyword,
					" but did you mean applies? \n   ", 
					"It has an I in it." 
		))
		try:
			comment.reply(message) #sends the message
		except praw.exceptions.APIException as e:
			if e.error_type == 'RATELIMIT':
				print('nap time boss')
				time.sleep(60)
		except Exception as e:
			print(e)
		print(message) #prints to console for fun

	if keyword2 in text.lower() and author != 'ApplesBot' and author != 'AutoModerator': #put username here so you dont match on yourself
		message = ''.join(("Hello everyone, my name is the ApplesBot.   \n   ",
					"u/{0}".format(author)," you typed ", keyword2,
					" but did you mean apples?   \n   ",
					"It doesn't have an I in it" 
		))
		try:
			comment.reply(message) #sends the message
		except praw.exceptions.APIException as e:
			if e.error_type == 'RATELIMIT':
				print('nap time boss')
				time.sleep(60)
		except Exception as e:
			print(e) 
		print(message) #prints to console for fun