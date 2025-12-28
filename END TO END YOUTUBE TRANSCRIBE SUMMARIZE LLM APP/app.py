import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables


# Configure Gemini API
genai.configure(api_key="")

# Prompt
prompt = """
You are a YouTube video summarizer.
Given the full transcript of a video, generate a clear and concise summary
in bullet points. Highlight the most important concepts, key takeaways,
and conclusions. The summary should be within 250 words.

Transcript:
"""

def extract_video_id(youtube_url):
    if "watch?v=" in youtube_url:
        return youtube_url.split("watch?v=")[1].split("&")[0]
    elif "youtu.be/" in youtube_url:
        return youtube_url.split("youtu.be/")[1].split("?")[0]
    else:
        return None

def extract_transcript_details(youtube_video_url):
    try:
        video_id = extract_video_id(youtube_video_url)
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = " ".join([item["text"] for item in transcript_list])
        return transcript

    except Exception as e:
        st.error("❌ Could not fetch transcript. The video may not have captions.")
        return None

def get_gemini_response(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# ----------------- Streamlit UI -----------------

st.set_page_config(page_title="YouTube Transcript Summarizer", layout="centered")

st.title("📺 YouTube Transcript to Detailed Notes Converter")

youtube_link = st.text_input("Enter the YouTube Video Link:")

if youtube_link:
    video_id = extract_video_id(youtube_link)
    if video_id:
        st.image(
            f"https://img.youtube.com/vi/{video_id}/0.jpg",
            use_column_width=True
        )

if st.button("📝 Get Detailed Notes"):
    with st.spinner("Fetching transcript and generating summary..."):
        transcript_text = extract_transcript_details(youtube_link)

        if transcript_text:
            summary = get_gemini_response(transcript_text, prompt)
            st.subheader("📌 Video Summary")
            st.write(summary)
