from dotenv import load_dotenv 
from langchain.document_loaders import WebBaseLoader
import streamlit as st 
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
#loads the .env file that contains the OPENAI_api key
# load_dotenv()

def main():
    st.set_page_config(page_title="👨‍💻 Lead Generation")
    st.title("👨‍💻 Send Email To Your Client")
    st.write("Please insert your link.")
    url = st.text_input("Insert The link")
    name = st.text_input("Inser The name")
    if st.button("Submit Query", type="primary"):
        # Load data from the specified URL
        loader = WebBaseLoader(url)
        data = loader.load()
        chat = OpenAI(openai_api_key="", model_name="text-davinci-003", temperature=0.3)
        chain = load_qa_chain(chat, chain_type="stuff")
        
        # Your main query to the language model - modify to your needs
        #.format name adds the name to the {} within the query that we are giving to the language model
        q = """
        Formulate a short 5-8 line email to {} pitching lead generation for his agency. The email should 
        make a reference to his work and give him a compliment.""".format(name)
        
        # The personalized email or paragraph you can send to Lemlist
        email = chain.run(input_documents=data, question=q)
        st.write(email)
#calls the main function if it exists
if __name__ == '__main__':
    main()
