from databricks.sdk import WorkspaceClient
from databricks.sdk.service.serving import ChatMessage, ChatMessageRole

# Connect to Databricks
w = WorkspaceClient()

# Simple chatbot function
def chatbot():
    print("Simple AI Chatbot")
    print("Type 'help' for capabilities")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        # Handle empty input
        if user_input.strip() == "":
            print("Bot: Please enter a valid message.\n")
            continue

        # Exit command
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        # Help command
        if user_input.lower() == "help":
            print("\nCapabilities:")
            print("- Answer questions")
            print("- Have conversations")
            print("- AI generated responses")
            print("- Handles invalid input\n")
            continue

        try:
            
            response = w.serving_endpoints.query(
                name="databricks-meta-llama-3-3-70b-instruct",
                messages=[
                    ChatMessage(
                        role=ChatMessageRole.USER,
                        content=user_input
                    )
                ]
            )

            
            answer = response.choices[0].message.content
            print(f"Bot: {answer}\n")

        except Exception as e:
            print(f"Bot Error: {e}\n")

# Run chatbot
chatbot()

