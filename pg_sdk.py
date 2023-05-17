import openai


class GPTPromptGeneratorSDK:

    api_key = str()
    question = str()

    def __init__(self, api_key, question):
        self.api_key = api_key
        self.question = question

    def generate_qa(self):
        openai.api_key = self.api_key
        response = openai.Completion.create(
            engine="text-davinci-003",  # Choose the most suitable engine
            prompt=f"{self.question}\n\nGenerate questions:",
            temperature=0.5,
            max_tokens=256
        )

        return response.choices[0].text.strip()
