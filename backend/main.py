from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import json
from plan_generator import generate_plan_logic

# FastAPI app
app = FastAPI(
    title="Running Plan API",
    description="API to receive running plan data",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Models
class Profile(BaseModel):
    experienceLevel: str
    weeklyDistance: float
    longestRun: float
    age: int
    gender: str

class Goal(BaseModel):
    raceDistance: str
    goalTime: float
    targetDate: str
    trainingDays: str

class RunningPlanRequest(BaseModel):
    profile: Profile
    goal: Goal

# Routes
@app.get("/")
async def root():
    return {
        "message": "Running Plan API", 
        "status": "running"
    }

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/api/generate-plan")
async def generate_plan(request: RunningPlanRequest):
    try:
        # Print received data
        print("\n" + "="*50)
        print("RECEIVED DATA FROM FRONTEND:")
        print("="*50)
        print(f"Profile: {request.profile.model_dump()}")
        print(f"Goal: {request.goal.model_dump()}")
        print("="*50 + "\n")
        with open("last_request.json", "w") as f:
            json.dump({
                "profile": request.profile.model_dump(),
                "goal": request.goal.model_dump()
            }, f, indent=4)
        plan = generate_plan_logic(request.profile, request.goal)
           
        # For now, just return a simple response
        return {
            "success": True,
            "message": "Data received successfully!",
            "plan": plan
            
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    print("\n🚀 Starting Running Plan API Server...")
    print("📍 Server running at: http://localhost:8000")
    print("📝 API docs at: http://localhost:8000/docs\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)