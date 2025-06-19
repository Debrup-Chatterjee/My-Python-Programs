from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client['student']
collection=db['student_details']
result=collection.aggregate([{'$group':{'_id':None,'maxscore':{'$max':'$st_marks'}}}])# find the maximum marks
maxres=list(result)[0]['maxscore']
print(f"Students with maximum marks ({maxres}): ")# find all students with max marks
for student in collection.find({'st_marks':maxres}):
     print(student)