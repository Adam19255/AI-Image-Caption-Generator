from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routers import caption

app = FastAPI(title="AI Image Caption Generator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173",
        "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(caption.router)

@app.get("/")
def root():
    return {"message": "AI Caption Generator API is running!"}
