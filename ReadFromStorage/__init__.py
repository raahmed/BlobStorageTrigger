import logging
import csv
import json
import base64

import azure.functions as func
from azure.storage.blob import BlockBlobService
from azure.storage.queue import QueueService
from azure.storage.queue.models import QueueMessageFormat


def main(myblob: func.InputStream):
    #//TODO: Ensure queue name is 'weather-data'
    queue_name = 'weather-data'
    #//TODO: Add Storage Account Name and Key from  https://portal.azure.com/#@[user_email]/resource/subscriptions/[subscription_id]/resourceGroups/[resource_group_name]/providers/Microsoft.Storage/storageAccounts/[storage_account_name]/keys
    block_blob_service = BlockBlobService(account_name='//TODO: ', account_key=' //TODO')
    queue_service = QueueService(account_name='//TODO', account_key='//TODO')
    queue_service.encode_function = QueueMessageFormat.text_base64encode
    file_name = myblob.name.split("/")[1]
    #// Ensure that files are added to a blob container named 'weather-data'
    block_blob_service.get_blob_to_path('weather-data', file_name, file_name)   
    with open(file_name, "r+") as file:
        reader = csv.reader(file)
        for idx, data in enumerate(reader):
            if idx != 0:
                if(len(data)> 13):
                    city, country = data[6].split(",")
                    datapoint =json.dumps({"date": data[1],"city": city, "country": country, "temperature": data[13][:-2]})   
                    queue_service.put_message(queue_name, datapoint)
                else:
                    logging.info(len(data))

    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes\n"
                )
