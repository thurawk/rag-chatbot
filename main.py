from src.rag_chatbot.pipeline import build_chatbot

def main():
    print("Starting Chatbot...")
    try:
        chatbot = build_chatbot()
        print("Chatbot ready! Type 'exit' or 'quit' to stop.")
    except Exception as e:
        print(f"Error initializing chatbot: {e}")
        return

    while True:
        try:
            query = input("You: ")
            if query.lower() in {"exit", "quit"}:
                break
            
            print("Thinking...")
            result = chatbot.invoke(query)

            print("\nBot:", result["result"])
            print(
                "Sources:",
                list(set([doc.metadata.get("source", "Unknown") for doc in result.get("source_documents", [])]))
            )
            print("-" * 50)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
