# accounts.py

class Account:
    def __init__(self, username: str, initial_deposit: float):
        """
        Initializes a new Account instance.

        :param username: The username of the account holder.
        :param initial_deposit: Initial funds deposited into the account.
        """
        self.username = username
        self.balance = initial_deposit
        self.holdings = {}  # key: stock symbol, value: quantity of shares
        self.transactions = []  # list of transactions made

    def deposit(self, amount: float) -> None:
        """
        Deposits funds into the account.

        :param amount: The amount of money to deposit.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount: float) -> None:
        """
        Withdraws funds from the account.

        :param amount: The amount of money to withdraw.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < 0:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount
        self.transactions.append(f"Withdrew: {amount}")

    def buy_shares(self, symbol: str, quantity: int) -> None:
        """
        Buys shares of a stock.

        :param symbol: The stock symbol to buy.
        :param quantity: The quantity of shares to buy.
        """
        share_price = get_share_price(symbol)
        total_cost = share_price * quantity
        
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if total_cost > self.balance:
            raise ValueError("Insufficient funds to buy shares.")

        self.balance -= total_cost
        if symbol in self.holdings:
            self.holdings[symbol] += quantity
        else:
            self.holdings[symbol] = quantity
        self.transactions.append(f"Bought: {quantity} shares of {symbol} at {share_price} each")

    def sell_shares(self, symbol: str, quantity: int) -> None:
        """
        Sells shares of a stock.

        :param symbol: The stock symbol to sell.
        :param quantity: The quantity of shares to sell.
        """
        if symbol not in self.holdings or self.holdings[symbol] < quantity:
            raise ValueError("Insufficient shares to sell.")

        share_price = get_share_price(symbol)
        total_revenue = share_price * quantity
        
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        
        self.balance += total_revenue
        self.transactions.append(f"Sold: {quantity} shares of {symbol} at {share_price} each")

    def calculate_portfolio_value(self) -> float:
        """
        Calculates the total value of the portfolio.

        :return: The total value of the portfolio.
        """
        total_value = self.balance
        for symbol, quantity in self.holdings.items():
            total_value += get_share_price(symbol) * quantity
        return total_value

    def calculate_profit_loss(self) -> float:
        """
        Calculates the profit or loss from the initial deposit.

        :return: Profit or loss value.
        """
        return self.calculate_portfolio_value() - self.initial_deposit

    def report_holdings(self) -> dict:
        """
        Reports the current holdings of the user.

        :return: A dictionary of stock symbols and their quantities.
        """
        return self.holdings

    def report_profit_loss(self) -> float:
        """
        Reports the current profit or loss of the user.

        :return: Total profit or loss.
        """
        return self.calculate_profit_loss()

    def list_transactions(self) -> list:
        """
        Lists all transactions made by the user.

        :return: A list of transactions.
        """
        return self.transactions


def get_share_price(symbol: str) -> float:
    """
    Mock function that returns the current price of a share.

    :param symbol: The stock symbol to get the price for.

    :return: The current price of the stock.
    """
    prices = {
        "AAPL": 150.00,
        "TSLA": 700.00,
        "GOOGL": 2800.00,
    }
    return prices.get(symbol, 0.0)  # Default to 0.0 if symbol not found