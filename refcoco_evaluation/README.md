# Evaluation this approach on refcoco dataset
Evaluating Recurrent RSA on refcoco test dataset 

## Generated Expression Result
- on the folder `result`

## Score
- Bleu-1 score: 0.1944833034026393 (on the file `Calculate_score_reuben.ipynb`)

## Steps
1. crop all images on the refcoco test dataset to get only the target, the result of cropped images is on folder `cropped` in this gdrive `https://drive.google.com/drive/folders/1HrCVW500Uak7TG7lMywwMWWSEp5Incnc?usp=sharing`
2. for each id, get the class name using REFER library. The result is on `dict_list_idx_class.json` (I grouped ids for each class)
3. for each id, pick some images that has the same class with that target as a distractors. The list of distractor that I choose randomly is on file `dict_list_distractor.json` (the number of distractor that I choose is min(4, n-1))
4. run the RSA using script `../run_all_refcoco.sh`
5. the generated expressions will be generated on folder `result`
6. evaluate the score using code from `Calculate_score_reuben.ipynb` 

## Note
- I only evaluated it on 4984 images on refcoco test dataset (not in all 5000 images), because there is an error when loading some images (somehow some image loaded as a grayscale image whereas the RSA needs an input of RGB image)

## References
- `https://github.com/lichengunc/refer`

