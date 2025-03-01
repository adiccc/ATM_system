from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from server.routes import accounts

# Initialize FastAPI app
app = FastAPI(
    title="ATM System API",
    description="A simple ATM system API for managing account operations",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(accounts.router)


@app.get("/")
def read_root():
    """Root endpoint for ATM system API."""
    return {"message": "Welcome to the ATM System API"}


if __name__ == "__main__":
    uvicorn.run("server.main:app", host="0.0.0.0", port=8000, reload=True)