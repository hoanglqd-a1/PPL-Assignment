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
        4,0,53,458,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,4,1,4,
        1,5,4,5,136,8,5,11,5,12,5,137,1,5,1,5,1,6,1,6,1,6,1,6,5,6,146,8,
        6,10,6,12,6,149,9,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,5,7,160,
        8,7,10,7,12,7,163,9,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,
        9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,
        1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,24,
        1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,
        1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,3,28,297,8,28,1,29,1,29,1,29,1,29,1,29,3,29,
        304,8,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,3,30,318,8,30,1,31,1,31,1,32,1,32,1,33,1,33,1,34,1,34,1,35,
        1,35,1,36,1,36,1,37,1,37,1,38,1,38,1,39,1,39,1,40,1,40,1,41,1,41,
        1,42,1,42,1,43,1,43,1,44,1,44,1,45,1,45,1,46,1,46,1,47,4,47,353,
        8,47,11,47,12,47,354,1,47,1,47,4,47,359,8,47,11,47,12,47,360,3,47,
        363,8,47,1,47,1,47,3,47,367,8,47,1,47,4,47,370,8,47,11,47,12,47,
        371,3,47,374,8,47,1,48,1,48,1,48,5,48,379,8,48,10,48,12,48,382,9,
        48,3,48,384,8,48,1,49,1,49,1,49,4,49,389,8,49,11,49,12,49,390,1,
        50,1,50,1,50,4,50,396,8,50,11,50,12,50,397,1,51,1,51,1,51,4,51,403,
        8,51,11,51,12,51,404,1,52,1,52,1,52,1,52,3,52,411,8,52,1,53,1,53,
        1,54,1,54,1,54,1,55,1,55,1,55,5,55,421,8,55,10,55,12,55,424,9,55,
        1,55,1,55,1,56,1,56,5,56,430,8,56,10,56,12,56,433,9,56,1,57,1,57,
        1,58,1,58,1,58,5,58,440,8,58,10,58,12,58,443,9,58,1,58,1,58,1,58,
        1,58,1,59,1,59,1,59,5,59,452,8,59,10,59,12,59,455,9,59,1,59,1,59,
        1,161,0,60,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,
        12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,
        23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,
        34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,43,87,44,89,
        45,91,46,93,0,95,47,97,0,99,0,101,0,103,0,105,48,107,0,109,0,111,
        49,113,50,115,51,117,52,119,53,1,0,16,3,0,9,9,13,13,32,32,2,0,10,
        10,13,13,1,0,48,57,2,0,69,69,101,101,2,0,43,43,45,45,1,0,49,57,2,
        0,66,66,98,98,1,0,48,49,2,0,79,79,111,111,1,0,48,55,2,0,88,88,120,
        120,3,0,48,57,65,70,97,102,2,0,34,34,92,92,5,0,34,34,92,92,110,110,
        114,114,116,116,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,
        122,487,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,
        0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,
        0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,
        0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,
        0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,
        0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,
        0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,
        0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,
        0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,
        0,0,0,91,1,0,0,0,0,95,1,0,0,0,0,105,1,0,0,0,0,111,1,0,0,0,0,113,
        1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,1,121,1,0,0,0,
        3,124,1,0,0,0,5,127,1,0,0,0,7,129,1,0,0,0,9,132,1,0,0,0,11,135,1,
        0,0,0,13,141,1,0,0,0,15,154,1,0,0,0,17,169,1,0,0,0,19,172,1,0,0,
        0,21,177,1,0,0,0,23,181,1,0,0,0,25,188,1,0,0,0,27,193,1,0,0,0,29,
        198,1,0,0,0,31,205,1,0,0,0,33,215,1,0,0,0,35,222,1,0,0,0,37,226,
        1,0,0,0,39,232,1,0,0,0,41,240,1,0,0,0,43,246,1,0,0,0,45,250,1,0,
        0,0,47,259,1,0,0,0,49,265,1,0,0,0,51,271,1,0,0,0,53,275,1,0,0,0,
        55,280,1,0,0,0,57,296,1,0,0,0,59,303,1,0,0,0,61,317,1,0,0,0,63,319,
        1,0,0,0,65,321,1,0,0,0,67,323,1,0,0,0,69,325,1,0,0,0,71,327,1,0,
        0,0,73,329,1,0,0,0,75,331,1,0,0,0,77,333,1,0,0,0,79,335,1,0,0,0,
        81,337,1,0,0,0,83,339,1,0,0,0,85,341,1,0,0,0,87,343,1,0,0,0,89,345,
        1,0,0,0,91,347,1,0,0,0,93,349,1,0,0,0,95,352,1,0,0,0,97,383,1,0,
        0,0,99,385,1,0,0,0,101,392,1,0,0,0,103,399,1,0,0,0,105,410,1,0,0,
        0,107,412,1,0,0,0,109,414,1,0,0,0,111,417,1,0,0,0,113,427,1,0,0,
        0,115,434,1,0,0,0,117,436,1,0,0,0,119,448,1,0,0,0,121,122,5,124,
        0,0,122,123,5,124,0,0,123,2,1,0,0,0,124,125,5,38,0,0,125,126,5,38,
        0,0,126,4,1,0,0,0,127,128,5,33,0,0,128,6,1,0,0,0,129,130,5,58,0,
        0,130,131,5,61,0,0,131,8,1,0,0,0,132,133,5,10,0,0,133,10,1,0,0,0,
        134,136,7,0,0,0,135,134,1,0,0,0,136,137,1,0,0,0,137,135,1,0,0,0,
        137,138,1,0,0,0,138,139,1,0,0,0,139,140,6,5,0,0,140,12,1,0,0,0,141,
        142,5,47,0,0,142,143,5,47,0,0,143,147,1,0,0,0,144,146,8,1,0,0,145,
        144,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,
        150,1,0,0,0,149,147,1,0,0,0,150,151,5,10,0,0,151,152,1,0,0,0,152,
        153,6,6,1,0,153,14,1,0,0,0,154,155,5,47,0,0,155,156,5,42,0,0,156,
        161,1,0,0,0,157,160,9,0,0,0,158,160,3,15,7,0,159,157,1,0,0,0,159,
        158,1,0,0,0,160,163,1,0,0,0,161,162,1,0,0,0,161,159,1,0,0,0,162,
        164,1,0,0,0,163,161,1,0,0,0,164,165,5,42,0,0,165,166,5,47,0,0,166,
        167,1,0,0,0,167,168,6,7,1,0,168,16,1,0,0,0,169,170,5,105,0,0,170,
        171,5,102,0,0,171,18,1,0,0,0,172,173,5,101,0,0,173,174,5,108,0,0,
        174,175,5,115,0,0,175,176,5,101,0,0,176,20,1,0,0,0,177,178,5,102,
        0,0,178,179,5,111,0,0,179,180,5,114,0,0,180,22,1,0,0,0,181,182,5,
        114,0,0,182,183,5,101,0,0,183,184,5,116,0,0,184,185,5,117,0,0,185,
        186,5,114,0,0,186,187,5,110,0,0,187,24,1,0,0,0,188,189,5,102,0,0,
        189,190,5,117,0,0,190,191,5,110,0,0,191,192,5,99,0,0,192,26,1,0,
        0,0,193,194,5,116,0,0,194,195,5,121,0,0,195,196,5,112,0,0,196,197,
        5,101,0,0,197,28,1,0,0,0,198,199,5,115,0,0,199,200,5,116,0,0,200,
        201,5,114,0,0,201,202,5,117,0,0,202,203,5,99,0,0,203,204,5,116,0,
        0,204,30,1,0,0,0,205,206,5,105,0,0,206,207,5,110,0,0,207,208,5,116,
        0,0,208,209,5,101,0,0,209,210,5,114,0,0,210,211,5,102,0,0,211,212,
        5,97,0,0,212,213,5,99,0,0,213,214,5,101,0,0,214,32,1,0,0,0,215,216,
        5,115,0,0,216,217,5,116,0,0,217,218,5,114,0,0,218,219,5,105,0,0,
        219,220,5,110,0,0,220,221,5,103,0,0,221,34,1,0,0,0,222,223,5,105,
        0,0,223,224,5,110,0,0,224,225,5,116,0,0,225,36,1,0,0,0,226,227,5,
        102,0,0,227,228,5,108,0,0,228,229,5,111,0,0,229,230,5,97,0,0,230,
        231,5,116,0,0,231,38,1,0,0,0,232,233,5,98,0,0,233,234,5,111,0,0,
        234,235,5,111,0,0,235,236,5,108,0,0,236,237,5,101,0,0,237,238,5,
        97,0,0,238,239,5,110,0,0,239,40,1,0,0,0,240,241,5,99,0,0,241,242,
        5,111,0,0,242,243,5,110,0,0,243,244,5,115,0,0,244,245,5,116,0,0,
        245,42,1,0,0,0,246,247,5,118,0,0,247,248,5,97,0,0,248,249,5,114,
        0,0,249,44,1,0,0,0,250,251,5,99,0,0,251,252,5,111,0,0,252,253,5,
        110,0,0,253,254,5,116,0,0,254,255,5,105,0,0,255,256,5,110,0,0,256,
        257,5,117,0,0,257,258,5,101,0,0,258,46,1,0,0,0,259,260,5,98,0,0,
        260,261,5,114,0,0,261,262,5,101,0,0,262,263,5,97,0,0,263,264,5,107,
        0,0,264,48,1,0,0,0,265,266,5,114,0,0,266,267,5,97,0,0,267,268,5,
        110,0,0,268,269,5,103,0,0,269,270,5,101,0,0,270,50,1,0,0,0,271,272,
        5,110,0,0,272,273,5,105,0,0,273,274,5,108,0,0,274,52,1,0,0,0,275,
        276,5,116,0,0,276,277,5,114,0,0,277,278,5,117,0,0,278,279,5,101,
        0,0,279,54,1,0,0,0,280,281,5,102,0,0,281,282,5,97,0,0,282,283,5,
        108,0,0,283,284,5,115,0,0,284,285,5,101,0,0,285,56,1,0,0,0,286,287,
        5,61,0,0,287,297,5,61,0,0,288,289,5,33,0,0,289,297,5,61,0,0,290,
        297,5,60,0,0,291,292,5,60,0,0,292,297,5,61,0,0,293,297,5,62,0,0,
        294,295,5,62,0,0,295,297,5,61,0,0,296,286,1,0,0,0,296,288,1,0,0,
        0,296,290,1,0,0,0,296,291,1,0,0,0,296,293,1,0,0,0,296,294,1,0,0,
        0,297,58,1,0,0,0,298,299,5,38,0,0,299,304,5,38,0,0,300,301,5,124,
        0,0,301,304,5,124,0,0,302,304,5,33,0,0,303,298,1,0,0,0,303,300,1,
        0,0,0,303,302,1,0,0,0,304,60,1,0,0,0,305,306,5,58,0,0,306,318,5,
        61,0,0,307,308,5,43,0,0,308,318,5,61,0,0,309,310,5,45,0,0,310,318,
        5,61,0,0,311,312,5,42,0,0,312,318,5,61,0,0,313,314,5,47,0,0,314,
        318,5,61,0,0,315,316,5,37,0,0,316,318,5,61,0,0,317,305,1,0,0,0,317,
        307,1,0,0,0,317,309,1,0,0,0,317,311,1,0,0,0,317,313,1,0,0,0,317,
        315,1,0,0,0,318,62,1,0,0,0,319,320,5,46,0,0,320,64,1,0,0,0,321,322,
        5,61,0,0,322,66,1,0,0,0,323,324,5,43,0,0,324,68,1,0,0,0,325,326,
        5,45,0,0,326,70,1,0,0,0,327,328,5,42,0,0,328,72,1,0,0,0,329,330,
        5,47,0,0,330,74,1,0,0,0,331,332,5,37,0,0,332,76,1,0,0,0,333,334,
        5,40,0,0,334,78,1,0,0,0,335,336,5,41,0,0,336,80,1,0,0,0,337,338,
        5,91,0,0,338,82,1,0,0,0,339,340,5,93,0,0,340,84,1,0,0,0,341,342,
        5,123,0,0,342,86,1,0,0,0,343,344,5,125,0,0,344,88,1,0,0,0,345,346,
        5,44,0,0,346,90,1,0,0,0,347,348,5,59,0,0,348,92,1,0,0,0,349,350,
        7,2,0,0,350,94,1,0,0,0,351,353,3,93,46,0,352,351,1,0,0,0,353,354,
        1,0,0,0,354,352,1,0,0,0,354,355,1,0,0,0,355,356,1,0,0,0,356,362,
        5,46,0,0,357,359,3,93,46,0,358,357,1,0,0,0,359,360,1,0,0,0,360,358,
        1,0,0,0,360,361,1,0,0,0,361,363,1,0,0,0,362,358,1,0,0,0,362,363,
        1,0,0,0,363,373,1,0,0,0,364,366,7,3,0,0,365,367,7,4,0,0,366,365,
        1,0,0,0,366,367,1,0,0,0,367,369,1,0,0,0,368,370,3,93,46,0,369,368,
        1,0,0,0,370,371,1,0,0,0,371,369,1,0,0,0,371,372,1,0,0,0,372,374,
        1,0,0,0,373,364,1,0,0,0,373,374,1,0,0,0,374,96,1,0,0,0,375,384,5,
        48,0,0,376,380,7,5,0,0,377,379,7,2,0,0,378,377,1,0,0,0,379,382,1,
        0,0,0,380,378,1,0,0,0,380,381,1,0,0,0,381,384,1,0,0,0,382,380,1,
        0,0,0,383,375,1,0,0,0,383,376,1,0,0,0,384,98,1,0,0,0,385,386,5,48,
        0,0,386,388,7,6,0,0,387,389,7,7,0,0,388,387,1,0,0,0,389,390,1,0,
        0,0,390,388,1,0,0,0,390,391,1,0,0,0,391,100,1,0,0,0,392,393,5,48,
        0,0,393,395,7,8,0,0,394,396,7,9,0,0,395,394,1,0,0,0,396,397,1,0,
        0,0,397,395,1,0,0,0,397,398,1,0,0,0,398,102,1,0,0,0,399,400,5,48,
        0,0,400,402,7,10,0,0,401,403,7,11,0,0,402,401,1,0,0,0,403,404,1,
        0,0,0,404,402,1,0,0,0,404,405,1,0,0,0,405,104,1,0,0,0,406,411,3,
        97,48,0,407,411,3,99,49,0,408,411,3,101,50,0,409,411,3,103,51,0,
        410,406,1,0,0,0,410,407,1,0,0,0,410,408,1,0,0,0,410,409,1,0,0,0,
        411,106,1,0,0,0,412,413,8,12,0,0,413,108,1,0,0,0,414,415,5,92,0,
        0,415,416,7,13,0,0,416,110,1,0,0,0,417,422,5,34,0,0,418,421,3,107,
        53,0,419,421,3,109,54,0,420,418,1,0,0,0,420,419,1,0,0,0,421,424,
        1,0,0,0,422,420,1,0,0,0,422,423,1,0,0,0,423,425,1,0,0,0,424,422,
        1,0,0,0,425,426,5,34,0,0,426,112,1,0,0,0,427,431,7,14,0,0,428,430,
        7,15,0,0,429,428,1,0,0,0,430,433,1,0,0,0,431,429,1,0,0,0,431,432,
        1,0,0,0,432,114,1,0,0,0,433,431,1,0,0,0,434,435,9,0,0,0,435,116,
        1,0,0,0,436,441,5,34,0,0,437,440,3,107,53,0,438,440,3,109,54,0,439,
        437,1,0,0,0,439,438,1,0,0,0,440,443,1,0,0,0,441,439,1,0,0,0,441,
        442,1,0,0,0,442,444,1,0,0,0,443,441,1,0,0,0,444,445,5,92,0,0,445,
        446,8,13,0,0,446,447,6,58,2,0,447,118,1,0,0,0,448,453,5,34,0,0,449,
        452,3,107,53,0,450,452,3,109,54,0,451,449,1,0,0,0,451,450,1,0,0,
        0,452,455,1,0,0,0,453,451,1,0,0,0,453,454,1,0,0,0,454,456,1,0,0,
        0,455,453,1,0,0,0,456,457,6,59,3,0,457,120,1,0,0,0,27,0,137,147,
        159,161,296,303,317,354,360,362,366,371,373,380,383,390,397,404,
        410,420,422,431,439,441,451,453,4,6,0,0,0,1,0,1,58,0,1,59,1
    ]

class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    NL = 5
    WS = 6
    SINGLE_LINE_CMT = 7
    MULTI_LINE_CMT = 8
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
    OP3 = 30
    ASSIGN1 = 31
    OP5 = 32
    ASSIGN = 33
    ADD = 34
    SUB = 35
    MUL = 36
    DIV = 37
    MOD = 38
    LPAREN = 39
    RPAREN = 40
    LSB = 41
    RSB = 42
    LCB = 43
    RCB = 44
    COMMA = 45
    SEMICOLON = 46
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
            "'||'", "'&&'", "'!'", "':='", "'\\n'", "'if'", "'else'", "'for'", 
            "'return'", "'func'", "'type'", "'struct'", "'interface'", "'string'", 
            "'int'", "'float'", "'boolean'", "'const'", "'var'", "'continue'", 
            "'break'", "'range'", "'nil'", "'true'", "'false'", "'.'", "'='", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "NL", "WS", "SINGLE_LINE_CMT", "MULTI_LINE_CMT", "IF_", "ELSE_", 
            "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", "INTERFACE_", 
            "STRING_", "INT_", "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
            "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", 
            "OP3", "ASSIGN1", "OP5", "ASSIGN", "ADD", "SUB", "MUL", "DIV", 
            "MOD", "LPAREN", "RPAREN", "LSB", "RSB", "LCB", "RCB", "COMMA", 
            "SEMICOLON", "FLOAT", "INTEGER", "STRING", "ID", "ERROR_CHAR", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "NL", "WS", "SINGLE_LINE_CMT", 
                  "MULTI_LINE_CMT", "IF_", "ELSE_", "FOR_", "RETURN_", "FUNC_", 
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
            actions[58] = self.ILLEGAL_ESCAPE_action 
            actions[59] = self.UNCLOSE_STRING_action 
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
     


