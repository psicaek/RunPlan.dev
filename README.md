# 🏃 Running Plan Generator

A full-stack web application that generates personalized running training plans based on runner profiles and race goals.

---

## 🚀 Overview

Running Plan Generator is a full-stack project designed to calculate realistic, progressive, and safe running training plans.

- Frontend: Vue 3 + TypeScript
- Backend: FastAPI (Python)

The frontend collects user input, and the backend processes it into a structured training plan.

---

## ✨ Features

- Personalized training plans
- Weekly mileage progression with safety caps
- Automatic taper before race day
- Clean, rounded mileage values
- Modular backend logic

---

## 🧱 Tech Stack

### Frontend

- Vue 3
- TypeScript
- Pinia
- Axios

### Backend

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn

---

## 📁 Project Structure

project-root/  
│  
├── frontend/  
│ ├── src/  
│ ├── package.json  
│  
├── backend/  
│ ├── main.py  
│ ├── models.py  
│ ├── logic/  
│ └── requirements.txt  
│  
└── README.md

---

## 🛠️ Getting Started

### Backend Setup

1. Navigate to the backend directory  
   `cd backend`

2. Create and activate a virtual environment  
   `python -m venv venv`  
   `source venv/bin/activate` (Windows: `venv\Scripts\activate`)

3. Install dependencies  
   `pip install -r requirements.txt`

4. Start the FastAPI server  
   `uvicorn main:app --reload`

Backend runs at:  
http://127.0.0.1:8000

---

### Frontend Setup

1. Navigate to the frontend directory  
   `cd frontend`

2. Install packages  
   `npm install`

3. Start the development server  
   `npm run dev`

Frontend runs at:  
http://localhost:5173

---

## 🔌 API Usage

### Generate Training Plan Endpoint

**POST /api/generate-plan**

Example Request Body:

{
"profile": {
"experienceLevel": "Intermediate",
"weeklyDistance": 30,
"longestRun": 12,
"age": 33,
"gender": "Male"
},
"goal": {
"raceDistance": "Half Marathon",
"goalTime": 105,
"targetDate": "2026-05-22",
"trainingDays": "4"
}
}

Example Response:

{
"success": true,
"data": {
"weeklyMileage": [22, 24, 26, 28, 30, 32, 35, 38],
"pace": 4.98,
"trainingStructure": ["easy", "interval", "long", "tempo"]
}
}

---

## 🧠 Training Logic Overview

The backend generates training plans using the following principles:

- Calculate weeks until race day
- Gradually increase weekly mileage with capped progression
- Peak mileage 2–3 weeks before race
- Apply a taper phase before race day
- Round mileage values for clean output
- Distribute mileage across training days

All logic is modularized in helper functions for clarity and easier maintenance.

---

## 🔮 Roadmap

- Long run distance progression
- Daily workout breakdown
- Pace zones (easy, tempo, interval)
- Adaptive plans based on missed sessions
- Export training plans as PDF

---

## ⚠️ Disclaimer

This application provides general training guidance only.  
It is not a substitute for professional coaching or medical advice.

---

## 👤 Author

Ioannis Psychogyios
