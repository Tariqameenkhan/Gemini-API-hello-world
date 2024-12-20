# first agentic ai
!pip install google-generativeai

!pip install -q -U google-generativeai

import google.generativeai as genai
from google.colab import userdata
google_api_key=userdata.get('google_api_key')
genai.configure(api_key=google_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how comp")
print(response.text)

# Images open in colab and ask question to ai

!curl -o image.jpg "https://storage.googleapis.com/generativeai-downloads/images/jetpack.jpg"

import PIL.Image
img = PIL.Image.open('image.jpg')
img

prompt = """This image contains a sketch of a potential product along with some notes.
Given the product sketch, describe the product as thoroughly as possible based on what you
see in the image, making sure to note all of the product features. Return output in json format:
{description: description, features: [feature1, feature2, feature3, etc]}"""

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content([prompt, img])
print(response.text)

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

response = chat.send_message("In one sentence, explain how a computer works to a young child.")
print(response.text)

print(chat.history)

model = genai.GenerativeModel(
    'gemini-1.5-flash',
    generation_config=genai.GenerationConfig(
        max_output_tokens=200,
        temperature=0.9,
    ))

response = model.generate_content(
    'Give me a numbered list of car',
    # Limit to 5 facts.
    generation_config = genai.GenerationConfig(stop_sequences=['\n6'])
)

print(response.text)