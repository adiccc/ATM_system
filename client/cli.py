import argparse
from .atm_client import ATMClient


def main():
    """
    Command-line interface for the ATM client.
    """
    parser = argparse.ArgumentParser(description="ATM Client CLI")

    # Server configuration
    parser.add_argument(
        "--server",
        default="http://localhost:8000",
        help="ATM server URL"
    )

    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Balance command
    balance_parser = subparsers.add_parser("balance", help="Check account balance")
    balance_parser.add_argument("account", help="Account number")

    # Withdraw command
    withdraw_parser = subparsers.add_parser("withdraw", help="Withdraw funds")
    withdraw_parser.add_argument("account", help="Account number")
    withdraw_parser.add_argument("amount", type=float, help="Amount to withdraw")

    # Deposit command
    deposit_parser = subparsers.add_parser("deposit", help="Deposit funds")
    deposit_parser.add_argument("account", help="Account number")
    deposit_parser.add_argument("amount", type=float, help="Amount to deposit")

    # Parse arguments
    args = parser.parse_args()

    # Create ATM client
    atm = ATMClient(base_url=args.server)

    # Execute requested command
    if args.command == "balance":
        result = atm.get_balance(args.account)
        if result:
            print(f"Account: {result['account_number']}")
            print(f"Balance: ${result['balance']:.2f}")

    elif args.command == "withdraw":
        result = atm.withdraw(args.account, args.amount)
        if result:
            print(f"Result: {result['message']}")
            print(f"New Balance: ${result['balance']:.2f}")

    elif args.command == "deposit":
        result = atm.deposit(args.account, args.amount)
        if result:
            print(f"Result: {result['message']}")
            print(f"New Balance: ${result['balance']:.2f}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()