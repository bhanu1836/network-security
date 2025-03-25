from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://bhanu:<@password>@machinelearning.36e8e.mongodb.net/?retryWrites=true&w=majority&appName=machineLearning"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment, You successfully connected to MongoDB")
except Exception as e:
    print(e)