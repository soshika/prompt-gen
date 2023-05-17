from pg_sdk import GPTPromptGeneratorSDK

if __name__ == '__main__':
    sdk = GPTPromptGeneratorSDK('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', 'what is marijuana ?')
    response = sdk.generate_qa()
    print(response)