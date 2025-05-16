#  prompt.json (I'm doing what he is doing to not change too much of his code)
import json
import os
from tqdm import tqdm

data = []
for filename in tqdm(os.listdir("./datasets/AllZurich_outline_MLSD_Groundtruth")[:50]):
    if filename.endswith(".png"):
        base_name = os.path.splitext(filename)[0].split("_mask")[0]
        
        target_path = f"./datasets/PNGAllzurich_tif_tiles_output/{base_name}.png"
        caption_path = f"./datasets/captions/{base_name}.txt"
        
        if os.path.exists(target_path) and os.path.exists(caption_path):
            with open(caption_path, "r") as f:
                caption = f.read().strip()
            
            data.append({
                "source": f"./datasets/AllZurich_outline_MLSD_Groundtruth/{filename}",
                "target": target_path,
                "prompt": caption
            })

with open("./datasets/prompt.json", "w") as f:
    for item in data:
        f.write(json.dumps(item) + "\n")
