from behave import *
import pandas as pd
import uuid
import datetime
@given('I use credit card {creditcardid}')
def step_impl(context, creditcardid):
    df = pd.read_csv("data/credit_card.csv", index_col = "credit_card_id")
    limit = int(df.loc[creditcardid,"limit"])
    context.credit_card_id = creditcardid
    context.limit = limit
    print(creditcardid)

@when('I have {transactionid}')
def step_impl(context, transactionid):
    context.transaction_id = transactionid
    df = pd.read_csv("enriched_transactions.csv", index_col="transaction_id")
    amount = int(df.loc[transactionid, "amount"])
    context.amount = amount

@then('percent limit should {percentlimit}')
def step_impl(context, percentlimit):
    print(percentlimit)
    oracle_result = context.amount / context.limit #Oracle
    print(oracle_result)
    transaction_id = context.transaction_id
    transaction_df = pd.read_csv("enriched_transactions.csv", index_col="transaction_id")
    actual_percent_limit = transaction_df.loc[transaction_id, "%limit"]
    assert float(oracle_result) == float(percentlimit)
    assert float(actual_percent_limit) == float(percentlimit)

@then('limit should {limit}')
def step_impl(context, limit):
    print(limit)
    transaction_id = context.transaction_id
    transaction_df = pd.read_csv("enriched_transactions.csv", index_col="transaction_id")
    actual_limit = transaction_df.loc[transaction_id, "limit"]

    assert float(context.limit) == float(limit) #Credit card table's limit
    assert float(actual_limit) == float(limit)  # Credit card table's limit
    

@then('transactions_last_24h should {transactions_last_24h}')
def step_impl(context, transactions_last_24h):
    transaction_id = context.transaction_id
    transaction_df = pd.read_csv("enriched_transactions.csv", index_col="transaction_id")
    current_date_time = transaction_df.loc[transaction_id,"date_time"]
    current_dt  =  datetime.datetime.strptime(current_date_time, "%Y-%m-%d %H:%M:%S.%f")
    hours_ago = current_dt - datetime.timedelta(hours=24)
    current_date_time_before_24 = hours_ago.strftime("%Y-%m-%d %H:%M:%S.%f")
  
    transaction_df = transaction_df[transaction_df["credit_card_id"] == current_date_time]
    transaction_df = transaction_df[transaction_df["credit_card_id"] == context.credit_card_id]
    recent_transactions = transaction_df[(transaction_df["date_time"] < current_date_time) & (transaction_df["date_time"] >= current_date_time_before_24) ]

    assert float(len(recent_transactions)) == float(transactions_last_24h) #Credit card table's limit
