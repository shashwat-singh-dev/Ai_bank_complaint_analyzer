from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from datetime import datetime
import joblib
from collections import Counter


app = FastAPI()

templates = Jinja2Templates(directory="templates")

model = joblib.load("banking_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
prediction_history = []


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):

    category_counts = Counter(
        item["category"]
        for item in prediction_history
    )

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "total_predictions": len(prediction_history),
            "history": prediction_history[::-1],
            "chart_labels": list(category_counts.keys()),
            "chart_values": list(category_counts.values())
        }
    )


class ComplaintRequest(BaseModel):
    complaint: str


@app.post("/predict")
def predict(data: ComplaintRequest):

    vec = vectorizer.transform([data.complaint])

    prediction = model.predict(vec)[0]

    confidence = model.predict_proba(vec).max() * 100
    prediction_history.append({
    "category": prediction,
    "confidence": round(confidence, 2),
    "time": datetime.now().strftime("%I:%M %p")
})
    prediction_history[:] = prediction_history[-50:]
    if confidence < 50:
        return {
        "category": "Invalid / Non-Banking Complaint",
        "confidence": round(confidence, 2)
    }
    

    return {
        "category": prediction,
        "confidence": round(confidence, 2)
    }