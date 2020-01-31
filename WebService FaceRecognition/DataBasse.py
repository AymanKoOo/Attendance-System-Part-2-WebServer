import sqlite3
import json
class database:
    def insert_AttendanceData(self,presentID,id_,IsPresent,date_time):

            conn = sqlite3.connect('/home/AymanKoOo/mysite/Fproject.db')
            c = conn.cursor()
            c.execute("insert into attendees(presentID,studentID,IsPresent,attendDate) values (?,?,?,?)",
                   (presentID,id_,IsPresent,date_time))

            conn.commit()
            conn.close()


    def get_AttendanceID(self,prs):
            conn = sqlite3.connect('/home/AymanKoOo/mysite/Fproject.db')
            cursor = conn.execute("SELECT students.studentName, attendees.studentID , attendees.attendDate FROM students INNER JOIN attendees ON students.studentID = attendees.studentID WHERE attendees.Ispresent =?",(prs,))

            #rows = cursor.fetchone()
            #print(rows)
            results = cursor.fetchall()
            rowarray_list = []
            for row in results:
               rowarray_list.append(row)
            j = json.dumps(rowarray_list)
            return j

















