#!/bin/sh
#SBATCH -J SFG_Search
#SBATCH -o job-%j.log
#SBATCH -e job-%j.err
#SBATCH -N 4 -n 8
cd /gpfs/home/quaninfo/yesunhuang/SFG
conda activate sfg_dev
python SFG_search.py
