import gdown
import os
#note to Daniel

'''Daniel  this code might take too long so it's preferable to 
 download the folders yourself manually and place them in a "datasets" folder'''


os.makedirs("datasets/AllZurich_outline_MLSD_Groundtruth", exist_ok=True)
os.makedirs("datasets/PNGAllzurich_tif_tiles_output", exist_ok=True)
os.makedirs("datasets/captions", exist_ok=True)

gdown.download_folder(
    "https://drive.google.com/drive/folders/1ipaukz56KNJtxnta5o_Uo62fRDqTa4HP",
    output="datasets/AllZurich_outline_MLSD_Groundtruth",
    quiet=False
)

gdown.download_folder(
    "https://drive.google.com/drive/folders/1rLzwuHvf6nq76IZSi-V9dxi__3fEYuqV",
    output="datasets/PNGAllzurich_tif_tiles_output",
    quiet=False
)

gdown.download_folder(
    "https://drive.google.com/drive/folders/1dTIPY90IeHd-WTzBObZxzWa5uzjWPH0V",
    output="datasets/captions",
    quiet=False
)