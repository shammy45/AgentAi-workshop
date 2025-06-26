from accounts import Account
import gradio as gr

# Initialize a global account instance
account = None

def create_account(username, initial_deposit):
    global account
    if not account:
        account = Account(username, float(initial_deposit))
        return f"Account created for {username} with an initial deposit of {initial_deposit}."
    else:
        return "Account already exists."

def deposit_funds(amount):
    global account
    try:
        account.deposit(float(amount))
        return f"Deposited {amount}. New balance: {account.balance}."
    except ValueError as e:
        return str(e)

def withdraw_funds(amount):
    global account
    try:
        account.withdraw(float(amount))
        return f"Withdrew {amount}. New balance: {account.balance}."
    except ValueError as e:
        return str(e)

def buy_shares(symbol, quantity):
    global account
    try:
        account.buy_shares(symbol, int(quantity))
        return f"Bought {quantity} shares of {symbol}."
    except ValueError as e:
        return str(e)

def sell_shares(symbol, quantity):
    global account
    try:
        account.sell_shares(symbol, int(quantity))
        return f"Sold {quantity} shares of {symbol}."
    except ValueError as e:
        return str(e)

def report_holdings():
    global account
    return account.report_holdings()

def report_profit_loss():
    global account
    return account.report_profit_loss()

def list_transactions():
    global account
    return account.list_transactions()

with gr.Blocks() as demo:
    gr.Markdown("# Trading Account Management System")
    
    with gr.Row():
        username = gr.Textbox(label="Username", placeholder="Enter your username")
        initial_deposit = gr.Number(label="Initial Deposit")

    create_btn = gr.Button("Create Account")
    create_output = gr.Textbox(label="Account Status")
    create_btn.click(create_account, inputs=[username, initial_deposit], outputs=create_output)

    with gr.Row():
        deposit_amount = gr.Number(label="Deposit Amount")
        deposit_btn = gr.Button("Deposit")
        deposit_output = gr.Textbox(label="Deposit Status")
        deposit_btn.click(deposit_funds, inputs=deposit_amount, outputs=deposit_output)

    with gr.Row():
        withdraw_amount = gr.Number(label="Withdraw Amount")
        withdraw_btn = gr.Button("Withdraw")
        withdraw_output = gr.Textbox(label="Withdraw Status")
        withdraw_btn.click(withdraw_funds, inputs=withdraw_amount, outputs=withdraw_output)

    with gr.Row():
        buy_symbol = gr.Textbox(label="Stock Symbol (e.g. AAPL)")
        buy_quantity = gr.Number(label="Quantity")
        buy_btn = gr.Button("Buy Shares")
        buy_output = gr.Textbox(label="Buy Status")
        buy_btn.click(buy_shares, inputs=[buy_symbol, buy_quantity], outputs=buy_output)

    with gr.Row():
        sell_symbol = gr.Textbox(label="Stock Symbol (e.g. AAPL)")
        sell_quantity = gr.Number(label="Quantity")
        sell_btn = gr.Button("Sell Shares")
        sell_output = gr.Textbox(label="Sell Status")
        sell_btn.click(sell_shares, inputs=[sell_symbol, sell_quantity], outputs=sell_output)

    with gr.Row():
        holdings_btn = gr.Button("Report Holdings")
        holdings_output = gr.JSON(label="Holdings")
        holdings_btn.click(report_holdings, outputs=holdings_output)

    with gr.Row():
        profit_loss_btn = gr.Button("Report Profit/Loss")
        profit_loss_output = gr.Number(label="Profit/Loss")
        profit_loss_btn.click(report_profit_loss, outputs=profit_loss_output)

    with gr.Row():
        transactions_btn = gr.Button("List Transactions")
        transactions_output = gr.JSON(label="Transactions")
        transactions_btn.click(list_transactions, outputs=transactions_output)

demo.launch()