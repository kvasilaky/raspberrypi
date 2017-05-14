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
├──  onmypi/                # Files that should be on your pi
│   ├──  upload.py        	# Pushes sensor readings to AWS
│   ├──  Adafruit_Python_MCP3008/examples  # Adafruit package to read sensor 
│   │   ├──  simpletest.py     # Test pgsql
_____________________________________________________________________________