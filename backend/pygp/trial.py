import guitarpro
import os


gps_folder = "/home/claudehu/Desktop/data/music/gps"

song = guitarpro.parse(os.path.join(gps_folder, "dyens_roland-la_javanaise.gp4"))
