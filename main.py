#https://webkul.com/blog/python-soap-clients-with-zeep/
#https://python-zeep.readthedocs.io/en/latest/transport.html#debugging


from zeep import Client,Settings
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport
# from zeep.plugins import HistoryPlugin
# from lxml import etree
import xml.etree.ElementTree as ET
from zeep.wsdl.utils import etree_to_string

# from zeep import Plugin
from zeep.exceptions import Fault, TransportError, XMLSyntaxError

# class MyLoggingPlugin(Plugin):
# 
#     def ingress(self, envelope, http_headers, operation):
#         print(etree.tostring(envelope, pretty_print=True))
#         return envelope, http_headers
# 
#     def egress(self, envelope, http_headers, operation, binding_options):
#         print(etree.tostring(envelope, pretty_print=True))
#         return envelope, http_headers
    
#python -m zeep "https://api.plexonline.com/DataSource/Service.asmx?WSDL"
wsdl = "https://api.plexonline.com/DataSource/Service.asmx?WSDL"
session = Session()
session.auth = HTTPBasicAuth('BuscheAvillaKorsws@plex.com', '5b11b45-f59f-')
settings = Settings(strict=False)
# settings = Settings(strict=False, raw_response=True)
# history = HistoryPlugin()
# client = Client(
#     'http://examples.python-zeep.org/basic.wsdl',
#     plugins=[history])
# client.service.DoSomething()
# 
# print(history.last_sent)
# print(history.last_received)

#An additional argument 'transport' is passed with the authentication details
# client = Client(wsdl, plugins=[MyLoggingPlugin],transport=Transport(session=session),settings=settings)
client = Client(wsdl, transport=Transport(session=session),settings=settings)

# try:

    
request_data = {
    'ExecuteDataSourceRequest':{
        'DataSourceKey':"2272",
        'InputParameters': {
            'InputParameter': {
                'Name':'Workcenter_Key',
                'Value':'61324',
                'Required':'false',
                'Output':'false'
            }
        }
    }
}


# node=client.create_message(client.service, 'ExecuteDataSource',**request_data2)
node=client.create_message(client.service, 'ExecuteDataSource',**request_data)
tree = ET.ElementTree(node)
# etree_to_string(tree).de.decode()
tree.write('test2.xml')
#     client.service.ExecuteDataSource(**request_data2)
# except Fault as error:
#     print(ET.tostring(error.detail))
# print(history.last_received)

response = client.service.ExecuteDataSource(**request_data)
# dsn = response.get('DataSourceName')
dsn=response['DataSourceName']
print(dsn)


#Here 'request_data' is the request parameter dictionary.
#Assuming that the operation named 'sendData' is defined in the passed wsdl.