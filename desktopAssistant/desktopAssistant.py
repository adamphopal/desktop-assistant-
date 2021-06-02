#from __future__ import unicode_literals
from gtts import gTTS
#import youtube_dl as dl
#import validators as valid
import speech_recognition as sr
import os
from downloader import *
import wikipedia
import datetime
import wolframalpha
import re
import webbrowser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.message import EmailMessage
import requests
from requests_html import HTML, HTMLSession
import csv
import requests
from bs4 import BeautifulSoup
import urllib.request
#from ebay_scraper import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
import threading
import math
import pyttsx3
import matplotlib.pyplot as plt
import itertools
import logging
import uuid
import numpy as np
from urllib.request import urlopen, Request
from image_downloader import *
#import youtube_dl
from sys import argv
from PrNdOwN import *
import imghdr
import numpy as np
from textblob import TextBlob 
import sys, tweepy
import matplotlib.pyplot as plt
import tweepy

import face_recognition
import numpy as np
from time import sleep
from PIL import Image, ImageDraw
from face_rec import *
import io

import time
from random import randint
import instagram_scraper as insta
#from instabot import Bot, utils
import json
from bs4 import BeautifulSoup
import webbrowser as wb


engine = pyttsx3.init('dummy')

#api wolframalpha used to qury random stuff, kinda like google home
#my app id from http://developer.wolframalpha.com/portal/myapps/index.html
client = wolframalpha.Client('')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def talkToMe(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()
    for line in audio.splitlines():
        os.system("say " + audio)

        #text_to_speech = gTTS(text=audio, lang='en')
        #text_to_speech.save('audio.mp3')
        #os.system('mpg123 audio.mp3')

talkToMe('When I start listening, speak to me with a query, or type it manually in terminal')
print(">>> Menu")
print(">>> 1 - translate arabic: translates arabic text into english")
print(">>> 2 - sentiment: The Tweepy module is used to stream live tweets directly from Twitter in real-time.The tweets are visualized and then the TextBlob module is used to do sentiment analysis on the tweets")
print(">>> 3 - scrape twitter csv: scrape twitter tweets, with username, and follower count, and save it in a csv file")
print(">>> 4 - scrape github: scrapes and saves the newest github python project name, description, and code link into a csv file named python_github.csv'")
print(">>> 5 - image: Enter a search term to google and then downloads specific number of a searched image into a specific folder")
print(">>> 6 - face: Face rec program that takes a jpg pic of a person or people, and outputs the same pic with labeled names on it, with a txt file containing all the names")
print(">>> 7 - insta scraper: Downloads a users instagram pics")
print(">>> 8 - youtube link: Downloads youtube video/song links into mp3 songs into a folder called songs, by typing (youtube songs.txt) at the query")
print(">>> 9 - joke: tells you a joke")
print(">>> 10 - open gmail: logs into your gmail automatically")
print(">>> 11 - send github csv email: sends github csv file that you scraped from scrape github query")
print(">>> 12 - send twitter email: send twitter csv")
print(">>> 13 - bye: will exit the program")
print()


def myCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listeing...')
        r.pause_threshold = 1
 #       r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('You said: ' + query + '\n')

    #loop back to continue to listen for querys if unrecognizable speech is received
    except sr.UnknownValueError:
        talkToMe('Your last query couldn\'t be heard')
        query = str(input('Command: '))

    return query

if __name__ == '__main__':
    def desktopAssistant(query):
        while True:
            query = myCommand();
            query = query.lower()

            if 'sentiment' in query:
                talkToMe('Twitter sentiment Analysis using Python')
                def percentange(part,whole):
                    return 100* float(part)/float(whole)

                consumer_key = ''
                consumer_secret = ''
                accessToken = ''
                accessTokenSecret = ''

                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(accessToken, accessTokenSecret)
                api = tweepy.API(auth)

                searchTerm = input("Enter keyword/hashtag to search about:")
                noOfSearchTerms = int(input("Enter number of tweet to analyze:"))

                tweets = tweepy.Cursor(api.search, q = searchTerm,lang = "en" ).items(noOfSearchTerms)

                positive = 0
                negative = 0
                neutral= 0
                polarity = 0
                total = 0

                for tweet in tweets:
                    print(tweet.text)
                    analysis = TextBlob(tweet.text)
                    polarity += analysis.sentiment.polarity
                    print(analysis.sentiment.polarity)
                    total += 1
                    if(analysis.sentiment.polarity == 0):
                        neutral += 1
                        #print("neutral increased " + str(neutral))
                        
                    elif(analysis.sentiment.polarity < 0.00):
                        negative += 1
                        #print("negative increased " + str(negative))
                        
                    elif(analysis.sentiment.polarity > 0.00):
                        positive += 1   
                        #print("positive increased " + str(positive))
                    
                #print("positive "+str(positive))
                #print("negative "+str(negative))
                #print("neutral "+str(neutral))

                positive = percentange(positive , total)
                negative = percentange(negative , total)
                neutral = percentange(neutral , total)

                positive = format(positive , '.2f' )
                negative = format(negative , '.2f' )
                neutral = format(neutral , '.2f' )

                #print("positive %"+str(positive))
                #print("negative %"+str(negative))
                #print("neutral %"+str(neutral))

                print("How are people reacting on #" + searchTerm + "by analyzing " + str(noOfSearchTerms)+ ' Tweets.')

                if(polarity == 0):
                    print("neutral")    
                elif(polarity > 0):
                    print("positive")
                elif(polarity < 0):
                    print("negative")
                    
                labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(negative) + '%]']
                sizes = [positive,neutral, negative ]
                colors = ['yellowgreen',  'gold','red']
                patches, texts = plt.pie(sizes, colors=colors, startangle=90)
                plt.legend(patches, labels, loc="best")
                plt.title('How people are reacting on #' + searchTerm + ' by analyzing ' + str(noOfSearchTerms) + ' Tweets.')
                plt.axis('equal')
                plt.tight_layout()
                plt.show()
          


            elif 'open hamims website' in query:
                talkToMe('opening your python code board website for you')
                driver = webdriver.Chrome('')
                url = ''
                driver.get(url)

            


            elif 'bye' in query:
                talkToMe('Bye Hamim, have a good day.')
                sys.exit()

            elif 'youtube link' in query:
                talkToMe('Downloads youtube video/song links into mp3 songs into a folder called songs')
                youtube_link = input("Enter song link to add to songs.txt: ")
                f = open('/Users/samehphopal/desktopAssistant/songs.txt', 'a')
                f.write("\n"+youtube_link)
                f.close()
                yt()
                             

            elif 'open gmail' in query:
                talkToMe('logging into gmail for you')
                usernameStr = ''
                passwordStr = getpass("Enter password: ")

                driver = webdriver.Chrome('')
                driver.get(('https://accounts.google.com/ServiceLogin?'
                         'service=mail&continue=https://mail.google'
                         '.com/mail/#identifier'))

        # fill in username and hit the next button
                username = driver.find_element_by_id('identifierId')
                username.send_keys(usernameStr)

                nextButton = driver.find_element_by_id('identifierNext')
                nextButton.click()
        # wait for transition then continue to fill items
                password = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "password")))

                password.send_keys(passwordStr)

                signInButton = driver.find_element_by_id('passwordNext')
                signInButton.click()
                print("successfully logged into gmail!")


            elif 'translate arabic' in query:
                talkToMe('translates arabic text into english')
                API_KEY = ''
                url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
                words = input("Enter arabic text to translate into english:" )

                params = dict(key=API_KEY, text=words, lang='ar-en') #translates text from arabic to englist
                r = requests.get(url, params=params)
                json = r.json()
                print(json['text'][0])
                
                

            elif 'scrape twitter csv' in query:
                    talkToMe('scrape twitter tweets, with username, and follower count, and save it in a csv file')
                    consumer_key = ''
                    consumer_secret = ''
                    access_token = ''
                    access_token_secret = ''

                    hashtag_phrase = input("Enter Hashtag Phrase to scrape its hashtags, timestamps, tweet-text, username, and follower count from twitter: ")

                    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #create authentication for accessing Twitter
                    auth.set_access_token(access_token, access_token_secret)

                    #initialize Tweepy API
                    api = tweepy.API(auth)
                    #get the name of the spreadsheet we will write to
                    fname = input("Enter name to give to twitter csv file to save data in: ")

                    csv_file = open(fname, 'w')
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(['timestamp', 'tweet_text', 'username', 'all_hashtags', 'followers_count'])

                    for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', \
                                                   lang="en", tweet_mode='extended').items(100):
                        csv_writer.writerow([tweet.created_at, tweet.full_text.replace('\n',' ').encode('utf-8'),
                        tweet.user.screen_name.encode('utf-8'), [e['text'] for e in tweet._json['entities']['hashtags']],
                        tweet.user.followers_count])

                    csv_file.close()
     

            elif 'send twitter email' in query:
                talkToMe('Sending email for you') 
                email_user = '' #input("what is your gmail address? \n ")
                email_password = getpass("what is the password for that email address? \n  ")
                email_send  = input("Who would you like to send this email too? \n ")

                subject = 'Python daily Twitter-Data'

                msg = MIMEMultipart()
                msg['From'] = email_user
                msg['To'] = email_send
                msg['Subject'] = subject

                body = 'Hi there, Ive added a png image which was created from a python twitter script that scrapes the 500 most recent tweets about python, and displays its sentimal analysis, based on how positive, negative, and neatral a tweet was is. My website: http://167.71.157.4/'
                msg.attach(MIMEText(body,'plain'))

                filename = input("Enter a filename, with extensions, for the twitter email your sending: ")
                attachment  =open(filename,'rb')

                part = MIMEBase('application','octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',"attachment; filename= "+filename)

                msg.attach(part)
                text = msg.as_string()
                server = smtplib.SMTP('smtp.gmail.com',587)#init gmail smtp
                server.starttls()#encrypt connection
                server.login(email_user,email_password)


                server.sendmail(email_user,email_send,text)
                server.quit() #close connection
                print("successfully sent the email message")     
                

            elif 'scrape github' in query:
                talkToMe('scraping the trending page for python project only, updated daily')
                talkToMe('saves the newest github python project name, description, and code link into a csv file named python_github.csv')
                csv_file = open('python_github.csv', 'w')
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['Name', 'Description', 'Link'])

                session = HTMLSession()
                r = session.get('https://github.com/trending/python?since=daily')

                articles = r.html.find('article')
                for article in articles:
                    headline = article.find('.text-normal', first=True).text
                    headline_u = headline.split("/")[0]
                    print("Python Github repo name: ", headline_u)

                    description = article.find('p', first=True).text 
                    print("Description: ", description)

                    try: 
                        link = article.find('a', first=True).attrs['href']
                        link_id = link.split('%2F')[1:3]
                        final_link = "/"
                        final_link = final_link.join(link_id)
                        gh_link = f'https://github.com/{final_link}'
                    except Exception as e:
                        gh_link = None

                    print("Github repo link: ", gh_link)
                    print()
                    csv_writer.writerow([headline_u, description, gh_link])

                csv_file.close()

            elif 'image' in query:
                talkToMe('Enter a search term to google and then downlaoda specific number of a searched image into a specific folder')
                search = input("Enter search term into google and download images: ")
                num = int(input("Enter number of images to downlaod: "))
                name = input("Enter dir name to store all search term from google images in: ")

                if not os.path.exists(name):
                    os.mkdir(name)
                else:
                    os.chdir(name)
        
                run(search, name, num)


            elif 'face' in query:
                talkToMe('Face rec program that takes a jpg pic of a person or people, and outputs the same pic with labeled names drawn on it, with a txt file containing all the reconized names')
                test_image = input("Enter the name of the image you would like to test for face rec: ")
                print(classify_face(test_image))
                while True:
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        return face_names

            elif 'insta scraper' in query:
                talkToMe('Downloads a users instagram pics')
                ig_users = input("Enter ig username, to add to ig_users.txt, to download images from: ")
                f = open('/desktopAssistant/ig_users.txt', 'a')
                f.write("\n"+ig_users)
                f.close()
                profiles = []
                with open("ig_users.txt") as file:
                    for l in file:
                        profiles.append(l.strip())

     #           number_of_pics = int(input("Enter the max number of isnta pics to download: "))
     #           number_last_photos = 10
                x = 0
                def InstaImageScraper():
                    number_of_pics = int(input("Enter the max number of isnta pics to download: "))
                    ''' Scrape image on profiles '''
                    imgScraper = insta.InstagramScraper(usernames=profiles,
                                                        maximum=number_of_pics,
                                                        media_metadata=True, latest=True,
                                                        media_types=['image', 'video'])
                    imgScraper.scrape()

                    print("image scraping is running, please wait 50 seconds.")


                InstaImageScraper()
                    
                
            elif 'what\'s up' in query:
                talkToMe('Just doing my thing')

            
            elif 'joke' in query:
                res = requests.get(
                        'https://icanhazdadjoke.com/',
                        headers={"Accept":"application/json"}
                        )
                if res.status_code == requests.codes.ok:
                    talkToMe(str(res.json()['joke']))
                else:
                    talkToMe('oops!I ran out of jokes')

            elif 'send github csv email' in query:
                talkToMe('sending email for you')
                email_user = '' #input("what is your gmail address? \n ")
                email_password = getpass("what is the password for that email address? \n  ")
                email_send  = input("Who would you like to send this email too? \n ")

                subject = 'Python daily CSV-Data'

                msg = MIMEMultipart()
                msg['From'] = email_user
                msg['To'] = email_send
                msg['Subject'] = subject

                body = 'Hi there,this csv file contains the updated/daily scraped python repos from github that are trending the most, containing the name, description, and code link. My website: http://167.71.157.4/'
                msg.attach(MIMEText(body,'plain'))

                filename = 'python_github.csv'
                attachment  =open(filename,'rb')

                part = MIMEBase('application','octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',"attachment; filename= "+filename)

                msg.attach(part)
                text = msg.as_string()
                server = smtplib.SMTP('smtp.gmail.com',587)#init gmail smtp
                server.starttls()#encrypt connection
                server.login(email_user,email_password)


                server.sendmail(email_user,email_send,text)
                server.quit() #close connection
                print("successfully sent the email message")



            else:
                query = query #for ex. asking the assistent a question, who is donald trump?
                talkToMe('Searching...')
                try:
                    try:
                        res = client.query(query)#takes your question
                        results = next(res.results).text#converts it to text to display on terminal
                        talkToMe('WOLFRAM-ALPHA says - ')
                        talkToMe('Got it.')
                        talkToMe(results)
                        
                    except:
                        results = wikipedia.summary(query, sentences=2)#searches your query in wiki, and gives 2 sentences of info
                        talkToMe('Got it.')
                        talkToMe('WIKIPEDIA says - ')
                        talkToMe(results)
            
                except:
                    webbrowser.open('www.google.com')

            talkToMe('Next query! Hamim!')


desktopAssistant(myCommand)
