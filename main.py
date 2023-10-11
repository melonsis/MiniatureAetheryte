import os

# "\033[31m红色 \033[0m"
# "\033[32m绿色 \033[0m"
print("========= 私用以太之光 V0.1 =========")
print("[INFO] "+"检查配置文件存在性")
# for root, dir, files in os.walk(".",topdown=False):
filelist = os.listdir(".")
if "maconfig.cfg" not in filelist:
    print("[\033[31mERROR\033[0m] "+"未检测到配置文件，将自动启动配置向导")
else:
    print("[INFO] "+"开始载入配置文件")


