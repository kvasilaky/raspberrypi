# raspberrypi

Follow the instructions to assemble a raspberry pi water sensor that pushes values to a AWS Dynamo DB. 

For overall instructions use: raspberry.pptx

For detailed instructions follow:
-PartI_Hardware.txt + wiring.pdf
-PARTII_SettingUpYourPi.txt
-PartIII_AWSnEC2.txt



Directory structure
_____________________________________________________________________________
├── .gitignore              # So that we don't commit environment passwords
├── table.py        		# Creates the table in the Dynamo db database
├── raspberrypi.pem        	# Credentials needed to sign in to AWS
├── credentials.csv  		# Stores your AWS keys 
├── onmypi/                # Files that should be on your pi
│   ├── upload.py        	# Pushes sensor readings to AWS
│   ├── Adafruit_Python_MCP3008/examples  # Adafruit package to read sensor 
│   │   ├── simpletest.py     # Test pgsql
_____________________________________________________________________________



AnotherForm_deployed
├── .gitignore              # So that we don't commit compiled files or our environment passwords
├── Procfile                # Use the Procfile to tell Heroku how to run various pieces of your app
├── .env                    # So that we don't commit compiled files or our environment passwords
├── README.md               # This will be how to test/run the app & have basic info
├── requirements.txt        # These are the dependencies that you need to install for the app to run
├── runtime.txt        	  # Tells Heroku to run in python 3.5.2
├── run.py  				  # Runs the app!
├── test.csv                # sample csv to load
├──  Form/                  # Everything our app includes is inside this folder
│   ├──  __init__.py        # App-wide setup. Called by `run.py`
│   ├──  config.py          # Configuration Files. i.e. Login related things. Pulls from .env
│   ├──  views.py           # All the view routes
│   ├──  database_helper.py # All the view routes
│   ├──  setup.py           # Folder for any data we might want to use
│   ├──  templates/         # HTML files go here
│   │   ├──  index.html     # JavaScript & HTML
│   ├──  scripts/           # Postgres database creation scripts 
│   │   ├──  test.pgsql     # Test pgsql