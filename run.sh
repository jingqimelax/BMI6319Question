#!/bin/bash

py=python
featureextractor=/app/src/generate_feature_file.py
evaluation=/app/src/evaluation.py
train=/app/bin/liblinear-2.30/train
predict=/app/bin/liblinear-2.30/predict

input=/data/input/breast-cancer.data.csv
featrain=/data/working/train.fea
featest=/data/working/test.fea
model=/data/working/model.bin
predictret=/data/working/test.predict

set -x

#1. data wrangling, convert the input data into liblinear feature files;
$py $featureextractor $input $featrain $featest

#2. train
$train $featrain $model

#3. test
$predict $featest $model $predictret


for c in 0.1 0.5 1 1.5 2.0
do
    $train -c $c $featrain $model$c
    $predict $featest $model$c $predictret$c
    $evaluation $featest $predictret$c > $predictret$c.eval
done







