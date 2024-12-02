"""
PyCore submodule.

Core functionalities for PlotNeuralNet, including TikZ primitives and block definitions.
"""

from .blocks import block_2ConvPool, block_Res, block_Unconv
from .tikzeng import (
    to_begin,
    to_connection,
    to_Conv,
    to_ConvConvRelu,
    to_ConvRes,
    to_ConvSoftMax,
    to_cor,
    to_end,
    to_FullyConnected,
    to_generate,
    to_head,
    to_input,
    to_Pool,
    to_skip,
    to_SoftMax,
    to_Sum,
    to_UnPool,
)

__all__ = [
    "block_2ConvPool",
    "block_Res",
    "block_Unconv",
    "to_begin",
    "to_connection",
    "to_Conv",
    "to_ConvConvRelu",
    "to_ConvRes",
    "to_ConvSoftMax",
    "to_cor",
    "to_end",
    "to_FullyConnected",
    "to_generate",
    "to_head",
    "to_input",
    "to_Pool",
    "to_skip",
    "to_SoftMax",
    "to_Sum",
    "to_UnPool",
]
