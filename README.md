

## 🧪 Clone and Install Diffusers from Source (I think there might be a better way to installing these requirements)

```bash
git clone https://github.com/huggingface/diffusers
cd diffusers
pip install -e .
```

---

## Install ControlNet Example Requirements

```bash
cd examples/controlnet
pip install -r requirements.txt
```

---

##  Additional Dependencies

```bash
pip install gdown tqdm accelerate peft wandb opencv-python
```
(Apologies if I forgot any dependencies, you gotta count on the errors in that once Daniel xD) 
---

## Accelerate

```bash
accelerate config default
```

---

## 📁 Dataset Preparation

### Option 1: Manual Download (Recommended)

- Place **MLSD outlines** in:  
  `datasets/AllZurich_outline_MLSD_Groundtruth`
  
    https://drive.google.com/drive/folders/1ipaukz56KNJtxnta5o_Uo62fRDqTa4HP

- Place **target images** in:  
  `datasets/PNGAllzurich_tif_tiles_output`
  
    https://drive.google.com/drive/folders/1rLzwuHvf6nq76IZSi-V9dxi__3fEYuqV"

- Place **captions** in:  
  `datasets/captions/`

    https://drive.google.com/drive/folders/1dTIPY90IeHd-WTzBObZxzWa5uzjWPH0V
---

### Option 2: Script Download

> ⚠️ This method is **super slow** Daniel because of gdown

```bash
python prepare_data.py
```

---

## 🧱 Create Dataset Loader

Generate the `prompt.json` mapping file:

```bash
python Create_loader.py
```

This creates a dictionary mapping between hints, targets, and captions.

---

## 🧰 Model Setup

- Download the **RealisticVision** model manually.

---

## 🚀 Execute the Training Command

```bash
accelerate launch train_control_lora.py   --pretrained_model_name_or_path="path_to_realistic_vision"   --output_dir="control-lora-model"   --conditioning_image_column="hint"   --image_column="jpg"   --caption_column="txt"   --resolution=512   --learning_rate=1e-4   --train_batch_size=4   --num_train_epochs=4   --max_train_steps=100000   --tracker_project_name="control-lora"   --checkpointing_steps=5000   --validation_steps=5000   --report_to wandb   --use_lora   --lora_r=32   --lora_bias="all"   --custom_dataset="custom.MyDataset"
```

---

