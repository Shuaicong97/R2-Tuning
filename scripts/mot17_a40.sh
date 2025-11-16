#!/bin/bash -l

#SBATCH --job-name=train_ovis_r2_a40
#SBATCH --time=24:00:00
#SBATCH --gres=gpu:a40:1
#SBATCH --output=/home/atuin/v100dd/v100dd19/sbatch_r2/result-%x-%j.txt

PYTHONPATH=$PYTHONPATH:. python tools/launch.py configs/qvhighlights/r2_tuning_ovis.py
