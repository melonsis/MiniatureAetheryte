import os
from lib.config import MAR_Config_Guide, MAR_Config_Loader,MAR_Config_Parser
from lib.network import MAR_Client_Create, MAR_Client_Scan, MAR_Client_List

# "\033[31m红色 \033[0m"
# "\033[32m绿色 \033[0m"
print("========= 私用以太之光 V0.1 =========")
print("[INFO] "+"检查配置文件存在性...",end="")
# for root, dir, files in os.walk(".",topdown=False):
filelist = os.listdir(".")
if "maconfig.json" not in filelist:
    print("FAILED")
    print("[\033[31mERROR\033[0m] "+"未检测到配置文件，将自动启动配置向导")
    MAR_Config_Guide()
print("OK")
print("[INFO] "+"载入配置文件")
conf_dict = MAR_Config_Loader()
MAR_Config_Parser(conf_dict)
print("备份ID："+conf_dict["PrimaryUserID"])

if conf_dict["LocalOnly"] != 1:
    mar_connect = MAR_Client_Create(conf_dict["CloudPath"],conf_dict["Account"],conf_dict["Password"] )
    print("[INFO] "+"从服务器获取信息...",end="")
    sync_time_list = MAR_Client_List(mar_client=mar_connect, user_ID=conf_dict["PrimaryUserID"])
    print("OK")
    print("云端最后备份时间："+sync_time_list[1])


