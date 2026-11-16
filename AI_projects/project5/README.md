# Project 5 - Chatbot and AI agent(ChatGPT API needs)

There are two program file
* Chatbot_pretrained.ipynb -  Pretrained chatBot. This one used facebook/blenderbot model. 
* test.py - Question answering bot. 
* main.py - AI ChatBot
To run main.py, you need to use Visual code and UV package. The instruction is as follows:

## 1. Preparing the environment
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
    v) You can see UV package is instlled.

4) Activate your Virtual Environment
> `conda activate MYENV`

## 2. Run your program
### 1) Copy and past the program code to main.py and test.py and save it.

### 2) Run the code
 > python main.py
 > python test.py

### 3) Install necessary libraries
When you run the code, you can see an error. It says that some libraries are missing. You need to install the libraries. Please type and enter the below line:
 > `pip install langgraph langchain python-dotenv langchain-openai`

### 4) Run the code again. If you do not have any errors, you can move forward.

### 5) Copy shell script files. Copy run.sh and test_run.sh
### 6) Make shell script files to executable
> `chmod +x run.sh`
> `chmod +x test_run.sh` 
 
### 7) Run the code again with the following line:
> `./run.sh`
> `./test_run.sh`
 
### 8) You can see the results at the terminal
### 9) You can finish your program with `exit`