from typing import Dict, Optional
from .models import Account


class InMemoryDatabase:
    """In-memory implementation of the database for the ATM system."""

    def __init__(self):
        """Initialize the in-memory database with some test accounts."""
        self.accounts: Dict[str, Account] = {}

        # Add some test accounts
        self.accounts["12345"] = Account(account_number="12345", balance=1000.0)
        self.accounts["67890"] = Account(account_number="67890", balance=5000.0)

    def get_account(self, account_number: str) -> Optional[Account]:
        """
        Retrieve an account by account number.

        Args:
            account_number: The account number to look up

        Returns:
            The account if found, None otherwise
        """
        return self.accounts.get(account_number)

    def update_account(self, account: Account) -> None:
        """
        Update or create an account in the database.

        Args:
            account: The account to update or create
        """
        self.accounts[account.account_number] = account

    def list_accounts(self) -> list[Account]:
        """
        List all accounts in the database.

        Returns:
            A list of all accounts
        """
        return list(self.accounts.values())


# Create a singleton instance of the database
db = InMemoryDatabase()