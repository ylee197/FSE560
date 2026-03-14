# Project 4 - Image classifier with MobileNetV2

1. MobileNetV2
MobileNetV2 is a lightweight, 53-layer convolutional neural network designed for mobile and embedded vision application. Pretrained on the ImageNet dataset( 1,000+ classes), it provides fast speed and high efficiency in transfer learning, feature extraction, and image classfication. 

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
 > uv add cv2 numpy streamlit tensorflow PIL

 9) Run the code again with the following line:
 > uv run streamlit run main.py

 10) It may ask your email address for the first time to use streamlit. Please enter your email address. 
 
 11) You can see the program is running on a window