import os
import langchain
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.environ.get("OPENAI_API_KEY")

# Retrieve the API key from the environment variable


train_data = "example_data.csv"

def predict_stock(open_price, high_price, low_price, volume):
    llm = OpenAI(api_key=openai_api_key, temperature=0)
    agent = create_csv_agent(llm, train_data, verbose=True)

    input_string = "Train and read the csv file and predict the future price of a stock based on Open Price: {}, High Price: {}, Low Price: {}, and Volume: {} if the values are in dataset, if not then predict a value learned from the data"
    
    input_string = input_string.format(open_price, high_price, low_price, volume)
    
    prediction = agent.run(input_string)
    return prediction


