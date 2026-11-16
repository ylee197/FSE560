# Project 7 - Stock Price Prediction

## 1. Program
This program predicting next 5 days stock price. Using LSTM sequential model, this program predicting next 5 days stock price. Please enter stock code such as AAPL, QQQ and NVDA, then it shows its predictions.   

## 2. Preparing the environment
### 1) Install Visual Studio Code
To run this python code, I recommended to install visual code. Please download a correct version of visual code from the following link and install it. -  https://code.visualstudio.com/download

### 2) Start the Visual Code
Starting the Visual Code and open your project directory. 

### 3) Creating a Virtual Environment(Optional)
Virtual Environment makes your python work much easier. 
After open your project directory in Visual code, open terminal. 
You can open the terminal with the following way:
    i) At the top of the screen there is [Terminal] tab on the manu bar.
    ii) Select [Terminal] - [New Terminal]
    iii) You can see the terminal at the bottom of your Visual code window
    iv) In the terminal, enter the following comment and creating a virtual environment(Choose your environment name and enter at MYENV):
    > `conda create --name MYENV python=3.12 numpy pandas` 

### 4) Activate your Virtual Environment
> `conda activate MYENV`

## 3. Run your program
### 1) Copy and past the program code to main.py and save it.

### 2) Run the code
 > `streamlit run app.py`

### 3) Install necessary libraries
When you run the code, you can see an error. It says that some libraries are missing. You need to install the libraries. Please type and enter the below line:
 > `pip install streamlit keras datetime matplotlib yfinance tensorflow `

### 4) Run the code again. If you do not have any errors, you can move forward.
### 5) You can see the results at the web browser
### 6) You can finish your program with `ctrl + c`



