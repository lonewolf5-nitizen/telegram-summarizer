import os
import json
import requests
from groq import Groq
from datetime import datetime as dt, timedelta as td, timezone as z
from telethon import TelegramClient

import os

api = os.getenv("API_ID")
apih = os.getenv("API_HASH")
gapi = os.getenv("GROQ_API_KEY")
class Fetcher:
    def __init__(self, api_id, api_hash):
        self.api_id = api_id
        self.api_hash = api_hash
        self.client = TelegramClient('anon', self.api_id, self.api_hash)
        self.messages = []
        self.lk=" "

    async def fetch(self, hours=2):
        two_hrs_ago = dt.now(z.utc) - td(hours=2)
        async for dialog in self.client.iter_dialogs(limit=5):
            async for message in self.client.iter_messages(dialog.id):
                if message.date < two_hrs_ago:
                    break
                if message.text:
                    self.messages.append(f"{dialog.name}: {message.text}")
                self.lk = " ".join(self.messages)
        
            

f = Fetcher(api, apih)
with f.client:
    f.client.loop.run_until_complete(f.fetch())


class Summarizer:
    def __init__(self):
     self.summary=[]   
     self.kwords=["because", "since", "therefore", "thus", "hence", "result", "but", "however", "although", "yet","conclusion", "overall", "finally", "importantly", "significantly","is defined as", "refers to", "means","transformed", "urgent", "important", "emergency", "deadline", "asap", "immediately", "critical", "help", "exam", "tomorrow"] 
        
    
    def abstsum(self, text):
       client = Groq(api_key=gapi)
       self.response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
        {"role": "system", "content": "You are a text summarizer. Summarize the given text in  concise sentences.Address the recipient as 'you' or 'your', not as a third person.And if codes are shared ignore it"},
        {"role": "user", "content": text}
     ]
     ) 
       self.yet=self.response.choices[0].message.content
    def displat(self):
       print(self.yet)
    
    def noti(self):
        requests.post("https://ntfy.sh/summary",data=self.yet.encode('utf-8'))
    def save(self):
        time=dt.now().strftime("%Y-%m-%d %H:%M:%S")
        data={
             "timestamp": time,
             "summary": self.yet
          }
        print(f"{data['timestamp']}\n{data['summary']}")
w=Summarizer()
w.abstsum(f.lk)
w.displat()
w.noti()
