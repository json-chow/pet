#!/bin/bash

python cli.py \
--method sequence_classifier \
--pattern_ids 0 1 2 3 \
--data_dir data/ \
--model_type roberta \
--model_name_or_path roberta-base \
--task_name hypo \
--output_dir output_supervised \
--overwrite_output_dir \
--do_train \
--do_eval