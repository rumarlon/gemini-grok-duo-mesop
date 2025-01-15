# gemini-grok-duo-mesop

This repo will help you setup an environment where you can use both Gemini or Grok simultaneously. You can also just each use model individualy.

_Get Started with with Mesop choose : Gemini &/or Grok_

*tl:dr* This is a simple implementation of mesep for Gemini &/or Grok. This is not a production app but rather it provides an opportunity to explore Gemini/Grok capabilities with a local app.  As this app runs locally your API will only be local not submitted or tracked.

The following instructions will help you deploy a Mesop app in a python environment on your Mac, feel free to checkout their docs and other examples [here](https://google.github.io/mesop/).

### Setup requirements as tested:

* MacOS Sequoia (install WSL Ubuntu on linux if necessary)
* Python 3.12.4
* Gemini API Key - Do not commit this in your code or share with others unintetionally. (sign up to get your key [Google AI Studio](https://aistudio.google.com/)
* Grok API Key - Do not commit this in your code or share with others unintetionally. (sign up and get one at [Grok Console](https://console.x.ai/) as of 11/24 you get a free $25 credit monthly until 1/25)

### Step by step:

1) Clone this repo to the directory of your choice
```
git clone https://github.com/rumarlon/gemini-grok-duo-mesop.git
```
2) Create python environment (preferably not in the directory you cloned)
```
python3 -m venv venv
```
3) Activate python environment
```
source venv/bin/activate
```
4) Install requirements
```
pip install -r requirements.txt
```
5) Run your app
   
Text only:
```
mesop main.py
```
6) Copy the url provided in terminal and paste into your favorite browser
7) You will need to input your key(s) in the UI to access the API. The minimum configuration is to add one key. This app is run locally so the key(s) will not be sent anywhere.
![image](https://github.com/rumarlon/gemini-grok-duo-mesop/blob/master/images/mesop_api_01.png)

![image](https://github.com/rumarlon/gemini-grok-duo-mesop/blob/master/images/mesop_api_02.png)


8) Try a user prompt example, "What is the meaning of life, the universe, and everything?"
9) Get creative and test some other user prompts keeping in mind the system prompt currently is "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."

## What to do next?

Go ahead and change the system prompt and see what you can do with Grok. The prompt for Grok is in [claude.py](https://github.com/rumarlon/gemini-grok-duo-mesop/blob/master/claude.py). You should not have to restart to see the changes as mesop automatically reloads. Sky is the limit!

From:
```
system="You are Grok, a chatbot inspired by the Hitchhiker's Guide to the Galaxy.",
```
To:
```
system="Your new awesome prompt goes here.",
```

## Troubleshooting

If you get an API access error make sure you have a valid Gemini API or Grok API key. 
