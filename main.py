import requests
import os
import json
#Geoserver configuration

geoserver_url = 'http://localhost:8080/geoserver'
username = 'admin'
password = 'geoserver'

#workspace and store information

workspace = 'my_tiff'
store = 'my_store'

data_dir = 'E:/tiff'

#create workspace if it doesn't exist
workspace_url = f"{geoserver_url}/rest/workspaces/{workspace}"

# Set the payload for the request body
payload = {
    "workspace":{
        "name":workspace
    }        
}

# Convert the payload to JSON string
json_payload = json.dumps(payload)
request = requests.post(f"{geoserver_url}/rest/workspaces", data=json_payload, auth = (username, password), headers={"Content-Type": "application/json"})

#Check if the request was successful (200 status code)
if request.status_code == 200:
    #Access ther response content as text
    res_text = request.text
    print(res_text)
else:
    #Request was not successful, handle the error
    print(f"Error: {request.status_code} - {request.text}")


# Create a new data store for GeoTIFF
def create_geotiff_datastore(datastore_name, geotiff_file):
    url = f"{geoserver_url}/rest/workspaces/{workspace}/datastores"
    headers = {'Content-Type': 'application/xml'}

    payload = f"""
        <dataStore>
            <name>{datastore_name}</name>
            <type>GeoTIFF</type>
            <enabled>true</enabled>
            <connectionParameters>
                <entry key="coverageName">{datastore_name}</entry>
                <entry key="path">{geotiff_file}</entry>
            </connectionParameters>
        </dataStore>
    """

    response = requests.post(url, auth=(username, password), headers=headers, data=payload)

    if response.status_code == 201:
        print('Data store created successfully.')
    else:
        print('Failed to create data store.')
        print(response.text)


#interate over the GeoTIFF files in the directory


for filename in os.listdir(data_dir):
    if(filename.endswith('.TIF')):
        layer_name = os.path.splitext(filename)[0]        
        


        # Call the function to create the data store
        create_geotiff_datastore(layer_name, os.path.join(data_dir, filename))


        # # Publish the layer
        # layer_url = f"{data_store_url}/featuretypes"
        # layer_payload = {
        #     "featureType": {
        #         "name": layer_name,
        #         "nativeName": layer_name,
        #         "title": layer_name,
        #         "enabled": True
        #     }
        # }
        # requests.post(layer_url, json=layer_payload, auth=(username, password))

        # print(f"Added layer: {layer_name}")

print("GeoTIFF files successfully added to GeoServer!")