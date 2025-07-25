import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv

def main():
    load_dotenv()
        
#    args = sys.argv
#    if len(sys.argv) < 2:
    
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    
    if not args:
        print("AI Program Asisstance")
        print('Usage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a deck?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")
    
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

#   if "--verbose" in user_prompt:
#       return generate_content_verbose(client, messages)
#   return generate_content(client, messages)

    generate_content_verbose(client, messages, verbose)

def generate_content_verbose(client, messages, verbose):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
    )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
