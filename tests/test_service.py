import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(project_root))

# Imports
from src.services.video_processor import process_video

url = input("URL: ")

result = process_video(url)

print(result["metadata"]["title"])
print(result["cached"])
