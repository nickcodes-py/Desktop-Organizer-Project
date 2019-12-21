#Project : Desktop Cleanup Automation
#Developer : Nikunj Dutt

import os, shutil

#Current Work Directory
cwd = os.getcwd()   

#Function to make directories to store the cleaned up files
def makeFolder(name):                             
    if os.path.isdir(name):
        return False
    else:
        os.makedirs(name)

#Function to move files to directories
def moveFile(name, dest):
    try:
        shutil.move(name, dest)
    except shutil.Error:        
        return False

#Creation of Folders 
makeFolder('Videos')
makeFolder('Pictures')
makeFolder('Documents')
makeFolder('Applications')
makeFolder('Audios')
makeFolder('Sheets')
makeFolder('Presentations')
makeFolder('Programming')
makeFolder('Archives')
makeFolder('Torrents')
makeFolder('Fonts')

#Variables for Destination Directory
dwd = cwd+'\\Pictures'              
dwd2 = cwd+'\\Videos'               
dwd3 = cwd+'\\Documents'            
dwd4 = cwd+'\\Applications'
dwd5 = cwd+'\\Audios'      
dwd6 = cwd+'\\Sheets'
dwd7 = cwd+'\\Presentations'
dwd8 = cwd+'\\Programming'  
dwd9 = cwd+'\\Archives' 
dwd10 = cwd+'\\Torrents'
dwd11 = cwd+'\\Fonts'   

#Cleanup Process Using For Loop and If Statements
for filename in os.listdir():

    if filename.endswith(('.png','.jpg','.jpeg','.gif','.PNG','.JPG','.JPEG','.GIF','.psd','.ai','.svg','.ico','.sketch','.webp')):
        moveFile(filename, dwd)

    if filename.endswith(('.mp4','.avi', '.mkv','.mov')):
        moveFile(filename, dwd2)
    
    if filename.endswith(('.pdf','.doc','.docx','.txt','epub')):
        moveFile(filename, dwd3)
    
    if filename.endswith(('.exe','.lnk','.msi')):
        moveFile(filename, dwd4)
    
    if filename.endswith(('.mp3','.wav')):
        moveFile(filename, dwd5)
    
    if filename.endswith(('.xls','.csv')):
        moveFile(filename, dwd6)
    
    if filename.endswith(('.ppt', '.pptx')):
        moveFile(filename, dwd7)
    
    if filename.endswith(('.html', '.c', '.cpp', '.js','.php','.json','.htm','.xml')):
        moveFile(filename, dwd8)
    
    if filename.endswith(('.zip', '.7z', '.rar', '.tar','.iso','.gz')):
        moveFile(filename, dwd9)
    
    if filename.endswith(('.torrent')):
        moveFile(filename, dwd10)
    
    if filename.endswith(('.ttf', '.otf')):
        moveFile(filename, dwd11)
