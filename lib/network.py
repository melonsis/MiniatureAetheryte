from webdav4.client import Client
import time

def MAR_Client_Create(url, user, pwd):
        mar_client = Client(base_url=url, auth=(user,pwd))
        return mar_client
def MAR_Client_List(mar_client, user_ID):
    backup_list = mar_client.ls(path="/MAR/",detail=False)
    last_sync_time = 0
    backup_count = 0
    for backup in backup_list:
        if user_ID in backup:
            sync_time = backup.split("_")[1]
            if int(sync_time) > last_sync_time:
                last_sync_time = int(sync_time)
            backup_count += 1
    last_sync_time_local = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(last_sync_time))
    print("Listing backup information for user " + user_ID)
    print("Total: "+str(backup_count))
    print("Last: "+last_sync_time_local)
    return 0
def MAR_Client_Scan(mar_client):
    backup_list = mar_client.ls(path = "/MAR/", detail = False)
    last_sync_time = []
    backup_count = []
    user_ID = []
    for backup in backup_list:
        sync_time = backup.split("_")[1]
        ID = backup.split("_")[2].split(".")[0]
        if ID not in user_ID:
            user_ID.append(ID)
            backup_count.append(1)
            last_sync_time.append(int(sync_time))
        else:
            ID_index = user_ID.index(ID)
            backup_count[ID_index] +=1
            if int(sync_time) > last_sync_time[ID_index]:
                last_sync_time[ID_index] = int(sync_time)
    return [user_ID, backup_count, last_sync_time]

    