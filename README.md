
# 📺 YouTube Transcript Summarizer using Gemini & Streamlit

A Generative AI-powered web application that extracts transcripts from YouTube videos and generates **concise, bullet-point summaries** using **Google Gemini Pro**. Built with **Streamlit** for a clean and interactive UI.

---

## 🚀 Features

- 🔗 Accepts any YouTube video link
- 📝 Automatically extracts video transcript
- 🤖 Uses **Google Gemini Pro** for AI-based summarization
- 📌 Generates clear, structured bullet-point notes
- ⚡ Fast, lightweight, and easy to use
- 🔐 Secure API key handling via `.env`

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Google Gemini Pro (Generative AI)**
- **YouTube Transcript API**
- **dotenv**

---

## 📂 Project Structure

```

├── app.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt

````

---

## 🔑 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/rameezuetian/Youtube-Transcript-Summarize-GEN-APP.git
cd Youtube-Transcript-Summarize-GEN-APP
````

---

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate     # Linux / macOS
venv\Scripts\activate        # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_google_gemini_api_key
```

⚠️ **Never upload your API key to GitHub**

---

### 5️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🎯 How It Works

1. User enters a YouTube video URL
2. App extracts the video transcript
3. Transcript is sent to **Gemini Pro**
4. AI generates a summarized version (≤ 250 words)
5. Output is displayed as structured notes

---

## 📌 Example Use Cases

* 🎓 Study notes from lectures
* 📚 Summarize tutorials & talks
* 🎙️ Podcast key takeaways
* 🧠 Quick revision content

---

## ⚠️ Limitations

* Video must have **captions enabled**
* Private or restricted videos may not work
* Very long transcripts may take extra time

---

## 🌟 Future Improvements

* PDF / Markdown export
* Timestamp-based summaries
* Language translation
* Streamlit Cloud deployment
* Topic-wise breakdown

---

## 👨‍💻 Author

**Muhammad Rameez**
🎓 Computer Science | AI / ML | Data Science
🔗 GitHub: [https://github.com/rameezuetian](https://github.com/rameezuetian)

---
