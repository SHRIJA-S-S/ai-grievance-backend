import sys
import os

# ---- FORCE PROJECT ROOT INTO PYTHON PATH ----
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
sys.path.append(PROJECT_ROOT)
# --------------------------------------------

from fastapi import FastAPI, UploadFile, File, Form
from backend.services.text_service import handle_text
from backend.services.image_service import handle_image

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Grievance Backend Running"}

@app.post("/submit-grievance")
async def submit_grievance(
    text: str = Form(None),
    image: UploadFile = File(None)
):
    result = {}

    if text:
        result["text_analysis"] = handle_text(text)

    if image:
        image_bytes = await image.read()
        result["image_analysis"] = handle_image(image_bytes)

    return {
        "status": "success",
        "result": result
    }
