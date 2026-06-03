# Imports
import os
import whisper
import yt_dlp

# Downloading the audio from the YouTube video
def download_audio(url: str, output_path: str = "data/audio") -> str:
    """
    Downloads the audio from a YouTube video.

    Args:
        url (str): The YouTube video URL.
        output_path (str): The path where the audio file will be saved.

    Returns:
        str: The path to the downloaded audio file.
    """

    os.makedirs(output_path, exist_ok=True)

    audio_path = os.path.join(output_path, "audio.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": audio_path,
        "quiet": True,
        "noplaylist": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        downloaded_file = ydl.prepare_filename(info)

    return downloaded_file

# Transcribing the audio using OpenAI's Whisper model
def transcribe_with_whisper(audio_path: str) -> str:
    """
    Transcribes the audio using OpenAI's Whisper model.

    Args:
        audio_path (str): The path to the audio file.

    Returns:
        str: The transcribed text.
    """

    model = whisper.load_model("base")

    result = model.transcribe(audio_path)

    transcript = result["text"]

    print("✅ Transcript generated using Whisper\n")

    return transcript

# Calling the functions
def generate_transcript_using_whisper(url: str) -> str:
    """
    Gets the transcript for a YouTube video using OpenAI's Whisper model.

    Args:
        url (str): The YouTube video URL.

    Returns:
        str: The transcribed text.
    """

    audio_file = download_audio(url)

    transcript = transcribe_with_whisper(audio_file)

    # Clean up the downloaded audio file
    os.remove(audio_file)

    return transcript
