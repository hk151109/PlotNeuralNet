from .tikzeng import *


# define new block
def block_2ConvPool(
    name,
    botton,
    top,
    s_filer=256,
    n_filer=64,
    offset="(1,0,0)",
    size=(32, 32, 3.5),
    opacity=0.5,
):
    """
    Create a block with two convolutional layers followed by a pooling layer.

    Parameters
    ----------
    name : str
        Base name for the layers in the block.
    botton : str
        The node from which the block starts.
    top : str
        The node where the block ends.
    s_filer : int, optional
        Size of the filter, by default 256.
    n_filer : int, optional
        Number of filters, by default 64.
    offset : str, optional
        Position offset, by default "(1,0,0)".
    size : tuple of int, optional
        Size dimensions (height, depth, width), by default (32, 32, 3.5).
    opacity : float, optional
        Opacity for the pooling layer, by default 0.5.

    Returns
    -------
    list of str
        LaTeX code for the convolutional and pooling layers.
    """
    return [
        to_ConvConvRelu(
            name=rf"ccr_{name}",
            s_filer=rf"{s_filer}",
            n_filer=(rf"{n_filer}", rf"{n_filer}"),
            offset=rf"{offset}",
            to=rf"({botton}-east)",
            width=(size[2], size[2]),
            height=size[0],
            depth=size[1],
        ),
        to_Pool(
            name=rf"{top}",
            offset=rf"(0,0,0)",
            to=rf"ccr_{name}-east",
            width=1,
            height=size[0] - int(size[0] / 4),
            depth=size[1] - int(size[0] / 4),
            opacity=opacity,
        ),
        to_connection(rf"{botton}", rf"ccr_{name}"),
    ]


def block_Unconv(
    name,
    botton,
    top,
    s_filer=256,
    n_filer=64,
    offset="(1,0,0)",
    size=(32, 32, 3.5),
    opacity=0.5,
):
    """
    Create a block with an unpooling layer and convolutional layers.

    Parameters
    ----------
    name : str
        Base name for the layers in the block.
    botton : str
        The node from which the block starts.
    top : str
        The node where the block ends.
    s_filer : int, optional
        Size of the filter, by default 256.
    n_filer : int, optional
        Number of filters, by default 64.
    offset : str, optional
        Position offset, by default "(1,0,0)".
    size : tuple of int, optional
        Size dimensions (height, depth, width), by default (32, 32, 3.5).
    opacity : float, optional
        Opacity for the layers, by default 0.5.

    Returns
    -------
    list of str
        LaTeX code for the unpooling and convolutional layers.
    """
    return [
        to_UnPool(
            name=rf"unpool_{name}",
            offset=rf"{offset}",
            to=rf"({botton}-east)",
            width=1,
            height=size[0],
            depth=size[1],
            opacity=opacity,
        ),
        to_ConvRes(
            name=rf"ccr_res_{name}",
            offset=rf"(0,0,0)",
            to=rf"unpool_{name}-east",
            s_filer=rf"{s_filer}",
            n_filer=rf"{n_filer}",
            width=size[2],
            height=size[0],
            depth=size[1],
            opacity=opacity,
        ),
        to_Conv(
            name=rf"ccr_{name}",
            offset=rf"(0,0,0)",
            to=rf"ccr_res_{name}-east",
            s_filer=rf"{s_filer}",
            n_filer=rf"{n_filer}",
            width=size[2],
            height=size[0],
            depth=size[1],
        ),
        to_ConvRes(
            name=rf"ccr_res_c_{name}",
            offset=rf"(0,0,0)",
            to=rf"ccr_{name}-east",
            s_filer=rf"{s_filer}",
            n_filer=rf"{n_filer}",
            width=size[2],
            height=size[0],
            depth=size[1],
            opacity=opacity,
        ),
        to_Conv(
            name=rf"{top}",
            offset=rf"(0,0,0)",
            to=rf"ccr_res_c_{name}-east",
            s_filer=rf"{s_filer}",
            n_filer=rf"{n_filer}",
            width=size[2],
            height=size[0],
            depth=size[1],
        ),
        to_connection(rf"{botton}", rf"unpool_{name}"),
    ]


def block_Res(
    num,
    name,
    botton,
    top,
    s_filer=256,
    n_filer=64,
    offset="(0,0,0)",
    size=(32, 32, 3.5),
    opacity=0.5,
):
    """
    Create a residual block with multiple convolutional layers and a skip connection.

    Parameters
    ----------
    num : int
        Number of convolutional layers in the block.
    name : str
        Base name for the layers in the block.
    botton : str
        The node from which the block starts.
    top : str
        The node where the block ends.
    s_filer : int, optional
        Size of the filter, by default 256.
    n_filer : int, optional
        Number of filters, by default 64.
    offset : str, optional
        Position offset, by default "(0,0,0)".
    size : tuple of int, optional
        Size dimensions (height, depth, width), by default (32, 32, 3.5).
    opacity : float, optional
        Opacity for the skip connection, by default 0.5.

    Returns
    -------
    list of str
        LaTeX code for the residual block.
    """
    lys = []
    layers = [rf"{name}_{i}" for i in range(num - 1)] + [rf"{top}"]
    for layer_name in layers:
        ly = [
            to_Conv(
                name=rf"{layer_name}",
                offset=rf"{offset}",
                to=rf"({botton}-east)",
                s_filer=rf"{s_filer}",
                n_filer=rf"{n_filer}",
                width=size[2],
                height=size[0],
                depth=size[1],
            ),
            to_connection(rf"{botton}", rf"{layer_name}"),
        ]
        botton = layer_name
        lys += ly

    lys += [
        to_skip(of=layers[1], to=layers[-2], pos=1.25),
    ]
    return lys
