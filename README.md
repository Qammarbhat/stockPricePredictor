# Stock Price Predictor

## Overview

The Stock Price Predictor is a web application that predicts future stock prices based on historical data. It utilizes the OpenAI GPT-3 language model and Streamlit for the user interface.

## Table of Contents

- [Demo](#demo)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Demo

You can try the app live at [Demo Link](https://stockpricepredictorapp.streamlit.app/).

## Files

- `main.py`: This is the main file that runs the Streamlit application. It creates input fields for Open Price, High Price, Low Price, and Volume. When the "Predict" button is clicked, it calls the `predict_stock` function from `prediction.py` to predict the future price of the stock.

- `prediction.py`: This file contains the `predict_stock` function. It uses the OpenAI API to train a model on a CSV file (`example_data.csv`) and predict the future price of a stock based on the provided Open Price, High Price, Low Price, and Volume.

- `requirements.txt`: This file lists all the Python dependencies that need to be installed for this application to run.

## Getting Started

### Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python (3.7+ recommended)
- pip (Python package manager)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/stock-price-predictor.git
2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt

3. Run the Streamlit application:
    ```bash
    streamlit run main.py