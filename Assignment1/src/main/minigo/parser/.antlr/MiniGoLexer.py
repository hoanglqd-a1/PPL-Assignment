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
        4,0,52,454,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,5,3,132,8,3,10,
        3,12,3,135,9,3,1,3,3,3,138,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,5,4,147,
        8,4,10,4,12,4,150,9,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,6,4,6,160,8,
        6,11,6,12,6,161,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,
        1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,
        11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,
        17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,
        19,1,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
        21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,
        23,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,
        26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,
        27,293,8,27,1,28,1,28,1,28,1,28,1,28,3,28,300,8,28,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,314,8,29,1,30,
        1,30,1,31,1,31,1,32,1,32,1,33,1,33,1,34,1,34,1,35,1,35,1,36,1,36,
        1,37,1,37,1,38,1,38,1,39,1,39,1,40,1,40,1,41,1,41,1,42,1,42,1,43,
        1,43,1,44,1,44,1,45,1,45,1,46,4,46,349,8,46,11,46,12,46,350,1,46,
        1,46,4,46,355,8,46,11,46,12,46,356,3,46,359,8,46,1,46,1,46,3,46,
        363,8,46,1,46,4,46,366,8,46,11,46,12,46,367,3,46,370,8,46,1,47,1,
        47,1,47,5,47,375,8,47,10,47,12,47,378,9,47,3,47,380,8,47,1,48,1,
        48,1,48,4,48,385,8,48,11,48,12,48,386,1,49,1,49,1,49,4,49,392,8,
        49,11,49,12,49,393,1,50,1,50,1,50,4,50,399,8,50,11,50,12,50,400,
        1,51,1,51,1,51,1,51,3,51,407,8,51,1,52,1,52,1,53,1,53,1,53,1,54,
        1,54,1,54,5,54,417,8,54,10,54,12,54,420,9,54,1,54,1,54,1,55,1,55,
        5,55,426,8,55,10,55,12,55,429,9,55,1,56,1,56,1,57,1,57,1,57,5,57,
        436,8,57,10,57,12,57,439,9,57,1,57,1,57,1,57,1,57,1,58,1,58,1,58,
        5,58,448,8,58,10,58,12,58,451,9,58,1,58,1,58,1,148,0,59,1,1,3,2,
        5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,
        15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,
        26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,
        37,75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,45,91,0,93,46,95,
        0,97,0,99,0,101,0,103,47,105,0,107,0,109,48,111,49,113,50,115,51,
        117,52,1,0,17,1,0,10,10,1,1,10,10,3,0,9,9,13,13,32,32,1,0,48,57,
        2,0,69,69,101,101,2,0,43,43,45,45,1,0,49,57,2,0,66,66,98,98,1,0,
        48,49,2,0,79,79,111,111,1,0,48,55,2,0,88,88,120,120,3,0,48,57,65,
        70,97,102,2,0,34,34,92,92,5,0,34,34,92,92,110,110,114,114,116,116,
        3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,483,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,
        0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,
        0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,
        0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,
        0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,
        0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,
        0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,
        0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,
        0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,93,1,0,0,0,
        0,103,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,115,1,
        0,0,0,0,117,1,0,0,0,1,119,1,0,0,0,3,122,1,0,0,0,5,125,1,0,0,0,7,
        127,1,0,0,0,9,141,1,0,0,0,11,156,1,0,0,0,13,159,1,0,0,0,15,165,1,
        0,0,0,17,168,1,0,0,0,19,173,1,0,0,0,21,177,1,0,0,0,23,184,1,0,0,
        0,25,189,1,0,0,0,27,194,1,0,0,0,29,201,1,0,0,0,31,211,1,0,0,0,33,
        218,1,0,0,0,35,222,1,0,0,0,37,228,1,0,0,0,39,236,1,0,0,0,41,242,
        1,0,0,0,43,246,1,0,0,0,45,255,1,0,0,0,47,261,1,0,0,0,49,267,1,0,
        0,0,51,271,1,0,0,0,53,276,1,0,0,0,55,292,1,0,0,0,57,299,1,0,0,0,
        59,313,1,0,0,0,61,315,1,0,0,0,63,317,1,0,0,0,65,319,1,0,0,0,67,321,
        1,0,0,0,69,323,1,0,0,0,71,325,1,0,0,0,73,327,1,0,0,0,75,329,1,0,
        0,0,77,331,1,0,0,0,79,333,1,0,0,0,81,335,1,0,0,0,83,337,1,0,0,0,
        85,339,1,0,0,0,87,341,1,0,0,0,89,343,1,0,0,0,91,345,1,0,0,0,93,348,
        1,0,0,0,95,379,1,0,0,0,97,381,1,0,0,0,99,388,1,0,0,0,101,395,1,0,
        0,0,103,406,1,0,0,0,105,408,1,0,0,0,107,410,1,0,0,0,109,413,1,0,
        0,0,111,423,1,0,0,0,113,430,1,0,0,0,115,432,1,0,0,0,117,444,1,0,
        0,0,119,120,5,124,0,0,120,121,5,124,0,0,121,2,1,0,0,0,122,123,5,
        38,0,0,123,124,5,38,0,0,124,4,1,0,0,0,125,126,5,33,0,0,126,6,1,0,
        0,0,127,128,5,47,0,0,128,129,5,47,0,0,129,133,1,0,0,0,130,132,8,
        0,0,0,131,130,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,
        0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,136,138,7,1,0,0,137,136,1,
        0,0,0,138,139,1,0,0,0,139,140,6,3,0,0,140,8,1,0,0,0,141,142,5,47,
        0,0,142,143,5,42,0,0,143,148,1,0,0,0,144,147,3,9,4,0,145,147,9,0,
        0,0,146,144,1,0,0,0,146,145,1,0,0,0,147,150,1,0,0,0,148,149,1,0,
        0,0,148,146,1,0,0,0,149,151,1,0,0,0,150,148,1,0,0,0,151,152,5,42,
        0,0,152,153,5,47,0,0,153,154,1,0,0,0,154,155,6,4,0,0,155,10,1,0,
        0,0,156,157,5,10,0,0,157,12,1,0,0,0,158,160,7,2,0,0,159,158,1,0,
        0,0,160,161,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,163,1,0,
        0,0,163,164,6,6,0,0,164,14,1,0,0,0,165,166,5,105,0,0,166,167,5,102,
        0,0,167,16,1,0,0,0,168,169,5,101,0,0,169,170,5,108,0,0,170,171,5,
        115,0,0,171,172,5,101,0,0,172,18,1,0,0,0,173,174,5,102,0,0,174,175,
        5,111,0,0,175,176,5,114,0,0,176,20,1,0,0,0,177,178,5,114,0,0,178,
        179,5,101,0,0,179,180,5,116,0,0,180,181,5,117,0,0,181,182,5,114,
        0,0,182,183,5,110,0,0,183,22,1,0,0,0,184,185,5,102,0,0,185,186,5,
        117,0,0,186,187,5,110,0,0,187,188,5,99,0,0,188,24,1,0,0,0,189,190,
        5,116,0,0,190,191,5,121,0,0,191,192,5,112,0,0,192,193,5,101,0,0,
        193,26,1,0,0,0,194,195,5,115,0,0,195,196,5,116,0,0,196,197,5,114,
        0,0,197,198,5,117,0,0,198,199,5,99,0,0,199,200,5,116,0,0,200,28,
        1,0,0,0,201,202,5,105,0,0,202,203,5,110,0,0,203,204,5,116,0,0,204,
        205,5,101,0,0,205,206,5,114,0,0,206,207,5,102,0,0,207,208,5,97,0,
        0,208,209,5,99,0,0,209,210,5,101,0,0,210,30,1,0,0,0,211,212,5,115,
        0,0,212,213,5,116,0,0,213,214,5,114,0,0,214,215,5,105,0,0,215,216,
        5,110,0,0,216,217,5,103,0,0,217,32,1,0,0,0,218,219,5,105,0,0,219,
        220,5,110,0,0,220,221,5,116,0,0,221,34,1,0,0,0,222,223,5,102,0,0,
        223,224,5,108,0,0,224,225,5,111,0,0,225,226,5,97,0,0,226,227,5,116,
        0,0,227,36,1,0,0,0,228,229,5,98,0,0,229,230,5,111,0,0,230,231,5,
        111,0,0,231,232,5,108,0,0,232,233,5,101,0,0,233,234,5,97,0,0,234,
        235,5,110,0,0,235,38,1,0,0,0,236,237,5,99,0,0,237,238,5,111,0,0,
        238,239,5,110,0,0,239,240,5,115,0,0,240,241,5,116,0,0,241,40,1,0,
        0,0,242,243,5,118,0,0,243,244,5,97,0,0,244,245,5,114,0,0,245,42,
        1,0,0,0,246,247,5,99,0,0,247,248,5,111,0,0,248,249,5,110,0,0,249,
        250,5,116,0,0,250,251,5,105,0,0,251,252,5,110,0,0,252,253,5,117,
        0,0,253,254,5,101,0,0,254,44,1,0,0,0,255,256,5,98,0,0,256,257,5,
        114,0,0,257,258,5,101,0,0,258,259,5,97,0,0,259,260,5,107,0,0,260,
        46,1,0,0,0,261,262,5,114,0,0,262,263,5,97,0,0,263,264,5,110,0,0,
        264,265,5,103,0,0,265,266,5,101,0,0,266,48,1,0,0,0,267,268,5,110,
        0,0,268,269,5,105,0,0,269,270,5,108,0,0,270,50,1,0,0,0,271,272,5,
        116,0,0,272,273,5,114,0,0,273,274,5,117,0,0,274,275,5,101,0,0,275,
        52,1,0,0,0,276,277,5,102,0,0,277,278,5,97,0,0,278,279,5,108,0,0,
        279,280,5,115,0,0,280,281,5,101,0,0,281,54,1,0,0,0,282,283,5,61,
        0,0,283,293,5,61,0,0,284,285,5,33,0,0,285,293,5,61,0,0,286,293,5,
        60,0,0,287,288,5,60,0,0,288,293,5,61,0,0,289,293,5,62,0,0,290,291,
        5,62,0,0,291,293,5,61,0,0,292,282,1,0,0,0,292,284,1,0,0,0,292,286,
        1,0,0,0,292,287,1,0,0,0,292,289,1,0,0,0,292,290,1,0,0,0,293,56,1,
        0,0,0,294,295,5,38,0,0,295,300,5,38,0,0,296,297,5,124,0,0,297,300,
        5,124,0,0,298,300,5,33,0,0,299,294,1,0,0,0,299,296,1,0,0,0,299,298,
        1,0,0,0,300,58,1,0,0,0,301,302,5,58,0,0,302,314,5,61,0,0,303,304,
        5,43,0,0,304,314,5,61,0,0,305,306,5,45,0,0,306,314,5,61,0,0,307,
        308,5,42,0,0,308,314,5,61,0,0,309,310,5,47,0,0,310,314,5,61,0,0,
        311,312,5,37,0,0,312,314,5,61,0,0,313,301,1,0,0,0,313,303,1,0,0,
        0,313,305,1,0,0,0,313,307,1,0,0,0,313,309,1,0,0,0,313,311,1,0,0,
        0,314,60,1,0,0,0,315,316,5,46,0,0,316,62,1,0,0,0,317,318,5,61,0,
        0,318,64,1,0,0,0,319,320,5,43,0,0,320,66,1,0,0,0,321,322,5,45,0,
        0,322,68,1,0,0,0,323,324,5,42,0,0,324,70,1,0,0,0,325,326,5,47,0,
        0,326,72,1,0,0,0,327,328,5,37,0,0,328,74,1,0,0,0,329,330,5,40,0,
        0,330,76,1,0,0,0,331,332,5,41,0,0,332,78,1,0,0,0,333,334,5,91,0,
        0,334,80,1,0,0,0,335,336,5,93,0,0,336,82,1,0,0,0,337,338,5,123,0,
        0,338,84,1,0,0,0,339,340,5,125,0,0,340,86,1,0,0,0,341,342,5,44,0,
        0,342,88,1,0,0,0,343,344,5,59,0,0,344,90,1,0,0,0,345,346,7,3,0,0,
        346,92,1,0,0,0,347,349,3,91,45,0,348,347,1,0,0,0,349,350,1,0,0,0,
        350,348,1,0,0,0,350,351,1,0,0,0,351,352,1,0,0,0,352,358,5,46,0,0,
        353,355,3,91,45,0,354,353,1,0,0,0,355,356,1,0,0,0,356,354,1,0,0,
        0,356,357,1,0,0,0,357,359,1,0,0,0,358,354,1,0,0,0,358,359,1,0,0,
        0,359,369,1,0,0,0,360,362,7,4,0,0,361,363,7,5,0,0,362,361,1,0,0,
        0,362,363,1,0,0,0,363,365,1,0,0,0,364,366,3,91,45,0,365,364,1,0,
        0,0,366,367,1,0,0,0,367,365,1,0,0,0,367,368,1,0,0,0,368,370,1,0,
        0,0,369,360,1,0,0,0,369,370,1,0,0,0,370,94,1,0,0,0,371,380,5,48,
        0,0,372,376,7,6,0,0,373,375,7,3,0,0,374,373,1,0,0,0,375,378,1,0,
        0,0,376,374,1,0,0,0,376,377,1,0,0,0,377,380,1,0,0,0,378,376,1,0,
        0,0,379,371,1,0,0,0,379,372,1,0,0,0,380,96,1,0,0,0,381,382,5,48,
        0,0,382,384,7,7,0,0,383,385,7,8,0,0,384,383,1,0,0,0,385,386,1,0,
        0,0,386,384,1,0,0,0,386,387,1,0,0,0,387,98,1,0,0,0,388,389,5,48,
        0,0,389,391,7,9,0,0,390,392,7,10,0,0,391,390,1,0,0,0,392,393,1,0,
        0,0,393,391,1,0,0,0,393,394,1,0,0,0,394,100,1,0,0,0,395,396,5,48,
        0,0,396,398,7,11,0,0,397,399,7,12,0,0,398,397,1,0,0,0,399,400,1,
        0,0,0,400,398,1,0,0,0,400,401,1,0,0,0,401,102,1,0,0,0,402,407,3,
        95,47,0,403,407,3,97,48,0,404,407,3,99,49,0,405,407,3,101,50,0,406,
        402,1,0,0,0,406,403,1,0,0,0,406,404,1,0,0,0,406,405,1,0,0,0,407,
        104,1,0,0,0,408,409,8,13,0,0,409,106,1,0,0,0,410,411,5,92,0,0,411,
        412,7,14,0,0,412,108,1,0,0,0,413,418,5,34,0,0,414,417,3,105,52,0,
        415,417,3,107,53,0,416,414,1,0,0,0,416,415,1,0,0,0,417,420,1,0,0,
        0,418,416,1,0,0,0,418,419,1,0,0,0,419,421,1,0,0,0,420,418,1,0,0,
        0,421,422,5,34,0,0,422,110,1,0,0,0,423,427,7,15,0,0,424,426,7,16,
        0,0,425,424,1,0,0,0,426,429,1,0,0,0,427,425,1,0,0,0,427,428,1,0,
        0,0,428,112,1,0,0,0,429,427,1,0,0,0,430,431,9,0,0,0,431,114,1,0,
        0,0,432,437,5,34,0,0,433,436,3,105,52,0,434,436,3,107,53,0,435,433,
        1,0,0,0,435,434,1,0,0,0,436,439,1,0,0,0,437,435,1,0,0,0,437,438,
        1,0,0,0,438,440,1,0,0,0,439,437,1,0,0,0,440,441,5,92,0,0,441,442,
        8,14,0,0,442,443,6,57,1,0,443,116,1,0,0,0,444,449,5,34,0,0,445,448,
        3,105,52,0,446,448,3,107,53,0,447,445,1,0,0,0,447,446,1,0,0,0,448,
        451,1,0,0,0,449,447,1,0,0,0,449,450,1,0,0,0,450,452,1,0,0,0,451,
        449,1,0,0,0,452,453,6,58,2,0,453,118,1,0,0,0,28,0,133,137,146,148,
        161,292,299,313,350,356,358,362,367,369,376,379,386,393,400,406,
        416,418,427,435,437,447,449,3,6,0,0,1,57,0,1,58,1
    ]

class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    SINGLE_LINE_CMT = 4
    MULTI_LINE_CMT = 5
    NL = 6
    WS = 7
    IF_ = 8
    ELSE_ = 9
    FOR_ = 10
    RETURN_ = 11
    FUNC_ = 12
    TYPE_ = 13
    STRUCT_ = 14
    INTERFACE_ = 15
    STRING_ = 16
    INT_ = 17
    FLOAT_ = 18
    BOOLEAN_ = 19
    CONST_ = 20
    VAR_ = 21
    CONTINUE_ = 22
    BREAK_ = 23
    RANGE_ = 24
    NIL_ = 25
    TRUE_ = 26
    FALSE_ = 27
    COMPARISON_OP = 28
    OP3 = 29
    ASSIGN1 = 30
    OP5 = 31
    ASSIGN = 32
    ADD = 33
    SUB = 34
    MUL = 35
    DIV = 36
    MOD = 37
    LPAREN = 38
    RPAREN = 39
    LSB = 40
    RSB = 41
    LCB = 42
    RCB = 43
    COMMA = 44
    SEMICOLON = 45
    FLOAT = 46
    INTEGER = 47
    STRING = 48
    ID = 49
    ERROR_CHAR = 50
    ILLEGAL_ESCAPE = 51
    UNCLOSE_STRING = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'||'", "'&&'", "'!'", "'\\n'", "'if'", "'else'", "'for'", "'return'", 
            "'func'", "'type'", "'struct'", "'interface'", "'string'", "'int'", 
            "'float'", "'boolean'", "'const'", "'var'", "'continue'", "'break'", 
            "'range'", "'nil'", "'true'", "'false'", "'.'", "'='", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "SINGLE_LINE_CMT", "MULTI_LINE_CMT", "NL", "WS", "IF_", "ELSE_", 
            "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", "INTERFACE_", 
            "STRING_", "INT_", "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
            "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", 
            "OP3", "ASSIGN1", "OP5", "ASSIGN", "ADD", "SUB", "MUL", "DIV", 
            "MOD", "LPAREN", "RPAREN", "LSB", "RSB", "LCB", "RCB", "COMMA", 
            "SEMICOLON", "FLOAT", "INTEGER", "STRING", "ID", "ERROR_CHAR", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "SINGLE_LINE_CMT", "MULTI_LINE_CMT", 
                  "NL", "WS", "IF_", "ELSE_", "FOR_", "RETURN_", "FUNC_", 
                  "TYPE_", "STRUCT_", "INTERFACE_", "STRING_", "INT_", "FLOAT_", 
                  "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", "BREAK_", "RANGE_", 
                  "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", "OP3", "ASSIGN1", 
                  "OP5", "ASSIGN", "ADD", "SUB", "MUL", "DIV", "MOD", "LPAREN", 
                  "RPAREN", "LSB", "RSB", "LCB", "RCB", "COMMA", "SEMICOLON", 
                  "Digit", "FLOAT", "DecInt", "BinInt", "OctInt", "HexInt", 
                  "INTEGER", "Char", "EscapeChar", "STRING", "ID", "ERROR_CHAR", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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
            actions[57] = self.ILLEGAL_ESCAPE_action 
            actions[58] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.split("\\n")[0][1:]
     


