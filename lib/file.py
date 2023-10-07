import zipfile
import os
import time
import hashlib
#game_path_fix = "/My Games/FINAL FANTASY XIV - A Realm Reborn/"
user_prefix = "FFXIV_CHR"

def MAR_Packing(mygame_path, user_prefix, user_ID):
    backup_timepoint = str(int(time.time()))
    filename = mygame_path+'backup_'+backup_timepoint+'_'+user_ID+'.zip'
    data_zip = zipfile.ZipFile(filename,'w')
    for root, dirs, files in os.walk(mygame_path+user_prefix+user_ID, topdown=False):
        for name in files:
            if "log" not in os.path.join(root,name):
                print("Compressing "+ name +" for "+user_ID)
                data_zip.write(os.path.join(root,name),name,compress_type=zipfile.ZIP_DEFLATED)
    data_zip.close()
    
    with open(filename, 'rb') as f:
        file_content = f.read()
        f.close()
    mar_zip_md5 = hashlib.md5(file_content).hexdigest()
    
    pbk_file = mygame_path+'backup_'+backup_timepoint+'_'+user_ID+'.pbkp'
    with open(pbk_file, 'wb+') as f:
        f.seek(0)
        f.write(backup_timepoint.encode('utf8'))
        f.write(user_ID.encode('utf8'))
        f.write(mar_zip_md5.encode('utf8'))
        f.write(file_content)
        f.close()
    
    return pbk_file
def MAR_Unpacking(mygame_path, pbk_file):
    with open(pbk_file,'rb+') as pbk_obj:
        pbk_obj.seek(0)
        backup_timepoint = pbk_obj.read(10).decode('utf8')
        user_ID = pbk_obj.read(16).decode('utf8')
        store_md5 = pbk_obj.read(32).decode('utf8')
        file_content = pbk_obj.read()
        pbk_obj.close()

    pbk_md5 = hashlib.md5(file_content).hexdigest()
    if pbk_md5 != store_md5:
        print("MD5 Check failed!")
        return -1
    else:
        backup_zip = mygame_path+"backup_temp.zip"
        with open (backup_zip, 'wb+') as zip_obj:
            zip_obj.seek(0)
            zip_obj.write(file_content)
            zip_obj.close()
        data_zip = zipfile.ZipFile(backup_zip, 'r')
        data_zip.extractall(mygame_path+user_prefix+user_ID+"/temp")
    
    print(user_ID)
    return 0