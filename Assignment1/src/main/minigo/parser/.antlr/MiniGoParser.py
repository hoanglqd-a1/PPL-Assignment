# Generated from c:/coding/PPL/Assignment1/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,62,581,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,65,
        2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,71,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,3,1,152,8,1,1,2,1,2,1,2,1,2,1,2,3,2,159,
        8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,172,8,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,182,8,4,10,4,12,4,185,9,4,1,5,1,
        5,1,5,1,5,1,5,1,5,5,5,193,8,5,10,5,12,5,196,9,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,5,6,205,8,6,10,6,12,6,208,9,6,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,5,7,219,8,7,10,7,12,7,222,9,7,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,236,8,8,10,8,12,8,239,9,8,1,9,1,
        9,1,9,1,9,1,9,3,9,246,8,9,1,10,1,10,1,10,1,10,1,10,5,10,253,8,10,
        10,10,12,10,256,9,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,264,8,11,
        1,12,1,12,1,12,3,12,269,8,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,
        1,15,1,15,1,15,1,15,1,16,1,16,3,16,284,8,16,1,17,1,17,1,17,1,17,
        1,17,3,17,291,8,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,300,8,
        18,1,19,1,19,3,19,304,8,19,1,20,1,20,1,20,3,20,309,8,20,1,20,1,20,
        1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,3,22,321,8,22,1,22,1,22,
        1,22,1,23,1,23,3,23,328,8,23,1,23,1,23,1,23,3,23,333,8,23,1,23,1,
        23,1,24,1,24,1,24,1,24,1,25,1,25,3,25,343,8,25,1,26,1,26,1,26,1,
        26,1,26,3,26,350,8,26,1,27,1,27,1,27,1,28,1,28,1,28,1,28,3,28,359,
        8,28,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,31,1,31,
        1,31,1,31,1,32,1,32,1,32,1,32,3,32,379,8,32,1,33,1,33,1,33,1,33,
        1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,
        3,36,398,8,36,1,37,1,37,1,37,3,37,403,8,37,1,37,1,37,1,38,1,38,1,
        38,1,38,1,39,1,39,1,39,3,39,414,8,39,1,40,1,40,1,40,1,40,3,40,420,
        8,40,1,41,1,41,1,41,1,41,1,41,3,41,427,8,41,1,42,1,42,1,42,1,42,
        3,42,433,8,42,1,43,1,43,1,43,1,44,1,44,1,44,1,44,1,45,1,45,1,45,
        1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,
        1,45,1,45,1,45,1,45,1,45,3,45,463,8,45,1,46,1,46,1,46,3,46,468,8,
        46,1,46,1,46,1,46,3,46,473,8,46,1,47,1,47,1,47,1,47,1,48,1,48,1,
        49,1,49,1,50,1,50,1,50,1,51,1,51,1,51,3,51,489,8,51,1,52,1,52,3,
        52,493,8,52,1,53,1,53,1,53,1,53,1,54,1,54,1,54,1,54,3,54,503,8,54,
        1,55,1,55,1,55,1,55,1,56,1,56,1,56,1,56,3,56,513,8,56,1,57,1,57,
        1,57,1,57,1,58,1,58,1,58,1,58,1,59,1,59,1,59,1,59,1,59,3,59,528,
        8,59,1,60,1,60,3,60,532,8,60,1,61,1,61,1,61,1,61,1,61,1,62,1,62,
        3,62,541,8,62,1,63,1,63,1,63,1,63,1,63,3,63,548,8,63,1,64,1,64,1,
        64,1,64,1,65,3,65,555,8,65,1,65,1,65,1,66,1,66,3,66,561,8,66,1,67,
        1,67,1,68,1,68,1,68,1,68,1,68,1,68,1,68,1,68,3,68,573,8,68,1,69,
        1,69,1,70,1,70,1,71,1,71,1,71,0,6,8,10,12,14,16,20,72,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,
        54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,
        98,100,102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,
        132,134,136,138,140,142,0,4,1,0,13,16,1,0,34,38,1,0,25,30,1,1,54,
        54,576,0,144,1,0,0,0,2,151,1,0,0,0,4,158,1,0,0,0,6,171,1,0,0,0,8,
        175,1,0,0,0,10,186,1,0,0,0,12,197,1,0,0,0,14,209,1,0,0,0,16,223,
        1,0,0,0,18,245,1,0,0,0,20,247,1,0,0,0,22,263,1,0,0,0,24,268,1,0,
        0,0,26,270,1,0,0,0,28,273,1,0,0,0,30,277,1,0,0,0,32,283,1,0,0,0,
        34,290,1,0,0,0,36,299,1,0,0,0,38,303,1,0,0,0,40,305,1,0,0,0,42,313,
        1,0,0,0,44,317,1,0,0,0,46,325,1,0,0,0,48,336,1,0,0,0,50,342,1,0,
        0,0,52,349,1,0,0,0,54,351,1,0,0,0,56,358,1,0,0,0,58,360,1,0,0,0,
        60,365,1,0,0,0,62,370,1,0,0,0,64,378,1,0,0,0,66,380,1,0,0,0,68,384,
        1,0,0,0,70,389,1,0,0,0,72,397,1,0,0,0,74,399,1,0,0,0,76,406,1,0,
        0,0,78,410,1,0,0,0,80,415,1,0,0,0,82,421,1,0,0,0,84,432,1,0,0,0,
        86,434,1,0,0,0,88,437,1,0,0,0,90,462,1,0,0,0,92,472,1,0,0,0,94,474,
        1,0,0,0,96,478,1,0,0,0,98,480,1,0,0,0,100,482,1,0,0,0,102,488,1,
        0,0,0,104,492,1,0,0,0,106,494,1,0,0,0,108,502,1,0,0,0,110,504,1,
        0,0,0,112,512,1,0,0,0,114,514,1,0,0,0,116,518,1,0,0,0,118,527,1,
        0,0,0,120,531,1,0,0,0,122,533,1,0,0,0,124,540,1,0,0,0,126,547,1,
        0,0,0,128,549,1,0,0,0,130,554,1,0,0,0,132,560,1,0,0,0,134,562,1,
        0,0,0,136,572,1,0,0,0,138,574,1,0,0,0,140,576,1,0,0,0,142,578,1,
        0,0,0,144,145,3,2,1,0,145,146,5,0,0,1,146,1,1,0,0,0,147,148,3,4,
        2,0,148,149,3,2,1,0,149,152,1,0,0,0,150,152,3,4,2,0,151,147,1,0,
        0,0,151,150,1,0,0,0,152,3,1,0,0,0,153,159,3,38,19,0,154,159,3,44,
        22,0,155,159,3,46,23,0,156,159,3,60,30,0,157,159,3,68,34,0,158,153,
        1,0,0,0,158,154,1,0,0,0,158,155,1,0,0,0,158,156,1,0,0,0,158,157,
        1,0,0,0,159,160,1,0,0,0,160,161,3,142,71,0,161,5,1,0,0,0,162,172,
        3,38,19,0,163,172,3,44,22,0,164,172,3,76,38,0,165,172,3,78,39,0,
        166,172,3,90,45,0,167,172,3,96,48,0,168,172,3,98,49,0,169,172,3,
        100,50,0,170,172,3,102,51,0,171,162,1,0,0,0,171,163,1,0,0,0,171,
        164,1,0,0,0,171,165,1,0,0,0,171,166,1,0,0,0,171,167,1,0,0,0,171,
        168,1,0,0,0,171,169,1,0,0,0,171,170,1,0,0,0,172,173,1,0,0,0,173,
        174,3,142,71,0,174,7,1,0,0,0,175,176,6,4,-1,0,176,177,3,10,5,0,177,
        183,1,0,0,0,178,179,10,2,0,0,179,180,5,32,0,0,180,182,3,10,5,0,181,
        178,1,0,0,0,182,185,1,0,0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,
        9,1,0,0,0,185,183,1,0,0,0,186,187,6,5,-1,0,187,188,3,12,6,0,188,
        194,1,0,0,0,189,190,10,2,0,0,190,191,5,31,0,0,191,193,3,12,6,0,192,
        189,1,0,0,0,193,196,1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,0,195,
        11,1,0,0,0,196,194,1,0,0,0,197,198,6,6,-1,0,198,199,3,14,7,0,199,
        206,1,0,0,0,200,201,10,2,0,0,201,202,3,140,70,0,202,203,3,14,7,0,
        203,205,1,0,0,0,204,200,1,0,0,0,205,208,1,0,0,0,206,204,1,0,0,0,
        206,207,1,0,0,0,207,13,1,0,0,0,208,206,1,0,0,0,209,210,6,7,-1,0,
        210,211,3,16,8,0,211,220,1,0,0,0,212,213,10,3,0,0,213,214,5,42,0,
        0,214,219,3,16,8,0,215,216,10,2,0,0,216,217,5,43,0,0,217,219,3,16,
        8,0,218,212,1,0,0,0,218,215,1,0,0,0,219,222,1,0,0,0,220,218,1,0,
        0,0,220,221,1,0,0,0,221,15,1,0,0,0,222,220,1,0,0,0,223,224,6,8,-1,
        0,224,225,3,18,9,0,225,237,1,0,0,0,226,227,10,4,0,0,227,228,5,44,
        0,0,228,236,3,18,9,0,229,230,10,3,0,0,230,231,5,45,0,0,231,236,3,
        18,9,0,232,233,10,2,0,0,233,234,5,46,0,0,234,236,3,18,9,0,235,226,
        1,0,0,0,235,229,1,0,0,0,235,232,1,0,0,0,236,239,1,0,0,0,237,235,
        1,0,0,0,237,238,1,0,0,0,238,17,1,0,0,0,239,237,1,0,0,0,240,241,5,
        33,0,0,241,246,3,18,9,0,242,243,5,43,0,0,243,246,3,18,9,0,244,246,
        3,20,10,0,245,240,1,0,0,0,245,242,1,0,0,0,245,244,1,0,0,0,246,19,
        1,0,0,0,247,248,6,10,-1,0,248,249,3,22,11,0,249,254,1,0,0,0,250,
        251,10,2,0,0,251,253,3,24,12,0,252,250,1,0,0,0,253,256,1,0,0,0,254,
        252,1,0,0,0,254,255,1,0,0,0,255,21,1,0,0,0,256,254,1,0,0,0,257,258,
        5,47,0,0,258,259,3,8,4,0,259,260,5,48,0,0,260,264,1,0,0,0,261,264,
        3,136,68,0,262,264,5,59,0,0,263,257,1,0,0,0,263,261,1,0,0,0,263,
        262,1,0,0,0,264,23,1,0,0,0,265,269,3,26,13,0,266,269,3,28,14,0,267,
        269,3,30,15,0,268,265,1,0,0,0,268,266,1,0,0,0,268,267,1,0,0,0,269,
        25,1,0,0,0,270,271,5,40,0,0,271,272,5,59,0,0,272,27,1,0,0,0,273,
        274,5,49,0,0,274,275,3,8,4,0,275,276,5,50,0,0,276,29,1,0,0,0,277,
        278,5,47,0,0,278,279,3,32,16,0,279,280,5,48,0,0,280,31,1,0,0,0,281,
        284,3,34,17,0,282,284,1,0,0,0,283,281,1,0,0,0,283,282,1,0,0,0,284,
        33,1,0,0,0,285,286,3,8,4,0,286,287,5,53,0,0,287,288,3,34,17,0,288,
        291,1,0,0,0,289,291,3,8,4,0,290,285,1,0,0,0,290,289,1,0,0,0,291,
        35,1,0,0,0,292,293,3,20,10,0,293,294,3,26,13,0,294,300,1,0,0,0,295,
        296,3,20,10,0,296,297,3,28,14,0,297,300,1,0,0,0,298,300,5,59,0,0,
        299,292,1,0,0,0,299,295,1,0,0,0,299,298,1,0,0,0,300,37,1,0,0,0,301,
        304,3,40,20,0,302,304,3,42,21,0,303,301,1,0,0,0,303,302,1,0,0,0,
        304,39,1,0,0,0,305,306,5,18,0,0,306,308,5,59,0,0,307,309,3,130,65,
        0,308,307,1,0,0,0,308,309,1,0,0,0,309,310,1,0,0,0,310,311,5,41,0,
        0,311,312,3,8,4,0,312,41,1,0,0,0,313,314,5,18,0,0,314,315,5,59,0,
        0,315,316,3,130,65,0,316,43,1,0,0,0,317,318,5,17,0,0,318,320,5,59,
        0,0,319,321,3,130,65,0,320,319,1,0,0,0,320,321,1,0,0,0,321,322,1,
        0,0,0,322,323,5,41,0,0,323,324,3,8,4,0,324,45,1,0,0,0,325,327,5,
        9,0,0,326,328,3,58,29,0,327,326,1,0,0,0,327,328,1,0,0,0,328,329,
        1,0,0,0,329,330,5,59,0,0,330,332,3,48,24,0,331,333,3,130,65,0,332,
        331,1,0,0,0,332,333,1,0,0,0,333,334,1,0,0,0,334,335,3,106,53,0,335,
        47,1,0,0,0,336,337,5,47,0,0,337,338,3,50,25,0,338,339,5,48,0,0,339,
        49,1,0,0,0,340,343,3,52,26,0,341,343,1,0,0,0,342,340,1,0,0,0,342,
        341,1,0,0,0,343,51,1,0,0,0,344,345,3,54,27,0,345,346,5,53,0,0,346,
        347,3,52,26,0,347,350,1,0,0,0,348,350,3,54,27,0,349,344,1,0,0,0,
        349,348,1,0,0,0,350,53,1,0,0,0,351,352,3,56,28,0,352,353,3,130,65,
        0,353,55,1,0,0,0,354,355,5,59,0,0,355,356,5,53,0,0,356,359,3,56,
        28,0,357,359,5,59,0,0,358,354,1,0,0,0,358,357,1,0,0,0,359,57,1,0,
        0,0,360,361,5,47,0,0,361,362,5,59,0,0,362,363,5,59,0,0,363,364,5,
        48,0,0,364,59,1,0,0,0,365,366,5,10,0,0,366,367,5,59,0,0,367,368,
        5,11,0,0,368,369,3,62,31,0,369,61,1,0,0,0,370,371,5,51,0,0,371,372,
        3,64,32,0,372,373,5,52,0,0,373,63,1,0,0,0,374,375,3,66,33,0,375,
        376,3,64,32,0,376,379,1,0,0,0,377,379,3,66,33,0,378,374,1,0,0,0,
        378,377,1,0,0,0,379,65,1,0,0,0,380,381,5,59,0,0,381,382,3,130,65,
        0,382,383,3,142,71,0,383,67,1,0,0,0,384,385,5,10,0,0,385,386,5,59,
        0,0,386,387,5,12,0,0,387,388,3,70,35,0,388,69,1,0,0,0,389,390,5,
        51,0,0,390,391,3,72,36,0,391,392,5,52,0,0,392,71,1,0,0,0,393,394,
        3,74,37,0,394,395,3,72,36,0,395,398,1,0,0,0,396,398,3,74,37,0,397,
        393,1,0,0,0,397,396,1,0,0,0,398,73,1,0,0,0,399,400,5,59,0,0,400,
        402,3,48,24,0,401,403,3,130,65,0,402,401,1,0,0,0,402,403,1,0,0,0,
        403,404,1,0,0,0,404,405,3,142,71,0,405,75,1,0,0,0,406,407,3,36,18,
        0,407,408,3,104,52,0,408,409,3,8,4,0,409,77,1,0,0,0,410,411,3,80,
        40,0,411,413,3,84,42,0,412,414,3,86,43,0,413,412,1,0,0,0,413,414,
        1,0,0,0,414,79,1,0,0,0,415,416,5,5,0,0,416,417,3,88,44,0,417,419,
        3,106,53,0,418,420,3,142,71,0,419,418,1,0,0,0,419,420,1,0,0,0,420,
        81,1,0,0,0,421,422,5,6,0,0,422,423,5,5,0,0,423,424,3,88,44,0,424,
        426,3,106,53,0,425,427,3,142,71,0,426,425,1,0,0,0,426,427,1,0,0,
        0,427,83,1,0,0,0,428,429,3,82,41,0,429,430,3,84,42,0,430,433,1,0,
        0,0,431,433,1,0,0,0,432,428,1,0,0,0,432,431,1,0,0,0,433,85,1,0,0,
        0,434,435,5,6,0,0,435,436,3,106,53,0,436,87,1,0,0,0,437,438,5,47,
        0,0,438,439,3,8,4,0,439,440,5,48,0,0,440,89,1,0,0,0,441,442,5,7,
        0,0,442,443,3,8,4,0,443,444,3,106,53,0,444,463,1,0,0,0,445,446,5,
        7,0,0,446,447,3,92,46,0,447,448,5,54,0,0,448,449,3,8,4,0,449,450,
        5,54,0,0,450,451,3,94,47,0,451,452,3,106,53,0,452,463,1,0,0,0,453,
        454,5,7,0,0,454,455,5,59,0,0,455,456,5,53,0,0,456,457,5,59,0,0,457,
        458,5,39,0,0,458,459,5,21,0,0,459,460,3,8,4,0,460,461,3,106,53,0,
        461,463,1,0,0,0,462,441,1,0,0,0,462,445,1,0,0,0,462,453,1,0,0,0,
        463,91,1,0,0,0,464,465,5,18,0,0,465,467,5,59,0,0,466,468,3,130,65,
        0,467,466,1,0,0,0,467,468,1,0,0,0,468,469,1,0,0,0,469,470,5,41,0,
        0,470,473,3,8,4,0,471,473,3,76,38,0,472,464,1,0,0,0,472,471,1,0,
        0,0,473,93,1,0,0,0,474,475,5,59,0,0,475,476,3,138,69,0,476,477,3,
        8,4,0,477,95,1,0,0,0,478,479,5,20,0,0,479,97,1,0,0,0,480,481,5,19,
        0,0,481,99,1,0,0,0,482,483,3,20,10,0,483,484,3,30,15,0,484,101,1,
        0,0,0,485,489,5,8,0,0,486,487,5,8,0,0,487,489,3,8,4,0,488,485,1,
        0,0,0,488,486,1,0,0,0,489,103,1,0,0,0,490,493,3,138,69,0,491,493,
        5,39,0,0,492,490,1,0,0,0,492,491,1,0,0,0,493,105,1,0,0,0,494,495,
        5,51,0,0,495,496,3,108,54,0,496,497,5,52,0,0,497,107,1,0,0,0,498,
        499,3,6,3,0,499,500,3,108,54,0,500,503,1,0,0,0,501,503,3,6,3,0,502,
        498,1,0,0,0,502,501,1,0,0,0,503,109,1,0,0,0,504,505,3,112,56,0,505,
        506,3,132,66,0,506,507,3,116,58,0,507,111,1,0,0,0,508,509,3,114,
        57,0,509,510,3,112,56,0,510,513,1,0,0,0,511,513,3,114,57,0,512,508,
        1,0,0,0,512,511,1,0,0,0,513,113,1,0,0,0,514,515,5,49,0,0,515,516,
        3,8,4,0,516,517,5,50,0,0,517,115,1,0,0,0,518,519,5,51,0,0,519,520,
        3,118,59,0,520,521,5,52,0,0,521,117,1,0,0,0,522,523,3,120,60,0,523,
        524,5,53,0,0,524,525,3,118,59,0,525,528,1,0,0,0,526,528,3,120,60,
        0,527,522,1,0,0,0,527,526,1,0,0,0,528,119,1,0,0,0,529,532,3,8,4,
        0,530,532,3,116,58,0,531,529,1,0,0,0,531,530,1,0,0,0,532,121,1,0,
        0,0,533,534,5,59,0,0,534,535,5,51,0,0,535,536,3,124,62,0,536,537,
        5,52,0,0,537,123,1,0,0,0,538,541,3,126,63,0,539,541,1,0,0,0,540,
        538,1,0,0,0,540,539,1,0,0,0,541,125,1,0,0,0,542,543,3,128,64,0,543,
        544,5,53,0,0,544,545,3,126,63,0,545,548,1,0,0,0,546,548,3,128,64,
        0,547,542,1,0,0,0,547,546,1,0,0,0,548,127,1,0,0,0,549,550,5,59,0,
        0,550,551,5,55,0,0,551,552,3,8,4,0,552,129,1,0,0,0,553,555,3,112,
        56,0,554,553,1,0,0,0,554,555,1,0,0,0,555,556,1,0,0,0,556,557,3,132,
        66,0,557,131,1,0,0,0,558,561,3,134,67,0,559,561,5,59,0,0,560,558,
        1,0,0,0,560,559,1,0,0,0,561,133,1,0,0,0,562,563,7,0,0,0,563,135,
        1,0,0,0,564,573,5,57,0,0,565,573,5,56,0,0,566,573,5,58,0,0,567,573,
        5,23,0,0,568,573,5,24,0,0,569,573,5,22,0,0,570,573,3,122,61,0,571,
        573,3,110,55,0,572,564,1,0,0,0,572,565,1,0,0,0,572,566,1,0,0,0,572,
        567,1,0,0,0,572,568,1,0,0,0,572,569,1,0,0,0,572,570,1,0,0,0,572,
        571,1,0,0,0,573,137,1,0,0,0,574,575,7,1,0,0,575,139,1,0,0,0,576,
        577,7,2,0,0,577,141,1,0,0,0,578,579,7,3,0,0,579,143,1,0,0,0,46,151,
        158,171,183,194,206,218,220,235,237,245,254,263,268,283,290,299,
        303,308,320,327,332,342,349,358,378,397,402,413,419,426,432,462,
        467,472,488,492,502,512,527,531,540,547,554,560,572
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'&&'", "'||'", "'!'", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "':='", "'.'", "'='", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "SINGLE_LINE_CMT", "MULTI_LINE_CMT", 
                      "NL", "WS", "IF_", "ELSE_", "FOR_", "RETURN_", "FUNC_", 
                      "TYPE_", "STRUCT_", "INTERFACE_", "STRING_", "INT_", 
                      "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
                      "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "EQCOM", 
                      "DIFFCOM", "LESSCOM", "LEQCOM", "GRECOM", "GEQCOM", 
                      "AND", "OR", "NOT", "ADDASSIGN", "SUBASSIGN", "MULASSIGN", 
                      "DIVASSIGN", "MODASSIGN", "ASSIGN", "DOT", "EQUAL", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "LP", "RP", "LSB", 
                      "RSB", "LCB", "RCB", "COMMA", "SEMICOLON", "COLON", 
                      "FLOAT", "INTEGER", "STRING", "ID", "ERROR_CHAR", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decl_lst = 1
    RULE_decl = 2
    RULE_stmt = 3
    RULE_expr = 4
    RULE_expr1 = 5
    RULE_expr2 = 6
    RULE_expr3 = 7
    RULE_expr4 = 8
    RULE_expr5 = 9
    RULE_expr6 = 10
    RULE_expr7 = 11
    RULE_tail = 12
    RULE_field_access_tail = 13
    RULE_arr_elem_access = 14
    RULE_funccall_tail = 15
    RULE_expr_lst = 16
    RULE_expr_lstprime = 17
    RULE_lhs = 18
    RULE_var_decl = 19
    RULE_withInit_var_decl = 20
    RULE_withoutInit_var_decl = 21
    RULE_const_decl = 22
    RULE_func_decl = 23
    RULE_funcparam = 24
    RULE_param_lst = 25
    RULE_param_lstprime = 26
    RULE_param = 27
    RULE_id_nnlst = 28
    RULE_receiver = 29
    RULE_struct_decl = 30
    RULE_structfield = 31
    RULE_fielddecl_nnlst = 32
    RULE_fielddecl = 33
    RULE_interface_decl = 34
    RULE_interfacemeth = 35
    RULE_interfacemeth_nnlst = 36
    RULE_interfacemethmem = 37
    RULE_assigning_stmt = 38
    RULE_ifelse_stmt = 39
    RULE_if_ = 40
    RULE_elseif_ = 41
    RULE_elseif_lst = 42
    RULE_else_ = 43
    RULE_condition = 44
    RULE_forloop_stmt = 45
    RULE_forloop_init = 46
    RULE_forloop_update = 47
    RULE_break_stmt = 48
    RULE_continue_stmt = 49
    RULE_funccall_stmt = 50
    RULE_return_stmt = 51
    RULE_assign = 52
    RULE_blockcode = 53
    RULE_stmt_nnlst = 54
    RULE_arr_literal = 55
    RULE_arridx_lst = 56
    RULE_arridx = 57
    RULE_arrvalue = 58
    RULE_arrelem_lst = 59
    RULE_arrelem = 60
    RULE_struct_literal = 61
    RULE_structparam_lst = 62
    RULE_structparam_lstprime = 63
    RULE_structparam = 64
    RULE_data_type = 65
    RULE_prime_datatype = 66
    RULE_primitive_datatype = 67
    RULE_literal = 68
    RULE_uptassign = 69
    RULE_compare_op = 70
    RULE_end_stm = 71

    ruleNames =  [ "program", "decl_lst", "decl", "stmt", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "tail", "field_access_tail", "arr_elem_access", "funccall_tail", 
                   "expr_lst", "expr_lstprime", "lhs", "var_decl", "withInit_var_decl", 
                   "withoutInit_var_decl", "const_decl", "func_decl", "funcparam", 
                   "param_lst", "param_lstprime", "param", "id_nnlst", "receiver", 
                   "struct_decl", "structfield", "fielddecl_nnlst", "fielddecl", 
                   "interface_decl", "interfacemeth", "interfacemeth_nnlst", 
                   "interfacemethmem", "assigning_stmt", "ifelse_stmt", 
                   "if_", "elseif_", "elseif_lst", "else_", "condition", 
                   "forloop_stmt", "forloop_init", "forloop_update", "break_stmt", 
                   "continue_stmt", "funccall_stmt", "return_stmt", "assign", 
                   "blockcode", "stmt_nnlst", "arr_literal", "arridx_lst", 
                   "arridx", "arrvalue", "arrelem_lst", "arrelem", "struct_literal", 
                   "structparam_lst", "structparam_lstprime", "structparam", 
                   "data_type", "prime_datatype", "primitive_datatype", 
                   "literal", "uptassign", "compare_op", "end_stm" ]

    EOF = Token.EOF
    SINGLE_LINE_CMT=1
    MULTI_LINE_CMT=2
    NL=3
    WS=4
    IF_=5
    ELSE_=6
    FOR_=7
    RETURN_=8
    FUNC_=9
    TYPE_=10
    STRUCT_=11
    INTERFACE_=12
    STRING_=13
    INT_=14
    FLOAT_=15
    BOOLEAN_=16
    CONST_=17
    VAR_=18
    CONTINUE_=19
    BREAK_=20
    RANGE_=21
    NIL_=22
    TRUE_=23
    FALSE_=24
    EQCOM=25
    DIFFCOM=26
    LESSCOM=27
    LEQCOM=28
    GRECOM=29
    GEQCOM=30
    AND=31
    OR=32
    NOT=33
    ADDASSIGN=34
    SUBASSIGN=35
    MULASSIGN=36
    DIVASSIGN=37
    MODASSIGN=38
    ASSIGN=39
    DOT=40
    EQUAL=41
    ADD=42
    SUB=43
    MUL=44
    DIV=45
    MOD=46
    LP=47
    RP=48
    LSB=49
    RSB=50
    LCB=51
    RCB=52
    COMMA=53
    SEMICOLON=54
    COLON=55
    FLOAT=56
    INTEGER=57
    STRING=58
    ID=59
    ERROR_CHAR=60
    ILLEGAL_ESCAPE=61
    UNCLOSE_STRING=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_lstContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.decl_lst()
            self.state = 145
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def decl_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_lst




    def decl_lst(self):

        localctx = MiniGoParser.Decl_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_lst)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.decl()
                self.state = 148
                self.decl_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interface_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 153
                self.var_decl()
                pass

            elif la_ == 2:
                self.state = 154
                self.const_decl()
                pass

            elif la_ == 3:
                self.state = 155
                self.func_decl()
                pass

            elif la_ == 4:
                self.state = 156
                self.struct_decl()
                pass

            elif la_ == 5:
                self.state = 157
                self.interface_decl()
                pass


            self.state = 160
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def assigning_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assigning_stmtContext,0)


        def ifelse_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Ifelse_stmtContext,0)


        def forloop_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Forloop_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_stmtContext,0)


        def funccall_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Funccall_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 162
                self.var_decl()
                pass

            elif la_ == 2:
                self.state = 163
                self.const_decl()
                pass

            elif la_ == 3:
                self.state = 164
                self.assigning_stmt()
                pass

            elif la_ == 4:
                self.state = 165
                self.ifelse_stmt()
                pass

            elif la_ == 5:
                self.state = 166
                self.forloop_stmt()
                pass

            elif la_ == 6:
                self.state = 167
                self.break_stmt()
                pass

            elif la_ == 7:
                self.state = 168
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.state = 169
                self.funccall_stmt()
                pass

            elif la_ == 9:
                self.state = 170
                self.return_stmt()
                pass


            self.state = 173
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 178
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 179
                    self.match(MiniGoParser.OR)
                    self.state = 180
                    self.expr1(0) 
                self.state = 185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 194
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 189
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 190
                    self.match(MiniGoParser.AND)
                    self.state = 191
                    self.expr2(0) 
                self.state = 196
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def compare_op(self):
            return self.getTypedRuleContext(MiniGoParser.Compare_opContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 206
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 200
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 201
                    self.compare_op()
                    self.state = 202
                    self.expr3(0) 
                self.state = 208
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 220
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 218
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 212
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 213
                        self.match(MiniGoParser.ADD)
                        self.state = 214
                        self.expr4(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 215
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 216
                        self.match(MiniGoParser.SUB)
                        self.state = 217
                        self.expr4(0)
                        pass

             
                self.state = 222
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 235
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 226
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 227
                        self.match(MiniGoParser.MUL)
                        self.state = 228
                        self.expr5()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 229
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 230
                        self.match(MiniGoParser.DIV)
                        self.state = 231
                        self.expr5()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 232
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 233
                        self.match(MiniGoParser.MOD)
                        self.state = 234
                        self.expr5()
                        pass

             
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr5)
        try:
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(MiniGoParser.NOT)
                self.state = 241
                self.expr5()
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.match(MiniGoParser.SUB)
                self.state = 243
                self.expr5()
                pass
            elif token in [22, 23, 24, 47, 49, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 3)
                self.state = 244
                self.expr6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def tail(self):
            return self.getTypedRuleContext(MiniGoParser.TailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 254
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 250
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 251
                    self.tail() 
                self.state = 256
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr7)
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.match(MiniGoParser.LP)
                self.state = 258
                self.expr(0)
                self.state = 259
                self.match(MiniGoParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 262
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_access_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Field_access_tailContext,0)


        def arr_elem_access(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_elem_accessContext,0)


        def funccall_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Funccall_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_tail




    def tail(self):

        localctx = MiniGoParser.TailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_tail)
        try:
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.field_access_tail()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.arr_elem_access()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 3)
                self.state = 267
                self.funccall_tail()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_access_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_field_access_tail




    def field_access_tail(self):

        localctx = MiniGoParser.Field_access_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_field_access_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(MiniGoParser.DOT)
            self.state = 271
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_elem_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_elem_access




    def arr_elem_access(self):

        localctx = MiniGoParser.Arr_elem_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_arr_elem_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(MiniGoParser.LSB)
            self.state = 274
            self.expr(0)
            self.state = 275
            self.match(MiniGoParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funccall_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_lstContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funccall_tail




    def funccall_tail(self):

        localctx = MiniGoParser.Funccall_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_funccall_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(MiniGoParser.LP)
            self.state = 278
            self.expr_lst()
            self.state = 279
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_lstprime(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_lstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_lst




    def expr_lst(self):

        localctx = MiniGoParser.Expr_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expr_lst)
        try:
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23, 24, 33, 43, 47, 49, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.expr_lstprime()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_lstprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def expr_lstprime(self):
            return self.getTypedRuleContext(MiniGoParser.Expr_lstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr_lstprime




    def expr_lstprime(self):

        localctx = MiniGoParser.Expr_lstprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr_lstprime)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.expr(0)
                self.state = 286
                self.match(MiniGoParser.COMMA)
                self.state = 287
                self.expr_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def field_access_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Field_access_tailContext,0)


        def arr_elem_access(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_elem_accessContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_lhs)
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.expr6(0)
                self.state = 293
                self.field_access_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.expr6(0)
                self.state = 296
                self.arr_elem_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 298
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def withInit_var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.WithInit_var_declContext,0)


        def withoutInit_var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.WithoutInit_var_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_decl)
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.withInit_var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.withoutInit_var_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WithInit_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_(self):
            return self.getToken(MiniGoParser.VAR_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_withInit_var_decl




    def withInit_var_decl(self):

        localctx = MiniGoParser.WithInit_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_withInit_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(MiniGoParser.VAR_)
            self.state = 306
            self.match(MiniGoParser.ID)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 577023702256967680) != 0):
                self.state = 307
                self.data_type()


            self.state = 310
            self.match(MiniGoParser.EQUAL)
            self.state = 311
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WithoutInit_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_(self):
            return self.getToken(MiniGoParser.VAR_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_withoutInit_var_decl




    def withoutInit_var_decl(self):

        localctx = MiniGoParser.WithoutInit_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_withoutInit_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(MiniGoParser.VAR_)
            self.state = 314
            self.match(MiniGoParser.ID)
            self.state = 315
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST_(self):
            return self.getToken(MiniGoParser.CONST_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_const_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(MiniGoParser.CONST_)
            self.state = 318
            self.match(MiniGoParser.ID)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 577023702256967680) != 0):
                self.state = 319
                self.data_type()


            self.state = 322
            self.match(MiniGoParser.EQUAL)
            self.state = 323
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_(self):
            return self.getToken(MiniGoParser.FUNC_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def funcparam(self):
            return self.getTypedRuleContext(MiniGoParser.FuncparamContext,0)


        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(MiniGoParser.FUNC_)
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 326
                self.receiver()


            self.state = 329
            self.match(MiniGoParser.ID)
            self.state = 330
            self.funcparam()
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 577023702256967680) != 0):
                self.state = 331
                self.data_type()


            self.state = 334
            self.blockcode()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncparamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def param_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Param_lstContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcparam




    def funcparam(self):

        localctx = MiniGoParser.FuncparamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_funcparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(MiniGoParser.LP)
            self.state = 337
            self.param_lst()
            self.state = 338
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_lstprime(self):
            return self.getTypedRuleContext(MiniGoParser.Param_lstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_lst




    def param_lst(self):

        localctx = MiniGoParser.Param_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_param_lst)
        try:
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.param_lstprime()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_lstprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def param_lstprime(self):
            return self.getTypedRuleContext(MiniGoParser.Param_lstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param_lstprime




    def param_lstprime(self):

        localctx = MiniGoParser.Param_lstprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_param_lstprime)
        try:
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.param()
                self.state = 345
                self.match(MiniGoParser.COMMA)
                self.state = 346
                self.param_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Id_nnlstContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.id_nnlst()
            self.state = 352
            self.data_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_nnlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def id_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Id_nnlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_id_nnlst




    def id_nnlst(self):

        localctx = MiniGoParser.Id_nnlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_id_nnlst)
        try:
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.match(MiniGoParser.ID)
                self.state = 355
                self.match(MiniGoParser.COMMA)
                self.state = 356
                self.id_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(MiniGoParser.LP)
            self.state = 361
            self.match(MiniGoParser.ID)
            self.state = 362
            self.match(MiniGoParser.ID)
            self.state = 363
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_(self):
            return self.getToken(MiniGoParser.TYPE_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT_(self):
            return self.getToken(MiniGoParser.STRUCT_, 0)

        def structfield(self):
            return self.getTypedRuleContext(MiniGoParser.StructfieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(MiniGoParser.TYPE_)
            self.state = 366
            self.match(MiniGoParser.ID)
            self.state = 367
            self.match(MiniGoParser.STRUCT_)
            self.state = 368
            self.structfield()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructfieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def fielddecl_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Fielddecl_nnlstContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structfield




    def structfield(self):

        localctx = MiniGoParser.StructfieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_structfield)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(MiniGoParser.LCB)
            self.state = 371
            self.fielddecl_nnlst()
            self.state = 372
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fielddecl_nnlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fielddecl(self):
            return self.getTypedRuleContext(MiniGoParser.FielddeclContext,0)


        def fielddecl_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Fielddecl_nnlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fielddecl_nnlst




    def fielddecl_nnlst(self):

        localctx = MiniGoParser.Fielddecl_nnlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_fielddecl_nnlst)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.fielddecl()
                self.state = 375
                self.fielddecl_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.fielddecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FielddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fielddecl




    def fielddecl(self):

        localctx = MiniGoParser.FielddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_fielddecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(MiniGoParser.ID)
            self.state = 381
            self.data_type()
            self.state = 382
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_(self):
            return self.getToken(MiniGoParser.TYPE_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE_(self):
            return self.getToken(MiniGoParser.INTERFACE_, 0)

        def interfacemeth(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacemethContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_decl




    def interface_decl(self):

        localctx = MiniGoParser.Interface_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_interface_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(MiniGoParser.TYPE_)
            self.state = 385
            self.match(MiniGoParser.ID)
            self.state = 386
            self.match(MiniGoParser.INTERFACE_)
            self.state = 387
            self.interfacemeth()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfacemethContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def interfacemeth_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Interfacemeth_nnlstContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfacemeth




    def interfacemeth(self):

        localctx = MiniGoParser.InterfacemethContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_interfacemeth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(MiniGoParser.LCB)
            self.state = 390
            self.interfacemeth_nnlst()
            self.state = 391
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interfacemeth_nnlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interfacemethmem(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacemethmemContext,0)


        def interfacemeth_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Interfacemeth_nnlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfacemeth_nnlst




    def interfacemeth_nnlst(self):

        localctx = MiniGoParser.Interfacemeth_nnlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_interfacemeth_nnlst)
        try:
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.interfacemethmem()
                self.state = 394
                self.interfacemeth_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                self.interfacemethmem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfacemethmemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def funcparam(self):
            return self.getTypedRuleContext(MiniGoParser.FuncparamContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfacemethmem




    def interfacemethmem(self):

        localctx = MiniGoParser.InterfacemethmemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_interfacemethmem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(MiniGoParser.ID)
            self.state = 400
            self.funcparam()
            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 577023702256967680) != 0):
                self.state = 401
                self.data_type()


            self.state = 404
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assigning_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def assign(self):
            return self.getTypedRuleContext(MiniGoParser.AssignContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assigning_stmt




    def assigning_stmt(self):

        localctx = MiniGoParser.Assigning_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_assigning_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.lhs()
            self.state = 407
            self.assign()
            self.state = 408
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ifelse_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_(self):
            return self.getTypedRuleContext(MiniGoParser.If_Context,0)


        def elseif_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Elseif_lstContext,0)


        def else_(self):
            return self.getTypedRuleContext(MiniGoParser.Else_Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifelse_stmt




    def ifelse_stmt(self):

        localctx = MiniGoParser.Ifelse_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_ifelse_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.if_()
            self.state = 411
            self.elseif_lst()
            self.state = 413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 412
                self.else_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_(self):
            return self.getToken(MiniGoParser.IF_, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_




    def if_(self):

        localctx = MiniGoParser.If_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_if_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(MiniGoParser.IF_)
            self.state = 416
            self.condition()
            self.state = 417
            self.blockcode()
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 418
                self.end_stm()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE_(self):
            return self.getToken(MiniGoParser.ELSE_, 0)

        def IF_(self):
            return self.getToken(MiniGoParser.IF_, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elseif_




    def elseif_(self):

        localctx = MiniGoParser.Elseif_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_elseif_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(MiniGoParser.ELSE_)
            self.state = 422
            self.match(MiniGoParser.IF_)
            self.state = 423
            self.condition()
            self.state = 424
            self.blockcode()
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 425
                self.end_stm()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_(self):
            return self.getTypedRuleContext(MiniGoParser.Elseif_Context,0)


        def elseif_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Elseif_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elseif_lst




    def elseif_lst(self):

        localctx = MiniGoParser.Elseif_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_elseif_lst)
        try:
            self.state = 432
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.elseif_()
                self.state = 429
                self.elseif_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE_(self):
            return self.getToken(MiniGoParser.ELSE_, 0)

        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_




    def else_(self):

        localctx = MiniGoParser.Else_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_else_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(MiniGoParser.ELSE_)
            self.state = 435
            self.blockcode()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_condition




    def condition(self):

        localctx = MiniGoParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(MiniGoParser.LP)
            self.state = 438
            self.expr(0)
            self.state = 439
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forloop_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_forloop_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForStepContext(Forloop_stmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Forloop_stmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR_(self):
            return self.getToken(MiniGoParser.FOR_, 0)
        def forloop_init(self):
            return self.getTypedRuleContext(MiniGoParser.Forloop_initContext,0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def forloop_update(self):
            return self.getTypedRuleContext(MiniGoParser.Forloop_updateContext,0)

        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)



    class ForBasicContext(Forloop_stmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Forloop_stmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR_(self):
            return self.getToken(MiniGoParser.FOR_, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)



    class ForEachContext(Forloop_stmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Forloop_stmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR_(self):
            return self.getToken(MiniGoParser.FOR_, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)
        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)
        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)
        def RANGE_(self):
            return self.getToken(MiniGoParser.RANGE_, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)




    def forloop_stmt(self):

        localctx = MiniGoParser.Forloop_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_forloop_stmt)
        try:
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                localctx = MiniGoParser.ForBasicContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.match(MiniGoParser.FOR_)
                self.state = 442
                self.expr(0)
                self.state = 443
                self.blockcode()
                pass

            elif la_ == 2:
                localctx = MiniGoParser.ForStepContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.match(MiniGoParser.FOR_)
                self.state = 446
                self.forloop_init()
                self.state = 447
                self.match(MiniGoParser.SEMICOLON)
                self.state = 448
                self.expr(0)
                self.state = 449
                self.match(MiniGoParser.SEMICOLON)
                self.state = 450
                self.forloop_update()
                self.state = 451
                self.blockcode()
                pass

            elif la_ == 3:
                localctx = MiniGoParser.ForEachContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 453
                self.match(MiniGoParser.FOR_)
                self.state = 454
                self.match(MiniGoParser.ID)
                self.state = 455
                self.match(MiniGoParser.COMMA)
                self.state = 456
                self.match(MiniGoParser.ID)
                self.state = 457
                self.match(MiniGoParser.ASSIGN)
                self.state = 458
                self.match(MiniGoParser.RANGE_)
                self.state = 459
                self.expr(0)
                self.state = 460
                self.blockcode()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forloop_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_(self):
            return self.getToken(MiniGoParser.VAR_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def assigning_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assigning_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forloop_init




    def forloop_init(self):

        localctx = MiniGoParser.Forloop_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_forloop_init)
        self._la = 0 # Token type
        try:
            self.state = 472
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.match(MiniGoParser.VAR_)
                self.state = 465
                self.match(MiniGoParser.ID)
                self.state = 467
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 577023702256967680) != 0):
                    self.state = 466
                    self.data_type()


                self.state = 469
                self.match(MiniGoParser.EQUAL)
                self.state = 470
                self.expr(0)
                pass
            elif token in [22, 23, 24, 47, 49, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 471
                self.assigning_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forloop_updateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def uptassign(self):
            return self.getTypedRuleContext(MiniGoParser.UptassignContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forloop_update




    def forloop_update(self):

        localctx = MiniGoParser.Forloop_updateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_forloop_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(MiniGoParser.ID)
            self.state = 475
            self.uptassign()
            self.state = 476
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK_(self):
            return self.getToken(MiniGoParser.BREAK_, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(MiniGoParser.BREAK_)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE_(self):
            return self.getToken(MiniGoParser.CONTINUE_, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(MiniGoParser.CONTINUE_)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funccall_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def funccall_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Funccall_tailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funccall_stmt




    def funccall_stmt(self):

        localctx = MiniGoParser.Funccall_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_funccall_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.expr6(0)
            self.state = 483
            self.funccall_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_(self):
            return self.getToken(MiniGoParser.RETURN_, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_return_stmt)
        try:
            self.state = 488
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.match(MiniGoParser.RETURN_)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 486
                self.match(MiniGoParser.RETURN_)
                self.state = 487
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def uptassign(self):
            return self.getTypedRuleContext(MiniGoParser.UptassignContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign




    def assign(self):

        localctx = MiniGoParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_assign)
        try:
            self.state = 492
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34, 35, 36, 37, 38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.uptassign()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 491
                self.match(MiniGoParser.ASSIGN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockcodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def stmt_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_nnlstContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_blockcode




    def blockcode(self):

        localctx = MiniGoParser.BlockcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_blockcode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(MiniGoParser.LCB)
            self.state = 495
            self.stmt_nnlst()
            self.state = 496
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_nnlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MiniGoParser.StmtContext,0)


        def stmt_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Stmt_nnlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt_nnlst




    def stmt_nnlst(self):

        localctx = MiniGoParser.Stmt_nnlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_stmt_nnlst)
        try:
            self.state = 502
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.stmt()
                self.state = 499
                self.stmt_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 501
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arridx_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Arridx_lstContext,0)


        def prime_datatype(self):
            return self.getTypedRuleContext(MiniGoParser.Prime_datatypeContext,0)


        def arrvalue(self):
            return self.getTypedRuleContext(MiniGoParser.ArrvalueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_literal




    def arr_literal(self):

        localctx = MiniGoParser.Arr_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_arr_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.arridx_lst()
            self.state = 505
            self.prime_datatype()
            self.state = 506
            self.arrvalue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arridx_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arridx(self):
            return self.getTypedRuleContext(MiniGoParser.ArridxContext,0)


        def arridx_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Arridx_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arridx_lst




    def arridx_lst(self):

        localctx = MiniGoParser.Arridx_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_arridx_lst)
        try:
            self.state = 512
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 508
                self.arridx()
                self.state = 509
                self.arridx_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 511
                self.arridx()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArridxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arridx




    def arridx(self):

        localctx = MiniGoParser.ArridxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_arridx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(MiniGoParser.LSB)
            self.state = 515
            self.expr(0)
            self.state = 516
            self.match(MiniGoParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def arrelem_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Arrelem_lstContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrvalue




    def arrvalue(self):

        localctx = MiniGoParser.ArrvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_arrvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.match(MiniGoParser.LCB)
            self.state = 519
            self.arrelem_lst()
            self.state = 520
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arrelem_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrelem(self):
            return self.getTypedRuleContext(MiniGoParser.ArrelemContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def arrelem_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Arrelem_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrelem_lst




    def arrelem_lst(self):

        localctx = MiniGoParser.Arrelem_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_arrelem_lst)
        try:
            self.state = 527
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 522
                self.arrelem()
                self.state = 523
                self.match(MiniGoParser.COMMA)
                self.state = 524
                self.arrelem_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 526
                self.arrelem()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrelemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def arrvalue(self):
            return self.getTypedRuleContext(MiniGoParser.ArrvalueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrelem




    def arrelem(self):

        localctx = MiniGoParser.ArrelemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_arrelem)
        try:
            self.state = 531
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23, 24, 33, 43, 47, 49, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 529
                self.expr(0)
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 530
                self.arrvalue()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def structparam_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Structparam_lstContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.match(MiniGoParser.ID)
            self.state = 534
            self.match(MiniGoParser.LCB)
            self.state = 535
            self.structparam_lst()
            self.state = 536
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Structparam_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structparam_lstprime(self):
            return self.getTypedRuleContext(MiniGoParser.Structparam_lstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structparam_lst




    def structparam_lst(self):

        localctx = MiniGoParser.Structparam_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_structparam_lst)
        try:
            self.state = 540
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 538
                self.structparam_lstprime()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Structparam_lstprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structparam(self):
            return self.getTypedRuleContext(MiniGoParser.StructparamContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def structparam_lstprime(self):
            return self.getTypedRuleContext(MiniGoParser.Structparam_lstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structparam_lstprime




    def structparam_lstprime(self):

        localctx = MiniGoParser.Structparam_lstprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_structparam_lstprime)
        try:
            self.state = 547
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 542
                self.structparam()
                self.state = 543
                self.match(MiniGoParser.COMMA)
                self.state = 544
                self.structparam_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 546
                self.structparam()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructparamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structparam




    def structparam(self):

        localctx = MiniGoParser.StructparamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_structparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.match(MiniGoParser.ID)
            self.state = 550
            self.match(MiniGoParser.COLON)
            self.state = 551
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prime_datatype(self):
            return self.getTypedRuleContext(MiniGoParser.Prime_datatypeContext,0)


        def arridx_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Arridx_lstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_data_type




    def data_type(self):

        localctx = MiniGoParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 553
                self.arridx_lst()


            self.state = 556
            self.prime_datatype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prime_datatypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_datatype(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_datatypeContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_prime_datatype




    def prime_datatype(self):

        localctx = MiniGoParser.Prime_datatypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_prime_datatype)
        try:
            self.state = 560
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 558
                self.primitive_datatype()
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 559
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_datatypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_(self):
            return self.getToken(MiniGoParser.INT_, 0)

        def FLOAT_(self):
            return self.getToken(MiniGoParser.FLOAT_, 0)

        def STRING_(self):
            return self.getToken(MiniGoParser.STRING_, 0)

        def BOOLEAN_(self):
            return self.getToken(MiniGoParser.BOOLEAN_, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_datatype




    def primitive_datatype(self):

        localctx = MiniGoParser.Primitive_datatypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_primitive_datatype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MiniGoParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def TRUE_(self):
            return self.getToken(MiniGoParser.TRUE_, 0)

        def FALSE_(self):
            return self.getToken(MiniGoParser.FALSE_, 0)

        def NIL_(self):
            return self.getToken(MiniGoParser.NIL_, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def arr_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_literal)
        try:
            self.state = 572
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 564
                self.match(MiniGoParser.INTEGER)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 565
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 3)
                self.state = 566
                self.match(MiniGoParser.STRING)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 567
                self.match(MiniGoParser.TRUE_)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 568
                self.match(MiniGoParser.FALSE_)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 6)
                self.state = 569
                self.match(MiniGoParser.NIL_)
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 7)
                self.state = 570
                self.struct_literal()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 8)
                self.state = 571
                self.arr_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UptassignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADDASSIGN(self):
            return self.getToken(MiniGoParser.ADDASSIGN, 0)

        def SUBASSIGN(self):
            return self.getToken(MiniGoParser.SUBASSIGN, 0)

        def MULASSIGN(self):
            return self.getToken(MiniGoParser.MULASSIGN, 0)

        def DIVASSIGN(self):
            return self.getToken(MiniGoParser.DIVASSIGN, 0)

        def MODASSIGN(self):
            return self.getToken(MiniGoParser.MODASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_uptassign




    def uptassign(self):

        localctx = MiniGoParser.UptassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_uptassign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 532575944704) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compare_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQCOM(self):
            return self.getToken(MiniGoParser.EQCOM, 0)

        def DIFFCOM(self):
            return self.getToken(MiniGoParser.DIFFCOM, 0)

        def LESSCOM(self):
            return self.getToken(MiniGoParser.LESSCOM, 0)

        def LEQCOM(self):
            return self.getToken(MiniGoParser.LEQCOM, 0)

        def GRECOM(self):
            return self.getToken(MiniGoParser.GRECOM, 0)

        def GEQCOM(self):
            return self.getToken(MiniGoParser.GEQCOM, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_compare_op




    def compare_op(self):

        localctx = MiniGoParser.Compare_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_compare_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2113929216) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class End_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_end_stm




    def end_stm(self):

        localctx = MiniGoParser.End_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_end_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 578
            _la = self._input.LA(1)
            if not(_la==-1 or _la==54):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        self._predicates[5] = self.expr1_sempred
        self._predicates[6] = self.expr2_sempred
        self._predicates[7] = self.expr3_sempred
        self._predicates[8] = self.expr4_sempred
        self._predicates[10] = self.expr6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




