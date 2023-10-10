# coding = utf8
import os
import time

def MAR_Local_Scan (mygame_path):
    # Get all avalible user configurations
    conf_list = []
    for root, dirs, files in os.walk(mygame_path, topdown=False):
        for dir in dirs:
            if "FFXIV_CHR" in dir:
                conf_list.append(dir[9:])
    # Get lastlogin information from cfg
    with open(mygame_path+"FFXIV.cfg", "r", encoding="utf8") as ffcfg:
        for line in ffcfg:
            line = line.strip()
            # 如果行以'LastLogin0'开头，则提取对应的值
            if line.startswith('LastLogin0'):
                last_login_0 = int(line.split('\t')[1])
        
            # 如果行以'LastLogin1'开头，则提取对应的值
            if line.startswith('LastLogin1'):
                last_login_1 = int(line.split('\t')[1])
        last_login_ID = "00" + hex(last_login_1)[2:] + hex(last_login_0)[2:]
        print(last_login_ID.upper())


    return conf_list