# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# Simple in-memory database
database = {
    "12345": {"name": "Harry Potter", 
              "balance": 1000, 
              'account_number': '12345',
              'transaction': 20000
              },
    "67890": {"name": "Marry Jane", 
              "balance": 2000, 
              'account_number': '67890',
              'transaction': 50000
              },
}

class ActionCheckBalance(Action):
    def name(self) -> Text:
        return "action_check_balance"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Extract the account_number entity
        account_number = tracker.get_slot("account_number")

        if account_number in database:
            account_info = database[account_number]
            # Extract the name and balance from the database entry
            name = account_info.get("name", "User")
            balance = account_info.get("balance", 0)
            
            # Send a response with personalized information
            dispatcher.utter_message(
                response="utter_balance",
                name=name,
                account_number=account_number,
                balance=balance
            )
        else:
            # Handle the case when the account number is not found
            dispatcher.utter_message("I couldn't find your account information. Please check your account number.")
        
        return []

class ActionTransactionHistory(Action):
    def name(self) -> Text:
        return "action_transaction_history"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
         # Extract the account_number entity
        account_number = tracker.get_slot("account_number")

        if account_number in database:
            account_info = database[account_number]
            # Extract the name and balance from the database entry
            name = account_info.get("name", "User")
            transaction = account_info.get("transaction", 0)
            
            # Send a response with personalized information
            dispatcher.utter_message(
                response="utter_transaction",
                name=name,
                account_number=account_number,
                transaction=transaction
            )
        else:
            # Handle the case when the account number is not found
            dispatcher.utter_message("I couldn't find your account information. Please check your account number.")
        
        return []


