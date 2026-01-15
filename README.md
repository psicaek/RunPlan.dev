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
├── src/
│ ├── assets/
│ ├── components/
│ ├── pages/
│ ├── router/
│ ├── services/
│ ├── App.vue
│ └── main.js
│
├── backend/
│ ├── main.py
│ ├── plan_generator.py
│ ├── test_plan_generator.py
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

4. Start the Main  
   `python main.py`

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
"experienceLevel": "Advance",
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
"PersonalBest": 110
}
}

Example Response:

{
"success": true,
"message": "Data received successfully!",
"plan": {
"weeks_until": 3,
"pace": "4:59",
"weeks": [
{
"week": 1,
"total_km": 32.4,
"runs": [
{
"type": "easy",
"distance": 5.8,
"pace_per_run_type": "5:26"
},
{
"type": "interval",
"distance": 6.5,
"pace_per_run_type": "4:44"
},
{
"type": "long",
"distance": 16.2,
"pace_per_run_type": "5:20"
},
{
"type": "recovery",
"distance": 3.9,
"pace_per_run_type": "5:35"
}
]
},
{
"week": 2,
"total_km": 36.3,
"runs": [
{
"type": "easy",
"distance": 6.5,
"pace_per_run_type": "5:26"
},
{
"type": "interval",
"distance": 7.3,
"pace_per_run_type": "4:44"
},
{
"type": "long",
"distance": 18.1,
"pace_per_run_type": "5:20"
},
{
"type": "recovery",
"distance": 4.4,
"pace_per_run_type": "5:35"
}
]
},
{
"week": 3,
"total_km": 18.1,
"runs": [
{
"type": "easy",
"distance": 3.3,
"pace_per_run_type": "5:26"
},
{
"type": "interval",
"distance": 3.6,
"pace_per_run_type": "4:44"
},
{
"type": "long",
"distance": 9.1,
"pace_per_run_type": "5:20"
},
{
"type": "recovery",
"distance": 2.2,
"pace_per_run_type": "5:35"
}
]
}
],
"type_of_runs": [
"easy",
"interval",
"long",
"recovery"
]
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

- Export training plans as PDF

---

## ⚠️ Disclaimer

This application provides general training guidance only.  
It is not a substitute for professional coaching or medical advice.

---

## 👤 Author

Ioannis Psychogyios - Test Automation Engineer
