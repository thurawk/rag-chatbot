import streamlit as st
from rag_chatbot.pipeline import build_chatbot

def main():
    st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")
    st.title("🤖 RAG Chatbot")
    st.markdown("Ask questions about your documents!")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Load chatbot once
    if "chatbot" not in st.session_state:
        with st.spinner("Loading knowledge base..."):
            try:
                st.session_state.chatbot = build_chatbot()
                st.success("Ready!")
            except Exception as e:
                st.error(f"Failed to load knowledge base: {e}")
                st.stop()

    if prompt := st.chat_input("What is your question?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = st.session_state.chatbot.invoke(prompt)
                    answer = response["result"]
                    sources = [doc.metadata.get("source", "Unknown") for doc in response.get("source_documents", [])]
                    
                    st.markdown(answer)
                    if sources:
                        st.markdown(f"\n\n*Sources: {', '.join(set(sources))}*")
                        
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error(f"Error generating response: {e}")

if __name__ == "__main__":
    main()
