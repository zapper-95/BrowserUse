# Browser Use
Wrapper code to run BrowserUse in the terminal, using o4 mini.

### Set Up
Create a .env file and type `OPENAI_API_KEY=KEY`, where `KEY` is your OpenAI API key.

Make sure you have Python 3.11 installed on your computer, and that it is installed to PATH.

It is recommended to use a virtual environment. You can do this with the virtualenv package.

#### Virtual Environment
```bash
pip install virtualenv
```
```bash
virtualenv .venv
source .venv/bin/activate
```

#### Installing the package
Install the following packages to your virtual environment
``` bash
pip install browser-use
sudo playwright install
```

### Running
To run, type `python agent.py --task "YOUR_TASK_HERE"`.

The agent will attempt to complete your task through the web browser. As it does this, certain information will be logged, and the final result at the end.
