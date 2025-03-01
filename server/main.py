from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from .routes.accounts import get_accounts_router

# Initialize FastAPI app
app = FastAPI(
    title="ATM System API",
    description="A simple ATM system API for managing account operations",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins in production, or specify your deployed frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(get_accounts_router())


@app.get("/")
def read_root():
    """Root endpoint for ATM system API."""
    return {"message": "Welcome to the ATM System API"}


# This is only used when running locally. When deployed to Google Cloud,
# gunicorn will use the app variable directly
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)