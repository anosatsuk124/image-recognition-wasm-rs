# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import os
import sys

ROOT = os.getcwd()
WORK = os.path.join(ROOT, "../data/")
MODEL = "20180402-114759"

# force tf2onnx to cpu
os.environ['CUDA_VISIBLE_DEVICES'] = "0"
os.environ['MODEL'] = MODEL
os.environ['WORK'] = WORK

# %%
# !python -m tf2onnx.convert --graphdef $WORK/$MODEL/$MODEL.pb --output $WORK/$MODEL.onnx --inputs input0:0,input1:0 --outputs output0:1:

# %%
