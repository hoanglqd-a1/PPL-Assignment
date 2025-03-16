# Generated from c:/coding/PPL/Assignment2/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
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
        4,1,62,569,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,65,
        2,66,7,66,2,67,7,67,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,144,8,1,1,2,
        1,2,1,2,1,2,1,2,3,2,151,8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,3,3,164,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,174,8,4,
        10,4,12,4,177,9,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,185,8,5,10,5,12,5,
        188,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,197,8,6,10,6,12,6,200,9,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,211,8,7,10,7,12,7,214,
        9,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,228,8,8,
        10,8,12,8,231,9,8,1,9,1,9,1,9,1,9,1,9,3,9,238,8,9,1,10,1,10,1,10,
        1,10,1,10,3,10,245,8,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,5,10,259,8,10,10,10,12,10,262,9,10,1,11,1,11,
        1,11,1,11,1,11,1,11,3,11,270,8,11,1,12,1,12,1,12,1,13,1,13,1,13,
        1,13,3,13,279,8,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,
        1,16,3,16,291,8,16,1,17,1,17,1,17,1,17,1,17,3,17,298,8,17,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,3,18,307,8,18,1,19,1,19,3,19,311,8,19,
        1,20,1,20,1,20,3,20,316,8,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,
        1,22,1,22,1,22,3,22,328,8,22,1,22,1,22,1,22,1,23,1,23,3,23,335,8,
        23,1,23,1,23,1,23,3,23,340,8,23,1,23,1,23,1,24,1,24,1,24,1,24,1,
        25,1,25,3,25,350,8,25,1,26,1,26,1,26,1,26,1,26,3,26,357,8,26,1,27,
        1,27,1,27,1,28,1,28,1,28,1,28,3,28,366,8,28,1,29,1,29,1,29,1,29,
        1,29,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,32,1,32,1,32,
        1,32,3,32,386,8,32,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,
        1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,3,36,405,8,36,1,37,1,37,
        1,37,3,37,410,8,37,1,37,1,37,1,38,1,38,1,38,1,38,1,39,1,39,1,39,
        3,39,421,8,39,1,40,1,40,1,40,1,40,3,40,427,8,40,1,41,1,41,1,41,1,
        41,1,41,3,41,434,8,41,1,42,1,42,1,42,1,42,3,42,440,8,42,1,43,1,43,
        1,43,1,44,1,44,1,44,1,44,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,
        1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,
        3,45,470,8,45,1,46,1,46,3,46,474,8,46,1,47,1,47,1,48,1,48,1,49,1,
        49,1,49,1,49,1,49,1,49,1,49,3,49,487,8,49,1,50,1,50,3,50,491,8,50,
        1,51,1,51,1,52,1,52,1,52,1,52,1,53,1,53,1,53,1,53,3,53,503,8,53,
        1,54,1,54,1,54,1,54,1,55,1,55,1,55,1,55,1,56,1,56,1,56,1,56,1,56,
        3,56,518,8,56,1,57,1,57,3,57,522,8,57,1,58,1,58,1,58,1,58,1,58,1,
        59,1,59,3,59,531,8,59,1,60,1,60,1,60,1,60,1,60,3,60,538,8,60,1,61,
        1,61,1,61,1,61,1,62,3,62,545,8,62,1,62,1,62,1,63,1,63,3,63,551,8,
        63,1,64,1,64,1,65,1,65,1,65,1,65,1,65,1,65,1,65,1,65,3,65,563,8,
        65,1,66,1,66,1,67,1,67,1,67,0,6,8,10,12,14,16,20,68,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,
        100,102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,
        132,134,0,4,1,0,34,39,1,0,13,16,1,0,25,30,1,1,54,54,569,0,136,1,
        0,0,0,2,143,1,0,0,0,4,150,1,0,0,0,6,163,1,0,0,0,8,167,1,0,0,0,10,
        178,1,0,0,0,12,189,1,0,0,0,14,201,1,0,0,0,16,215,1,0,0,0,18,237,
        1,0,0,0,20,244,1,0,0,0,22,269,1,0,0,0,24,271,1,0,0,0,26,278,1,0,
        0,0,28,280,1,0,0,0,30,284,1,0,0,0,32,290,1,0,0,0,34,297,1,0,0,0,
        36,306,1,0,0,0,38,310,1,0,0,0,40,312,1,0,0,0,42,320,1,0,0,0,44,324,
        1,0,0,0,46,332,1,0,0,0,48,343,1,0,0,0,50,349,1,0,0,0,52,356,1,0,
        0,0,54,358,1,0,0,0,56,365,1,0,0,0,58,367,1,0,0,0,60,372,1,0,0,0,
        62,377,1,0,0,0,64,385,1,0,0,0,66,387,1,0,0,0,68,391,1,0,0,0,70,396,
        1,0,0,0,72,404,1,0,0,0,74,406,1,0,0,0,76,413,1,0,0,0,78,417,1,0,
        0,0,80,422,1,0,0,0,82,428,1,0,0,0,84,439,1,0,0,0,86,441,1,0,0,0,
        88,444,1,0,0,0,90,469,1,0,0,0,92,473,1,0,0,0,94,475,1,0,0,0,96,477,
        1,0,0,0,98,486,1,0,0,0,100,488,1,0,0,0,102,492,1,0,0,0,104,494,1,
        0,0,0,106,502,1,0,0,0,108,504,1,0,0,0,110,508,1,0,0,0,112,517,1,
        0,0,0,114,521,1,0,0,0,116,523,1,0,0,0,118,530,1,0,0,0,120,537,1,
        0,0,0,122,539,1,0,0,0,124,544,1,0,0,0,126,550,1,0,0,0,128,552,1,
        0,0,0,130,562,1,0,0,0,132,564,1,0,0,0,134,566,1,0,0,0,136,137,3,
        2,1,0,137,138,5,0,0,1,138,1,1,0,0,0,139,140,3,4,2,0,140,141,3,2,
        1,0,141,144,1,0,0,0,142,144,3,4,2,0,143,139,1,0,0,0,143,142,1,0,
        0,0,144,3,1,0,0,0,145,151,3,38,19,0,146,151,3,44,22,0,147,151,3,
        46,23,0,148,151,3,60,30,0,149,151,3,68,34,0,150,145,1,0,0,0,150,
        146,1,0,0,0,150,147,1,0,0,0,150,148,1,0,0,0,150,149,1,0,0,0,151,
        152,1,0,0,0,152,153,3,134,67,0,153,5,1,0,0,0,154,164,3,38,19,0,155,
        164,3,44,22,0,156,164,3,76,38,0,157,164,3,78,39,0,158,164,3,90,45,
        0,159,164,3,94,47,0,160,164,3,96,48,0,161,164,3,98,49,0,162,164,
        3,100,50,0,163,154,1,0,0,0,163,155,1,0,0,0,163,156,1,0,0,0,163,157,
        1,0,0,0,163,158,1,0,0,0,163,159,1,0,0,0,163,160,1,0,0,0,163,161,
        1,0,0,0,163,162,1,0,0,0,164,165,1,0,0,0,165,166,3,134,67,0,166,7,
        1,0,0,0,167,168,6,4,-1,0,168,169,3,10,5,0,169,175,1,0,0,0,170,171,
        10,2,0,0,171,172,5,32,0,0,172,174,3,10,5,0,173,170,1,0,0,0,174,177,
        1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,9,1,0,0,0,177,175,1,
        0,0,0,178,179,6,5,-1,0,179,180,3,12,6,0,180,186,1,0,0,0,181,182,
        10,2,0,0,182,183,5,31,0,0,183,185,3,12,6,0,184,181,1,0,0,0,185,188,
        1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,11,1,0,0,0,188,186,1,
        0,0,0,189,190,6,6,-1,0,190,191,3,14,7,0,191,198,1,0,0,0,192,193,
        10,2,0,0,193,194,3,132,66,0,194,195,3,14,7,0,195,197,1,0,0,0,196,
        192,1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,
        13,1,0,0,0,200,198,1,0,0,0,201,202,6,7,-1,0,202,203,3,16,8,0,203,
        212,1,0,0,0,204,205,10,3,0,0,205,206,5,42,0,0,206,211,3,16,8,0,207,
        208,10,2,0,0,208,209,5,43,0,0,209,211,3,16,8,0,210,204,1,0,0,0,210,
        207,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,213,1,0,0,0,213,
        15,1,0,0,0,214,212,1,0,0,0,215,216,6,8,-1,0,216,217,3,18,9,0,217,
        229,1,0,0,0,218,219,10,4,0,0,219,220,5,44,0,0,220,228,3,18,9,0,221,
        222,10,3,0,0,222,223,5,45,0,0,223,228,3,18,9,0,224,225,10,2,0,0,
        225,226,5,46,0,0,226,228,3,18,9,0,227,218,1,0,0,0,227,221,1,0,0,
        0,227,224,1,0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,
        0,230,17,1,0,0,0,231,229,1,0,0,0,232,233,5,33,0,0,233,238,3,18,9,
        0,234,235,5,43,0,0,235,238,3,18,9,0,236,238,3,20,10,0,237,232,1,
        0,0,0,237,234,1,0,0,0,237,236,1,0,0,0,238,19,1,0,0,0,239,240,6,10,
        -1,0,240,245,3,22,11,0,241,242,3,22,11,0,242,243,3,26,13,0,243,245,
        1,0,0,0,244,239,1,0,0,0,244,241,1,0,0,0,245,260,1,0,0,0,246,247,
        10,6,0,0,247,259,3,24,12,0,248,249,10,5,0,0,249,259,3,30,15,0,250,
        251,10,3,0,0,251,252,3,24,12,0,252,253,3,26,13,0,253,259,1,0,0,0,
        254,255,10,2,0,0,255,256,3,30,15,0,256,257,3,26,13,0,257,259,1,0,
        0,0,258,246,1,0,0,0,258,248,1,0,0,0,258,250,1,0,0,0,258,254,1,0,
        0,0,259,262,1,0,0,0,260,258,1,0,0,0,260,261,1,0,0,0,261,21,1,0,0,
        0,262,260,1,0,0,0,263,264,5,47,0,0,264,265,3,8,4,0,265,266,5,48,
        0,0,266,270,1,0,0,0,267,270,3,130,65,0,268,270,5,59,0,0,269,263,
        1,0,0,0,269,267,1,0,0,0,269,268,1,0,0,0,270,23,1,0,0,0,271,272,5,
        40,0,0,272,273,5,59,0,0,273,25,1,0,0,0,274,275,3,28,14,0,275,276,
        3,26,13,0,276,279,1,0,0,0,277,279,3,28,14,0,278,274,1,0,0,0,278,
        277,1,0,0,0,279,27,1,0,0,0,280,281,5,49,0,0,281,282,3,8,4,0,282,
        283,5,50,0,0,283,29,1,0,0,0,284,285,5,47,0,0,285,286,3,32,16,0,286,
        287,5,48,0,0,287,31,1,0,0,0,288,291,3,34,17,0,289,291,1,0,0,0,290,
        288,1,0,0,0,290,289,1,0,0,0,291,33,1,0,0,0,292,293,3,8,4,0,293,294,
        5,53,0,0,294,295,3,34,17,0,295,298,1,0,0,0,296,298,3,8,4,0,297,292,
        1,0,0,0,297,296,1,0,0,0,298,35,1,0,0,0,299,300,3,20,10,0,300,301,
        3,24,12,0,301,307,1,0,0,0,302,303,3,20,10,0,303,304,3,26,13,0,304,
        307,1,0,0,0,305,307,5,59,0,0,306,299,1,0,0,0,306,302,1,0,0,0,306,
        305,1,0,0,0,307,37,1,0,0,0,308,311,3,40,20,0,309,311,3,42,21,0,310,
        308,1,0,0,0,310,309,1,0,0,0,311,39,1,0,0,0,312,313,5,18,0,0,313,
        315,5,59,0,0,314,316,3,124,62,0,315,314,1,0,0,0,315,316,1,0,0,0,
        316,317,1,0,0,0,317,318,5,41,0,0,318,319,3,8,4,0,319,41,1,0,0,0,
        320,321,5,18,0,0,321,322,5,59,0,0,322,323,3,124,62,0,323,43,1,0,
        0,0,324,325,5,17,0,0,325,327,5,59,0,0,326,328,3,124,62,0,327,326,
        1,0,0,0,327,328,1,0,0,0,328,329,1,0,0,0,329,330,5,41,0,0,330,331,
        3,8,4,0,331,45,1,0,0,0,332,334,5,9,0,0,333,335,3,58,29,0,334,333,
        1,0,0,0,334,335,1,0,0,0,335,336,1,0,0,0,336,337,5,59,0,0,337,339,
        3,48,24,0,338,340,3,124,62,0,339,338,1,0,0,0,339,340,1,0,0,0,340,
        341,1,0,0,0,341,342,3,104,52,0,342,47,1,0,0,0,343,344,5,47,0,0,344,
        345,3,50,25,0,345,346,5,48,0,0,346,49,1,0,0,0,347,350,3,52,26,0,
        348,350,1,0,0,0,349,347,1,0,0,0,349,348,1,0,0,0,350,51,1,0,0,0,351,
        352,3,54,27,0,352,353,5,53,0,0,353,354,3,52,26,0,354,357,1,0,0,0,
        355,357,3,54,27,0,356,351,1,0,0,0,356,355,1,0,0,0,357,53,1,0,0,0,
        358,359,3,56,28,0,359,360,3,124,62,0,360,55,1,0,0,0,361,362,5,59,
        0,0,362,363,5,53,0,0,363,366,3,56,28,0,364,366,5,59,0,0,365,361,
        1,0,0,0,365,364,1,0,0,0,366,57,1,0,0,0,367,368,5,47,0,0,368,369,
        5,59,0,0,369,370,5,59,0,0,370,371,5,48,0,0,371,59,1,0,0,0,372,373,
        5,10,0,0,373,374,5,59,0,0,374,375,5,11,0,0,375,376,3,62,31,0,376,
        61,1,0,0,0,377,378,5,51,0,0,378,379,3,64,32,0,379,380,5,52,0,0,380,
        63,1,0,0,0,381,382,3,66,33,0,382,383,3,64,32,0,383,386,1,0,0,0,384,
        386,3,66,33,0,385,381,1,0,0,0,385,384,1,0,0,0,386,65,1,0,0,0,387,
        388,5,59,0,0,388,389,3,124,62,0,389,390,3,134,67,0,390,67,1,0,0,
        0,391,392,5,10,0,0,392,393,5,59,0,0,393,394,5,12,0,0,394,395,3,70,
        35,0,395,69,1,0,0,0,396,397,5,51,0,0,397,398,3,72,36,0,398,399,5,
        52,0,0,399,71,1,0,0,0,400,401,3,74,37,0,401,402,3,72,36,0,402,405,
        1,0,0,0,403,405,3,74,37,0,404,400,1,0,0,0,404,403,1,0,0,0,405,73,
        1,0,0,0,406,407,5,59,0,0,407,409,3,48,24,0,408,410,3,124,62,0,409,
        408,1,0,0,0,409,410,1,0,0,0,410,411,1,0,0,0,411,412,3,134,67,0,412,
        75,1,0,0,0,413,414,3,36,18,0,414,415,3,102,51,0,415,416,3,8,4,0,
        416,77,1,0,0,0,417,418,3,80,40,0,418,420,3,84,42,0,419,421,3,86,
        43,0,420,419,1,0,0,0,420,421,1,0,0,0,421,79,1,0,0,0,422,423,5,5,
        0,0,423,424,3,88,44,0,424,426,3,104,52,0,425,427,3,134,67,0,426,
        425,1,0,0,0,426,427,1,0,0,0,427,81,1,0,0,0,428,429,5,6,0,0,429,430,
        5,5,0,0,430,431,3,88,44,0,431,433,3,104,52,0,432,434,3,134,67,0,
        433,432,1,0,0,0,433,434,1,0,0,0,434,83,1,0,0,0,435,436,3,82,41,0,
        436,437,3,84,42,0,437,440,1,0,0,0,438,440,1,0,0,0,439,435,1,0,0,
        0,439,438,1,0,0,0,440,85,1,0,0,0,441,442,5,6,0,0,442,443,3,104,52,
        0,443,87,1,0,0,0,444,445,5,47,0,0,445,446,3,8,4,0,446,447,5,48,0,
        0,447,89,1,0,0,0,448,449,5,7,0,0,449,450,3,8,4,0,450,451,3,104,52,
        0,451,470,1,0,0,0,452,453,5,7,0,0,453,454,3,92,46,0,454,455,5,54,
        0,0,455,456,3,8,4,0,456,457,5,54,0,0,457,458,3,76,38,0,458,459,3,
        104,52,0,459,470,1,0,0,0,460,461,5,7,0,0,461,462,5,59,0,0,462,463,
        5,53,0,0,463,464,5,59,0,0,464,465,5,39,0,0,465,466,5,21,0,0,466,
        467,3,8,4,0,467,468,3,104,52,0,468,470,1,0,0,0,469,448,1,0,0,0,469,
        452,1,0,0,0,469,460,1,0,0,0,470,91,1,0,0,0,471,474,3,40,20,0,472,
        474,3,76,38,0,473,471,1,0,0,0,473,472,1,0,0,0,474,93,1,0,0,0,475,
        476,5,20,0,0,476,95,1,0,0,0,477,478,5,19,0,0,478,97,1,0,0,0,479,
        480,5,59,0,0,480,487,3,30,15,0,481,482,3,20,10,0,482,483,5,40,0,
        0,483,484,5,59,0,0,484,485,3,30,15,0,485,487,1,0,0,0,486,479,1,0,
        0,0,486,481,1,0,0,0,487,99,1,0,0,0,488,490,5,8,0,0,489,491,3,8,4,
        0,490,489,1,0,0,0,490,491,1,0,0,0,491,101,1,0,0,0,492,493,7,0,0,
        0,493,103,1,0,0,0,494,495,5,51,0,0,495,496,3,106,53,0,496,497,5,
        52,0,0,497,105,1,0,0,0,498,499,3,6,3,0,499,500,3,106,53,0,500,503,
        1,0,0,0,501,503,3,6,3,0,502,498,1,0,0,0,502,501,1,0,0,0,503,107,
        1,0,0,0,504,505,3,26,13,0,505,506,3,126,63,0,506,507,3,110,55,0,
        507,109,1,0,0,0,508,509,5,51,0,0,509,510,3,112,56,0,510,511,5,52,
        0,0,511,111,1,0,0,0,512,513,3,114,57,0,513,514,5,53,0,0,514,515,
        3,112,56,0,515,518,1,0,0,0,516,518,3,114,57,0,517,512,1,0,0,0,517,
        516,1,0,0,0,518,113,1,0,0,0,519,522,3,8,4,0,520,522,3,110,55,0,521,
        519,1,0,0,0,521,520,1,0,0,0,522,115,1,0,0,0,523,524,5,59,0,0,524,
        525,5,51,0,0,525,526,3,118,59,0,526,527,5,52,0,0,527,117,1,0,0,0,
        528,531,3,120,60,0,529,531,1,0,0,0,530,528,1,0,0,0,530,529,1,0,0,
        0,531,119,1,0,0,0,532,533,3,122,61,0,533,534,5,53,0,0,534,535,3,
        120,60,0,535,538,1,0,0,0,536,538,3,122,61,0,537,532,1,0,0,0,537,
        536,1,0,0,0,538,121,1,0,0,0,539,540,5,59,0,0,540,541,5,55,0,0,541,
        542,3,8,4,0,542,123,1,0,0,0,543,545,3,26,13,0,544,543,1,0,0,0,544,
        545,1,0,0,0,545,546,1,0,0,0,546,547,3,126,63,0,547,125,1,0,0,0,548,
        551,3,128,64,0,549,551,5,59,0,0,550,548,1,0,0,0,550,549,1,0,0,0,
        551,127,1,0,0,0,552,553,7,1,0,0,553,129,1,0,0,0,554,563,5,57,0,0,
        555,563,5,56,0,0,556,563,5,58,0,0,557,563,5,23,0,0,558,563,5,24,
        0,0,559,563,5,22,0,0,560,563,3,116,58,0,561,563,3,108,54,0,562,554,
        1,0,0,0,562,555,1,0,0,0,562,556,1,0,0,0,562,557,1,0,0,0,562,558,
        1,0,0,0,562,559,1,0,0,0,562,560,1,0,0,0,562,561,1,0,0,0,563,131,
        1,0,0,0,564,565,7,2,0,0,565,133,1,0,0,0,566,567,7,3,0,0,567,135,
        1,0,0,0,46,143,150,163,175,186,198,210,212,227,229,237,244,258,260,
        269,278,290,297,306,310,315,327,334,339,349,356,365,385,404,409,
        420,426,433,439,469,473,486,490,502,517,521,530,537,544,550,562
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
    RULE_field_access_tail = 12
    RULE_arridx_nnlst = 13
    RULE_arridx = 14
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
    RULE_break_stmt = 47
    RULE_continue_stmt = 48
    RULE_funccall_stmt = 49
    RULE_return_stmt = 50
    RULE_assign = 51
    RULE_blockcode = 52
    RULE_stmt_nnlst = 53
    RULE_arr_literal = 54
    RULE_arrvalue = 55
    RULE_arrelem_lst = 56
    RULE_arrelem = 57
    RULE_struct_literal = 58
    RULE_structparam_lst = 59
    RULE_structparam_lstprime = 60
    RULE_structparam = 61
    RULE_data_type = 62
    RULE_prime_datatype = 63
    RULE_primitive_datatype = 64
    RULE_literal = 65
    RULE_compare_op = 66
    RULE_end_stm = 67

    ruleNames =  [ "program", "decl_lst", "decl", "stmt", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "field_access_tail", "arridx_nnlst", "arridx", "funccall_tail", 
                   "expr_lst", "expr_lstprime", "lhs", "var_decl", "withInit_var_decl", 
                   "withoutInit_var_decl", "const_decl", "func_decl", "funcparam", 
                   "param_lst", "param_lstprime", "param", "id_nnlst", "receiver", 
                   "struct_decl", "structfield", "fielddecl_nnlst", "fielddecl", 
                   "interface_decl", "interfacemeth", "interfacemeth_nnlst", 
                   "interfacemethmem", "assigning_stmt", "ifelse_stmt", 
                   "if_", "elseif_", "elseif_lst", "else_", "condition", 
                   "forloop_stmt", "forloop_init", "break_stmt", "continue_stmt", 
                   "funccall_stmt", "return_stmt", "assign", "blockcode", 
                   "stmt_nnlst", "arr_literal", "arrvalue", "arrelem_lst", 
                   "arrelem", "struct_literal", "structparam_lst", "structparam_lstprime", 
                   "structparam", "data_type", "prime_datatype", "primitive_datatype", 
                   "literal", "compare_op", "end_stm" ]

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
            self.state = 136
            self.decl_lst()
            self.state = 137
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
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.decl()
                self.state = 140
                self.decl_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
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
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 145
                self.var_decl()
                pass

            elif la_ == 2:
                self.state = 146
                self.const_decl()
                pass

            elif la_ == 3:
                self.state = 147
                self.func_decl()
                pass

            elif la_ == 4:
                self.state = 148
                self.struct_decl()
                pass

            elif la_ == 5:
                self.state = 149
                self.interface_decl()
                pass


            self.state = 152
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
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 154
                self.var_decl()
                pass

            elif la_ == 2:
                self.state = 155
                self.const_decl()
                pass

            elif la_ == 3:
                self.state = 156
                self.assigning_stmt()
                pass

            elif la_ == 4:
                self.state = 157
                self.ifelse_stmt()
                pass

            elif la_ == 5:
                self.state = 158
                self.forloop_stmt()
                pass

            elif la_ == 6:
                self.state = 159
                self.break_stmt()
                pass

            elif la_ == 7:
                self.state = 160
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.state = 161
                self.funccall_stmt()
                pass

            elif la_ == 9:
                self.state = 162
                self.return_stmt()
                pass


            self.state = 165
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
            self.state = 168
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 175
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 170
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 171
                    self.match(MiniGoParser.OR)
                    self.state = 172
                    self.expr1(0) 
                self.state = 177
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
            self.state = 179
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 181
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 182
                    self.match(MiniGoParser.AND)
                    self.state = 183
                    self.expr2(0) 
                self.state = 188
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
            self.state = 190
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 198
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 192
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 193
                    self.compare_op()
                    self.state = 194
                    self.expr3(0) 
                self.state = 200
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
            self.state = 202
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 210
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 204
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 205
                        self.match(MiniGoParser.ADD)
                        self.state = 206
                        self.expr4(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 207
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 208
                        self.match(MiniGoParser.SUB)
                        self.state = 209
                        self.expr4(0)
                        pass

             
                self.state = 214
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
            self.state = 216
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 227
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 218
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 219
                        self.match(MiniGoParser.MUL)
                        self.state = 220
                        self.expr5()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 221
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 222
                        self.match(MiniGoParser.DIV)
                        self.state = 223
                        self.expr5()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 224
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 225
                        self.match(MiniGoParser.MOD)
                        self.state = 226
                        self.expr5()
                        pass

             
                self.state = 231
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
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(MiniGoParser.NOT)
                self.state = 233
                self.expr5()
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(MiniGoParser.SUB)
                self.state = 235
                self.expr5()
                pass
            elif token in [22, 23, 24, 47, 49, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 3)
                self.state = 236
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


        def arridx_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Arridx_nnlstContext,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def field_access_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Field_access_tailContext,0)


        def funccall_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Funccall_tailContext,0)


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
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 240
                self.expr7()
                pass

            elif la_ == 2:
                self.state = 241
                self.expr7()
                self.state = 242
                self.arridx_nnlst()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 260
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 258
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 246
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 247
                        self.field_access_tail()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 248
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 249
                        self.funccall_tail()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 250
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 251
                        self.field_access_tail()
                        self.state = 252
                        self.arridx_nnlst()
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 254
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 255
                        self.funccall_tail()
                        self.state = 256
                        self.arridx_nnlst()
                        pass

             
                self.state = 262
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.match(MiniGoParser.LP)
                self.state = 264
                self.expr(0)
                self.state = 265
                self.match(MiniGoParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 268
                self.match(MiniGoParser.ID)
                pass


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
        self.enterRule(localctx, 24, self.RULE_field_access_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(MiniGoParser.DOT)
            self.state = 272
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arridx_nnlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arridx(self):
            return self.getTypedRuleContext(MiniGoParser.ArridxContext,0)


        def arridx_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Arridx_nnlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arridx_nnlst




    def arridx_nnlst(self):

        localctx = MiniGoParser.Arridx_nnlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arridx_nnlst)
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.arridx()
                self.state = 275
                self.arridx_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
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
        self.enterRule(localctx, 28, self.RULE_arridx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(MiniGoParser.LSB)
            self.state = 281
            self.expr(0)
            self.state = 282
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
            self.state = 284
            self.match(MiniGoParser.LP)
            self.state = 285
            self.expr_lst()
            self.state = 286
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
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23, 24, 33, 43, 47, 49, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
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
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.expr(0)
                self.state = 293
                self.match(MiniGoParser.COMMA)
                self.state = 294
                self.expr_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
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


        def arridx_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Arridx_nnlstContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_lhs)
        try:
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.expr6(0)
                self.state = 300
                self.field_access_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.expr6(0)
                self.state = 303
                self.arridx_nnlst()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 305
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
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.withInit_var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
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
            self.state = 312
            self.match(MiniGoParser.VAR_)
            self.state = 313
            self.match(MiniGoParser.ID)
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 577023702256967680) != 0):
                self.state = 314
                self.data_type()


            self.state = 317
            self.match(MiniGoParser.EQUAL)
            self.state = 318
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
            self.state = 320
            self.match(MiniGoParser.VAR_)
            self.state = 321
            self.match(MiniGoParser.ID)
            self.state = 322
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
            self.state = 324
            self.match(MiniGoParser.CONST_)
            self.state = 325
            self.match(MiniGoParser.ID)
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 577023702256967680) != 0):
                self.state = 326
                self.data_type()


            self.state = 329
            self.match(MiniGoParser.EQUAL)
            self.state = 330
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
            self.state = 332
            self.match(MiniGoParser.FUNC_)
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 333
                self.receiver()


            self.state = 336
            self.match(MiniGoParser.ID)
            self.state = 337
            self.funcparam()
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 577023702256967680) != 0):
                self.state = 338
                self.data_type()


            self.state = 341
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
            self.state = 343
            self.match(MiniGoParser.LP)
            self.state = 344
            self.param_lst()
            self.state = 345
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
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
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
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.param()
                self.state = 352
                self.match(MiniGoParser.COMMA)
                self.state = 353
                self.param_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
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
            self.state = 358
            self.id_nnlst()
            self.state = 359
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
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.match(MiniGoParser.ID)
                self.state = 362
                self.match(MiniGoParser.COMMA)
                self.state = 363
                self.id_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
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
            self.state = 367
            self.match(MiniGoParser.LP)
            self.state = 368
            self.match(MiniGoParser.ID)
            self.state = 369
            self.match(MiniGoParser.ID)
            self.state = 370
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
            self.state = 372
            self.match(MiniGoParser.TYPE_)
            self.state = 373
            self.match(MiniGoParser.ID)
            self.state = 374
            self.match(MiniGoParser.STRUCT_)
            self.state = 375
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
            self.state = 377
            self.match(MiniGoParser.LCB)
            self.state = 378
            self.fielddecl_nnlst()
            self.state = 379
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
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.fielddecl()
                self.state = 382
                self.fielddecl_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
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
            self.state = 387
            self.match(MiniGoParser.ID)
            self.state = 388
            self.data_type()
            self.state = 389
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
            self.state = 391
            self.match(MiniGoParser.TYPE_)
            self.state = 392
            self.match(MiniGoParser.ID)
            self.state = 393
            self.match(MiniGoParser.INTERFACE_)
            self.state = 394
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
            self.state = 396
            self.match(MiniGoParser.LCB)
            self.state = 397
            self.interfacemeth_nnlst()
            self.state = 398
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
            self.state = 404
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.interfacemethmem()
                self.state = 401
                self.interfacemeth_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
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
            self.state = 406
            self.match(MiniGoParser.ID)
            self.state = 407
            self.funcparam()
            self.state = 409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 577023702256967680) != 0):
                self.state = 408
                self.data_type()


            self.state = 411
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
            self.state = 413
            self.lhs()
            self.state = 414
            self.assign()
            self.state = 415
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
            self.state = 417
            self.if_()
            self.state = 418
            self.elseif_lst()
            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 419
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
            self.state = 422
            self.match(MiniGoParser.IF_)
            self.state = 423
            self.condition()
            self.state = 424
            self.blockcode()
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
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
            self.state = 428
            self.match(MiniGoParser.ELSE_)
            self.state = 429
            self.match(MiniGoParser.IF_)
            self.state = 430
            self.condition()
            self.state = 431
            self.blockcode()
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 432
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
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.elseif_()
                self.state = 436
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
            self.state = 441
            self.match(MiniGoParser.ELSE_)
            self.state = 442
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
            self.state = 444
            self.match(MiniGoParser.LP)
            self.state = 445
            self.expr(0)
            self.state = 446
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

        def assigning_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assigning_stmtContext,0)

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
            self.state = 469
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                localctx = MiniGoParser.ForBasicContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.match(MiniGoParser.FOR_)
                self.state = 449
                self.expr(0)
                self.state = 450
                self.blockcode()
                pass

            elif la_ == 2:
                localctx = MiniGoParser.ForStepContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                self.match(MiniGoParser.FOR_)
                self.state = 453
                self.forloop_init()
                self.state = 454
                self.match(MiniGoParser.SEMICOLON)
                self.state = 455
                self.expr(0)
                self.state = 456
                self.match(MiniGoParser.SEMICOLON)
                self.state = 457
                self.assigning_stmt()
                self.state = 458
                self.blockcode()
                pass

            elif la_ == 3:
                localctx = MiniGoParser.ForEachContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 460
                self.match(MiniGoParser.FOR_)
                self.state = 461
                self.match(MiniGoParser.ID)
                self.state = 462
                self.match(MiniGoParser.COMMA)
                self.state = 463
                self.match(MiniGoParser.ID)
                self.state = 464
                self.match(MiniGoParser.ASSIGN)
                self.state = 465
                self.match(MiniGoParser.RANGE_)
                self.state = 466
                self.expr(0)
                self.state = 467
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

        def withInit_var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.WithInit_var_declContext,0)


        def assigning_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assigning_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forloop_init




    def forloop_init(self):

        localctx = MiniGoParser.Forloop_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_forloop_init)
        try:
            self.state = 473
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 471
                self.withInit_var_decl()
                pass
            elif token in [22, 23, 24, 47, 49, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 472
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
        self.enterRule(localctx, 94, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
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
        self.enterRule(localctx, 96, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def funccall_tail(self):
            return self.getTypedRuleContext(MiniGoParser.Funccall_tailContext,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funccall_stmt




    def funccall_stmt(self):

        localctx = MiniGoParser.Funccall_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_funccall_stmt)
        try:
            self.state = 486
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 479
                self.match(MiniGoParser.ID)
                self.state = 480
                self.funccall_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
                self.expr6(0)
                self.state = 482
                self.match(MiniGoParser.DOT)
                self.state = 483
                self.match(MiniGoParser.ID)
                self.state = 484
                self.funccall_tail()
                pass


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
        self.enterRule(localctx, 100, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(MiniGoParser.RETURN_)
            self.state = 490
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1081576402723012608) != 0):
                self.state = 489
                self.expr(0)


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

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

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
            return MiniGoParser.RULE_assign




    def assign(self):

        localctx = MiniGoParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0)):
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
        self.enterRule(localctx, 104, self.RULE_blockcode)
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
        self.enterRule(localctx, 106, self.RULE_stmt_nnlst)
        try:
            self.state = 502
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
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

        def arridx_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Arridx_nnlstContext,0)


        def prime_datatype(self):
            return self.getTypedRuleContext(MiniGoParser.Prime_datatypeContext,0)


        def arrvalue(self):
            return self.getTypedRuleContext(MiniGoParser.ArrvalueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_literal




    def arr_literal(self):

        localctx = MiniGoParser.Arr_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_arr_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.arridx_nnlst()
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
        self.enterRule(localctx, 110, self.RULE_arrvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.match(MiniGoParser.LCB)
            self.state = 509
            self.arrelem_lst()
            self.state = 510
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
        self.enterRule(localctx, 112, self.RULE_arrelem_lst)
        try:
            self.state = 517
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 512
                self.arrelem()
                self.state = 513
                self.match(MiniGoParser.COMMA)
                self.state = 514
                self.arrelem_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 516
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
        self.enterRule(localctx, 114, self.RULE_arrelem)
        try:
            self.state = 521
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23, 24, 33, 43, 47, 49, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 519
                self.expr(0)
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 520
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
        self.enterRule(localctx, 116, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(MiniGoParser.ID)
            self.state = 524
            self.match(MiniGoParser.LCB)
            self.state = 525
            self.structparam_lst()
            self.state = 526
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
        self.enterRule(localctx, 118, self.RULE_structparam_lst)
        try:
            self.state = 530
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 528
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
        self.enterRule(localctx, 120, self.RULE_structparam_lstprime)
        try:
            self.state = 537
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 532
                self.structparam()
                self.state = 533
                self.match(MiniGoParser.COMMA)
                self.state = 534
                self.structparam_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 536
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
        self.enterRule(localctx, 122, self.RULE_structparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self.match(MiniGoParser.ID)
            self.state = 540
            self.match(MiniGoParser.COLON)
            self.state = 541
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


        def arridx_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Arridx_nnlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_data_type




    def data_type(self):

        localctx = MiniGoParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 543
                self.arridx_nnlst()


            self.state = 546
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
        self.enterRule(localctx, 126, self.RULE_prime_datatype)
        try:
            self.state = 550
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 548
                self.primitive_datatype()
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 549
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
        self.enterRule(localctx, 128, self.RULE_primitive_datatype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
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
        self.enterRule(localctx, 130, self.RULE_literal)
        try:
            self.state = 562
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 554
                self.match(MiniGoParser.INTEGER)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 555
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 3)
                self.state = 556
                self.match(MiniGoParser.STRING)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 557
                self.match(MiniGoParser.TRUE_)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 558
                self.match(MiniGoParser.FALSE_)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 6)
                self.state = 559
                self.match(MiniGoParser.NIL_)
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 7)
                self.state = 560
                self.struct_literal()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 8)
                self.state = 561
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
        self.enterRule(localctx, 132, self.RULE_compare_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
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
        self.enterRule(localctx, 134, self.RULE_end_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 566
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
                return self.precpred(self._ctx, 6)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         




