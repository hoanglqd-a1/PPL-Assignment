# Generated from c:/coding/PPL/Assignment2/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
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
        4,0,53,530,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,1,0,1,0,1,0,1,0,5,0,126,8,0,10,0,12,0,129,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,5,1,138,8,1,10,1,12,1,141,9,1,1,1,1,1,1,1,
        1,1,1,1,1,2,3,2,149,8,2,1,2,1,2,1,2,1,3,4,3,155,8,3,11,3,12,3,156,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,330,8,24,1,25,1,25,1,25,
        1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,357,8,28,1,29,
        1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,31,1,31,1,31,1,32,1,32,1,32,
        1,33,1,33,1,33,1,34,1,34,1,34,1,35,1,35,1,35,1,36,1,36,1,36,1,37,
        1,37,1,37,1,38,1,38,1,38,1,39,1,39,1,39,1,40,1,40,1,40,1,41,1,41,
        1,41,1,42,1,42,1,42,1,43,1,43,1,43,1,44,1,44,1,44,1,45,1,45,1,45,
        1,46,1,46,1,47,4,47,415,8,47,11,47,12,47,416,1,47,1,47,4,47,421,
        8,47,11,47,12,47,422,3,47,425,8,47,1,47,1,47,3,47,429,8,47,1,47,
        4,47,432,8,47,11,47,12,47,433,3,47,436,8,47,1,47,1,47,1,48,1,48,
        1,48,5,48,443,8,48,10,48,12,48,446,9,48,3,48,448,8,48,1,49,1,49,
        1,49,4,49,453,8,49,11,49,12,49,454,1,50,1,50,1,50,4,50,460,8,50,
        11,50,12,50,461,1,51,1,51,1,51,4,51,467,8,51,11,51,12,51,468,1,52,
        1,52,1,52,1,52,3,52,475,8,52,1,52,1,52,1,53,1,53,1,54,1,54,1,54,
        1,55,1,55,1,55,5,55,487,8,55,10,55,12,55,490,9,55,1,55,1,55,1,55,
        1,56,1,56,5,56,497,8,56,10,56,12,56,500,9,56,1,56,1,56,1,57,1,57,
        1,57,1,58,1,58,1,58,5,58,510,8,58,10,58,12,58,513,9,58,1,58,1,58,
        1,58,1,58,1,58,1,59,1,59,1,59,5,59,523,8,59,10,59,12,59,526,9,59,
        1,59,1,59,1,59,1,139,0,60,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,
        9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,
        20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,
        31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,83,
        42,85,43,87,44,89,45,91,46,93,0,95,47,97,0,99,0,101,0,103,0,105,
        48,107,0,109,0,111,49,113,50,115,51,117,52,119,53,1,0,16,1,0,10,
        10,3,0,9,9,13,13,32,32,1,0,48,57,2,0,69,69,101,101,2,0,43,43,45,
        45,1,0,49,57,2,0,66,66,98,98,1,0,48,49,2,0,79,79,111,111,1,0,48,
        55,2,0,88,88,120,120,3,0,48,57,65,70,97,102,2,0,34,34,92,92,5,0,
        34,34,92,92,110,110,114,114,116,116,3,0,65,90,95,95,97,122,4,0,48,
        57,65,90,95,95,97,122,557,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,
        7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,
        1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,
        1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,
        1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,
        1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,
        1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,
        1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,
        1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,
        1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,95,1,0,0,0,0,105,1,0,0,0,0,111,
        1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,
        1,121,1,0,0,0,3,132,1,0,0,0,5,148,1,0,0,0,7,154,1,0,0,0,9,160,1,
        0,0,0,11,165,1,0,0,0,13,172,1,0,0,0,15,178,1,0,0,0,17,187,1,0,0,
        0,19,194,1,0,0,0,21,201,1,0,0,0,23,210,1,0,0,0,25,222,1,0,0,0,27,
        231,1,0,0,0,29,237,1,0,0,0,31,245,1,0,0,0,33,255,1,0,0,0,35,263,
        1,0,0,0,37,269,1,0,0,0,39,280,1,0,0,0,41,288,1,0,0,0,43,296,1,0,
        0,0,45,302,1,0,0,0,47,309,1,0,0,0,49,329,1,0,0,0,51,331,1,0,0,0,
        53,336,1,0,0,0,55,341,1,0,0,0,57,356,1,0,0,0,59,358,1,0,0,0,61,363,
        1,0,0,0,63,366,1,0,0,0,65,369,1,0,0,0,67,372,1,0,0,0,69,375,1,0,
        0,0,71,378,1,0,0,0,73,381,1,0,0,0,75,384,1,0,0,0,77,387,1,0,0,0,
        79,390,1,0,0,0,81,393,1,0,0,0,83,396,1,0,0,0,85,399,1,0,0,0,87,402,
        1,0,0,0,89,405,1,0,0,0,91,408,1,0,0,0,93,411,1,0,0,0,95,414,1,0,
        0,0,97,447,1,0,0,0,99,449,1,0,0,0,101,456,1,0,0,0,103,463,1,0,0,
        0,105,474,1,0,0,0,107,478,1,0,0,0,109,480,1,0,0,0,111,483,1,0,0,
        0,113,494,1,0,0,0,115,503,1,0,0,0,117,506,1,0,0,0,119,519,1,0,0,
        0,121,122,5,47,0,0,122,123,5,47,0,0,123,127,1,0,0,0,124,126,8,0,
        0,0,125,124,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,1,0,
        0,0,128,130,1,0,0,0,129,127,1,0,0,0,130,131,6,0,0,0,131,2,1,0,0,
        0,132,133,5,47,0,0,133,134,5,42,0,0,134,139,1,0,0,0,135,138,3,3,
        1,0,136,138,9,0,0,0,137,135,1,0,0,0,137,136,1,0,0,0,138,141,1,0,
        0,0,139,140,1,0,0,0,139,137,1,0,0,0,140,142,1,0,0,0,141,139,1,0,
        0,0,142,143,5,42,0,0,143,144,5,47,0,0,144,145,1,0,0,0,145,146,6,
        1,0,0,146,4,1,0,0,0,147,149,5,13,0,0,148,147,1,0,0,0,148,149,1,0,
        0,0,149,150,1,0,0,0,150,151,5,10,0,0,151,152,6,2,1,0,152,6,1,0,0,
        0,153,155,7,1,0,0,154,153,1,0,0,0,155,156,1,0,0,0,156,154,1,0,0,
        0,156,157,1,0,0,0,157,158,1,0,0,0,158,159,6,3,0,0,159,8,1,0,0,0,
        160,161,5,105,0,0,161,162,5,102,0,0,162,163,1,0,0,0,163,164,6,4,
        2,0,164,10,1,0,0,0,165,166,5,101,0,0,166,167,5,108,0,0,167,168,5,
        115,0,0,168,169,5,101,0,0,169,170,1,0,0,0,170,171,6,5,3,0,171,12,
        1,0,0,0,172,173,5,102,0,0,173,174,5,111,0,0,174,175,5,114,0,0,175,
        176,1,0,0,0,176,177,6,6,4,0,177,14,1,0,0,0,178,179,5,114,0,0,179,
        180,5,101,0,0,180,181,5,116,0,0,181,182,5,117,0,0,182,183,5,114,
        0,0,183,184,5,110,0,0,184,185,1,0,0,0,185,186,6,7,5,0,186,16,1,0,
        0,0,187,188,5,102,0,0,188,189,5,117,0,0,189,190,5,110,0,0,190,191,
        5,99,0,0,191,192,1,0,0,0,192,193,6,8,6,0,193,18,1,0,0,0,194,195,
        5,116,0,0,195,196,5,121,0,0,196,197,5,112,0,0,197,198,5,101,0,0,
        198,199,1,0,0,0,199,200,6,9,7,0,200,20,1,0,0,0,201,202,5,115,0,0,
        202,203,5,116,0,0,203,204,5,114,0,0,204,205,5,117,0,0,205,206,5,
        99,0,0,206,207,5,116,0,0,207,208,1,0,0,0,208,209,6,10,8,0,209,22,
        1,0,0,0,210,211,5,105,0,0,211,212,5,110,0,0,212,213,5,116,0,0,213,
        214,5,101,0,0,214,215,5,114,0,0,215,216,5,102,0,0,216,217,5,97,0,
        0,217,218,5,99,0,0,218,219,5,101,0,0,219,220,1,0,0,0,220,221,6,11,
        9,0,221,24,1,0,0,0,222,223,5,115,0,0,223,224,5,116,0,0,224,225,5,
        114,0,0,225,226,5,105,0,0,226,227,5,110,0,0,227,228,5,103,0,0,228,
        229,1,0,0,0,229,230,6,12,10,0,230,26,1,0,0,0,231,232,5,105,0,0,232,
        233,5,110,0,0,233,234,5,116,0,0,234,235,1,0,0,0,235,236,6,13,11,
        0,236,28,1,0,0,0,237,238,5,102,0,0,238,239,5,108,0,0,239,240,5,111,
        0,0,240,241,5,97,0,0,241,242,5,116,0,0,242,243,1,0,0,0,243,244,6,
        14,12,0,244,30,1,0,0,0,245,246,5,98,0,0,246,247,5,111,0,0,247,248,
        5,111,0,0,248,249,5,108,0,0,249,250,5,101,0,0,250,251,5,97,0,0,251,
        252,5,110,0,0,252,253,1,0,0,0,253,254,6,15,13,0,254,32,1,0,0,0,255,
        256,5,99,0,0,256,257,5,111,0,0,257,258,5,110,0,0,258,259,5,115,0,
        0,259,260,5,116,0,0,260,261,1,0,0,0,261,262,6,16,14,0,262,34,1,0,
        0,0,263,264,5,118,0,0,264,265,5,97,0,0,265,266,5,114,0,0,266,267,
        1,0,0,0,267,268,6,17,15,0,268,36,1,0,0,0,269,270,5,99,0,0,270,271,
        5,111,0,0,271,272,5,110,0,0,272,273,5,116,0,0,273,274,5,105,0,0,
        274,275,5,110,0,0,275,276,5,117,0,0,276,277,5,101,0,0,277,278,1,
        0,0,0,278,279,6,18,16,0,279,38,1,0,0,0,280,281,5,98,0,0,281,282,
        5,114,0,0,282,283,5,101,0,0,283,284,5,97,0,0,284,285,5,107,0,0,285,
        286,1,0,0,0,286,287,6,19,17,0,287,40,1,0,0,0,288,289,5,114,0,0,289,
        290,5,97,0,0,290,291,5,110,0,0,291,292,5,103,0,0,292,293,5,101,0,
        0,293,294,1,0,0,0,294,295,6,20,18,0,295,42,1,0,0,0,296,297,5,110,
        0,0,297,298,5,105,0,0,298,299,5,108,0,0,299,300,1,0,0,0,300,301,
        6,21,19,0,301,44,1,0,0,0,302,303,5,116,0,0,303,304,5,114,0,0,304,
        305,5,117,0,0,305,306,5,101,0,0,306,307,1,0,0,0,307,308,6,22,20,
        0,308,46,1,0,0,0,309,310,5,102,0,0,310,311,5,97,0,0,311,312,5,108,
        0,0,312,313,5,115,0,0,313,314,5,101,0,0,314,315,1,0,0,0,315,316,
        6,23,21,0,316,48,1,0,0,0,317,318,5,61,0,0,318,330,5,61,0,0,319,320,
        5,33,0,0,320,330,5,61,0,0,321,330,5,60,0,0,322,323,5,60,0,0,323,
        330,5,61,0,0,324,330,5,62,0,0,325,326,5,62,0,0,326,327,5,61,0,0,
        327,328,1,0,0,0,328,330,6,24,22,0,329,317,1,0,0,0,329,319,1,0,0,
        0,329,321,1,0,0,0,329,322,1,0,0,0,329,324,1,0,0,0,329,325,1,0,0,
        0,330,50,1,0,0,0,331,332,5,38,0,0,332,333,5,38,0,0,333,334,1,0,0,
        0,334,335,6,25,23,0,335,52,1,0,0,0,336,337,5,124,0,0,337,338,5,124,
        0,0,338,339,1,0,0,0,339,340,6,26,24,0,340,54,1,0,0,0,341,342,5,33,
        0,0,342,343,6,27,25,0,343,56,1,0,0,0,344,345,5,43,0,0,345,357,5,
        61,0,0,346,347,5,45,0,0,347,357,5,61,0,0,348,349,5,42,0,0,349,357,
        5,61,0,0,350,351,5,47,0,0,351,357,5,61,0,0,352,353,5,37,0,0,353,
        354,5,61,0,0,354,355,1,0,0,0,355,357,6,28,26,0,356,344,1,0,0,0,356,
        346,1,0,0,0,356,348,1,0,0,0,356,350,1,0,0,0,356,352,1,0,0,0,357,
        58,1,0,0,0,358,359,5,58,0,0,359,360,5,61,0,0,360,361,1,0,0,0,361,
        362,6,29,27,0,362,60,1,0,0,0,363,364,5,46,0,0,364,365,6,30,28,0,
        365,62,1,0,0,0,366,367,5,61,0,0,367,368,6,31,29,0,368,64,1,0,0,0,
        369,370,5,43,0,0,370,371,6,32,30,0,371,66,1,0,0,0,372,373,5,45,0,
        0,373,374,6,33,31,0,374,68,1,0,0,0,375,376,5,42,0,0,376,377,6,34,
        32,0,377,70,1,0,0,0,378,379,5,47,0,0,379,380,6,35,33,0,380,72,1,
        0,0,0,381,382,5,37,0,0,382,383,6,36,34,0,383,74,1,0,0,0,384,385,
        5,40,0,0,385,386,6,37,35,0,386,76,1,0,0,0,387,388,5,41,0,0,388,389,
        6,38,36,0,389,78,1,0,0,0,390,391,5,91,0,0,391,392,6,39,37,0,392,
        80,1,0,0,0,393,394,5,93,0,0,394,395,6,40,38,0,395,82,1,0,0,0,396,
        397,5,123,0,0,397,398,6,41,39,0,398,84,1,0,0,0,399,400,5,125,0,0,
        400,401,6,42,40,0,401,86,1,0,0,0,402,403,5,44,0,0,403,404,6,43,41,
        0,404,88,1,0,0,0,405,406,5,59,0,0,406,407,6,44,42,0,407,90,1,0,0,
        0,408,409,5,58,0,0,409,410,6,45,43,0,410,92,1,0,0,0,411,412,7,2,
        0,0,412,94,1,0,0,0,413,415,3,93,46,0,414,413,1,0,0,0,415,416,1,0,
        0,0,416,414,1,0,0,0,416,417,1,0,0,0,417,418,1,0,0,0,418,424,5,46,
        0,0,419,421,3,93,46,0,420,419,1,0,0,0,421,422,1,0,0,0,422,420,1,
        0,0,0,422,423,1,0,0,0,423,425,1,0,0,0,424,420,1,0,0,0,424,425,1,
        0,0,0,425,435,1,0,0,0,426,428,7,3,0,0,427,429,7,4,0,0,428,427,1,
        0,0,0,428,429,1,0,0,0,429,431,1,0,0,0,430,432,3,93,46,0,431,430,
        1,0,0,0,432,433,1,0,0,0,433,431,1,0,0,0,433,434,1,0,0,0,434,436,
        1,0,0,0,435,426,1,0,0,0,435,436,1,0,0,0,436,437,1,0,0,0,437,438,
        6,47,44,0,438,96,1,0,0,0,439,448,5,48,0,0,440,444,7,5,0,0,441,443,
        7,2,0,0,442,441,1,0,0,0,443,446,1,0,0,0,444,442,1,0,0,0,444,445,
        1,0,0,0,445,448,1,0,0,0,446,444,1,0,0,0,447,439,1,0,0,0,447,440,
        1,0,0,0,448,98,1,0,0,0,449,450,5,48,0,0,450,452,7,6,0,0,451,453,
        7,7,0,0,452,451,1,0,0,0,453,454,1,0,0,0,454,452,1,0,0,0,454,455,
        1,0,0,0,455,100,1,0,0,0,456,457,5,48,0,0,457,459,7,8,0,0,458,460,
        7,9,0,0,459,458,1,0,0,0,460,461,1,0,0,0,461,459,1,0,0,0,461,462,
        1,0,0,0,462,102,1,0,0,0,463,464,5,48,0,0,464,466,7,10,0,0,465,467,
        7,11,0,0,466,465,1,0,0,0,467,468,1,0,0,0,468,466,1,0,0,0,468,469,
        1,0,0,0,469,104,1,0,0,0,470,475,3,97,48,0,471,475,3,99,49,0,472,
        475,3,101,50,0,473,475,3,103,51,0,474,470,1,0,0,0,474,471,1,0,0,
        0,474,472,1,0,0,0,474,473,1,0,0,0,475,476,1,0,0,0,476,477,6,52,45,
        0,477,106,1,0,0,0,478,479,8,12,0,0,479,108,1,0,0,0,480,481,5,92,
        0,0,481,482,7,13,0,0,482,110,1,0,0,0,483,488,5,34,0,0,484,487,3,
        107,53,0,485,487,3,109,54,0,486,484,1,0,0,0,486,485,1,0,0,0,487,
        490,1,0,0,0,488,486,1,0,0,0,488,489,1,0,0,0,489,491,1,0,0,0,490,
        488,1,0,0,0,491,492,5,34,0,0,492,493,6,55,46,0,493,112,1,0,0,0,494,
        498,7,14,0,0,495,497,7,15,0,0,496,495,1,0,0,0,497,500,1,0,0,0,498,
        496,1,0,0,0,498,499,1,0,0,0,499,501,1,0,0,0,500,498,1,0,0,0,501,
        502,6,56,47,0,502,114,1,0,0,0,503,504,9,0,0,0,504,505,6,57,48,0,
        505,116,1,0,0,0,506,511,5,34,0,0,507,510,3,107,53,0,508,510,3,109,
        54,0,509,507,1,0,0,0,509,508,1,0,0,0,510,513,1,0,0,0,511,509,1,0,
        0,0,511,512,1,0,0,0,512,514,1,0,0,0,513,511,1,0,0,0,514,515,5,92,
        0,0,515,516,8,13,0,0,516,517,6,58,49,0,517,518,6,58,50,0,518,118,
        1,0,0,0,519,524,5,34,0,0,520,523,3,107,53,0,521,523,3,109,54,0,522,
        520,1,0,0,0,522,521,1,0,0,0,523,526,1,0,0,0,524,522,1,0,0,0,524,
        525,1,0,0,0,525,527,1,0,0,0,526,524,1,0,0,0,527,528,6,59,51,0,528,
        529,6,59,52,0,529,120,1,0,0,0,27,0,127,137,139,148,156,329,356,416,
        422,424,428,433,435,444,447,454,461,468,474,486,488,498,509,511,
        522,524,53,6,0,0,1,2,0,1,4,1,1,5,2,1,6,3,1,7,4,1,8,5,1,9,6,1,10,
        7,1,11,8,1,12,9,1,13,10,1,14,11,1,15,12,1,16,13,1,17,14,1,18,15,
        1,19,16,1,20,17,1,21,18,1,22,19,1,23,20,1,24,21,1,25,22,1,26,23,
        1,27,24,1,28,25,1,29,26,1,30,27,1,31,28,1,32,29,1,33,30,1,34,31,
        1,35,32,1,36,33,1,37,34,1,38,35,1,39,36,1,40,37,1,41,38,1,42,39,
        1,43,40,1,44,41,1,45,42,1,47,43,1,52,44,1,55,45,1,56,46,1,57,47,
        1,58,48,1,58,49,1,59,50,1,59,51
    ]

class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SINGLE_LINE_CMT = 1
    MULTI_LINE_CMT = 2
    NL = 3
    WS = 4
    IF_ = 5
    ELSE_ = 6
    FOR_ = 7
    RETURN_ = 8
    FUNC_ = 9
    TYPE_ = 10
    STRUCT_ = 11
    INTERFACE_ = 12
    STRING_ = 13
    INT_ = 14
    FLOAT_ = 15
    BOOLEAN_ = 16
    CONST_ = 17
    VAR_ = 18
    CONTINUE_ = 19
    BREAK_ = 20
    RANGE_ = 21
    NIL_ = 22
    TRUE_ = 23
    FALSE_ = 24
    COMPARISON_OP = 25
    AND = 26
    OR = 27
    NOT = 28
    UPT_ASSIGN = 29
    ASSIGN = 30
    DOT = 31
    EQUAL = 32
    ADD = 33
    SUB = 34
    MUL = 35
    DIV = 36
    MOD = 37
    LP = 38
    RP = 39
    LSB = 40
    RSB = 41
    LCB = 42
    RCB = 43
    COMMA = 44
    SEMICOLON = 45
    COLON = 46
    FLOAT = 47
    INTEGER = 48
    STRING = 49
    ID = 50
    ERROR_CHAR = 51
    ILLEGAL_ESCAPE = 52
    UNCLOSE_STRING = 53

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'&&'", "'||'", "'!'", "':='", "'.'", "'='", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "SINGLE_LINE_CMT", "MULTI_LINE_CMT", "NL", "WS", "IF_", "ELSE_", 
            "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", "INTERFACE_", 
            "STRING_", "INT_", "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
            "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", 
            "AND", "OR", "NOT", "UPT_ASSIGN", "ASSIGN", "DOT", "EQUAL", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "LP", "RP", "LSB", "RSB", 
            "LCB", "RCB", "COMMA", "SEMICOLON", "COLON", "FLOAT", "INTEGER", 
            "STRING", "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "SINGLE_LINE_CMT", "MULTI_LINE_CMT", "NL", "WS", "IF_", 
                  "ELSE_", "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", 
                  "INTERFACE_", "STRING_", "INT_", "FLOAT_", "BOOLEAN_", 
                  "CONST_", "VAR_", "CONTINUE_", "BREAK_", "RANGE_", "NIL_", 
                  "TRUE_", "FALSE_", "COMPARISON_OP", "AND", "OR", "NOT", 
                  "UPT_ASSIGN", "ASSIGN", "DOT", "EQUAL", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "LP", "RP", "LSB", "RSB", "LCB", 
                  "RCB", "COMMA", "SEMICOLON", "COLON", "Digit", "FLOAT", 
                  "DecInt", "BinInt", "OctInt", "HexInt", "INTEGER", "Char", 
                  "EscapeChar", "STRING", "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING" ]

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
            actions[2] = self.NL_action 
            actions[4] = self.IF__action 
            actions[5] = self.ELSE__action 
            actions[6] = self.FOR__action 
            actions[7] = self.RETURN__action 
            actions[8] = self.FUNC__action 
            actions[9] = self.TYPE__action 
            actions[10] = self.STRUCT__action 
            actions[11] = self.INTERFACE__action 
            actions[12] = self.STRING__action 
            actions[13] = self.INT__action 
            actions[14] = self.FLOAT__action 
            actions[15] = self.BOOLEAN__action 
            actions[16] = self.CONST__action 
            actions[17] = self.VAR__action 
            actions[18] = self.CONTINUE__action 
            actions[19] = self.BREAK__action 
            actions[20] = self.RANGE__action 
            actions[21] = self.NIL__action 
            actions[22] = self.TRUE__action 
            actions[23] = self.FALSE__action 
            actions[24] = self.COMPARISON_OP_action 
            actions[25] = self.AND_action 
            actions[26] = self.OR_action 
            actions[27] = self.NOT_action 
            actions[28] = self.UPT_ASSIGN_action 
            actions[29] = self.ASSIGN_action 
            actions[30] = self.DOT_action 
            actions[31] = self.EQUAL_action 
            actions[32] = self.ADD_action 
            actions[33] = self.SUB_action 
            actions[34] = self.MUL_action 
            actions[35] = self.DIV_action 
            actions[36] = self.MOD_action 
            actions[37] = self.LP_action 
            actions[38] = self.RP_action 
            actions[39] = self.LSB_action 
            actions[40] = self.RSB_action 
            actions[41] = self.LCB_action 
            actions[42] = self.RCB_action 
            actions[43] = self.COMMA_action 
            actions[44] = self.SEMICOLON_action 
            actions[45] = self.COLON_action 
            actions[47] = self.FLOAT_action 
            actions[52] = self.INTEGER_action 
            actions[55] = self.STRING_action 
            actions[56] = self.ID_action 
            actions[57] = self.ERROR_CHAR_action 
            actions[58] = self.ILLEGAL_ESCAPE_action 
            actions[59] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            if self.lastTokenType in ['ID', 'INTEGER', 'FLOAT', 'TRUE_', 'FALSE_', 'STRING', 'INT_', 'FLOAT_', 'BOOLEAN_', 'STRING_', 'RETURN_', 'CONTINUE_', 'BREAK_', 'RP', 'RSB', 'RCB']:
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
     

    def AND_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 22:
            self.lastTypeToken = 'AND'
     

    def OR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 23:
            self.lastTypeToken = 'OR'
     

    def NOT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 24:
            self.lastTypeToken = 'NOT'
     

    def UPT_ASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 25:
            self.lastTokenType = 'UPT_ASSIGN'
     

    def ASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 26:
            self.lastTokenType = 'ASSIGN'
     

    def DOT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 27:
            self.lastTokenType = 'DOT'
     

    def EQUAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 28:
            self.lastTokenType = 'EQUAL'
     

    def ADD_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 29:
            self.lastTokenType = 'ADD'
     

    def SUB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 30:
            self.lastTokenType = 'SUB'
     

    def MUL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 31:
            self.lastTokenType = 'MUL'
     

    def DIV_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 32:
            self.lastTokenType = 'DIV'
     

    def MOD_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 33:
            self.lastTokenType = 'MOD'
     

    def LP_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 34:
            self.lastTokenType = 'LP'
     

    def RP_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 35:
            self.lastTokenType = 'RP'
     

    def LSB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 36:
            self.lastTokenType = 'LSB'
     

    def RSB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 37:
            self.lastTokenType = 'RSB'
     

    def LCB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 38:
            self.lastTokenType = 'LCB'
     

    def RCB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 39:
            self.lastTokenType = 'RCB'
     

    def COMMA_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 40:
            self.lastTokenType = 'COMMA'
     

    def SEMICOLON_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 41:
            self.lastTokenType = 'SEMICOLON'
     

    def COLON_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 42:
            self.lastTokenType = 'COLON'
     

    def FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 43:
            self.lastTokenType = 'FLOAT'
     

    def INTEGER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 44:
            self.lastTokenType = 'INTEGER'
     

    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 45:
            self.lastTokenType = 'STRING'
     

    def ID_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 46:
            self.lastTokenType = 'ID'
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 47:
            self.lastTokenType = 'ERROR_CHAR'
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 48:
            self.text = self.text[1:]
     

        if actionIndex == 49:
            self.lastTokenType = 'ILLEGAL_ESCAPE'
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 50:
            self.text = self.text.replace('\r','\n').split('\n')[0][1:]
     

        if actionIndex == 51:
            self.lastTokenType = 'UNCLOSE_STRING'
     


