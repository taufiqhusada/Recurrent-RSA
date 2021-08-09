# Evaluation on refcoco dataset
Evaluating Recurrent RSA on refcoco test dataset 

## Generated Expression Result
- on the file `recurrentRSA_generated_pragmatic_exps.json`

## Score
- bleu-1: 0.168943800017137
- rouge1: 0.14807628272710655
- rougeL: 0.14305185991986696
- meteor: 0.13534073040601782

## Note
- I only evaluated it on 4984 images on refcoco test dataset (not in all 5000 images), because there is an error when loading some images (somehow some image loaded as a grayscale image whereas the RSA needs an input of RGB image)
