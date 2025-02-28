from ..database import db
from ..models import Account, TransactionResponse
from fastapi import HTTPException


class AccountService:
    """Service for handling account-related business logic."""

    @staticmethod
    def get_account(account_number: str) -> Account:
        """
        Get an account by account number.

        Args:
            account_number: The account number to retrieve

        Returns:
            The account object

        Raises:
            HTTPException: If the account doesn't exist
        """
        account = db.get_account(account_number)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        return account

    @staticmethod
    def withdraw(account_number: str, amount: float) -> TransactionResponse:
        """
        Withdraw funds from an account.

        Args:
            account_number: The account to withdraw from
            amount: The amount to withdraw

        Returns:
            Transaction response with updated balance

        Raises:
            HTTPException: If the withdrawal cannot be processed
        """
        account = AccountService.get_account(account_number)

        if amount <= 0:
            raise HTTPException(status_code=400, detail="Withdrawal amount must be positive")

        if account.balance < amount:
            raise HTTPException(status_code=400, detail="Insufficient funds")

        account.balance -= amount
        db.update_account(account)

        return TransactionResponse(
            account_number=account.account_number,
            balance=account.balance,
            message=f"Successfully withdrew ${amount:.2f}"
        )

    @staticmethod
    def deposit(account_number: str, amount: float) -> TransactionResponse:
        """
        Deposit funds into an account.

        Args:
            account_number: The account to deposit to
            amount: The amount to deposit

        Returns:
            Transaction response with updated balance

        Raises:
            HTTPException: If the deposit cannot be processed
        """
        account = AccountService.get_account(account_number)

        if amount <= 0:
            raise HTTPException(status_code=400, detail="Deposit amount must be positive")

        account.balance += amount
        db.update_account(account)

        return TransactionResponse(
            account_number=account.account_number,
            balance=account.balance,
            message=f"Successfully deposited ${amount:.2f}"
        )