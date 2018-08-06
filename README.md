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

### Download chromedriver
Go to the following link and download the version that matches you Operating System. 

[ChromeDriver](https://chromedriver.storage.googleapis.com/index.html?path=2.41/)

Choose a directory to store the chrome driver, preferably one that is already in your PATH like `/bin/`.

If the directory is not in your PATH then you will need to add it with `export PATH=$PATH;My/Directory`. Note that for Windows users you will need to add it to your PATH manually.

### Setting up Python and Pip
If you already have Python 3.6 or greater and pip for Python 3 then skip this step.

If not then either 
Ubuntu Linux: `sudo apt-get install Python3`
Mac with HomeBrew: `brew install Python3`
or visit [Python.org](https://www.python.org/) for more options.

To check if you have Python and pip installed and that they are the correct version:
`python -v`
`pip -v`

If you have multiple versions of Python on your system then you may need to run:
`python3 -v`
`pip3 -v`

### Installing Python Dependecies
The speedtest program requires Selenium and BeautifulSoup4.

To install these, simply run:
`pip install beautifulsoup4 selenium`

### Testing the program

Clone this repository `git clone https://www.python.org/` .

Run `python speedtest-lite.py`.

You should get a few messages printed to the screen and at the end your current download speed should be printed to the console.



