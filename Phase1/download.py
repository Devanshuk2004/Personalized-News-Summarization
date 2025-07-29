import gdown
import os
import tarfile

BASE_DIR = os.path.dirname(__file__)
MODEL_DIR = os.path.join(BASE_DIR, "checkpoints", "checkpoint-215337")
ARCHIVE_PATH = os.path.join(BASE_DIR, "checkpoint-215337.tar.gz")

URL = "https://drive.google.com/uc?id=1ZDLQqKt52M5jW5AijuIqLnZpdWgGMofr"

def download_model():
    if not os.path.exists(MODEL_DIR):
        print("Downloading model from Google Drive...")
        gdown.download(URL, ARCHIVE_PATH, quiet=False, fuzzy=True)

        print("Extracting model...")
        with tarfile.open(ARCHIVE_PATH, "r:gz") as tar:
            tar.extractall(os.path.join(BASE_DIR, "checkpoints"))

        print("Model extracted successfully!")
    else:
        print("Model already exists. Skipping download.")
