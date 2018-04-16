import os
import time
from shutil import copyfile, move

def rename_files():
    source_dir = "D:/Projects/Udacity Full-Stack Projects/rename_files/alphabet/"
    check_out_dir = os.listdir(source_dir)
    b_out_dir = False
    for dir in check_out_dir:
        if dir == "secret_message":
            b_out_dir = True
    if b_out_dir == False:
        os.mkdir(source_dir+"secret_message")
    os.chdir(source_dir)
    file_list = os.listdir(source_dir)
    
    out_list = {"athens": 1, "austin": 1, "barcelona": 2, "beijing": 5, "chennai": 1, "chicago": 3, "colombo": 1, "dallas": 2, "gainesville": 2, "houston": 2, "hyderabad": 2, "istanbul": 1, "kiev": 1, "madrid": 5}
    scrt_msg = "DONT LET YOUR DREAMS BE MEMES"
    for key,val in out_list.items():
        if val == 1:
            copyfile(source_dir+key+".jpg", source_dir+"secret_message/"+key+".jpg")
        else:
            for i in range(0, val):
                if i == 0:
                    copyfile(source_dir+key+".jpg", source_dir+"secret_message/"+key+".jpg")
                else:
                    copyfile(source_dir+key+".jpg", source_dir+"secret_message/"+key+str(i)+".jpg")
    for file_name in file_list:
        if file_name != "secret_message":
            os.remove(file_name)
    out_file_list = os.listdir(source_dir+"/secret_message")
    for file in out_file_list:
        move(source_dir+"/secret_message/"+file, source_dir+file)

    dcount = 0
    ecount = 0
    mcount = 0
    ocount = 0
    rcount = 0
    scount = 0
    tcount = 0
    white_count = 0
    for c in scrt_msg:
        if c == "A":
            os.rename("athens.jpg", "18athens.jpg")
        elif c == "B":
            os.rename("austin.jpg", "22austin.jpg")
        elif c == "D":
            if dcount == 0:
                if os.access("barcelona.jpg", os.R_OK):
                    os.rename("barcelona.jpg", "1barcelona.jpg")
                    dcount = dcount + 1
            else:
                os.rename("barcelona1.jpg", "15barcelona.jpg")
        elif c == "E":
            if ecount == 0:
                if os.access("beijing.jpg", os.R_OK):
                    os.rename("beijing.jpg", "7beijing.jpg")
                    ecount = ecount + 1
            elif ecount == 1:
                os.rename("beijing1.jpg", "17beijing.jpg")
                ecount = ecount + 1
            elif ecount == 2:
                os.rename("beijing2.jpg", "23beijing.jpg")
                ecount = ecount + 1
            elif ecount == 3:
                os.rename("beijing3.jpg", "26beijing.jpg")
                ecount = ecount + 1
            elif ecount == 4:
                os.rename("beijing4.jpg", "28beijing.jpg")
        elif c == "L":
            os.rename("chennai.jpg", "6chennai.jpg")
        elif c == "M":
            if mcount == 0:
                if os.access("chicago.jpg", os.R_OK):
                    os.rename("chicago.jpg", "19chicago.jpg")
                    mcount = mcount + 1
            elif mcount == 1:
                os.rename("chicago1.jpg", "25chicago.jpg")
                mcount = mcount + 1
            elif mcount == 2:
                os.rename("chicago2.jpg", "27chicago.jpg")
        elif c == "N":
            os.rename("colombo.jpg", "3colombo.jpg")
        elif c == "O":
            if ocount == 0:
                if os.access("dallas.jpg", os.R_OK):
                    os.rename("dallas.jpg", "2dallas.jpg")
                    ocount = ocount + 1
            else:
                os.rename("dallas1.jpg", "11dallas.jpg")
        elif c == "R":
            if rcount == 0:
                if os.access("gainesville.jpg", os.R_OK):
                    os.rename("gainesville.jpg","13gainesville.jpg")
                    rcount = rcount + 1
            else:
                os.rename("gainesville1.jpg", "16gainesville.jpg")
        elif c == "S":
            if scount == 0:
                if os.access("houston.jpg", os.R_OK):
                    os.rename("houston.jpg", "20houston.jpg")
                    scount = scount + 1
            else:
                os.rename("houston1.jpg", "29houston.jpg")
        elif c == "T":
            if tcount == 0:
                if os.access("hyderabad.jpg", os.R_OK):
                    os.rename("hyderabad.jpg", "4hyderabad.jpg")
                    tcount = tcount + 1
            elif tcount == 1:
                os.rename("hyderabad1.jpg", "8hyderabad.jpg")
        elif c == "U":
            os.rename("istanbul.jpg", "12istanbul.jpg")
        elif c == "Y":
            os.rename("kiev.jpg", "10kiev.jpg")
        elif c == " ":
            if white_count == 0:
                if os.access("madrid.jpg", os.R_OK):
                    os.rename("madrid.jpg", "5madrid.jpg")
                    white_count = white_count + 1
            elif white_count == 1:
                os.rename("madrid1.jpg", "9madrid.jpg")
                white_count = white_count + 1
            elif white_count == 2:
                os.rename("madrid2.jpg", "14madrid.jpg")
                white_count = white_count + 1
            elif white_count == 3:
                os.rename("madrid3.jpg", "21madrid.jpg")
                white_count = white_count + 1
            elif white_count == 4:
                os.rename("madrid4.jpg", "24madrid.jpg")
rename_files()
