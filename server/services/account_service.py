from fastapi import HTTPException
from ..models import Account, TransactionResponse
from ..database import db


class AccountService:
    @staticmethod
    def get_account(account_number: str) -> Account:
        """
        Get an account by account number.

        Args:
            account_number: The account number to look up

        Returns:
            The account if found

        Raises:
            HTTPException: If the account is not found
        """
        account = db.get_account(account_number)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        return account

    @staticmethod
    def create_account(account_number: str, initial_balance: float = 0) -> Account:
        """
        Create a new account with specified initial balance.

        Args:
            account_number: The account number to create
            initial_balance: The initial balance for the account, defaults to 0

        Returns:
            The newly created account
        """
        new_account = Account(account_number=account_number, balance=initial_balance)
        db.update_account(new_account)  # Using update_account since it handles creation too
        return new_account

    @staticmethod
    def withdraw(account_number: str, amount: float) -> TransactionResponse:
        """
        Withdraw funds from an account.

        Args:
            account_number: The account to withdraw from
            amount: The amount to withdraw

        Returns:
            TransactionResponse with updated balance and message

        Raises:
            HTTPException: If the account is not found or insufficient funds
        """
        account = AccountService.get_account(account_number)

        # Check if enough balance
        if account.balance < amount:
            raise HTTPException(status_code=400, detail="Insufficient funds")

        # Update balance
        account.balance -= amount
        db.update_account(account)

        return TransactionResponse(
            account_number=account.account_number,
            balance=account.balance,
            message=f"${amount:.2f} withdrawn successfully"
        )

    @staticmethod
    def deposit(account_number: str, amount: float) -> TransactionResponse:
        """
        Deposit funds to an account.

        Args:
            account_number: The account to deposit to
            amount: The amount to deposit

        Returns:
            TransactionResponse with updated balance and message
        """
        try:
            account = AccountService.get_account(account_number)
        except HTTPException:
            # Create a new account if not exists
            account = AccountService.create_account(account_number)

        # Update balance
        account.balance += amount
        db.update_account(account)

        return TransactionResponse(
            account_number=account.account_number,
            balance=account.balance,
            message=f"${amount:.2f} deposited successfully"
        )