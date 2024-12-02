import os


def to_head(projectpath):
    """
    Generate the LaTeX header for the TikZ diagram.

    Parameters
    ----------
    projectpath : str
        The path to the project directory.

    Returns
    -------
    str
        LaTeX code for the document header.
    """
    pathlayers = os.path.join(projectpath, "layers/").replace("\\", "/")
    return (
        r"""
\documentclass[border=8pt, multi, tikz]{standalone}
\usepackage{import}
\subimport{"""
        + pathlayers
        + r"""}{init}
\usetikzlibrary{positioning}
\usetikzlibrary{3d} %for including external image
"""
    )


def to_cor():
    """
    Define color schemes for different layers.

    Parameters
    ----------
    None

    Returns
    -------
    str
        LaTeX code defining color schemes.
    """
    return r"""
\def\ConvColor{rgb:yellow,5;red,2.5;white,5}
\def\ConvReluColor{rgb:yellow,5;red,5;white,5}
\def\PoolColor{rgb:red,1;black,0.3}
\def\UnpoolColor{rgb:blue,2;green,1;black,0.3}
\def\FcColor{rgb:blue,5;red,2.5;white,5}
\def\FcReluColor{rgb:blue,5;red,5;white,4}
\def\SoftmaxColor{rgb:magenta,5;black,7}
\def\SumColor{rgb:blue,5;green,15}
"""


def to_begin():
    """
    Initialize the TikZ picture environment.

    Parameters
    ----------
    None

    Returns
    -------
    str
        LaTeX code to begin the TikZ environment.
    """
    return r"""
\newcommand{\copymidarrow}{\tikz \draw[-Stealth,line width=0.8mm,draw={rgb:blue,4;red,1;green,1;black,3}] (-0.3,0) -- ++(0.3,0);}

\begin{document}
\begin{tikzpicture}
\tikzstyle{connection}=[ultra thick,every node/.style={sloped,allow upside down},draw=\edgecolor,opacity=0.7]
\tikzstyle{copyconnection}=[ultra thick,every node/.style={sloped,allow upside down},draw={rgb:blue,4;red,1;green,1;black,3},opacity=0.7]
"""


# layers definition


def to_input(pathfile, to="(-3,0,0)", width=8, height=8, name="temp"):
    """
    Create an input node with an image.

    Parameters
    ----------
    pathfile : str
        Path to the input image file.
    to : str, optional
        Position coordinate, by default "(-3,0,0)".
    width : int, optional
        Width of the image in cm, by default 8.
    height : int, optional
        Height of the image in cm, by default 8.
    name : str, optional
        Name of the node, by default "temp".

    Returns
    -------
    str
        LaTeX code for the input node.
    """
    return (
        r"""
\node[canvas is zy plane at x=0] ("""
        + name
        + """) at """
        + to
        + """ {\includegraphics[width="""
        + str(width)
        + "cm"
        + """,height="""
        + str(height)
        + "cm"
        + """]{"""
        + pathfile
        + """}};
"""
    )


# Conv
def to_Conv(
    name,
    s_filer=256,
    n_filer=64,
    offset="(0,0,0)",
    to="(0,0,0)",
    width=1,
    height=40,
    depth=40,
    caption=" ",
):
    """
    Create a convolutional layer node.

    Parameters
    ----------
    name : str
        Name of the layer.
    s_filer : int, optional
        Size of the filter, by default 256.
    n_filer : int, optional
        Number of filters, by default 64.
    offset : str, optional
        Position offset, by default "(0,0,0)".
    to : str, optional
        Position to attach, by default "(0,0,0)".
    width : int, optional
        Width of the box, by default 1.
    height : int, optional
        Height of the box, by default 40.
    depth : int, optional
        Depth of the box, by default 40.
    caption : str, optional
        Caption for the layer, by default " ".

    Returns
    -------
    str
        LaTeX code for the convolutional layer.
    """
    return (
        r"""
\pic[shift={"""
        + offset
        + """}] at """
        + to
        + """
    {Box={
        name="""
        + name
        + """,
        caption="""
        + caption
        + r""",
        xlabel={{"""
        + str(n_filer)
        + """, }},
        zlabel="""
        + str(s_filer)
        + """,
        fill=\ConvColor,
        height="""
        + str(height)
        + """,
        width="""
        + str(width)
        + """,
        depth="""
        + str(depth)
        + """
        }
    };
"""
    )


# Conv,Conv,relu
# Bottleneck
def to_ConvConvRelu(
    name,
    s_filer=256,
    n_filer=(64, 64),
    offset="(0,0,0)",
    to="(0,0,0)",
    width=(2, 2),
    height=40,
    depth=40,
    caption=" ",
):
    """
    Create a convolutional layer followed by ReLU activation.

    Parameters
    ----------
    name : str
        Name of the layer.
    s_filer : int, optional
        Size of the filter, by default 256.
    n_filer : tuple of int, optional
        Number of filters, by default (64, 64).
    offset : str, optional
        Position offset, by default "(0,0,0)".
    to : str, optional
        Position to attach, by default "(0,0,0)".
    width : tuple of int, optional
        Width of the box, by default (2, 2).
    height : int, optional
        Height of the box, by default 40.
    depth : int, optional
        Depth of the box, by default 40.
    caption : str, optional
        Caption for the layer, by default " ".

    Returns
    -------
    str
        LaTeX code for the Conv-Conv-ReLU layer.
    """
    return (
        r"""
\pic[shift={ """
        + offset
        + """ }] at """
        + to
        + """
    {RightBandedBox={
        name="""
        + name
        + """,
        caption="""
        + caption
        + """,
        xlabel={{ """
        + str(n_filer[0])
        + """, """
        + str(n_filer[1])
        + """ }},
        zlabel="""
        + str(s_filer)
        + """,
        fill=\ConvColor,
        bandfill=\ConvReluColor,
        height="""
        + str(height)
        + """,
        width={ """
        + str(width[0])
        + """ , """
        + str(width[1])
        + """ },
        depth="""
        + str(depth)
        + """
        }
    };
"""
    )


# Pool
def to_Pool(
    name,
    offset="(0,0,0)",
    to="(0,0,0)",
    width=1,
    height=32,
    depth=32,
    opacity=0.5,
    caption=" ",
):
    """
    Create a pooling layer node.

    Parameters
    ----------
    name : str
        Name of the pooling layer.
    offset : str, optional
        Position offset, by default "(0,0,0)".
    to : str, optional
        Position to attach, by default "(0,0,0)".
    width : int, optional
        Width of the box, by default 1.
    height : int, optional
        Height of the box, by default 32.
    depth : int, optional
        Depth of the box, by default 32.
    opacity : float, optional
        Opacity of the box, by default 0.5.
    caption : str, optional
        Caption for the layer, by default " ".

    Returns
    -------
    str
        LaTeX code for the pooling layer.
    """
    return (
        r"""
\pic[shift={ """
        + offset
        + """ }] at """
        + to
        + """
    {Box={
        name="""
        + name
        + """,
        caption="""
        + caption
        + r""",
        fill=\PoolColor,
        opacity="""
        + str(opacity)
        + """,
        height="""
        + str(height)
        + """,
        width="""
        + str(width)
        + """,
        depth="""
        + str(depth)
        + """
        }
    };
"""
    )


# unpool4,
def to_UnPool(
    name,
    offset="(0,0,0)",
    to="(0,0,0)",
    width=1,
    height=32,
    depth=32,
    opacity=0.5,
    caption=" ",
):
    """
    Create an unpooling layer node.

    Parameters
    ----------
    name : str
        Name of the unpooling layer.
    offset : str, optional
        Position offset, by default "(0,0,0)".
    to : str, optional
        Position to attach, by default "(0,0,0)".
    width : int, optional
        Width of the box, by default 1.
    height : int, optional
        Height of the box, by default 32.
    depth : int, optional
        Depth of the box, by default 32.
    opacity : float, optional
        Opacity of the box, by default 0.5.
    caption : str, optional
        Caption for the layer, by default " ".

    Returns
    -------
    str
        LaTeX code for the unpooling layer.
    """
    return (
        r"""
\pic[shift={ """
        + offset
        + """ }] at """
        + to
        + """
    {Box={
        name="""
        + name
        + r""",
        caption="""
        + caption
        + r""",
        fill=\UnpoolColor,
        opacity="""
        + str(opacity)
        + """,
        height="""
        + str(height)
        + """,
        width="""
        + str(width)
        + """,
        depth="""
        + str(depth)
        + """
        }
    };
"""
    )


def to_ConvRes(
    name,
    s_filer=256,
    n_filer=64,
    offset="(0,0,0)",
    to="(0,0,0)",
    width=6,
    height=40,
    depth=40,
    opacity=0.2,
    caption=" ",
):
    """
    Create a convolutional residual layer node.

    Parameters
    ----------
    name : str
        Name of the residual layer.
    s_filer : int, optional
        Size of the filter, by default 256.
    n_filer : int, optional
        Number of filters, by default 64.
    offset : str, optional
        Position offset, by default "(0,0,0)".
    to : str, optional
        Position to attach, by default "(0,0,0)".
    width : int, optional
        Width of the box, by default 6.
    height : int, optional
        Height of the box, by default 40.
    depth : int, optional
        Depth of the box, by default 40.
    opacity : float, optional
        Opacity of the box, by default 0.2.
    caption : str, optional
        Caption for the layer, by default " ".

    Returns
    -------
    str
        LaTeX code for the convolutional residual layer.
    """
    return (
        r"""
\pic[shift={ """
        + offset
        + """ }] at """
        + to
        + """
    {RightBandedBox={
        name="""
        + name
        + """,
        caption="""
        + caption
        + """,
        xlabel={{ """
        + str(n_filer)
        + """, }},
        zlabel="""
        + str(s_filer)
        + r""",
        fill={rgb:white,1;black,3},
        bandfill={rgb:white,1;black,2},
        opacity="""
        + str(opacity)
        + """,
        height="""
        + str(height)
        + """,
        width="""
        + str(width)
        + """,
        depth="""
        + str(depth)
        + """
        }
    };
"""
    )


# ConvSoftMax
def to_ConvSoftMax(
    name,
    s_filer=40,
    offset="(0,0,0)",
    to="(0,0,0)",
    width=1,
    height=40,
    depth=40,
    caption=" ",
):
    """
    Create a convolutional softmax layer node.

    Parameters
    ----------
    name : str
        Name of the softmax layer.
    s_filer : int, optional
        Size of the filter, by default 40.
    offset : str, optional
        Position offset, by default "(0,0,0)".
    to : str, optional
        Position to attach, by default "(0,0,0)".
    width : int, optional
        Width of the box, by default 1.
    height : int, optional
        Height of the box, by default 40.
    depth : int, optional
        Depth of the box, by default 40.
    caption : str, optional
        Caption for the layer, by default " ".

    Returns
    -------
    str
        LaTeX code for the convolutional softmax layer.
    """
    return (
        r"""
\pic[shift={"""
        + offset
        + """}] at """
        + to
        + """
    {Box={
        name="""
        + name
        + """,
        caption="""
        + caption
        + """,
        zlabel="""
        + str(s_filer)
        + """,
        fill=\SoftmaxColor,
        height="""
        + str(height)
        + """,
        width="""
        + str(width)
        + """,
        depth="""
        + str(depth)
        + """
        }
    };
"""
    )


# SoftMax
def to_SoftMax(
    name,
    s_filer=10,
    offset="(0,0,0)",
    to="(0,0,0)",
    width=1.5,
    height=3,
    depth=25,
    opacity=0.8,
    caption=" ",
):
    """
    Create a softmax layer node.

    Parameters
    ----------
    name : str
        Name of the softmax layer.
    s_filer : int, optional
        Size of the filter, by default 10.
    offset : str, optional
        Position offset, by default "(0,0,0)".
    to : str, optional
        Position to attach, by default "(0,0,0)".
    width : float, optional
        Width of the box, by default 1.5.
    height : float, optional
        Height of the box, by default 3.
    depth : int, optional
        Depth of the box, by default 25.
    opacity : float, optional
        Opacity of the box, by default 0.8.
    caption : str, optional
        Caption for the layer, by default " ".

    Returns
    -------
    str
        LaTeX code for the softmax layer.
    """
    return (
        r"""
\pic[shift={"""
        + offset
        + """}] at """
        + to
        + """
    {Box={
        name="""
        + name
        + """,
        caption="""
        + caption
        + """,
        xlabel={{" ","dummy"}},
        zlabel="""
        + str(s_filer)
        + """,
        fill=\SoftmaxColor,
        opacity="""
        + str(opacity)
        + """,
        height="""
        + str(height)
        + """,
        width="""
        + str(width)
        + """,
        depth="""
        + str(depth)
        + """
        }
    };
"""
    )


def to_Sum(name, offset="(0,0,0)", to="(0,0,0)", radius=2.5, opacity=0.6):
    """
    Create a summation node.

    Parameters
    ----------
    name : str
        Name of the summation node.
    offset : str, optional
        Position offset, by default "(0,0,0)".
    to : str, optional
        Position to attach, by default "(0,0,0)".
    radius : float, optional
        Radius of the ball, by default 2.5.
    opacity : float, optional
        Opacity of the ball, by default 0.6.

    Returns
    -------
    str
        LaTeX code for the summation node.
    """
    return (
        r"""
\pic[shift={"""
        + offset
        + """}] at """
        + to
        + """
    {Ball={
        name="""
        + name
        + """,
        fill=\SumColor,
        opacity="""
        + str(opacity)
        + """,
        radius="""
        + str(radius)
        + """,
        logo=$+$
        }
    };
"""
    )


def to_connection(of, to):
    """
    Draw a connection between two nodes.

    Parameters
    ----------
    of : str
        Source node.
    to : str
        Target node.

    Returns
    -------
    str
        LaTeX code for the connection.
    """
    return (
        r"""
\draw [connection]  ("""
        + of
        + """-east)    -- node {\midarrow} ("""
        + to
        + """-west);
"""
    )


def to_skip(of, to, pos=1.25):
    """
    Create a skip connection between two nodes.

    Parameters
    ----------
    of : str
        Source node.
    to : str
        Target node.
    pos : float, optional
        Position ratio for the connection, by default 1.25.

    Returns
    -------
    str
        LaTeX code for the skip connection.
    """
    return (
        r"""
\path ("""
        + of
        + """-southeast) -- ("""
        + of
        + """-northeast) coordinate[pos="""
        + str(pos)
        + """] ("""
        + of
        + """-top) ;
\path ("""
        + to
        + """-south)  -- ("""
        + to
        + """-north)  coordinate[pos="""
        + str(pos)
        + """] ("""
        + to
        + """-top) ;
\draw [copyconnection]  ("""
        + of
        + """-northeast)
-- node {\copymidarrow}("""
        + of
        + """-top)
-- node {\copymidarrow}("""
        + to
        + """-top)
-- node {\copymidarrow} ("""
        + to
        + """-north);
"""
    )


def to_end():
    """
    End the TikZ picture environment.

    Parameters
    ----------
    None

    Returns
    -------
    str
        LaTeX code to end the TikZ environment.
    """
    return r"""
\end{tikzpicture}
\end{document}
"""


def to_generate(arch, pathname="file.tex"):
    """
    Generate the LaTeX file from the architecture list.

    Parameters
    ----------
    arch : list of str
        List of LaTeX commands.
    pathname : str, optional
        Path to the output .tex file, by default "file.tex".

    Returns
    -------
    None
    """
    with open(pathname, "w") as f:
        for c in arch:
            print(c)
            f.write(c)


def to_FullyConnected(
    name,
    s_filer=256,
    offset="(0,0,0)",
    to="(0,0,0)",
    width=1,
    height=2,
    depth=40,
    caption=" ",
):
    """
    Create a fully connected layer node.

    Parameters
    ----------
    name : str
        Name of the fully connected layer.
    s_filer : int, optional
        Size of the filter, by default 256.
    offset : str, optional
        Position offset, by default "(0,0,0)".
    to : str, optional
        Position to attach, by default "(0,0,0)".
    width : int, optional
        Width of the box, by default 1.
    height : int, optional
        Height of the box, by default 2.
    depth : int, optional
        Depth of the box, by default 40.
    caption : str, optional
        Caption for the layer, by default " ".

    Returns
    -------
    str
        LaTeX code for the fully connected layer.
    """
    return (
        r"""
\pic[shift={ """
        + offset
        + """ }] at """
        + to
        + """
    {Box={
        name="""
        + name
        + """,
        caption="""
        + caption
        + """,
        xlabel={{" ","dummy"}},
        zlabel="""
        + str(s_filer)
        + """,
        fill=\FcColor,
        height="""
        + str(height)
        + """,
        width="""
        + str(width)
        + """,
        depth="""
        + str(depth)
        + """
        }
    };
"""
    )
