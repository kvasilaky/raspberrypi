import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.create_table(
    TableName='DAILYWATER',
    KeySchema=[
        {
            'AttributeName': 'FIELD1',
            'KeyType': 'RANGE'  #Partition key, (primary key)
        },
        {
            'AttributeName': 'LEVEL',
            'KeyType': 'RANGE'  #Sort key, (how entries are sorted)
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'FIELD1',
            'AttributeType': 'S' #made this a string so i can use the date as unique id
        },
        {
            'AttributeName': 'LEVEL',
            'AttributeType': 'N'
        }

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)   