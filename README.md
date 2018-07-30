# Python-Speedtest

This program can give you an idea as to what your current internet download speed is using fast.com. The program is written in pure python and will open a headless chromium browser which will then connect to fast.com. Then it will scrape the webpage for the download speed computed by fast.com. This will repeat three time over the course of about 30 seconds and average them to get a more accurate reading.


## Versions and Setup

There are currently two versions of this program. Both compute the download speed the same but one stores the values in a CSV for easy graphing and analysis while the other simply returns the computed value if you have a separate application you want to handle them.

As far as setup goes it is pretty straight forward. Simply select the version below you want to setup on your system and follow the instructions. Unfortunately, there is currently only one automated and tested way to set this up and that is on Linux or MacOS. 

## Setup instructions for CSV stored version
This version is for those that just want to run this application on its own and includes a simple bash script to automate running it on a schedule.

INSTRUCTIONS TO BE PROVIDED

## Setup instructions for the stripped down version
This version is stripped down and simply calculated your download speed and returns the value in the form of an integer.

