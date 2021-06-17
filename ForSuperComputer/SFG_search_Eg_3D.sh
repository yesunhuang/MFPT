#!/bin/sh
#SBATCH -J SFG_Search
#SBATCH -o job-%j.log
#SBATCH -e job-%j.err
#SBATCH -p CPU-Large
#SBATCH --qos=jobnumlimit
#SBATCH -N 4 -n 32
cd /gpfs/home/quaninfo/yesunhuang/SFG
python SFG_search_Eg_3D.py
