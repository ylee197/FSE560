# Project 6 - AI Resume Critiquer(chatGPU API needs)

1. Program
This program analize your resume. When you upload your resume with pdf version, it analises your resume and returns the result. This program used gpt-4o-mini model.   

2. Preparing the environment
1) Install Visual Studio Code
To run this python code, I recommended to install visual code. Please download a correct version of visual code from the following link and install it. -  https://code.visualstudio.com/download

2) Start the Visual Code
Starting the Visual Code and open your project directory. 

3) Install UV package
UV is a python package to run the python program easily. We will use UV to run programs. 
After open your project directory in Visual code, open terminal. 
You can open the terminal with the following way:
    i) At the top of the screen there is [Terminal] tab on the manu bar.
    ii) Select [Terminal] - [New Terminal]
    iii) You can see the terminal at the bottom of your Visual code window
    iv) In the terminal, please enter "pip3 install uv" or "pip install uv"
    v) You can see UV package is instlled.

4) Start UV
In ther terminal, type "uv init"
 > uv init

5) UV environment is started
You can see the uv environment is started. You can see the multiple files are created and one vertual environment is created. 

6) Copy and past the program code to main.py and save it.

7) Run the code
 > uv run main.py

8) Install necessary libraries
When you run the code, you can see an error. It says that some libraries are missing. You need to install the libraries. Please type and enter the below line:
 > uv add streamlit PyPDF2 openai pyhton-dotenv

9) Run the code again
 > uv run main.py

 10) If the program does not have any error, it shows that you do not have ChatGPT API. You need to save the Chat GPT API. Please create a file with name '.env'. Save a ChatGPT API in this file. 

 11) Run the code again with the following line:
 > uv run streamlit run main.py

 12) It may ask your email address for the first time to use streamlit. Please enter your email address. 
 
 13) You can see the program is running on a window