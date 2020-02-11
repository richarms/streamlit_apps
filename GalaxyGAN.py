from __future__ import absolute_import, division, print_function, unicode_literals
import streamlit as st
import pandas as pd
import numpy as np

import tensorflow as tf

import glob
import imageio
import matplotlib.pyplot as plt
import numpy as np
import os

import PIL
from tensorflow.keras import layers
import time

from IPython import display

checkpoint_dir = './training_checkpoints'
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)

status = checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))

st.title('Galaxy GAN')
st.subheader("A Generative Adverserial Network trained on the FRICAT, FRIICAT, and NVSS sample of extended radio galaxies. Click the button to perform inference on this model.")

st.subheader("Button")
st.subheader("")
w1 = st.button("Generate Radio Galaxy from GAN Model")
st.write(w1)

if w1:
    st.write("Hello, Interactive Streamlit!")


