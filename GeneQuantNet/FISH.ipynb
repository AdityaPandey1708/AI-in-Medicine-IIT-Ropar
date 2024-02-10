{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e421e284",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Conversion completed successfully.\n"
     ]
    }
   ],
   "source": [
    "from PIL import Image\n",
    "import os\n",
    "import shutil\n",
    "import random\n",
    "\n",
    "# Set the input and output directories\n",
    "input_directory = r\"/Users/adityapandey/Desktop/IIT Ropar/input2\"\n",
    "output_directory = r\"/Volumes/SUPER/OnlyCellData/Cases\"\n",
    "\n",
    "# CSV file directory for spots\n",
    "spots_csv_directory = r\"/Volumes/SUPER/ContrastData/Cases/spots\"\n",
    "\n",
    "# Create the output directories if they don't exist\n",
    "os.makedirs(output_directory, exist_ok=True)\n",
    "os.makedirs(os.path.join(output_directory, 'images'), exist_ok=True)\n",
    "os.makedirs(os.path.join(output_directory, 'labels'), exist_ok=True)\n",
    "heatmaps_folder = os.path.join(output_directory, 'HeatMaps')\n",
    "os.makedirs(heatmaps_folder, exist_ok=True)\n",
    "heatmap_folder = os.path.join(heatmaps_folder, 'HeatMap')\n",
    "heatmap_all_folder = os.path.join(heatmaps_folder, 'HeatMap_all')\n",
    "os.makedirs(heatmap_folder, exist_ok=True)\n",
    "os.makedirs(heatmap_all_folder, exist_ok=True)\n",
    "os.makedirs(os.path.join(output_directory, 'spots'), exist_ok=True)\n",
    "\n",
    "# Process each image\n",
    "for filename in os.listdir(input_directory):\n",
    "    if filename.endswith(\".tif\") and not filename.startswith(\"._\"):\n",
    "        # Open the image\n",
    "        image_path = os.path.join(input_directory, filename)\n",
    "        img = Image.open(image_path)\n",
    "\n",
    "        # Resize the image to 256x256\n",
    "        img_resized = img.resize((256, 256))\n",
    "\n",
    "        # Save as JPG in the 'images' folder\n",
    "        img_resized.save(os.path.join(output_directory, 'images', f\"{os.path.splitext(filename)[0]}_image.jpg\"))\n",
    "\n",
    "        # Save as PNG in the 'labels' folder\n",
    "        img_resized.save(os.path.join(output_directory, 'labels', f\"{os.path.splitext(filename)[0]}_label.png\"))\n",
    "\n",
    "        # Save as JPG in the 'HeatMap' folder\n",
    "        img_resized.save(os.path.join(heatmap_folder, f\"{os.path.splitext(filename)[0]}_gaumap.jpg\"))\n",
    "\n",
    "        # Save as JPG in the 'HeatMap_all' folder\n",
    "        img_resized.save(os.path.join(heatmap_all_folder, f\"{os.path.splitext(filename)[0]}_gaumap_all.jpg\"))\n",
    "\n",
    "        # Pick a random CSV file from spots_csv_directory\n",
    "        csv_files = [file for file in os.listdir(spots_csv_directory) if file.endswith(\".csv\")]\n",
    "        if csv_files:\n",
    "            random_csv_file = random.choice(csv_files)\n",
    "            csv_file_path = os.path.join(spots_csv_directory, random_csv_file)\n",
    "\n",
    "            # Create spots folder within the output directory\n",
    "            spots_folder = os.path.join(output_directory, 'spots')\n",
    "            os.makedirs(spots_folder, exist_ok=True)\n",
    "\n",
    "            # Copy the CSV file to the spots folder with the desired name\n",
    "            output_csv_name = f\"{os.path.splitext(filename)[0]}_spot.csv\"\n",
    "            output_csv_path = os.path.join(spots_folder, output_csv_name)\n",
    "            shutil.copy(csv_file_path, output_csv_path)\n",
    "\n",
    "print(\"Conversion completed successfully.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "5d3c7f94",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2024-02-02 17:48:35,339 [INFO] WRITING LOG OUTPUT TO /Users/adityapandey/.GeneSegNet/GeneSegNet.log\n",
      "2024-02-02 17:48:35,339 [INFO] >>>> START TEST\n",
      "2024-02-02 17:48:35,342 [INFO] TORCH CUDA version not installed/working.\n",
      "2024-02-02 17:48:35,342 [INFO] >>>> using CPU\n",
      "['.DS_Store', 'Cases']\n",
      "['Cases']\n",
      "2024-02-02 17:48:35,346 [INFO] not all flows are present, running flow generation for all images\n",
      "2024-02-02 17:48:35,386 [INFO] 14 / 14 images in /Users/adityapandey/Documents/OData/Cases folder have labels\n",
      "2024-02-02 17:48:35,389 [INFO] >>>> running GeneSegNet on 14 images\n",
      "2024-02-02 17:48:35,389 [INFO] >>>> loading model /Users/adityapandey/Downloads/GeneSegNet_hippocampus_residual_on_style_on_concatenation_off.929131_epoch_499\n",
      "2024-02-02 17:48:35,389 [INFO] WARNING: MKL version on torch not working/installed - CPU version will be slightly slower.\n",
      "2024-02-02 17:48:35,389 [INFO] see https://pytorch.org/docs/stable/backends.html?highlight=mkl\n",
      "2024-02-02 17:48:35,521 [INFO] >>>> model diam_mean =  34.000 (ROIs rescaled to this size during training)\n",
      "2024-02-02 17:48:35,522 [INFO] >>>> model diam_labels =  62.429 (mean diameter of training ROIs)\n",
      "2024-02-02 17:48:35,522 [INFO] >>>> save predicted results\n",
      "2024-02-02 17:48:50,775 [INFO] >>>> finish test in 15.434 sec\n",
      "2024-02-02 17:48:50,777 [INFO] >>>> finsh test\n",
      "\u001b[0m"
     ]
    }
   ],
   "source": [
    "!python ./GeneSegNet/GeneSeg_test.py --verbose --use_gpu --test_dir \"/Users/adityapandey/Documents/OData\" --pretrained_model \"/Users/adityapandey/Downloads/GeneSegNet_hippocampus_residual_on_style_on_concatenation_off.929131_epoch_499\" --save_png --img_filter _image --mask_filter _label --all_channels --metrics --dir_above --output_filename \"/Users/adityapandey/Documents/OData/labels\""
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
