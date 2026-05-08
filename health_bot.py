import shutil
import os

limit = 80
folder_backup="/home/hammad/Desktop"
backup_destination="/home/hammad/my_backups"

total, used, free = shutil.disk_usage("/")
percentage_used= (used / total)*100
print(f"Storage used for now: {percentage_used:.2f}%")

if percentage_used > limit:
	print("Storage limit has crossed 80%, Backup starting...")

	if not os.path.exists(backup_destination):
		os.makedirs(backup_destination)

	shutil.make_archive(f"{backup_destination}/backup_file", 'zip', folder_to_backup)

	print("Done! Your data is safe and Zip file has been created.")

else:
	print("No need for zip, Occupied storage is less than 80%.")

