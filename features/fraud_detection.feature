Feature: Fraud detection data quality assurance
  Ensure the quality of `transactions_last_24h` and `transactions_last_2weeks` columns.

  Scenario: Validate transactions_last_24h values
    Given a set of transaction data
    When the transactions_last_24h values are checked
    Then the transactions_last_24h values should be within expected ranges

  Scenario: Validate transactions_last_2weeks values
    Given a set of transaction data
    When the transactions_last_2weeks values are checked
    Then the transactions_last_2weeks values should be within expected ranges
