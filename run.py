import os
import pathlib
import random
import requests
import schedule
import subprocess
import time

WALLPAPER_FOLDER = 'wallpapers'
SET_WALLPAPER_OSASCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "{}"
end tell
END"""


def get_filenames_from_directory(folder_location):
	files = os.listdir(folder_location)
	return files


def set_wallpaper():
	print(f"Setting the wallpaper")
	wallpapers = get_filenames_from_directory(WALLPAPER_FOLDER)
	random_wallpaper = random.choice(wallpapers)
	full_image_path = os.path.join(
		pathlib.Path().absolute(),
		WALLPAPER_FOLDER,
		random_wallpaper
	)

	subprocess.Popen(SET_WALLPAPER_OSASCRIPT.format(full_image_path), shell=True)


def run():
	schedule.every(10).seconds.do(set_wallpaper)
	while True:
		schedule.run_pending()
		time.sleep(1)


if __name__ == '__main__':
	run()
