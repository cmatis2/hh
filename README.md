

### Requirements
```
	Python 3.9.2
	- pyrcon (included)
	- discord.py
	- numpy
	- time
	- json
	- requests
	FXServer
	ESX 1.1 and older
```



### Installation

```
Make sure you have Python 3.9.2 installed to PATH

1. Open Command Prompt
2. Enter the following in order
	pip install discord
	pip install json
	pip install requests
	pip install numpy
	pip install string
	pip install time
3. Add script to your resources and server.cfg
4. Add your settings into config.lua (script) and config.json (python) -- Config settings will be displayed in the next section
5. Run the bot with run.bat
```

### Config (FiveM)

```lua
Config = {}

Config.ReviveEvent = 'esx_ambulancejob:revive' -- The event used to revive people (default: esx_ambulancejob:revive)
				
--Webhook settings
Config.Webhook = 'yourwebhookhere' -- Reports error messages in commands
Config.WebhookTitle = 'Liberty RP' -- Title for webhook
Config.WebhookFooter = 'made by Melktert' -- Footer of webhook
--Embed colors
Config.Success = 3145631 --
Config.Error = 16711680 -- https://www.mathsisfun.com/hexadecimal-decimal-colors.html (decimal colors)
Config.Neutral = 9606296 -- 
		
```
## Config (Python)
```lua
{
    "general":{
        "servername": "yourservername", -- Server name that will be displayed on embeds
        "website": "yourwebsite", -- Website displayed in footer
        "maxclients": 64, -- Max clients your sevrer is running
        "logourl": "yourserverlogo.png" -- Logo that will be displayed in embeds
    },
    "discord":{
        "token":"yourbottoken", -- Bot token (https://discord.com/developers/applications)
        "cmd_channel": 843744030343954432, -- Only channel that will accept commands
        "role":"Admin", -- Role that can use commands
        "prefix":"=", -- Bot Prefix
    },
    "rcon":{
        "host":"serverip", -- Your server ip
        "password":"rconpassword", -- Server rconpassword
        "port":"30120" -- FiveM port (default 30120)
    }
}```

