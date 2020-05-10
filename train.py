import face_recognition
import pickle
import os
import imghdr

directory = "database/"
save_dir =  "data/"

known_faces = []
people = []
for filename in os.listdir(directory):
	
	if imghdr.what(directory + filename) == 'jpeg':
		known_faces.append(face_recognition.face_encodings(face_recognition.load_image_file(directory + filename))[0])
		people.append(filename)
db = open(save_dir + 'faces.data','wb')
pickle.dump(known_faces,db)
db.close()

sv = open(save_dir + 'people.data','wb')
pickle.dump(people,sv)
sv.close()