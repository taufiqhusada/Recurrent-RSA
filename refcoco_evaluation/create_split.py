import json
import random

from collections import defaultdict

with open('dict_list_idx_class.json') as jsonFile:
    dict_list_idx_class = json.load(jsonFile)

with open('map_idx_to_imgs_id.json') as jsonFile:
    map_idx_to_imgs_id = json.load(jsonFile)

dict_list_distractor = defaultdict(list)
ideal_num_distractor = 4
for class_name in dict_list_idx_class:
    list_idx = dict_list_idx_class[class_name]
    if (len(list_idx)==1):
        dict_list_distractor[list_idx[0]] = []
    else:
        num_distractor = min(len(list_idx)-1, ideal_num_distractor)
        for idx in list_idx:
            while(True):
                list_distractor_idx = random.choices(list_idx, k=num_distractor)
                if (idx not in list_distractor_idx):
                    dict_list_distractor[idx] = list_distractor_idx
                    break

with open('dict_list_distractor.json', 'w') as jsonFile:
    json.dump(dict_list_distractor, jsonFile)                 
