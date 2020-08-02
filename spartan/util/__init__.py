#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Desc    :   Import part and configuration part, including names exposed to spartan.
'''

# here put the import lib

from spartan.tensor import TensorData, TensorStream

from .ioutil import loadTensor, File, loadTensorStream
from .basicutil import set_trace, TimeMapper, StringMapper,\
    IntMapper, ScoreMapper, DenseIntMapper
    IntMapper, ScoreMapper, IntRemapper
from .drawutil import plot_graph, drawEigenPulse

MODEL_PATH = 'spartan.model'

__all__ = [
    'loadTensor',
    'File',
    'loadTensorStream',
    'set_trace',
    'TimeMapper',
    'StringMapper',
    'IntMapper',
    'ScoreMapper',
    'DenseIntMapper',
    'plot_graph'
    'IntRemapper',
    'plot_graph',
    'drawEigenPulse'
]
