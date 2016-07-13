# halo5quickstats

Created by Josiah Philipsen on 7/12/2016. Thank you for using this file and I hope that it helps you track stats
for your Halo 5 games easily. If you find any changes or updates please submit a pull requst and help build this. I
create this project for a member in the Halo Community to be able to track stats on people, however if you feel the
need to use it please feel free. I only ask that you give me a shout out somewhere in your project and let me know on
twitter @lazerhawk05.


# To use

Update the config.py file to track the stats, gametype and spartans that you want and insert your API key in Modules/Stats.py

## Instructions are for Ubuntu.

sudo apt-get install python python3 python3-dev python3-pip
mkdir stats
cd stats

### now you will want to clone the git repsoitory to this folder and for this README we will call that folder quickstats

sudo pip3 install -r requirements.txt

### make a cron job for the cron.py file
sudo crontab -e

### add this line to the bottom this will run every day on the 20th hour of the day.
0 20 * * * * /usr/bin/python3 /path/to/file/cron.py

### optionally add the report.py if you want to create a report everynight. Please note it will overwrite the existing file
15 20 * * * * /usr/bin/python3 /path/to/file/report.py



Remember if you have any questions or need anything you can find me on twitter @lazerhawk05 or submit a pull request
to get something changed.

Enjoy!!





