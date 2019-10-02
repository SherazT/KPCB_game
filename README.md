# KPCB_game

<b>MAC Instructions:</b> 

`pip install -r requirements.txt` \
`python Memory_Match.py`

<b>For macOS greater than Mojave 10.14.6 - there are some compatibly issues with one of the libaries in the program and as such you must use Python3.6. Instructions are below:</b>

If you don't have Python3.6 installed, please use the following to install.\
`brew unlink python`\
`brew install --ignore-dependencies https://raw.githubusercontent.com/Homebrew/homebrew-core/f2a764ef944b1080be64bd88dca9a1d80130c558/Formula/python.rb`

Follow the steps below to create a virtual environment and run the program.\
`virtualenv venv --python=python3.6`\
`source venv/bin/activate`\
`pip install -r requirements.txt`\
`python3.6 Memory_Match.py`

<b>Linux/Ubuntu Instructions: </b> \
`pip install -r requirements.txt` \
`python Memory_Match.py`
