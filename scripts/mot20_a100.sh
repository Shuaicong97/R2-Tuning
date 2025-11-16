#!/bin/bash -l

#SBATCH --job-name=train_mot20_r2_a100
#SBATCH --time=24:00:00
#SBATCH --gres=gpu:a100:1
#SBATCH --output=/home/atuin/v100dd/v100dd19/sbatch_r2/result-%x-%j.txt
#SBATCH -C a100_80

PYTHONPATH=$PYTHONPATH:. python tools/launch.py configs/qvhighlights/r2_tuning_mot20.py
