#!/bin/sh
#SBATCH -J SFG_Search
#SBATCH -o job-%j.log
#SBATCH -e job-%j.err
#SBatch -p CPU-Large
#SBATCH -N 4 -n 64
cd /gpfs/home/quaninfo/yesunhuang/SFG
python SFG_search_Eg_3D.py
