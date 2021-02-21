import slack
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path.name)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

client.chat_postMessage(channel='#slack-integration',text="Your Slack CICD Pipeline Job is finished")
