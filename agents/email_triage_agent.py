# os reads environment variables from the operating system.
# We use it to get the Groq API key without writing the key directly in the code.
import os
import json
from groq import Groq # groq client used to communicate with the cloud AI model.

# Create the Groq client.
# The API key is taken from the terminal environment.
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

def analyze_email(email_text):
    """
    Analyze an email for phishing and social engineering indicators.
    """

    # The f before the triple quotes allows to insert
    # the value of email_text into the prompt using {email_text}.
    prompt = f"""
You are a phishing email triage agent.

Analyze the email below.

Return ONLY valid JSON with exactly these fields:

{{
  "urgency": true or false,
  "threat": true or false,
  "credential_request": true or false,
  "financial_request": true or false,
  "sensitive_data_request": true or false,
  "possible_impersonation": true or false,
  "social_engineering_techniques": [],
  "preliminary_risk": "low", "medium", or "high",
  "explanation": []
}}

Do not evaluate whether any URL or domain is malicious, legitimate, official,
or suspicious. URL and domain analysis belongs to another agent.

Email:
{email_text}
"""

    # Send the email analysis request to the cloud model.
    response = client.chat.completions.create(
        model="qwen/qwen3.8-27b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        response_format={
            "type": "json_object"
        },
    )

    # Get the model's response text.
    content = response.choices[0].message.content

    # Convert JSON text into a Python dictionary.
    return json.loads(content)


# Temporary test.
if __name__ == "__main__":
    result = analyze_email(
        "Your account will be suspended. Verify your password immediately."
    )

    print(result)