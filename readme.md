# BlobTrigger - Python

The `BlobTrigger` makes it incredibly easy to react to new Blobs inside of Azure Blob Storage. This sample demonstrates a simple use case of processing data from a given Blob using Python.

## How it works

For a `BlobTrigger` to work, you provide a path which dictates where the blobs are located inside your container, and can also help restrict the types of blobs you wish to return. For instance, you can set the path to `samples/{name}.png` to restrict the trigger to only the samples path and only blobs with ".png" at the end of their name.

## Learn more

Documentation:

1) Note: You must create a Storage Account and add it's name and keys in __init__.py
2) Within that same account, you must create a Queue with the name 'weather-data'.
3) Within that same account, you must create a Blob container with the name 'weather-data'.
4) You must then upload .csv files into this area. You can find these in the samples folder.
5) Update the AzureWebJobsStorage value in local.settings.json.
6) Note that if you want to change the queue name, you must also change it in the other function (QueueProj)