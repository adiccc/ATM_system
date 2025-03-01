from fastapi import APIRouter, HTTPException
from ..models import WithdrawRequest, DepositRequest, TransactionResponse
from ..services.account_service import AccountService

router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.get("/{account_number}/balance")
def get_balance(account_number: str):
    """Get the current balance of a specific account. Creates account if it doesn't exist."""
    try:
        account = AccountService.get_account(account_number)
    except Exception:  # Assuming get_account raises an exception when account doesn't exist
        # Create a new account with balance 0
        account = AccountService.create_account(account_number, 0)

    return {
        "account_number": account.account_number,
        "balance": account.balance
    }
@router.post("/{account_number}/withdraw", response_model=TransactionResponse)
def withdraw_money(account_number: str, request: WithdrawRequest):
    """Withdraw a specified amount of money from an account."""
    return AccountService.withdraw(account_number, request.amount)


@router.post("/{account_number}/deposit", response_model=TransactionResponse)
def deposit_money(account_number: str, request: DepositRequest):
    """Deposit a specified amount of money into an account."""
    return AccountService.deposit(account_number, request.amount)