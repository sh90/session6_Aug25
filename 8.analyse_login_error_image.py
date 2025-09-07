import openai
import base64
import os

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") # Replace this with your open ai key "SK-"
openai.api_key = OPENAI_API_KEY

# Step 2: Load and encode the image
image_path = "login_error.png"  # Your local image file
with open(image_path, "rb") as f:
    image_bytes = f.read()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

data_url = f"data:image/png;base64,{image_base64}"

# Step 3: Send to GPT-4o with a prompt
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Analyze this image for any login errors or issues. Respond only in one line"},
                {"type": "image_url", "image_url": {"url": data_url}}
            ]
        }
    ],
    temperature=0,
    max_tokens=1000,

)

# Step 4: Print the result
print(response.choices[0].message.content)
