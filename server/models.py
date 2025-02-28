from pydantic import BaseModel, Field
from typing import Optional


class Account(BaseModel):
    """Data model for a bank account."""
    account_number: str
    balance: float = Field(ge=0.0)


class WithdrawRequest(BaseModel):
    """Request model for withdrawal operations."""
    amount: float = Field(gt=0.0, description="Amount to withdraw (must be positive)")


class DepositRequest(BaseModel):
    """Request model for deposit operations."""
    amount: float = Field(gt=0.0, description="Amount to deposit (must be positive)")


class TransactionResponse(BaseModel):
    """Response model for transaction operations."""
    account_number: str
    balance: float
    message: str