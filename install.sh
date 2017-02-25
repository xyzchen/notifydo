#!/bin/bash

#copy file to /usr/local/bin/
cp notify.py /usr/local/bin/
cp notifydo /usr/local/bin/

#setup config
echo "{" > ~/notify_config.json
echo "\"bot_token\":\"$1\"," >> ~/notify_config.json
echo "\"chat_id\":\"$2\""  >> ~/notify_config.json
echo "}" >> ~/notify_config.json
