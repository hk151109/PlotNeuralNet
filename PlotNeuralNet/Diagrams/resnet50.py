import sys
from PlotNeuralNet.PyCore.TikzGen import (
    ToBegin,
    ToConnection,
    ToConv,
    ToCor,
    ToEnd,
    ToGenerate,
    ToHead,
    ToPool,
    ToSoftMax,
    ToSum,
)

# Helper for bottleneck residual block (1x1 -> 3x3 -> 1x1)
def ResBlock(name, s_filter, offset, to, height, depth, width, caption=""):
    return [
        ToConv(f"{name}_conv1", s_filter, s_filter, offset=offset, to=to, height=height, depth=depth, width=1, caption="1x1"),
        ToConv(f"{name}_conv2", s_filter, s_filter, offset="{(1,0,0)}", to=f"({name}_conv1-east)", height=height, depth=depth, width=2, caption="3x3"),
        ToConv(f"{name}_conv3", s_filter*4, s_filter*4, offset="{(1,0,0)}", to=f"({name}_conv2-east)", height=height, depth=depth, width=1, caption="1x1"),
        ToConnection(f"{name}_conv1", f"{name}_conv2"),
        ToConnection(f"{name}_conv2", f"{name}_conv3"),
    ]

# Define ResNet-50 architecture
arch = [
    ToHead(".."),
    ToCor(),
    ToBegin(),

    # Stem
    ToConv("conv1", 64, 64, offset="{(0,0,0)}", to="(0,0,0)", height=80, depth=80, width=2, caption="7x7 Conv"),
    ToPool("pool1", offset="{(1,0,0)}", to="(conv1-east)", height=40, depth=40, width=1, caption="3x3 MaxPool"),

    # Conv2_x (3 blocks)
    *ResBlock("conv2_1", 64, "{(1,0,0)}", "(pool1-east)", 40, 40, 2),
    *ResBlock("conv2_2", 64, "{(1,0,0)}", "(conv2_1_conv3-east)", 40, 40, 2),
    *ResBlock("conv2_3", 64, "{(1,0,0)}", "(conv2_2_conv3-east)", 40, 40, 2),

    # Conv3_x (4 blocks)
    *ResBlock("conv3_1", 128, "{(1,0,0)}", "(conv2_3_conv3-east)", 32, 32, 2),
    *ResBlock("conv3_2", 128, "{(1,0,0)}", "(conv3_1_conv3-east)", 32, 32, 2),
    *ResBlock("conv3_3", 128, "{(1,0,0)}", "(conv3_2_conv3-east)", 32, 32, 2),
    *ResBlock("conv3_4", 128, "{(1,0,0)}", "(conv3_3_conv3-east)", 32, 32, 2),

    # Conv4_x (6 blocks)
    *ResBlock("conv4_1", 256, "{(1,0,0)}", "(conv3_4_conv3-east)", 24, 24, 2),
    *ResBlock("conv4_2", 256, "{(1,0,0)}", "(conv4_1_conv3-east)", 24, 24, 2),
    *ResBlock("conv4_3", 256, "{(1,0,0)}", "(conv4_2_conv3-east)", 24, 24, 2),
    *ResBlock("conv4_4", 256, "{(1,0,0)}", "(conv4_3_conv3-east)", 24, 24, 2),
    *ResBlock("conv4_5", 256, "{(1,0,0)}", "(conv4_4_conv3-east)", 24, 24, 2),
    *ResBlock("conv4_6", 256, "{(1,0,0)}", "(conv4_5_conv3-east)", 24, 24, 2),

    # Conv5_x (3 blocks)
    *ResBlock("conv5_1", 512, "{(1,0,0)}", "(conv4_6_conv3-east)", 16, 16, 2),
    *ResBlock("conv5_2", 512, "{(1,0,0)}", "(conv5_1_conv3-east)", 16, 16, 2),
    *ResBlock("conv5_3", 512, "{(1,0,0)}", "(conv5_2_conv3-east)", 16, 16, 2),

    # Global AvgPool + FC
    ToPool("avgpool", offset="{(1,0,0)}", to="(conv5_3_conv3-east)", height=1, depth=1, width=1, caption="AvgPool"),
    ToSoftMax("fc", 1000, offset="{(2,0,0)}", to="(avgpool-east)", caption="FC + Softmax"),

    ToEnd(),
]


def Main():
    """Generate LaTeX for ResNet50"""
    nameFile = str(sys.argv[0]).split(".")[0]
    ToGenerate(arch, nameFile + ".tex")


if __name__ == "__main__":
    Main()
