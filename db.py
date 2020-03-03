from pyArango.connection import *

class ArangoDB:
    def __init__(self):
        self.app = None
        self.connection = None

    def init_app(self, app):
        self.app = app
        self.connect()

    def connect(self):
        self.connection = Connection(username="root", password="admin")
        return self.connection

    def get_db(self):
        if not self.connection:
            self.connect()
            if not self.connection.hasDatabase("NBA"):
                self.connection.createDatabase(name="NBA")

            db = self.connection["NBA"]
            return db

        if not self.connection.hasDatabase("NBA"):
            self.connection.createDatabase(name="NBA")

        db = self.connection["NBA"]
        return db

    def get_collection(self, collectionName):
        schema = self.get_db()

        if not schema.hasCollection(collectionName):
            return schema.createCollection(name=collectionName)

        return schema[collectionName]

    def get_document(self, collection, docName):
        if docName in collection:
            return collection[docName]

        doc = collection.createDocument()
        doc._key = docName
        return doc