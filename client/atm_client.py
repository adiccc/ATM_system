import requests
from typing import Dict, Any, Optional


class ATMClient:
    """Client for interacting with the ATM system API."""

    def __init__(self, base_url="http://localhost:8000"):
        """
        Initialize ATM client with the server base URL.

        Args:
            base_url: The base URL of the ATM server
        """
        self.base_url = base_url

    def get_balance(self, account_number: str) -> Optional[Dict[str, Any]]:
        """
        Get the current balance of an account.

        Args:
            account_number: The account number to query

        Returns:
            Dictionary containing account details and balance, or None if the request fails
        """
        url = f"{self.base_url}/accounts/{account_number}/balance"

        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving balance: {e}")
            if hasattr(e, 'response') and e.response:
                print(f"Server response: {e.response.text}")
            return None

    def withdraw(self, account_number: str, amount: float) -> Optional[Dict[str, Any]]:
        """
        Withdraw money from an account.

        Args:
            account_number: The account number to withdraw from
            amount: The amount to withdraw

        Returns:
            Dictionary containing transaction details, or None if the request fails
        """
        url = f"{self.base_url}/accounts/{account_number}/withdraw"
        data = {"amount": amount}

        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error withdrawing funds: {e}")
            if hasattr(e, 'response') and e.response:
                print(f"Server response: {e.response.text}")
            return None

    def deposit(self, account_number: str, amount: float) -> Optional[Dict[str, Any]]:
        """
        Deposit money into an account.

        Args:
            account_number: The account number to deposit to
            amount: The amount to deposit

        Returns:
            Dictionary containing transaction details, or None if the request fails
        """
        url = f"{self.base_url}/accounts/{account_number}/deposit"
        data = {"amount": amount}

        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error depositing funds: {e}")
            if hasattr(e, 'response') and e.response:
                print(f"Server response: {e.response.text}")
            return None