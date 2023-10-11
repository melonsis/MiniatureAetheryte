import os
from lib.config import MAR_Config_Guide, MAR_Config_Loader,MAR_Config_Parser

# "\033[31m红色 \033[0m"
# "\033[32m绿色 \033[0m"
print("========= 私用以太之光 V0.1 =========")
print("[INFO]"+"检查配置文件存在性")
# for root, dir, files in os.walk(".",topdown=False):
filelist = os.listdir(".")
if "maconfig.json" not in filelist:
    print("[\033[31mERROR\033[0m] "+"未检测到配置文件，将自动启动配置向导")
    MAR_Config_Guide()
print("[INFO]"+"载入配置文件")
conf_dict = MAR_Config_Loader()
MAR_Config_Parser(conf_dict)


