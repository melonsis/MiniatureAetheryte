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

    