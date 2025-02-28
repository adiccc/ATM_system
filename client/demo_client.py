from atm_client import ATMClient


def demo():
    """
    Demonstrates the ATM client functionality.
    """
    # Create ATM client
    atm = ATMClient()

    # Example account number
    account_num = "12345"

    # Check balance
    print("\n--- Checking Balance ---")
    balance_info = atm.get_balance(account_num)
    if balance_info:
        print(f"Account: {balance_info['account_number']}")
        print(f"Balance: ${balance_info['balance']:.2f}")

    # Make a deposit
    print("\n--- Making Deposit ---")
    deposit_amount = 500
    deposit_result = atm.deposit(account_num, deposit_amount)
    if deposit_result:
        print(f"Result: {deposit_result['message']}")
        print(f"New Balance: ${deposit_result['balance']:.2f}")

    # Make a withdrawal
    print("\n--- Making Withdrawal ---")
    withdraw_amount = 200
    withdraw_result = atm.withdraw(account_num, withdraw_amount)
    if withdraw_result:
        print(f"Result: {withdraw_result['message']}")
        print(f"New Balance: ${withdraw_result['balance']:.2f}")


if __name__ == "__main__":
    demo()