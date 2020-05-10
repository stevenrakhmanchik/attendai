import face_recognition
import os
import pickle
import datetime
import imghdr
import shutil
def getdata():
	data_dir = "data/"
	logs_dir = "logs/"
	frame_dir= "unidentified/"

	db = open(data_dir + 'faces.data','rb')
	known_faces = pickle.load(db)
	db.close()

	sv = open(data_dir + 'people.data','rb')
	people = pickle.load(sv)
	sv.close()

	d = datetime.date.today().strftime("%b,%d,%Y")
	log = open(logs_dir + d + '.log', 'w')
	identified = []
	last_found = None
	return(log,data_dir,logs_dir,frame_dir, known_faces, people, identified, last_found)

def match(vars):
	(log,data_dir,logs_dir,frame_dir, known_faces, people, identified, last_found) = vars
	for filename in os.listdir(frame_dir):
		if imghdr.what(frame_dir + filename) == 'jpeg':

			unk_img = face_recognition.load_image_file(frame_dir + filename)
			os.remove(frame_dir + filename)
			try:
				unknown_face_encoding = face_recognition.face_encodings(unk_img)[0]
			except IndexError:
				now = datetime.datetime.now()
				d = now.strftime('%I:%M:%S%p')
				log.write('[' + d + '] ' + 'No face found in ' + filename + '\n')
				break

			results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
			flag = 0
			for x in range(0,len(results)):
				if results[x] == True:
					ID = os.path.splitext(people[x])[0]
					now = datetime.datetime.now()
					last_found = None
					flag = 1
			if not(not True in results) and (ID not in identified) and flag == 1:
				d = now.strftime('%I:%M:%S%p')
				print('[' + d + '] ' + ID + ' found (in frame ' + filename + ')')
				log.write('[' + d + '] ' + ID + ' found (in frame ' + filename + ')' + '\n')
				last_found = ID
				identified = list([ID] + identified)
				print(identified)
			elif (ID not in identified) and flag == 1:
				d = now.strftime('%I:%M:%S%p')
				print('[' + d + '] ' + 'Unidentified Subject (in frame ' + filename + ')')
				log.write('[' + d + '] ' + 'Unidentified Subject (in frame ' + filename + ')' + '\n')
	return(log,data_dir,logs_dir,frame_dir, known_faces, people,identified,last_found)
