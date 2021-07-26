# this code will generate a literal caption and a pragmatic caption (referring expression) for the first of the urls provided in the context of the rest
import sys

import matplotlib
matplotlib.use('Agg')
import re
import requests
import time
import pickle
import tensorflow as tf
import numpy as np
from keras.preprocessing import image
from collections import defaultdict

from utils.config import *
from utils.numpy_functions import uniform_vector, make_initial_prior
from recursion_schemes.recursion_schemes import ana_greedy,ana_beam
from bayesian_agents.joint_rsa import RSA

import json
import os
from tqdm import tqdm

def process_this_id(id, dict_list_idx_class, map_idx_to_imgs_id, dict_list_distractor, result_crop_folder_path):
	id = str(id)
	urls = [os.path.join(result_crop_folder_path, f'{map_idx_to_imgs_id[id]}.jpg')]
	for id_distractor in dict_list_distractor[id]:
		urls.append(os.path.join(result_crop_folder_path, f'{map_idx_to_imgs_id[id]}.jpg'))

	# urls = [
	# 	"https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Arriva_T6_nearside.JPG/1200px-Arriva_T6_nearside.JPG",
	# 	"https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/First_Student_IC_school_bus_202076.jpg/220px-First_Student_IC_school_bus_202076.jpg"
	# 	]

	# code is written to be able to jointly infer speaker's rationality and neural model, but for simplicity, let's assume these are fixed
	# the rationality of the S1
	rat = [100.0]
	# the neural model: captions trained on MSCOCO ("coco") are more verbose than VisualGenome ("vg")
	model = ["vg"]
	number_of_images = len(urls)
	# the model starts of assuming it's equally likely any image is the intended referent
	initial_image_prior=uniform_vector(number_of_images)
	initial_rationality_prior=uniform_vector(1)
	initial_speaker_prior=uniform_vector(1)
	initial_world_prior = make_initial_prior(initial_image_prior,initial_rationality_prior,initial_speaker_prior)

	# make a character level speaker, using torch model (instead of tensorflow model)
	speaker_model = RSA(seg_type="char",tf=False)
	speaker_model.initialize_speakers(model)
	# set the possible images and rationalities
	speaker_model.speaker_prior.set_features(images=urls,tf=False,rationalities=rat)
	speaker_model.initial_speakers[0].set_features(images=urls,tf=False,rationalities=rat)
	# generate a sentence by unfolding stepwise, from the speaker: greedy unrolling used here, not beam search: much better to use beam search generally
	literal_caption = ana_greedy(
		speaker_model,
		target=0,
		depth=0,
		speaker_rationality=0,
		speaker=0,
		start_from=list(""),
		initial_world_prior=initial_world_prior)

	pragmatic_caption = ana_greedy(
		speaker_model,
		target=0,
		depth=1,
		speaker_rationality=0,
		speaker=0,
		start_from=list(""),
		initial_world_prior=initial_world_prior)

	print("Literal caption:\n",literal_caption)
	print("Pragmatic caption:\n",pragmatic_caption)

	output_literal_caption = (literal_caption[0][0], str(literal_caption[0][1]))
	output_pragmatic_caption = (pragmatic_caption[0][0], str(pragmatic_caption[0][1]))
  
	return output_literal_caption, output_pragmatic_caption

if __name__=='__main__':	
	idx_from = int(sys.argv[1])
	idx_to = int(sys.argv[2])
	print(idx_from, idx_to)

	with open('refcoco_evaluation/dict_list_idx_class.json') as jsonFile:
		dict_list_idx_class = json.load(jsonFile)
	with open('refcoco_evaluation/map_idx_to_imgs_id.json') as jsonFile:
		map_idx_to_imgs_id = json.load(jsonFile)
	with open('refcoco_evaluation/dict_list_distractor.json') as jsonFile:
		dict_list_distractor = json.loads(jsonFile.read())

	result_crop_folder_path = 'cropped'

	result_literal_caption = {}
	result_pragmatic_caption = {}
	for i in tqdm(range(idx_from, idx_to)):
 		try:
		    literal_caption, pragmatic_caption = process_this_id(i, dict_list_idx_class, map_idx_to_imgs_id, dict_list_distractor, result_crop_folder_path)	
		    result_literal_caption[i] = literal_caption
		    result_pragmatic_caption[i] = pragmatic_caption
 		except Exception:
		    result_literal_caption[i] = 'ERROR'
		    result_pragmatic_caption[i] = 'ERROR'

	
	with open(f'refcoco_evaluation/result_literal_caption_{idx_from}_{idx_to}.json', 'w') as jsonFile:
		json.dump(result_literal_caption, jsonFile)     
	with open(f'refcoco_evaluation/result_pragmatic_caption_{idx_from}_{idx_to}.json', 'w') as jsonFile:
		json.dump(result_pragmatic_caption, jsonFile)      
