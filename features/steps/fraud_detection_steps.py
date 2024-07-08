from behave import given, when, then
import pandas as pd

# Load the dataset (assuming the file is in the same directory)
data = pd.read_csv('enriched_transactions.csv')

@given('a set of transaction data')
def step_given_set_of_transaction_data(context):
    context.data = data

@when('the {column_name} values are checked')
def step_when_values_are_checked(context, column_name):
    context.transactions = context.data[column_name].dropna()

@then('the {column_name} values should be within expected ranges')
def step_then_values_should_be_within_expected_ranges(context, column_name):
    MAX_EXPECTED_TRANSACTIONS_24H = 500  # Example threshold for transactions in 24h
    MAX_EXPECTED_TRANSACTIONS_2WEEKS = 2000  # Example threshold for transactions in 2 weeks

    for value in context.transactions:
        if column_name == 'transactions_last_24h':
            assert 0 <= value <= MAX_EXPECTED_TRANSACTIONS_24H, f"{column_name} value {value} is out of expected range"
        elif column_name == 'transactions_last_2weeks':
            assert 0 <= value <= MAX_EXPECTED_TRANSACTIONS_2WEEKS, f"{column_name} value {value} is out of expected range"
