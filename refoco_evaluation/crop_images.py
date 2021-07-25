import json
import os
from PIL import Image
from tqdm import tqdm

imgs_folder_path = '/content/imgs_by_id'
labels_folder_path = '/content/labels'

result_crop_folder_path = '/content/cropped'

dict_list_idx_class = json.load('dict_list_idx_class.json')
map_idx_to_imgs_id = json.load('map_idx_to_imgs_id.json')

for i in tqdm(range(5000)):
    label = json.load(os.path.join(labels_folder_path, f'lab_{i}.json'))
    bbox = label.bbox[0]
    im = Image.open(os.path.join(imgs_folder_path, f'{map_idx_to_imgs_id[i]}.jpg'))
    cropped_img = im.crop((bbox[0],bbox[1],bbox[2],bbox[3]))
    cropped_img.save(os.path.join(result_crop_folder_path, f'{map_idx_to_imgs_id[i]}.jpg'))





