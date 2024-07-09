Feature: Percent Limit
    The percent limit is what percent the transaction amount is with respect to the credit card limit that transacted

    Scenario Outline: Percent Limit
        Given I use credit card <creditcardid>
        When I have <transactionid>
        Then percent limit should <percentlimit>

     Examples: credit cards
       | creditcardid         | transactionid | percentlimit |
       | a2c6e477-37d1-4b70-8287-3c8d19eb4d9e | ca424c0a-17fb-4d5c-90b2-009b3f69c466 | .23 |
       | 14dea739-1647-4b00-b044-53bddccafd0b | 77619230-c653-4183-9ef8-b59cb312987f | .35 |

    Scenario Outline:  Limit
        Given I use credit card <creditcardid>
        When I have <transactionid>
        Then limit should <limit>

     Examples: credit cards
       | creditcardid         | transactionid | limit |
       | a2c6e477-37d1-4b70-8287-3c8d19eb4d9e |ca424c0a-17fb-4d5c-90b2-009b3f69c466 | 300 |
       | 14dea739-1647-4b00-b044-53bddccafd0b | 77619230-c653-4183-9ef8-b59cb312987f | 1000000 |

    Scenario Outline:  transactions_last_24h
        Given I use credit card <creditcardid>
        When I have <transactionid>
        Then transactions_last_24h should <transactions_last_24h>

     Examples: credit cards
       | creditcardid         | transactionid | transactions_last_24h |
       | a2c6e477-37d1-4b70-8287-3c8d19eb4d9e |ca424c0a-17fb-4d5c-90b2-009b3f69c466 | 0 |
       | a2c6e477-37d1-4b70-8287-3c8d19eb4d9e |48d4b239-cb28-4328-a055-bcb14fc4f5ab | 1 |
       | 14dea739-1647-4b00-b044-53bddccafd0b | 77619230-c653-4183-9ef8-b59cb312581f | 0 |


   Scenario Outline:  transactions_last_2weeks
         Given I use credit card <creditcardid>
         When I have <transactionid>
         Then transactions_last_2weeks should <transactions_last_2weeks>

      Examples: credit cards
         | creditcardid         | transactionid | transactions_last_2weeks |
         | a2c6e477-37d1-4b70-8287-3c8d19eb4d9e |ca424c0a-17fb-4d5c-90b2-009b3f69c466 | 0 |
         | a2c6e477-37d1-4b70-8287-3c8d19eb4d9e |48d4b239-cb28-4328-a055-bcb14fc4f5ab | 1 |
         | 14dea739-1647-4b00-b044-53bddccafd0b | 77619230-c653-4183-9ef8-b59cb312581f | 2 |
         | 14dea739-1647-4b00-b044-53bddccafd0b | 12dac25d-6099-4de3-ab5c-77a6618dd818 | 4 |
      