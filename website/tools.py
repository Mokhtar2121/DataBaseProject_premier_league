import mysql.connector
mydp = mysql.connector.connect(host="localhost", user="root", password="Qaisaleh12010@auc", database="premier_league",
                               auth_plugin='mysql_native_password')

if (mydp):
    print("connected")
    mycursor = mydp.cursor()
else:
    print("Notconnected")


def get_reviews(x):
    if (mydp):
        print("connected")
        mycursor = mydp.cursor()
        return ['connected', 'sql']
    else:
        print("Notconnected")
        return ['not connected', 'sql']