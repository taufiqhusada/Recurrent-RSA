#!/bin/bash -l

#$ -l h_rt=48:00:00   # Specify the hard time limit for the job
#$ -N reuben_rsa_refcoco # Give job a name
#$ -j y               # Merge the error and output streams into a single file
#$ -V
#$ -m

python run_all_refcoco.py 0 1000
python run_all_refcoco.py 0 2000
python run_all_refcoco.py 0 3000
python run_all_refcoco.py 0 4000
python run_all_refcoco.py 0 5000
