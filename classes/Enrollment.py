from classes.Course import Course

class Enrollment:

    def __init__(self, student_id, course_id, failed,  id=""):
        self.student_id = student_id
        self.course_id = course_id
        self.failed = failed
        self.__id = id
        self.__collection = "enrollment"

    def save(self, db):        
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id = result.inserted_id

    @staticmethod
    def return_list(db):        
        collection = db["enrollment"]

        list_enrollment = []
        for d in collection.find():
            enrollment = Enrollment(
                d['student_id']
                , d['course_id']
                , d['failed']
                , d["_id"] 
            )
            list_enrollment.append(enrollment)       

        return list_enrollment

    def delete(self, db):        
        collection = db[self.__collection]
        filterToUse = {'_id': self.__id}
        collection.delete_one(filterToUse)

    @staticmethod
    def print_count_courses_report(db):
        report = {}
        dict_courses = Course.return_dict_id(db)

        for d in Enrollment.return_list(db):
            course_descripcion = dict_courses[ d.course_id ]

            if course_descripcion not in report.keys():
                report[course_descripcion] = { "aprobados": 0, "reprobados": 0 }
            
            if d.failed:
                report[course_descripcion]["reprobados"] += 1
            else:
                report[course_descripcion]["aprobados"] += 1

        print(report)
    @staticmethod
    def delete_all(db):
        for d in Enrollment.return_list(db):
            d.delete(db)

    @staticmethod
    def print_count_courses_report_2_manera(db):
        collection = db["enrollment"]

        result =  collection.aggregate([{
            
            '$lookup': {
                'from': 'course'
                , 'localField': 'course_id'
                , 'foreignField': '_id'
                , 'as': 'c'
            }
        },{
            '$project': {
                'failed': 1
                , 'c.descripcion': 1
                , 'c.descripcion': 1

            }
        }])

        report = {}
        for d in result:
            course = d['c'][0]['descripcion']
            if course not in report.keys():
                report[ course ] = { "aprobados": 0, "reprobados": 0 }
            
            if d['failed']:
                report[course]['reprobados'] += 1
            else:
                report[course]['aprobados'] += 1
        print(report)
