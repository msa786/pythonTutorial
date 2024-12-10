import os
import win32api
import string

def list_drives():
    """Lists all available drives on a Windows system."""
    drives = []
    bitmask = win32api.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter + ":")
        bitmask >>= 1

    return drives

if __name__ == "__main__":
    drives = list_drives()
    for drive in drives:
        print(drive)