import telebot
import openai
import os

# Set up the Telegram bot using your bot token
bot = telebot.TeleBot('TOKEN')

# Set up OpenAI API using your API key
openai.api_key = 'TOKEN'

# Define a function to process user input and get the OpenAI API response
def process_input(input_text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_text,
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Get the generated response text from the OpenAI API response
    response_text = response.choices[0].text.strip()
    return response_text

# Define a handler function for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi there! I'm an AI chatbot. What can I help you with today?")

# Define a handler function for any other user messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Get the user's input text
    input_text = message.text

    # Get the OpenAI API response for the user's input
    response_text = process_input(input_text)

    # Send the response back to the user
    bot.reply_to(message, response_text)

# Start
bot.polling()




