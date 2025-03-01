from fastapi import APIRouter, HTTPException
from ..models import WithdrawRequest, DepositRequest, TransactionResponse, Account
from ..services.account_service import AccountService
from ..database import db

router = APIRouter(prefix="/accounts", tags=["accounts"])


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
    try:
        return AccountService.deposit(account_number, request.amount)
    except HTTPException as e:
        if e.status_code == 404:
            # Create account and then deposit
            account = AccountService.create_account(account_number)
            account.balance += request.amount
            db.update_account(account)

            return TransactionResponse(
                account_number=account.account_number,
                balance=account.balance,
                message=f"Account created and ${request.amount:.2f} deposited successfully"
            )
        raise e


# Add this method to your AccountService class
class AccountService:
    # ... existing methods ...

    @staticmethod
    def create_account(account_number: str) -> Account:
        """
        Create a new account with a balance of 0.

        Args:
            account_number: The account number to create

        Returns:
            The newly created account object
        """
        # Create a new account object with balance 0
        new_account = Account(account_number=account_number, balance=0)

        # Save it to the database
        db.create_account(new_account)

        return new_account