import shutil
import psutil

def checkDiskUsage(disk):
	du = shutil.disk_usage(disk)
	free = du.free / du.total * 100
	return free > 20

def checkCPUse():
	usage = psutil.cpu_percent(1)
	return usage < 75

if not checkDiskUsage("/") or not checkCPUse():
	print("ERROR")
else:
	print("Everything is okay!")