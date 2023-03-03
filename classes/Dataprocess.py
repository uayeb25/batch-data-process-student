from classes.Career import Career
from classes.Course import Course
from classes.Student import Student
from classes.Enrollment import Enrollment

class Dataprocess:

    def __init__(self, data):
        self.__data = data

    def create_careers(self, db):
        ## Do something to create careers on your mongodb collection using __data

        dict_carreras = {}
        for d in self.__data:
            dict_carreras[d['carrera']] = 1

        for k in dict_carreras.keys():
            carrera = Career(k)
            carrera.save(db)
            print(f"{k} created!")

        return True
    def create_courses(self, db):
        ## Do something to create courses on your mongodb collection using __data

        dict_courses = {}
        for d in self.__data:
            for c in d["cursos_aprobados"]:
                dict_courses[c]= 1
            
            for c in d["cursos_reprobados"]:
                dict_courses[c]= 1

        for k in dict_courses.keys():
            carrera = Course(k)
            carrera.save(db)
            print(f"{k} created!")
        

        return True
    def create_students(self, db):
        ## Do something to create students on your mongodb collection using __data
        dict_careers =  Career.return_dict(db)
        for d in self.__data:
            estudiante = Student(
                d['numero_cuenta']
                , d['nombre_completo']
                , d['edad']
                , dict_careers[ d['carrera'] ]
            )
            estudiante.save(db)
            print(f"{d['numero_cuenta']} created!")
            

        return True
    def create_enrollments(self, db):
        ## Do something to create enrollments on your mongodb collection using __data

        dict_students = Student.return_dict(db)
        dict_courses = Course.return_dict(db)

        for d in self.__data:
            student_id = dict_students[ d["numero_cuenta"] ]

            for c in d["cursos_aprobados"]:
                course_id = dict_courses[ c ]
                enrollment = Enrollment(student_id, course_id, False)
                enrollment.save(db)
            for c in d["cursos_reprobados"]:
                course_id = dict_courses[ c ]
                enrollment = Enrollment(student_id, course_id, True)
                enrollment.save(db)

            print(f"{d['numero_cuenta']} courses enrolled!")


        return True