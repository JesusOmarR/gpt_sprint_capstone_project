#!/usr/bin/env python3

import os
from openai import OpenAI
from dotenv import load_dotenv

conversation_history = []


class ChatGPT:
    """A class to interact with OpenAI's ChatGPT model."""

    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv()

        # Retrieve the OPENAI_API_KEY environment variable

        self.api_key = os.getenv("OPENAI_API_KEY")
    def request_openai(self, message, role="system"):
        """
        Make a request to the OpenAI API.

        Args:
        - message (str): The message to be sent to the OpenAI API.
        - role (str, optional): The role associated with the message. Defaults to "system".

        Returns:
        - str: The response content from the OpenAI API.
        """
        client = OpenAI(api_key=self.api_key)

        # Create a chat completion with the provided message and role
        conversation_history.append({'role': 'user', 'content': message})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=conversation_history
        )
        conversation_history.append({'role': 'assistant', 'content': response.choices[0].message.content})

        return conversation_history


# If you need to test or use this directly, you can do:
# if __name__ == "__main__":
#     chat_gpt = ChatGPT()
#     print(chat_gpt.request_openai("Hello!"))
