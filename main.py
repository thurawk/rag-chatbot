from src.rag_chatbot.pipeline import build_chatbot

def main():
    chatbot = build_chatbot()
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            break
        result = chatbot(query)
        print("\nBot:", result["result"])
        print("Sources:", [doc.metadata.get("source") for doc in result["source_documents"]])
        print("-" * 50)

if __name__ == "__main__":
    main()
