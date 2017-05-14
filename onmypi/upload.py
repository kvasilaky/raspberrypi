#!/usr/bin/sudo python

import boto3
import json
import decimal
import time
import datetime
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import random

#access the database
dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id="AKIAIHXXXXMTT5HEONVA",
                          aws_secret_access_key="makiXXXXLdzGXMoq/V5bYyS+rXXXepx2kQvCW/3G",
                          region_name="us-east-1")

#This is not working because it can't find the aws credentials so I'm hardcoding them in above
#dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('DAILYWATER')


#put the code to print water levels here
# Hardware SPI configuration (taken from pi@raspberrypi:~/Adafruit_Python_MCP3008/examples/simpletest.py)
SPI_PORT   = 0
SPI_DEVICE = 1
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
#test the water level out
m = mcp.read_adc(5)

#put the code for a timestamp here
ts = time.time()
field1 = format(ts, ".15g")
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

field = random.randrange(10, 25, 5)
#in the cron job runs scraper to get rainfall.json
#we should have already run the table.py to create a table called DAILYWATER which had Keys FIELD1 and TIME, LEV$
#because we don't have distict or rain keys, dynamodb will add them in (unlike with a ER db)

table.put_item(
Item={
        'FIELD1':field1,
        'LEVEL': m,
        'TIME': st,
}
)

#This part will email you the water level, stored in m 
import smtplib
#You might have to allow less secure apps
#https://myaccount.google.com/lesssecureapps?pli=1
fromaddr = 'from@gmail.com'
toaddrs  = 'to@gmail.com'

msg = 'Be calm. The water level is at' + " " + str(m)

# Credentials (if needed)
username = 'myusername'
password = 'email_password'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

