from scraper import func
from google import genai

f = open("geminiAPI.txt", "r")
apikey = f.read()
f.close()

input_prompt="Explain how AI works"

print(func())
# client = genai.Client(api_key=apikey)
# response = client.models.generate_content(
#     model="gemini-2.0-flash", contents=input_prompt
# )
# print(response.text)
