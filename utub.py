from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
client = MongoClient('mongodb://test:test@localhost',27017)
db = client.dbsparta

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

import datetime, time
import schedule

def job():
    DEVELOPER_KEY = "AIzaSyAmmHbqw6Dz1JH_qNs5IzTLy4gt7O7HAEo"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"  
    youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(q = "미국주식", order = "date", part = "snippet", maxResults = 10).execute()
    videos = []
    channels = []
    playlists = []
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s $(%s)" % (search_result["snippet"]["title"],search_result["id"]["videoId"]))
            doc = {
                            'VIDEOID' : search_result["id"]["videoId"],
                            'TITLE' : search_result["snippet"]["title"],
                            'URL' : search_result["snippet"]["thumbnails"]["medium"]["url"]
                         }
            

        elif search_result["id"]["kind"] == "youtube#channel":
            channels.append("%s (%s)" %(search_result["snippet"]["title"], search_result["id"]["channelID"]))
        
        elif search_result["id"]["kind"] == "youtube#playlist":
            playlists.append("%s (%s)" %(search_result["snippet"]["title"], search_result["id"]["playlistID"]))
        db.videoList.insert_one(doc)      
        print(doc)

def run():
    # schedule.every().day.at('09:00').do(job)
    schedule.every(10).seconds.do(job)
    while True:
        schedule.run_pending()

if __name__ == "__main__":
    run()

