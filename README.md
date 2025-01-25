# Browser Use
Command line code to run BrowserUse, using the DeepSeek API.

### Set Up
Create a .env file and type OPENAI_API_KEY=KEY, where KEY is your DeepSeek API key.

Make sure you have Python 3.11 installed on your computer, and that it is installed to PATH.

After installing Python, make a virtual environment, and install all the neccecssary packages using `pip install -r requirements.txt`

### Running
To run, type `python agent.py --task "YOUR_TASK_HERE"`.

The agent will attempt to complete your task through the web browser. As it does this, certain information will be logged, and the final result at the end.
