#!/bin/sh
#SBATCH -J SFG_Search
#SBATCH -o job-%j.log
#SBATCH -e job-%j.err
#SBATCH -N 16 -n 128
cd /gpfs/home/quaninfo/yesunhuang/SFG
python SFG_search_Eg.py
