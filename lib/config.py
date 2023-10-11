import os
import json
from lib.utility import MAR_Local_Lastlogin

mygame_prefix = "game/My Games/FINAL FANTASY XIV - A Realm Reborn/"

def MAR_Config_Loader():
    conf_dict = {}
    with open("./maconfig.json","r",encoding="utf8") as macfg:
        conf_dict = json.load(macfg)
    macfg.close()
    return conf_dict
def MAR_Config_Guide():
    conf_dict = {}
    print("私用型以太之光-配置生成向导\n请根据向导提示来输入配置项内容。完成后，向导将自动生成配置文件。")
    print("设置过程中，除部分选项外，直接按回车提交将会使得本设置项设置为推荐值。")
    cloudpath = input("[1/8] 请输入你的WebDAV服务商提供给你的网址，按回车提交。\n")
    if cloudpath == "":
        conf_dict['CloudPath'] = "https://dav.jianguoyun.com/dav/"
    else:
        conf_dict["CloudPath"] = cloudpath

    account = input("[2/8] 请输入你的WebDAV服务商账户，按回车提交。此处若直接按回车，则自动跳过云服务设置，并设置为仅本地备份模式。\n")
    if account != "":
        conf_dict["Account"] = account

        password = input("[3/8] 请输入你的WebDAV服务商密码，按回车提交。\n")
        conf_dict["Password"] = password

        folder = input("[4/8] 请输入你想要的备份文件夹名，按回车提交。\n")
        if folder == "":
            conf_dict["Folder"] = "/mabackup"
        else:
            conf_dict["Folder"] = str(folder)
    
    gamepath = ""
    retry = 0
    while gamepath == "":
        retry +=1
        if retry > 1:
            print("路径不能为空！")
        gamepath = input("[5/8] 请输入你的游戏路径（国服）或我的文档路径（国际服），按回车提交。\n")
    if gamepath[-1] != "/":
        gamepath = gamepath + "\\"
        conf_dict["GamePath"] = gamepath

    PrimaryUserID = input("[6/8] 请输入你要备份的用户ID(只包含CHR后的部分)，按回车提交。如果你不知道ID，可直接按回车，程序将自动获取你上次登录用户的ID。\n")
    if PrimaryUserID == "":
        PrimaryUserID = MAR_Local_Lastlogin(gamepath + mygame_prefix)
    conf_dict["PrimaryUserID"] = PrimaryUserID
        
    
    local = input("[7/8] 请指定是否仅本地备份。若你仅需要本地备份，请输入1并回车，否则请直接回车。\n")
    if local == 1:
        conf_dict["LocalOnly"] = 1
    else:
        conf_dict["LocalOnly"] = 0

    backuptype = input("[8/8] 请指定是否备份模式,默认为0。\n0:在备份角色配置的同时，备份全局配置、全局宏和捏脸。\n1:只备份角色配置。\n2:备份角色配置和全局配置。\n3:只备份角色配置和捏脸。\n")
    if backuptype not in range(0,3):
        backuptype = 0
    conf_dict["BackupType"] = backuptype

    print("设置完毕! 配置文件已导出到maconfig.json。")
    with open("maconfig.json","w+") as macfg:
        json.dump(conf_dict, macfg, indent=4)
    return 0 

def MAR_Config_Parser(conf_dict):
    backupplain = ["全备份","仅备份个人配置","仅备份个人配置和全局配置","仅备份个人配置和捏脸"]
    localplain = ["云端备份","仅本地备份"]
    print("备份模式：【"+backupplain[conf_dict['BackupType']]+"】,【"+localplain[conf_dict['LocalOnly']]+"】")
    return 0

    