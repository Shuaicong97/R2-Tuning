#!/bin/bash -l

#SBATCH --job-name=r2_mot20_test
#SBATCH --time=24:00:00
#SBATCH --gres=gpu:a40:1
#SBATCH --output=/home/atuin/v100dd/v100dd19/sbatch_r2/result-%x-%j.txt

python tools/launch.py configs/qvhighlights/r2_tuning_mot20.py --checkpoint /home/atuin/v100dd/v100dd19/R2-Tuning/work_dirs/r2_tuning_mot20/epoch_30.pth --eval --work_dir /home/atuin/v100dd/v100dd19/R2-Tuning/outputs/mot20