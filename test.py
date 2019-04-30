import requests
import json

urlPrefix ="http://localhost:8086/CIRBA/api/v2"
# Sample Basic Auth Url with login values as username and password
#url = "http://localhost:8086/CIRBA/api/v1/today-value"
urlGetBookings = urlPrefix + "/workloads/status/PLACED" # or BOOKED

targetEnv = ""
targetCluster = ""
sourceEnv = "FIS_PDC"
sourceEnvId = "651bd135-0188-4e2a-a9e1-b619860fee9b"
sourceCluster = "FIS_PDC_CORE1"
sourceClusterId = "1a19e81d-5956-4109-b9f1-032e1cbb282"

user = "admin"
passwd = "admin"
 
# Make a request to the endpoint using the correct auth values
auth_values = (user, passwd)
response = requests.get(urlGetBookings, auth=auth_values)
 
# Convert JSON to dict and print
#print(response.json())

#ret = json.loads(response.json())
ret = json.loads(response.text)
retWorkloads = ret.get("workloads")


## /workloads/
            # "disks": [
            #     {
            #         "name": "SYSTEM",
            #         "provisioned_space": 81920,
            #         "used_space": 20480,
            #         "pref_datastore": "FIS_PDC_CORE1-8040-T3-0001",
            #         "attributes": [
            #             {
            #                 "id": "attr_DiskDatastoreLink",
            #                 "name": "Disk Datastore Link",
            #                 "value": "46cd2158-b388-4d08-bceb-e8543cc43693"
            #             }
            #         ]
            #     }
            # ],
###
for wld in retWorkloads:
    print (wld.get("infrastructure_group").get("id"), wld.get("infrastructure_group").get("name"),
         wld.get("name"), wld.get("id"))
    print("1")
print("a")
