from fastapi import APIRouter, HTTPException
from ..models import WithdrawRequest, DepositRequest, TransactionResponse
from ..services.account_service import AccountService

router = APIRouter(prefix="/accounts", tags=["accounts"])

def get_accounts_router():
    return router

@router.get("/{account_number}/balance")
def get_balance(account_number: str):
    """Get the current balance of a specific account. Creates account if it doesn't exist."""
    try:
        account = AccountService.get_account(account_number)
    except HTTPException as e:
        if e.status_code == 404:
            # Create a new account with balance 0
            account = AccountService.create_account(account_number)
        else:
            raise e

    return {
        "account_number": account.account_number,
        "balance": account.balance
    }


@router.post("/{account_number}/withdraw", response_model=TransactionResponse)
def withdraw_money(account_number: str, request: WithdrawRequest):
    """Withdraw a specified amount of money from an account."""
    try:
        return AccountService.withdraw(account_number, request.amount)
    except HTTPException as e:
        if e.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail="Account not found. Please make a balance inquiry first to create the account."
            )
        raise e


@router.post("/{account_number}/deposit", response_model=TransactionResponse)
def deposit_money(account_number: str, request: DepositRequest):
    """Deposit a specified amount of money into an account."""
    return AccountService.deposit(account_number, request.amount)