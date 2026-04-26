# Telegram Message Summarizer (Auto + Cloud)

A Python-based system that automatically reads your recent Telegram messages, summarizes them using AI, and sends the summary to your phone via notifications — without needing your laptop to stay on.

---

## 🚀 Features

* 📥 Fetches recent Telegram messages using Telethon
* 🧠 Summarizes messages using Groq (LLaMA model)
* 📲 Sends summaries to your phone via ntfy
* ☁️ Runs automatically on GitHub Actions (cloud)
* 🔁 Fully automated — no manual execution required

---

## 🧠 How It Works

1. Fetch recent messages from Telegram
2. Combine them into a single text block
3. Send text to AI model for summarization
4. Push summary to your phone using ntfy
5. Runs periodically using GitHub Actions

---

## 🛠️ Tech Stack

* Python
* Telethon (Telegram API)
* Groq API (AI summarization)
* ntfy (notifications)
* GitHub Actions (automation)

---

## ⚙️ Setup

### 1. Clone the repo

```
git clone <your-repo-link>
cd <repo-name>
```

---

### 2. Install dependencies

```
pip install -r rec.txt
```

---

### 3. Add environment variables

Set these:

* `API_ID` → Telegram API ID
* `API_HASH` → Telegram API Hash
* `GROQ_API_KEY` → Groq API key

---

### 4. Login once (IMPORTANT)

Run locally:

```
python summarizer.py
```

* Enter phone number
* Enter OTP
* This creates a file:

```
anon.session
```

Upload this file to your repo.

---

### 5. GitHub Setup

Go to:

```
Settings → Secrets → Actions
```

Add:

* `API_ID`
* `API_HASH`
* `GROQ_API_KEY`

---

### 6. Automation

GitHub Actions runs the script automatically using a cron schedule.

---

## 📲 Notifications

Install **ntfy app** on your phone and subscribe to:

```
summary
```

You will receive summaries there.

---

## ⚠️ Limitations

* GitHub cron timing is not exact
* Session file is required for Telegram login
* Designed for personal use (not multi-user yet)

---

## 🧠 Future Improvements

* Multi-user support
* Chat filtering / priority detection
* Better summarization logic
* Custom notification topics

---

## 📌 Author

Built by a student experimenting with automation, AI, and real-world systems.

---

## 💀 Note

This project may look simple, but it involves:

* async programming
* cloud automation
* API integration
* session handling

So if it breaks… welcome to real engineering.
