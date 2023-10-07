import zipfile
from webdav4.client import Client
import os
import time
from lib.file import MAR_Packing,MAR_Unpacking
from lib.network import MAR_Client_Create, MAR_Client_List

#print("Connecting to WebDAV server...",end="")
#mar_client = Client(base_url="https://dav.jianguoyun.com/dav/", auth=("tch1995@live.com", "adkc8sya3r7axfyg"))
#print("Done.")
#print(client.ls(path='/MAR',detail=False))

# Setting path
game_path = "D:/Project/MAR/testdata"
game_path_fix = "/My Games/FINAL FANTASY XIV - A Realm Reborn/"
user_prefix = "FFXIV_CHR"
user_ID = "00438D8134B2E335"

mygame_path = game_path+game_path_fix
pbk_file = MAR_Packing(mygame_path,user_prefix,user_ID)
#MAR_Unpacking(mygame_path, mygame_path+"backup_1696671155_00438D8134B2E335.pbkp")
mar_client = MAR_Client_Create("https://dav.jianguoyun.com/dav/", "tch1995@live.com", "adkc8sya3r7axfyg")
mar_client.upload_file(from_path=pbk_file, to_path = "/MAR/"+pbk_file.split("/")[-1], overwrite = True)
MAR_Client_List(mar_client, user_ID) 



'''
mygame_path = game_path+game_path_fix

backup_timepoint = str(int(time.time()))
filename = 'backup_'+backup_timepoint+'_'+user_ID+'.zip'

data_zip = zipfile.ZipFile(filename,'w')
for root, dirs, files in os.walk(mygame_path+user_prefix+user_ID, topdown=False):
    for name in files:
        if "log" not in os.path.join(root,name):
            print("Compressing "+ name +" for "+user_ID)
            data_zip.write(os.path.join(root,name),name,compress_type=zipfile.ZIP_DEFLATED)
data_zip.close()

print("Uploading file...",end="")
mar_client.upload_file(from_path = filename, to_path="/MAR/"+filename, overwrite=True)
print("Done.")
'''




