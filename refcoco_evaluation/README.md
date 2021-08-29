# Evaluation on refcoco dataset
Evaluating Recurrent RSA on refcoco test dataset 

## Generated Expression Result
- on the file `recurrentRSA_generated_pragmatic_exps.json`

## Note
- I only evaluated it on 4984 images on refcoco test dataset (not in all 5000 images), because there is an error when loading some images (somehow some image loaded as a grayscale image whereas the RSA needs an input of RGB image)

## Steps to reproduce result
1. for each image in refcoco dataset, crop all the objects based on detectron detection. Then create a folder structure like this
```
cropped_imgs_RecurrentRSA
    - <id>
        - target.jpg
        - distractor_<0>.jpg
        - distractor_<1>.jpg
        - ...
```
2. in file `../run_all_refcoco.py` change the `CROPPED_IMG_FOLDER`
3. go to root directory `cd ..`
4. run `sh run_all_refcoco.sh`
