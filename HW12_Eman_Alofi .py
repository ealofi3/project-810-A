from flask import Flask, render_template
import sqlite3
app = Flask( __name__ )
@ app.route('/')
def instructor_cources():
    dbpath = '/Users/ealofi3/Documents/Database_SSW810/test_startup.db'
    
    query = """select i.CWID, i.Name, 
    i.Dept, g.Course, count(*) as Students 
    from grades as g join instructors as i on 
    g.InstructorCWID=i.CWID group by i.CWID, 
    i.Name, i.Dept, g.Course"""
    db = sqlite3.connect(dbpath)
    data = [{'cwid': cwid, 'name':name, 'dept': dept, 'course': course, 
    'students': students} 
    for cwid, name, dept, course, students in db.execute(query)]

    db.close() 
    return render_template ('instructors_cources.html', 
                 title = 'Stevens Repository',
                  table_title = 'Cources and students count',
                   instructors = data )  
app.run(debug=True)   
