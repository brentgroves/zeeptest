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
settings = Settings(strict=False, raw_response=True)
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

    
request_data1 = {
'ExecuteDataSourceRequest':{
                'DataSourceKey':"2272",

                'InputParameters':{
                    'InputParameter':{'Name':'Workcenter_Key','Value':'61324'}
                }
            
        }
        }
request_data2 = {
        'ExecuteDataSourceRequest':{
            'InputParameters':{
                'InputParameter':[{
                    'Name':'@PLC_Name',
                    'Value':'CNC103'
                }]
            },
            'DataSourceKey':'7868'
            
        }
}
request_data3 = {
        'ExecuteDataSourceRequest':{
            'InputParameters':{
                'InputParameter':{
                    'Name':'@PLC_Name',
                    'Value':'CNC103'
                }
            },
            'DataSourceKey':'7868'
            
        }
}
request_data4 = {
    'InputParameters':{
        'InputParameter':{
            'Name':'@PLC_Name',
            'Value':'CNC103'
        }
    },
    'DataSourceKey':'7868'
}
test2 = {
    'DataSourceKey':"2272",
    'InputParameters': [{
        'InputParameter': {
            'Name':'Workcenter_Key',
            'Value':'61324',
            'Required':'None',
            'Output':'None',
            'DefaultValue':'None',
            'Message':'None'
        }
    }]
}


# node=client.create_message(client.service, 'ExecuteDataSource',**request_data2)
node=client.create_message(client.service, 'ExecuteDataSource',ExecuteDataSourceRequest=test2)
tree = ET.ElementTree(node)
# etree_to_string(tree).de.decode()
tree.write('test.xml')
#     client.service.ExecuteDataSource(**request_data2)
# except Fault as error:
#     print(ET.tostring(error.detail))


# print(history.last_received)

request_data = {
        'ExecuteDataSourceRequest':{
            'InputParameters':{
                'InputParameter':{
                    'Name':'Workcenter_Key',
                    'Value':61324
                }
            },
            'DataSourceKey':"2272"
            
        }
}


#          <ExecuteDataSourceRequest>
#             <DataSourceKey>7868</DataSourceKey>
#             <InputParameters>
#                <InputParameter>
#                   <Value>CNC103</Value>
#                   <Name>@PLC_Name</Name>
#                </InputParameter>
#             </InputParameters>
#             <DataSourceName>Workcenter_Key_From_PLCName_Get</DataSourceName>
#          </ExecuteDataSourceRequest>
#       </ExecuteDataSource>

                    #===========================================================
                    # 'Name':'Workcenter_Key',
                    # 'Value':'61324'
                    #===========================================================

 
#         <dat:ExecuteDataSource xmlns="http://www.plexus-online.com/DataSource">
#             <dat:ExecuteDataSourceRequest>
#                 <dat:DataSourceKey>2272</dat:DataSourceKey>
#                 <dat:InputParameters>
#                     <dat:InputParameter>
#                         <dat:Name>Workcenter_Key</dat:Name>
#                         <dat:Value>61324</dat:Value>
#                     </dat:InputParameter>
#                 </dat:InputParameters>
#             </dat:ExecuteDataSourceRequest>
#         </dat:ExecuteDataSource>

# response = client.service.ExecuteDataSource(
#     {
#         'ExecuteDataSourceRequest':{
#             'DataSourceKey':'2272',
#             'InputParameters':{
#                 'InputParameter':{
#                     'Name':'Workcenter_Key',
#                     'Value':'61324'
#                 }
#              }   
#         }
#     })
#response = client.service.ExecuteDataSource(**request_data)
# dsn=response['DataSourceName']
# print(dsn)


#Here 'request_data' is the request parameter dictionary.
#Assuming that the operation named 'sendData' is defined in the passed wsdl.