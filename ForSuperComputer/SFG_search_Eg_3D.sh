#!/bin/sh
#SBATCH -J SFG_Search
#SBATCH -o job-%j.log
#SBATCH -e job-%j.err
#SBATCH -n 64
cd /gpfs/home/quaninfo/yesunhuang/SFG
python SFG_search_Eg_3D.py
