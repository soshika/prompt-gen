from pg_sdk import GPTPromptGeneratorSDK
import os

if __name__ == '__main__':
    print(os.environ.get('OPENAI_API_KEY'))
    sdk = GPTPromptGeneratorSDK('what is marijuana ?')
    # response = sdk.generate_qa()
    # print(response)