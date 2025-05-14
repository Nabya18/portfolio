# Discord Bot

## Create Application
1. Go to the Discord Developer Portal
https://discord.com/developers/applications
2. Click on "New Application"
3. Name your application and click "Create"
4. Go to the "Bot" tab on the left sidebar


### Authorization Flow
1. Public bot
2. Server Members Intent
3. Message Content Intent


### OAuth2 URL Generator
1. Go to the "OAuth2" tab on the left sidebar
2. Select "bot"
3. Select General Permissions
   - Manage Roles
   - View Channels
4. Select Text Permissions
   - Send Messages
   - Create Public Threads
   - Read Messages in Threads
   - Manage Messages
   - Manage Threads
   - Embed Links
   - Attach Files
   - Read Message History
   - Use External Emojis
   - Add Reactions
   - Create Polls
5. Copy the generated URL and paste it into your browser
6. Select the server you want to add the bot to and click "Authorize"
7. Running Python script to make the bot online

## Make environment and Install requirements
```
# Create a virtual environment
python -m venv env

# Activate the virtual environment
source env/bin/activate    #Linux/Mac
env\Scripts\activate       #Windows

# Install the required packages
pip install -r requirements.txt
```

## Running the Bot


