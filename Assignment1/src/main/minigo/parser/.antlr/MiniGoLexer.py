# Generated from c:/coding/PPL/Assignment1/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,54,531,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,
        4,1,4,1,4,1,4,5,4,138,8,4,10,4,12,4,141,9,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,5,5,150,8,5,10,5,12,5,153,9,5,1,5,1,5,1,5,1,5,1,5,1,6,1,
        6,1,6,1,7,4,7,164,8,7,11,7,12,7,165,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,
        25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,
        27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,339,8,28,1,29,1,29,1,29,1,
        29,1,29,1,29,3,29,347,8,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,
        30,1,30,1,30,1,30,1,30,3,30,361,8,30,1,31,1,31,1,31,1,31,1,31,1,
        32,1,32,1,32,1,33,1,33,1,33,1,34,1,34,1,34,1,35,1,35,1,35,1,36,1,
        36,1,36,1,37,1,37,1,37,1,38,1,38,1,38,1,39,1,39,1,39,1,40,1,40,1,
        40,1,41,1,41,1,41,1,42,1,42,1,42,1,43,1,43,1,43,1,44,1,44,1,44,1,
        45,1,45,1,45,1,46,1,46,1,46,1,47,1,47,1,48,4,48,416,8,48,11,48,12,
        48,417,1,48,1,48,4,48,422,8,48,11,48,12,48,423,3,48,426,8,48,1,48,
        1,48,3,48,430,8,48,1,48,4,48,433,8,48,11,48,12,48,434,3,48,437,8,
        48,1,48,1,48,1,49,1,49,1,49,5,49,444,8,49,10,49,12,49,447,9,49,3,
        49,449,8,49,1,50,1,50,1,50,4,50,454,8,50,11,50,12,50,455,1,51,1,
        51,1,51,4,51,461,8,51,11,51,12,51,462,1,52,1,52,1,52,4,52,468,8,
        52,11,52,12,52,469,1,53,1,53,1,53,1,53,3,53,476,8,53,1,53,1,53,1,
        54,1,54,1,55,1,55,1,55,1,56,1,56,1,56,5,56,488,8,56,10,56,12,56,
        491,9,56,1,56,1,56,1,56,1,57,1,57,5,57,498,8,57,10,57,12,57,501,
        9,57,1,57,1,57,1,58,1,58,1,58,1,59,1,59,1,59,5,59,511,8,59,10,59,
        12,59,514,9,59,1,59,1,59,1,59,1,59,1,59,1,60,1,60,1,60,5,60,524,
        8,60,10,60,12,60,527,9,60,1,60,1,60,1,60,1,151,0,61,1,1,3,2,5,3,
        7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,
        31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,
        53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,
        75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,45,91,46,93,47,95,0,
        97,48,99,0,101,0,103,0,105,0,107,49,109,0,111,0,113,50,115,51,117,
        52,119,53,121,54,1,0,16,1,0,10,10,3,0,9,9,13,13,32,32,1,0,48,57,
        2,0,69,69,101,101,2,0,43,43,45,45,1,0,49,57,2,0,66,66,98,98,1,0,
        48,49,2,0,79,79,111,111,1,0,48,55,2,0,88,88,120,120,3,0,48,57,65,
        70,97,102,2,0,34,34,92,92,5,0,34,34,92,92,110,110,114,114,116,116,
        3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,559,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,
        0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,
        0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,
        0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,
        0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,
        0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,
        0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,
        0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,
        0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,
        0,93,1,0,0,0,0,97,1,0,0,0,0,107,1,0,0,0,0,113,1,0,0,0,0,115,1,0,
        0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,1,123,1,0,0,0,3,126,
        1,0,0,0,5,129,1,0,0,0,7,131,1,0,0,0,9,133,1,0,0,0,11,144,1,0,0,0,
        13,159,1,0,0,0,15,163,1,0,0,0,17,169,1,0,0,0,19,174,1,0,0,0,21,181,
        1,0,0,0,23,187,1,0,0,0,25,196,1,0,0,0,27,203,1,0,0,0,29,210,1,0,
        0,0,31,219,1,0,0,0,33,231,1,0,0,0,35,240,1,0,0,0,37,246,1,0,0,0,
        39,254,1,0,0,0,41,264,1,0,0,0,43,272,1,0,0,0,45,278,1,0,0,0,47,289,
        1,0,0,0,49,297,1,0,0,0,51,305,1,0,0,0,53,311,1,0,0,0,55,318,1,0,
        0,0,57,338,1,0,0,0,59,346,1,0,0,0,61,360,1,0,0,0,63,362,1,0,0,0,
        65,367,1,0,0,0,67,370,1,0,0,0,69,373,1,0,0,0,71,376,1,0,0,0,73,379,
        1,0,0,0,75,382,1,0,0,0,77,385,1,0,0,0,79,388,1,0,0,0,81,391,1,0,
        0,0,83,394,1,0,0,0,85,397,1,0,0,0,87,400,1,0,0,0,89,403,1,0,0,0,
        91,406,1,0,0,0,93,409,1,0,0,0,95,412,1,0,0,0,97,415,1,0,0,0,99,448,
        1,0,0,0,101,450,1,0,0,0,103,457,1,0,0,0,105,464,1,0,0,0,107,475,
        1,0,0,0,109,479,1,0,0,0,111,481,1,0,0,0,113,484,1,0,0,0,115,495,
        1,0,0,0,117,504,1,0,0,0,119,507,1,0,0,0,121,520,1,0,0,0,123,124,
        5,124,0,0,124,125,5,124,0,0,125,2,1,0,0,0,126,127,5,38,0,0,127,128,
        5,38,0,0,128,4,1,0,0,0,129,130,5,33,0,0,130,6,1,0,0,0,131,132,5,
        58,0,0,132,8,1,0,0,0,133,134,5,47,0,0,134,135,5,47,0,0,135,139,1,
        0,0,0,136,138,8,0,0,0,137,136,1,0,0,0,138,141,1,0,0,0,139,137,1,
        0,0,0,139,140,1,0,0,0,140,142,1,0,0,0,141,139,1,0,0,0,142,143,6,
        4,0,0,143,10,1,0,0,0,144,145,5,47,0,0,145,146,5,42,0,0,146,151,1,
        0,0,0,147,150,3,11,5,0,148,150,9,0,0,0,149,147,1,0,0,0,149,148,1,
        0,0,0,150,153,1,0,0,0,151,152,1,0,0,0,151,149,1,0,0,0,152,154,1,
        0,0,0,153,151,1,0,0,0,154,155,5,42,0,0,155,156,5,47,0,0,156,157,
        1,0,0,0,157,158,6,5,0,0,158,12,1,0,0,0,159,160,5,10,0,0,160,161,
        6,6,1,0,161,14,1,0,0,0,162,164,7,1,0,0,163,162,1,0,0,0,164,165,1,
        0,0,0,165,163,1,0,0,0,165,166,1,0,0,0,166,167,1,0,0,0,167,168,6,
        7,0,0,168,16,1,0,0,0,169,170,5,105,0,0,170,171,5,102,0,0,171,172,
        1,0,0,0,172,173,6,8,2,0,173,18,1,0,0,0,174,175,5,101,0,0,175,176,
        5,108,0,0,176,177,5,115,0,0,177,178,5,101,0,0,178,179,1,0,0,0,179,
        180,6,9,3,0,180,20,1,0,0,0,181,182,5,102,0,0,182,183,5,111,0,0,183,
        184,5,114,0,0,184,185,1,0,0,0,185,186,6,10,4,0,186,22,1,0,0,0,187,
        188,5,114,0,0,188,189,5,101,0,0,189,190,5,116,0,0,190,191,5,117,
        0,0,191,192,5,114,0,0,192,193,5,110,0,0,193,194,1,0,0,0,194,195,
        6,11,5,0,195,24,1,0,0,0,196,197,5,102,0,0,197,198,5,117,0,0,198,
        199,5,110,0,0,199,200,5,99,0,0,200,201,1,0,0,0,201,202,6,12,6,0,
        202,26,1,0,0,0,203,204,5,116,0,0,204,205,5,121,0,0,205,206,5,112,
        0,0,206,207,5,101,0,0,207,208,1,0,0,0,208,209,6,13,7,0,209,28,1,
        0,0,0,210,211,5,115,0,0,211,212,5,116,0,0,212,213,5,114,0,0,213,
        214,5,117,0,0,214,215,5,99,0,0,215,216,5,116,0,0,216,217,1,0,0,0,
        217,218,6,14,8,0,218,30,1,0,0,0,219,220,5,105,0,0,220,221,5,110,
        0,0,221,222,5,116,0,0,222,223,5,101,0,0,223,224,5,114,0,0,224,225,
        5,102,0,0,225,226,5,97,0,0,226,227,5,99,0,0,227,228,5,101,0,0,228,
        229,1,0,0,0,229,230,6,15,9,0,230,32,1,0,0,0,231,232,5,115,0,0,232,
        233,5,116,0,0,233,234,5,114,0,0,234,235,5,105,0,0,235,236,5,110,
        0,0,236,237,5,103,0,0,237,238,1,0,0,0,238,239,6,16,10,0,239,34,1,
        0,0,0,240,241,5,105,0,0,241,242,5,110,0,0,242,243,5,116,0,0,243,
        244,1,0,0,0,244,245,6,17,11,0,245,36,1,0,0,0,246,247,5,102,0,0,247,
        248,5,108,0,0,248,249,5,111,0,0,249,250,5,97,0,0,250,251,5,116,0,
        0,251,252,1,0,0,0,252,253,6,18,12,0,253,38,1,0,0,0,254,255,5,98,
        0,0,255,256,5,111,0,0,256,257,5,111,0,0,257,258,5,108,0,0,258,259,
        5,101,0,0,259,260,5,97,0,0,260,261,5,110,0,0,261,262,1,0,0,0,262,
        263,6,19,13,0,263,40,1,0,0,0,264,265,5,99,0,0,265,266,5,111,0,0,
        266,267,5,110,0,0,267,268,5,115,0,0,268,269,5,116,0,0,269,270,1,
        0,0,0,270,271,6,20,14,0,271,42,1,0,0,0,272,273,5,118,0,0,273,274,
        5,97,0,0,274,275,5,114,0,0,275,276,1,0,0,0,276,277,6,21,15,0,277,
        44,1,0,0,0,278,279,5,99,0,0,279,280,5,111,0,0,280,281,5,110,0,0,
        281,282,5,116,0,0,282,283,5,105,0,0,283,284,5,110,0,0,284,285,5,
        117,0,0,285,286,5,101,0,0,286,287,1,0,0,0,287,288,6,22,16,0,288,
        46,1,0,0,0,289,290,5,98,0,0,290,291,5,114,0,0,291,292,5,101,0,0,
        292,293,5,97,0,0,293,294,5,107,0,0,294,295,1,0,0,0,295,296,6,23,
        17,0,296,48,1,0,0,0,297,298,5,114,0,0,298,299,5,97,0,0,299,300,5,
        110,0,0,300,301,5,103,0,0,301,302,5,101,0,0,302,303,1,0,0,0,303,
        304,6,24,18,0,304,50,1,0,0,0,305,306,5,110,0,0,306,307,5,105,0,0,
        307,308,5,108,0,0,308,309,1,0,0,0,309,310,6,25,19,0,310,52,1,0,0,
        0,311,312,5,116,0,0,312,313,5,114,0,0,313,314,5,117,0,0,314,315,
        5,101,0,0,315,316,1,0,0,0,316,317,6,26,20,0,317,54,1,0,0,0,318,319,
        5,102,0,0,319,320,5,97,0,0,320,321,5,108,0,0,321,322,5,115,0,0,322,
        323,5,101,0,0,323,324,1,0,0,0,324,325,6,27,21,0,325,56,1,0,0,0,326,
        327,5,61,0,0,327,339,5,61,0,0,328,329,5,33,0,0,329,339,5,61,0,0,
        330,339,5,60,0,0,331,332,5,60,0,0,332,339,5,61,0,0,333,339,5,62,
        0,0,334,335,5,62,0,0,335,336,5,61,0,0,336,337,1,0,0,0,337,339,6,
        28,22,0,338,326,1,0,0,0,338,328,1,0,0,0,338,330,1,0,0,0,338,331,
        1,0,0,0,338,333,1,0,0,0,338,334,1,0,0,0,339,58,1,0,0,0,340,341,5,
        38,0,0,341,347,5,38,0,0,342,343,5,124,0,0,343,347,5,124,0,0,344,
        345,5,33,0,0,345,347,6,29,23,0,346,340,1,0,0,0,346,342,1,0,0,0,346,
        344,1,0,0,0,347,60,1,0,0,0,348,349,5,43,0,0,349,361,5,61,0,0,350,
        351,5,45,0,0,351,361,5,61,0,0,352,353,5,42,0,0,353,361,5,61,0,0,
        354,355,5,47,0,0,355,361,5,61,0,0,356,357,5,37,0,0,357,358,5,61,
        0,0,358,359,1,0,0,0,359,361,6,30,24,0,360,348,1,0,0,0,360,350,1,
        0,0,0,360,352,1,0,0,0,360,354,1,0,0,0,360,356,1,0,0,0,361,62,1,0,
        0,0,362,363,5,58,0,0,363,364,5,61,0,0,364,365,1,0,0,0,365,366,6,
        31,25,0,366,64,1,0,0,0,367,368,5,46,0,0,368,369,6,32,26,0,369,66,
        1,0,0,0,370,371,5,61,0,0,371,372,6,33,27,0,372,68,1,0,0,0,373,374,
        5,43,0,0,374,375,6,34,28,0,375,70,1,0,0,0,376,377,5,45,0,0,377,378,
        6,35,29,0,378,72,1,0,0,0,379,380,5,42,0,0,380,381,6,36,30,0,381,
        74,1,0,0,0,382,383,5,47,0,0,383,384,6,37,31,0,384,76,1,0,0,0,385,
        386,5,37,0,0,386,387,6,38,32,0,387,78,1,0,0,0,388,389,5,40,0,0,389,
        390,6,39,33,0,390,80,1,0,0,0,391,392,5,41,0,0,392,393,6,40,34,0,
        393,82,1,0,0,0,394,395,5,91,0,0,395,396,6,41,35,0,396,84,1,0,0,0,
        397,398,5,93,0,0,398,399,6,42,36,0,399,86,1,0,0,0,400,401,5,123,
        0,0,401,402,6,43,37,0,402,88,1,0,0,0,403,404,5,125,0,0,404,405,6,
        44,38,0,405,90,1,0,0,0,406,407,5,44,0,0,407,408,6,45,39,0,408,92,
        1,0,0,0,409,410,5,59,0,0,410,411,6,46,40,0,411,94,1,0,0,0,412,413,
        7,2,0,0,413,96,1,0,0,0,414,416,3,95,47,0,415,414,1,0,0,0,416,417,
        1,0,0,0,417,415,1,0,0,0,417,418,1,0,0,0,418,419,1,0,0,0,419,425,
        5,46,0,0,420,422,3,95,47,0,421,420,1,0,0,0,422,423,1,0,0,0,423,421,
        1,0,0,0,423,424,1,0,0,0,424,426,1,0,0,0,425,421,1,0,0,0,425,426,
        1,0,0,0,426,436,1,0,0,0,427,429,7,3,0,0,428,430,7,4,0,0,429,428,
        1,0,0,0,429,430,1,0,0,0,430,432,1,0,0,0,431,433,3,95,47,0,432,431,
        1,0,0,0,433,434,1,0,0,0,434,432,1,0,0,0,434,435,1,0,0,0,435,437,
        1,0,0,0,436,427,1,0,0,0,436,437,1,0,0,0,437,438,1,0,0,0,438,439,
        6,48,41,0,439,98,1,0,0,0,440,449,5,48,0,0,441,445,7,5,0,0,442,444,
        7,2,0,0,443,442,1,0,0,0,444,447,1,0,0,0,445,443,1,0,0,0,445,446,
        1,0,0,0,446,449,1,0,0,0,447,445,1,0,0,0,448,440,1,0,0,0,448,441,
        1,0,0,0,449,100,1,0,0,0,450,451,5,48,0,0,451,453,7,6,0,0,452,454,
        7,7,0,0,453,452,1,0,0,0,454,455,1,0,0,0,455,453,1,0,0,0,455,456,
        1,0,0,0,456,102,1,0,0,0,457,458,5,48,0,0,458,460,7,8,0,0,459,461,
        7,9,0,0,460,459,1,0,0,0,461,462,1,0,0,0,462,460,1,0,0,0,462,463,
        1,0,0,0,463,104,1,0,0,0,464,465,5,48,0,0,465,467,7,10,0,0,466,468,
        7,11,0,0,467,466,1,0,0,0,468,469,1,0,0,0,469,467,1,0,0,0,469,470,
        1,0,0,0,470,106,1,0,0,0,471,476,3,99,49,0,472,476,3,101,50,0,473,
        476,3,103,51,0,474,476,3,105,52,0,475,471,1,0,0,0,475,472,1,0,0,
        0,475,473,1,0,0,0,475,474,1,0,0,0,476,477,1,0,0,0,477,478,6,53,42,
        0,478,108,1,0,0,0,479,480,8,12,0,0,480,110,1,0,0,0,481,482,5,92,
        0,0,482,483,7,13,0,0,483,112,1,0,0,0,484,489,5,34,0,0,485,488,3,
        109,54,0,486,488,3,111,55,0,487,485,1,0,0,0,487,486,1,0,0,0,488,
        491,1,0,0,0,489,487,1,0,0,0,489,490,1,0,0,0,490,492,1,0,0,0,491,
        489,1,0,0,0,492,493,5,34,0,0,493,494,6,56,43,0,494,114,1,0,0,0,495,
        499,7,14,0,0,496,498,7,15,0,0,497,496,1,0,0,0,498,501,1,0,0,0,499,
        497,1,0,0,0,499,500,1,0,0,0,500,502,1,0,0,0,501,499,1,0,0,0,502,
        503,6,57,44,0,503,116,1,0,0,0,504,505,9,0,0,0,505,506,6,58,45,0,
        506,118,1,0,0,0,507,512,5,34,0,0,508,511,3,109,54,0,509,511,3,111,
        55,0,510,508,1,0,0,0,510,509,1,0,0,0,511,514,1,0,0,0,512,510,1,0,
        0,0,512,513,1,0,0,0,513,515,1,0,0,0,514,512,1,0,0,0,515,516,5,92,
        0,0,516,517,8,13,0,0,517,518,6,59,46,0,518,519,6,59,47,0,519,120,
        1,0,0,0,520,525,5,34,0,0,521,524,3,109,54,0,522,524,3,111,55,0,523,
        521,1,0,0,0,523,522,1,0,0,0,524,527,1,0,0,0,525,523,1,0,0,0,525,
        526,1,0,0,0,526,528,1,0,0,0,527,525,1,0,0,0,528,529,6,60,48,0,529,
        530,6,60,49,0,530,122,1,0,0,0,27,0,139,149,151,165,338,346,360,417,
        423,425,429,434,436,445,448,455,462,469,475,487,489,499,510,512,
        523,525,50,6,0,0,1,6,0,1,8,1,1,9,2,1,10,3,1,11,4,1,12,5,1,13,6,1,
        14,7,1,15,8,1,16,9,1,17,10,1,18,11,1,19,12,1,20,13,1,21,14,1,22,
        15,1,23,16,1,24,17,1,25,18,1,26,19,1,27,20,1,28,21,1,29,22,1,30,
        23,1,31,24,1,32,25,1,33,26,1,34,27,1,35,28,1,36,29,1,37,30,1,38,
        31,1,39,32,1,40,33,1,41,34,1,42,35,1,43,36,1,44,37,1,45,38,1,46,
        39,1,48,40,1,53,41,1,56,42,1,57,43,1,58,44,1,59,45,1,59,46,1,60,
        47,1,60,48
    ]

class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    SINGLE_LINE_CMT = 5
    MULTI_LINE_CMT = 6
    NL = 7
    WS = 8
    IF_ = 9
    ELSE_ = 10
    FOR_ = 11
    RETURN_ = 12
    FUNC_ = 13
    TYPE_ = 14
    STRUCT_ = 15
    INTERFACE_ = 16
    STRING_ = 17
    INT_ = 18
    FLOAT_ = 19
    BOOLEAN_ = 20
    CONST_ = 21
    VAR_ = 22
    CONTINUE_ = 23
    BREAK_ = 24
    RANGE_ = 25
    NIL_ = 26
    TRUE_ = 27
    FALSE_ = 28
    COMPARISON_OP = 29
    BOOLEAN_OP = 30
    UPT_ASSIGN = 31
    ASSIGN = 32
    DOT = 33
    INIT = 34
    ADD = 35
    SUB = 36
    MUL = 37
    DIV = 38
    MOD = 39
    LPAREN = 40
    RPAREN = 41
    LSB = 42
    RSB = 43
    LCB = 44
    RCB = 45
    COMMA = 46
    SEMICOLON = 47
    FLOAT = 48
    INTEGER = 49
    STRING = 50
    ID = 51
    ERROR_CHAR = 52
    ILLEGAL_ESCAPE = 53
    UNCLOSE_STRING = 54

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'||'", "'&&'", "'!'", "':'", "'\\n'", "'if'", "'else'", "'for'", 
            "'return'", "'func'", "'type'", "'struct'", "'interface'", "'string'", 
            "'int'", "'float'", "'boolean'", "'const'", "'var'", "'continue'", 
            "'break'", "'range'", "'nil'", "'true'", "'false'", "':='", 
            "'.'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "SINGLE_LINE_CMT", "MULTI_LINE_CMT", "NL", "WS", "IF_", "ELSE_", 
            "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", "INTERFACE_", 
            "STRING_", "INT_", "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
            "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", 
            "BOOLEAN_OP", "UPT_ASSIGN", "ASSIGN", "DOT", "INIT", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "LPAREN", "RPAREN", "LSB", "RSB", 
            "LCB", "RCB", "COMMA", "SEMICOLON", "FLOAT", "INTEGER", "STRING", 
            "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "SINGLE_LINE_CMT", "MULTI_LINE_CMT", 
                  "NL", "WS", "IF_", "ELSE_", "FOR_", "RETURN_", "FUNC_", 
                  "TYPE_", "STRUCT_", "INTERFACE_", "STRING_", "INT_", "FLOAT_", 
                  "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", "BREAK_", "RANGE_", 
                  "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", "BOOLEAN_OP", 
                  "UPT_ASSIGN", "ASSIGN", "DOT", "INIT", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "LPAREN", "RPAREN", "LSB", "RSB", "LCB", 
                  "RCB", "COMMA", "SEMICOLON", "Digit", "FLOAT", "DecInt", 
                  "BinInt", "OctInt", "HexInt", "INTEGER", "Char", "EscapeChar", 
                  "STRING", "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    lastTokenType = None

    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[6] = self.NL_action 
            actions[8] = self.IF__action 
            actions[9] = self.ELSE__action 
            actions[10] = self.FOR__action 
            actions[11] = self.RETURN__action 
            actions[12] = self.FUNC__action 
            actions[13] = self.TYPE__action 
            actions[14] = self.STRUCT__action 
            actions[15] = self.INTERFACE__action 
            actions[16] = self.STRING__action 
            actions[17] = self.INT__action 
            actions[18] = self.FLOAT__action 
            actions[19] = self.BOOLEAN__action 
            actions[20] = self.CONST__action 
            actions[21] = self.VAR__action 
            actions[22] = self.CONTINUE__action 
            actions[23] = self.BREAK__action 
            actions[24] = self.RANGE__action 
            actions[25] = self.NIL__action 
            actions[26] = self.TRUE__action 
            actions[27] = self.FALSE__action 
            actions[28] = self.COMPARISON_OP_action 
            actions[29] = self.BOOLEAN_OP_action 
            actions[30] = self.UPT_ASSIGN_action 
            actions[31] = self.ASSIGN_action 
            actions[32] = self.DOT_action 
            actions[33] = self.INIT_action 
            actions[34] = self.ADD_action 
            actions[35] = self.SUB_action 
            actions[36] = self.MUL_action 
            actions[37] = self.DIV_action 
            actions[38] = self.MOD_action 
            actions[39] = self.LPAREN_action 
            actions[40] = self.RPAREN_action 
            actions[41] = self.LSB_action 
            actions[42] = self.RSB_action 
            actions[43] = self.LCB_action 
            actions[44] = self.RCB_action 
            actions[45] = self.COMMA_action 
            actions[46] = self.SEMICOLON_action 
            actions[48] = self.FLOAT_action 
            actions[53] = self.INTEGER_action 
            actions[56] = self.STRING_action 
            actions[57] = self.ID_action 
            actions[58] = self.ERROR_CHAR_action 
            actions[59] = self.ILLEGAL_ESCAPE_action 
            actions[60] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            if self.lastTokenType in ['ID', 'INTEGER', 'FLOAT', 'TRUE_', 'FALSE_', 'STRING', 'INT_', 'FLOAT_', 'BOOLEAN_', 'STRING_', 'RETURN_', 'CONTINUE_', 'BREAK_', 'RPAREN', 'RSB', 'RCB']:
                self.text = ';'
                self.type = self.SEMICOLON
                self.lastTokenType = 'SEMICOLON'
            else:
                self.skip()

     

    def IF__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.lastTokenType = 'IF_'
     

    def ELSE__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.lastTokenType = 'ELSE_'
     

    def FOR__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.lastTokenType = 'FOR_'
     

    def RETURN__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.lastTokenType = 'RETURN_'
     

    def FUNC__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.lastTokenType = 'FUNC_'
     

    def TYPE__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            self.lastTokenType = 'TYPE_'
     

    def STRUCT__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            self.lastTokenType = 'STRUCT_'
     

    def INTERFACE__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:
            self.lastTokenType = 'INTERFACE_'
     

    def STRING__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 9:
            self.lastTokenType = 'STRING_'
     

    def INT__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 10:
            self.lastTokenType = 'INT_'
     

    def FLOAT__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 11:
            self.lastTokenType = 'FLOAT_'
     

    def BOOLEAN__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 12:
            self.lastTokenType = 'BOOLEAN_'
     

    def CONST__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 13:
            self.lastTokenType = 'CONST_'
     

    def VAR__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 14:
            self.lastTokenType = 'VAR_'
     

    def CONTINUE__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 15:
            self.lastTokenType = 'CONTINUE_'
     

    def BREAK__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 16:
            self.lastTokenType = 'BREAK_'
     

    def RANGE__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 17:
            self.lastTokenType = 'RANGE_'
     

    def NIL__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 18:
            self.lastTokenType = 'NIL_'
     

    def TRUE__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 19:
            self.lastTokenType = 'TRUE_'
     

    def FALSE__action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 20:
            self.lastTokenType = 'FALSE_'
     

    def COMPARISON_OP_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 21:
            self.lastTypeToken = 'COMPARISON_OP'
     

    def BOOLEAN_OP_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 22:
            self.lastTokenType = 'BOOLEAN_OP'
     

    def UPT_ASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 23:
            self.lastTokenType = 'UPT_ASSIGN'
     

    def ASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 24:
            self.lastTokenType = 'ASSIGN'
     

    def DOT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 25:
            self.lastTokenType = 'DOT'
     

    def INIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 26:
            self.lastTokenType = 'INIT'
     

    def ADD_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 27:
            self.lastTokenType = 'ADD'
     

    def SUB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 28:
            self.lastTokenType = 'SUB'
     

    def MUL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 29:
            self.lastTokenType = 'MUL'
     

    def DIV_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 30:
            self.lastTokenType = 'DIV'
     

    def MOD_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 31:
            self.lastTokenType = 'MOD'
     

    def LPAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 32:
            self.lastTokenType = 'LPAREN'
     

    def RPAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 33:
            self.lastTokenType = 'RPAREN'
     

    def LSB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 34:
            self.lastTokenType = 'LSB'
     

    def RSB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 35:
            self.lastTokenType = 'RSB'
     

    def LCB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 36:
            self.lastTokenType = 'LCB'
     

    def RCB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 37:
            self.lastTokenType = 'RCB'
     

    def COMMA_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 38:
            self.lastTokenType = 'COMMA'
     

    def SEMICOLON_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 39:
            self.lastTokenType = 'SEMICOLON'
     

    def FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 40:
            self.lastTokenType = 'FLOAT'
     

    def INTEGER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 41:
            self.lastTokenType = 'INTEGER'
     

    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 42:
            self.lastTokenType = 'STRING'
     

    def ID_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 43:
            self.lastTokenType = 'ID'
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 44:
            self.lastTokenType = 'ERROR_CHAR'
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 45:
            self.text = self.text[1:]
     

        if actionIndex == 46:
            self.lastTokenType = 'ILLEGAL_ESCAPE'
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 47:
            self.text = self.text.replace('\r','\n').split('\n')[0][1:]
     

        if actionIndex == 48:
            self.lastTokenType = 'UNCLOSE_STRING'
     


