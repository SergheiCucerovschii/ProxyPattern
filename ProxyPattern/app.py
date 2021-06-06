from storage import *



storage = StorageProxy("memory")   # in memory
storage.save("Test Data")
print(storage.load())

storage = StorageProxy("file")   # in file
storage.save("Test Data")
print(storage.load())

storage = StorageProxy("json")   # in json
storage.save({"name": "Serghei", "age": "35"})
print(storage.load())

