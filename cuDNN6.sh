#!/bin/bash

rm -f /usr/include/cudnn.h
rm -f /usr/lib/x86_64-linux-gnu/libcudnn.so
rm -f /usr/lib/x86_64-linux-gnu/libcudnn.so.5
rm -f /usr/lib/x86_64-linux-gnu/libcudnn.so.5.1.10
rm -f /usr/lib/x86_64-linux-gnu/libcudnn_static.a

rm -f /usr/local/cuda-8.0/lib64/libcudnn.so
rm -f /usr/local/cuda-8.0/lib64/libcudnn.so.5
rm -f /usr/local/cuda-8.0/lib64/libcudnn.so.5.1.10
rm -f /usr/local/cuda-8.0/lib64/libcudnn_static.a

rm -f /usr/lib/x86_64-linux-gnu/libcudnn.so
rm -f /usr/lib/x86_64-linux-gnu/libcudnn.so.7
rm -f /usr/lib/x86_64-linux-gnu/libcudnn.so.7.0.1
rm -f /usr/lib/x86_64-linux-gnu/libcudnn_static.a

rm -f /usr/local/cuda-8.0/lib64/libcudnn.so
rm -f /usr/local/cuda-8.0/lib64/libcudnn.so.7
rm -f /usr/local/cuda-8.0/lib64/libcudnn.so.7.0.1
rm -f /usr/local/cuda-8.0/lib64/libcudnn_static.a


cp -P packages/cudnn6/include/cudnn.h /usr/include
cp -P packages/cudnn6/lib64/libcudnn* /usr/lib/x86_64-linux-gnu/
chmod a+r /usr/lib/x86_64-linux-gnu/libcudnn*

# printf "\nSwitched to cuDNN v6.0\n"
