from fastapi import FastAPI, Request
from pydantic import BaseModel
import httpx 
from WeatherAgentFolder.weather_agent import weather_agent

app = FastAPI()

# Input schema
class LLMRequest(BaseModel):
    city: str
    WEATHER_API_KEY : str

# Simulated response function — replace with your model call
async def run_weather_agent(city: str, WEATHER_API_KEY:str) -> str:
    output = weather_agent.invoke({"messages":[city, WEATHER_API_KEY]})
    return output["messages"][-1].content
    
# FastAPI POST endpoint
@app.post("/chat")
async def infer(request: LLMRequest):
    output = await run_weather_agent(request.city, request.WEATHER_API_KEY)
    return {"response": output}
