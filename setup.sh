echo "Starting..."

# Install dependencies
apt-get install -y wget

apt-get install -y unzip

apt-get install -y python3

apt-get install -y python3-pip

# Install Python Dependencies
pip install selenium

# Change to Downloads directory
cd ~/Downloads

# Download chromedriver, the headless web browser
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip

# Unzip chromedriver
unzip chromedriver_linux64.zip

# Add Downloads to the PATH so that the python program can access chromedriver
# Make PATH equal itself + ~/Downloads
export PATH=$PATH;~/Downloads

echo "Complete!"
