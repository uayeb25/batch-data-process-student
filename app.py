import pymongo
from classes import DATA, Dataprocess, DbMongo, Student, Course, Career, Enrollment

from dotenv import load_dotenv

def main():

    client, db = DbMongo.getDB()

    #### clean all####
    Enrollment.delete_all(db)
    Career.delete_all(db)
    Course.delete_all(db)
    Student.delete_all(db)
    ##################

    pipeline = Dataprocess(DATA)
    
    pipeline.create_careers(db)
    pipeline.create_courses(db)
    pipeline.create_students(db)
    pipeline.create_enrollments(db)

    print("############### resultados reportes sin queries ################")
    ### resuelto sin queries ####
    print("############### reporte 1 ################")
    print('')
    Student.count_students_by_careers(db)
    print("############### reporte 2 ################")
    print('') 
    Enrollment.print_count_courses_report(db)

    print("############### resultados reportes sin queries ################")
    ## resuelto con queries ##
    print("############### reporte 1 ################")
    print('')
    Student.count_students_by_careers_2_manera(db)
    
    print("############### reporte 2 ################")
    print('')
    Enrollment.print_count_courses_report_2_manera(db)

    client.close()
    return True

if __name__ == "__main__":
    load_dotenv()
    main()



