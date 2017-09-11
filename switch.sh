#!/bin/bash

rm -f /usr/include/cudnn.h
rm -f /usr/lib/x86_64-linux-gnu/*libcudnn*
rm -f /usr/local/cuda-*/lib64/*libcudnn*


cp -P packages/cudnn/include/cudnn.h /usr/include
cp -P packages/cudnn/lib64/libcudnn* /usr/lib/x86_64-linux-gnu/
chmod a+r /usr/lib/x86_64-linux-gnu/libcudnn*

rm -rf packages/cudnn
