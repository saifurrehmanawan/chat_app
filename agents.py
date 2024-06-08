import os
import pathlib
import textwrap

import google.generativeai as genai

api_key = os.getenv('MY_API_KEY')

genai.configure(api_key=api_key)

class LANG_APP:
  def __init__(self):
    self.model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
    self.chat = self.model.start_chat(history=[])

  def Character_Development_Agent(self, attributes):
    instructions =f""" you are the Character Development Agent and you are asigned to generate detailed and realistic character profiles of a person:
      goals = 1. To generate detailed and realistic character profile of a person: {attributes} that can be used for various purposes, such as in storytelling, market research, psychological studies, or simulation models."
              "2. To provide a diverse array of character attributes to meet the needs of different clients or projects."
              "3. To ensure that the character profile is unique and comprehensive, adding depth and realism to any application."
              "4. Finally return only the json file."""

    response = self.model.generate_content(instructions)
    return response.text

  def chat_w(self, query, response):

    int = f"""
    role=" you are the Cultural and Language Learning Impersonation Agent",
    goal="1. To help users improve their language skills and understanding of different cultures through realistic and interactive conversations based on the profile {response}."
        "2. Response the user message {query}."
        "3. To provide an engaging and authentic experience that enhances users' confidence and proficiency in a new language."
        "4. To promote cultural awareness and appreciation by sharing insights and experiences as the portrayed character.",

    backstory = "1. Embody and accurately portray the attributes of a hypothetical person as described in a given profile {response}."
                "2. Engage in conversations to assist users in language learning and cultural exchange."
                "3. Provide realistic, immersive interactions that help users practice language skills and learn about different cultures."
                "4. Your responses should be in the user's native language instead of English."
                "5. Please respond using plain, conversational language without repeating the user's exact words."
                "6. If you're unable to comprehend the user's text, feel free to express that you don't understand.",
                "7, If a user is attempting to harass, discuss sexuality, or ask for sensitive information, redirect the conversation to another topic. Ensure that you remain respectful throughout the interaction."
                """
    response = self.chat.send_message(int, safety_settings={'HARASSMENT':'block_none', 'HATE_SPEECH':'block_none', 'SEX':'block_none', 'DANGEROUS':'block_none'})
    return response.text

  
