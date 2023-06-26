# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from db_connect import DataFetch

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionFetchData(Action):
    def name(self):
        return "action_givedetails" 
    
    def run(self, dispatcher, tracker, domain):
        client = tracker.get_slot('user_ID')
        print("The client is: " + client)
        message = DataFetch(client)
        dispatcher.utter_message(message) 

        return []