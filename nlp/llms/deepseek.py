from openai import OpenAI
import llms.llm_key


def get_respones(question, api_company="deepseek"):
    if api_company == "deepseek":
        client = OpenAI(
            api_key=llms.llm_key.deepseek_key, base_url="https://api.deepseek.com"
        )
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": question},
            ],
            stream=False,
        )
        return response.choices[0].message.content
