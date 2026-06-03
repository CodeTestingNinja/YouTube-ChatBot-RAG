# Imports
import re
import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable

# Extracting the video ID from the YouTube URL
def extract_video_id(url):
    """
    Extracts the video ID from a YouTube URL.

    Args:
        url (str): The YouTube URL.

    Returns:
        str: The extracted video ID.
    """

    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)

    if match:
        return match.group(1)

    return None

# Fetching the transcript using the YouTube Transcript API
def get_youtube_transcript(video_id):
    """
    Fetches the transcript for a given YouTube video ID.

    Args:
        video_id (str): The YouTube video ID.

    Returns:
        str: The extracted transcript.
    """

    api = YouTubeTranscriptApi()

    try:
        # Try English captions first
        fetched_transcript = api.fetch(video_id, languages=["en"])

        # Removing the timestamps and concetinating the remaining fetched text
        transcript = " ".join(chunk.text for chunk in fetched_transcript)

        print("✅ Transcript fetched from YouTube captions")

        return transcript

    except (TranscriptsDisabled, NoTranscriptFound):
        print("⚠ No English captions found.")
        return None

    except VideoUnavailable:
        print("❌ Video unavailable.")
        return None

    except Exception as e:
        print("⚠ YouTube transcript API failed.")
        print(e)
        return None

# Fetching metadata from the YouTube video using yt-dlp
def get_video_metadata(url: str) -> dict:
    """
    Extract metadata from a YouTube video.

    Args:
        url (str): YouTube video URL

    Returns:
        dict: Video metadata
    """

    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": False
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        metadata = {
            "video_id": info.get("id"),
            "title": info.get("title"),
            "channel": info.get("uploader"),
            "duration": info.get("duration"),
            "view_count": info.get("view_count"),
            "upload_date": info.get("upload_date"),
            "thumbnail": info.get("thumbnail"),
            "webpage_url": info.get("webpage_url"),
        }

        return metadata
    
    except Exception as e:
        raise Exception(f"Failed to fetch video metadata: {str(e)}")
