api=34732992
apih='e90a20bbc71e4ed820c0e2ac61342478'
gapi="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"


import json
import requests
import re
from groq import Groq
import win32com.client as wincl
al = ["urgent", "important", "emergency", "deadline", "asap", "immediately", "critical", "help", "exam", "tomorrow"]
from datetime import datetime as dt, timedelta as td, timezone as z
from telethon import TelegramClient


class Fetcher:
    def __init__(self, api_id, api_hash):
        self.api_id = api_id
        self.api_hash = api_hash
        self.client = TelegramClient('anon', self.api_id, self.api_hash)
        self.messages = []
        self.lk=" "

    async def fetch(self, hours=24):
        two_hrs_ago = dt.now(z.utc) - td(hours=24)
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
    def input_(self):
     self.text = f.lk
        
    def summarye(self):
        text2=self.text.lower()
        sen= re.split(r'[.!?]\s+', self.text)
        sen2=re.split(r'[.!?]\s+', text2)
        for i in range(len(sen2)):
         x = sen2[i] 
         y = sen[i] 
         z=x.split()
         for u in z:
             if u in self.kwords:
                 if y not in self.summary:
                      self.summary.append(y)
    def abstsum(self):
       client = Groq(api_key=gapi)
       self.response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
        {"role": "system", "content": "You are a text summarizer. Summarize the given text in  concise sentences.Address the recipient as 'you' or 'your', not as a third person.And if codes are shared ignore it"},
        {"role": "user", "content": self.text}
     ]
     ) 
       self.yet=self.response.choices[0].message.content
    def displat(self):
       print(self.yet)
    def display(self):
      print("Summary :")
      for i in self.summary:
          print("*", end=" ")
          print(i)
    def alert(self):
       speaker = wincl.Dispatch("SAPI.SpVoice")
       voices= speaker.GetVoices()
       speaker.Voice= voices.Item(1)
       speaker.Rate = 3
       speaker.Volume = 100
       speaker.Speak("ALERT U HAVE AN EMERGENCY")
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
w.input_()
w.abstsum()
w.displat()
w.noti()
w.save()