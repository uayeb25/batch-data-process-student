class Course:

    def __init__(self, descripcion,  id=""):
        self.descripcion = descripcion
        self.__id = id
        self.__collection = "course"

    def save(self, db):        
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id = result.inserted_id

    @staticmethod
    def return_list(db):        
        collection = db["course"]

        list_course = []
        for d in collection.find():
            course = Course(
                d['descripcion']
                , d["_id"] 
            )
            list_course.append(course)       

        return list_course

    def delete(self, db):        
        collection = db[self.__collection]
        filterToUse = {'_id': self.__id}
        collection.delete_one(filterToUse)

    @staticmethod
    def return_dict(db):        
        collection = db["course"]

        dict_course = {}
        for d in collection.find():
            dict_course[d['descripcion']] = d["_id"]

        return dict_course
    
    @staticmethod
    def return_dict_id(db):        
        collection = db["course"]

        dict_course = {}
        for d in collection.find():
            dict_course[d['_id']] = d["descripcion"]

        return dict_course
    
    @staticmethod
    def delete_all(db):
        for d in Course.return_list(db):
            d.delete(db)