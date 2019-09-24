#https://webkul.com/blog/python-soap-clients-with-zeep/
from zeep import Client
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport

wsdl = "https://api.plexonline.com/DataSource/Service.asmx?WSDL"
session = Session()
session.auth = HTTPBasicAuth('BuscheAvillaKorsws@plex.com', '5b11b45-f59f-')

#An additional argument 'transport' is passed with the authentication details
client = Client(wsdl, transport=Transport(session=session))
#<dat:Name>Workcenter_Key</dat:Name>
#<dat:Value>61324</dat:Value>

request_data = {
    'ExecuteDataSourceRequest':{
        'DataSourceKey':'2272',
        'InputParameters':{
            'InputParameter':{
                'Workcenter_Key': '61324'
            }
        }
    }
}

response = client.service.ExecuteDataSource(**request_data)
dsn=response['DataSourceName']
print(dsn)


#Here 'request_data' is the request parameter dictionary.
#Assuming that the operation named 'sendData' is defined in the passed wsdl.