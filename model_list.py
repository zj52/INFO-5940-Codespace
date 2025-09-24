from openai import OpenAI
import os

client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.ai.it.cornell.edu/v1"),
    api_key=os.getenv("OPENAI_API_KEY")
)

models = client.models.list()
for m in models.data:
    print(m.id)