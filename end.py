# Filename:: end.py
# Author:: Archit Kalra
# Email:: archit.kalra@gmail.com

#importing rquired modules
import slack
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path.name) #loading the virtual pyenv

client = slack.WebClient(token=os.environ['SLACK_TOKEN']) #initiating the slack weblist, SLACK_TOKEN is an env variable on jenkins instance.

client.chat_postMessage(channel='#slack-integration',text="Your Slack CICD Pipeline Job is finished") #Posting SLACK message
