import os
import openai

# openai.api_key = os.getenv("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")
openai.api_key = "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"
os.environ["http_proxy"] = "http://127.0.0.1:1087"
os.environ["https_proxy"] = "http://127.0.0.1:1087"


# openai.proxy =  {'http': "http://127.0.0.1:1087",'https': "http://127.0.0.1:1087"}


# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Summarize apple patent US20200410738A1",
#   temperature=0.7,
#   max_tokens=64,
#   top_p=1.0,
#   frequency_penalty=0.0,
#   presence_penalty=0.0
# )
# list models
# completion = openai.Completion.create(model="ada", prompt="Hello world")
# print(completion.choices[0].text)

# completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world!"}])
# print(completion.choices[0].message.content)
response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

print(image_url)