from fastapi import FastAPI
import uvicorn
from server.routes import accounts

# Initialize FastAPI app
app = FastAPI(
    title="ATM System API",
    description="A simple ATM system API for managing account operations",
    version="1.0.0"
)

# Include routers
app.include_router(accounts.router)


@app.get("/")
def read_root():
    """Root endpoint for ATM system API."""
    return {"message": "Welcome to the ATM System API"}


if __name__ == "__main__":
    uvicorn.run("server.main:app", host="0.0.0.0", port=8000, reload=True)