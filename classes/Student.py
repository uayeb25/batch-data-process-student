from classes.Career import Career

class Student:

    def __init__(self, numero_cuenta, nombre, edad, career_id, id=""):
        self.numero_cuenta = numero_cuenta
        self.nombre = nombre
        self.edad = edad
        self.career_id = career_id        
        self.__id = id
        self.__collection = "student"

    def save(self, db):        
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id = result.inserted_id

    @staticmethod
    def return_list(db):        
        collection = db["student"]

        list_student = []
        for d in collection.find():
            student = Student(
                d['numero_cuenta']
                , d['nombre']
                , d['edad']
                , d['career_id']
                , d["_id"] 
            )
            list_student.append(student)       

        return list_student

    def delete(self, db):        
        collection = db[self.__collection]
        filterToUse = {'_id': self.__id}
        collection.delete_one(filterToUse)

    @staticmethod
    def return_dict(db):        
        collection = db["student"]

        dict_student = {}
        for d in collection.find():
            dict_student[d['numero_cuenta']] = d["_id"]

        return dict_student
    
    @staticmethod
    def delete_all(db):
        for d in Student.return_list(db):
            d.delete(db)

    @staticmethod
    def count_students_by_careers(db):
        dict_careers = Career.return_dict_id(db)

        dict_report = {}
        
        for s in Student.return_list(db):
            
            career_description = dict_careers[ s.career_id ]
            if career_description in dict_report.keys():
                dict_report[ career_description ] += 1
            else:  
                dict_report[ career_description ] = 1
        
        print(dict_report)

    @staticmethod
    def count_students_by_careers_2_manera(db):
        collection = db["student"]

        result =  collection.aggregate([{
            '$lookup': {
                'from': 'career'
                , 'localField': 'career_id'
                , 'foreignField': '_id'
                , 'as': 'c'
            }
        },{
            '$project': {
                'numero_cuenta': 1
                , 'c.descripcion': 1
            }
        }])

        report = {}
        for d in result:
            career = d['c'][0]['descripcion']
            if career in report.keys():
                report[ career ] += 1
            else:
                report[ career ] = 1

        print(report)