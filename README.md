# Frappe Framework App


## AWS Rabbit MQ EDA (Event Driven Architecture)
### To Use Library

See The below Code

```sh 
from eda.publisher import Publisher --> Import this to your Program
from eda.publisher import site_routing_key -->Import this to your Program
p = Publisher() --> Inilize the class
route_to = site_routing_key().procurement --> Choose the server to send your data

##Publisher.send() --> Takes Two Paramete first one is dict and second one is str, Please refer the below code 
p.send({
"module":"eda_test.receiver", #--> Specify the file path
"function":"receive_notes", #--> Specify the function inside the file
"argument":{                 #--> Specify the arguments in form of dict
"note":"i am testing this end to end",
"uuid":"23563452362346"
},
"doc_uuid":"1234567890"
},route_to) 
```
