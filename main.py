from get_frame import *
from identify import *
import os
import shutil

def main():
    vars = getdata()
    (log,data_dir,logs_dir,frame_dir, known_faces, people, identified, last_found) = vars

    shutil.rmtree('found')
    os.mkdir('found')

    while True:
        getframe()
        if not(last_found == None):
            print(last_found)
        vars = match(vars)
        (log,data_dir,logs_dir,frame_dir, known_faces, people, identified, last_found) = vars
    log.close()

main()
