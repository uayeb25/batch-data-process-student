class Career:

    def __init__(self, descripcion,  id=""):
        self.descripcion = descripcion
        self.__id = id
        self.__collection = "career"

    def save(self, db):        
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id = result.inserted_id

    @staticmethod
    def return_list(db):        
        collection = db["career"]

        list_career = []
        for d in collection.find():
            career = Career(
                d['descripcion']
                , d["_id"] 
            )
            list_career.append(career)       

        return list_career

    def delete(self, db):        
        collection = db[self.__collection]
        filterToUse = {'_id': self.__id}
        collection.delete_one(filterToUse)

    @staticmethod
    def return_dict(db):        
        collection = db["career"]

        dict_career = {}
        for d in collection.find():
            dict_career[d['descripcion']] = d["_id"]

        return dict_career
    
    @staticmethod
    def return_dict_id(db):        
        collection = db["career"]

        dict_career = {}
        for d in collection.find():
            dict_career[ d['_id'] ] = d["descripcion"]

        return dict_career
    
    @staticmethod
    def delete_all(db):
        for d in Career.return_list(db):
            d.delete(db)