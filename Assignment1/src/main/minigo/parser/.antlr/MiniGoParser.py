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
        4,1,53,589,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,
        1,134,8,1,1,2,1,2,1,2,1,2,1,2,3,2,141,8,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,3,3,153,8,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,161,8,
        4,10,4,12,4,164,9,4,1,5,1,5,1,5,1,5,1,5,1,5,5,5,172,8,5,10,5,12,
        5,175,9,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,183,8,6,10,6,12,6,186,9,6,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,197,8,7,10,7,12,7,200,9,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,214,8,8,10,
        8,12,8,217,9,8,1,9,1,9,1,9,1,9,1,9,3,9,224,8,9,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,
        10,242,8,10,10,10,12,10,245,9,10,1,11,1,11,1,11,1,11,1,11,1,11,3,
        11,253,8,11,1,12,1,12,3,12,257,8,12,1,13,1,13,1,13,1,13,1,13,3,13,
        264,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        5,14,277,8,14,10,14,12,14,280,9,14,1,15,1,15,1,15,1,15,1,15,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,3,16,305,8,16,1,17,1,17,1,17,1,17,1,17,1,17,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,3,18,327,8,18,1,19,1,19,1,19,1,19,3,19,333,8,19,1,20,1,20,1,
        20,1,20,1,21,1,21,3,21,341,8,21,1,21,1,21,1,21,3,21,346,8,21,1,21,
        1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,3,23,357,8,23,1,24,1,24,
        1,24,1,24,1,24,3,24,364,8,24,1,25,1,25,1,25,1,26,1,26,1,26,1,26,
        1,26,1,27,1,27,1,27,1,27,3,27,378,8,27,1,28,1,28,1,28,1,28,1,28,
        1,28,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,3,30,394,8,30,1,31,
        1,31,1,31,3,31,399,8,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,
        3,31,409,8,31,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,
        1,34,1,34,1,34,1,34,3,34,425,8,34,1,35,1,35,1,35,3,35,430,8,35,1,
        35,1,35,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,3,37,443,8,
        37,1,38,1,38,1,38,1,38,1,38,3,38,450,8,38,1,39,1,39,1,39,1,39,3,
        39,456,8,39,1,40,1,40,1,40,3,40,461,8,40,1,41,1,41,1,41,1,41,1,42,
        1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,
        1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,1,42,
        1,42,3,42,495,8,42,1,43,1,43,3,43,499,8,43,1,44,1,44,1,44,1,45,1,
        45,1,45,1,46,1,46,1,46,1,46,1,46,1,46,1,47,1,47,1,47,1,47,1,47,1,
        47,3,47,519,8,47,1,48,1,48,1,49,1,49,1,49,1,49,1,50,1,50,1,50,1,
        50,3,50,531,8,50,1,51,1,51,1,51,1,51,1,52,1,52,1,52,1,52,1,53,1,
        53,1,53,1,53,1,53,3,53,546,8,53,1,54,1,54,3,54,550,8,54,1,55,1,55,
        1,55,1,55,1,55,1,56,1,56,3,56,559,8,56,1,57,1,57,1,57,1,57,1,57,
        3,57,566,8,57,1,58,1,58,1,58,1,58,1,59,1,59,3,59,574,8,59,1,60,1,
        60,1,61,1,61,1,61,1,61,1,61,1,61,1,61,3,61,585,8,61,1,62,1,62,1,
        62,0,7,8,10,12,14,16,20,28,63,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,
        70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,
        110,112,114,116,118,120,122,124,0,3,1,0,29,30,1,0,13,16,1,1,45,45,
        593,0,126,1,0,0,0,2,133,1,0,0,0,4,140,1,0,0,0,6,152,1,0,0,0,8,154,
        1,0,0,0,10,165,1,0,0,0,12,176,1,0,0,0,14,187,1,0,0,0,16,201,1,0,
        0,0,18,223,1,0,0,0,20,225,1,0,0,0,22,252,1,0,0,0,24,256,1,0,0,0,
        26,263,1,0,0,0,28,265,1,0,0,0,30,281,1,0,0,0,32,304,1,0,0,0,34,306,
        1,0,0,0,36,326,1,0,0,0,38,332,1,0,0,0,40,334,1,0,0,0,42,338,1,0,
        0,0,44,350,1,0,0,0,46,356,1,0,0,0,48,363,1,0,0,0,50,365,1,0,0,0,
        52,368,1,0,0,0,54,377,1,0,0,0,56,379,1,0,0,0,58,385,1,0,0,0,60,393,
        1,0,0,0,62,408,1,0,0,0,64,410,1,0,0,0,66,416,1,0,0,0,68,424,1,0,
        0,0,70,426,1,0,0,0,72,433,1,0,0,0,74,438,1,0,0,0,76,444,1,0,0,0,
        78,455,1,0,0,0,80,460,1,0,0,0,82,462,1,0,0,0,84,494,1,0,0,0,86,498,
        1,0,0,0,88,500,1,0,0,0,90,503,1,0,0,0,92,506,1,0,0,0,94,518,1,0,
        0,0,96,520,1,0,0,0,98,522,1,0,0,0,100,530,1,0,0,0,102,532,1,0,0,
        0,104,536,1,0,0,0,106,545,1,0,0,0,108,549,1,0,0,0,110,551,1,0,0,
        0,112,558,1,0,0,0,114,565,1,0,0,0,116,567,1,0,0,0,118,573,1,0,0,
        0,120,575,1,0,0,0,122,584,1,0,0,0,124,586,1,0,0,0,126,127,3,2,1,
        0,127,128,5,0,0,1,128,1,1,0,0,0,129,130,3,4,2,0,130,131,3,2,1,0,
        131,134,1,0,0,0,132,134,3,4,2,0,133,129,1,0,0,0,133,132,1,0,0,0,
        134,3,1,0,0,0,135,141,3,6,3,0,136,141,3,32,16,0,137,141,3,42,21,
        0,138,141,3,56,28,0,139,141,3,64,32,0,140,135,1,0,0,0,140,136,1,
        0,0,0,140,137,1,0,0,0,140,138,1,0,0,0,140,139,1,0,0,0,141,5,1,0,
        0,0,142,153,3,30,15,0,143,153,3,32,16,0,144,153,3,36,18,0,145,153,
        3,34,17,0,146,153,3,72,36,0,147,153,3,84,42,0,148,153,3,90,45,0,
        149,153,3,88,44,0,150,153,3,92,46,0,151,153,3,94,47,0,152,142,1,
        0,0,0,152,143,1,0,0,0,152,144,1,0,0,0,152,145,1,0,0,0,152,146,1,
        0,0,0,152,147,1,0,0,0,152,148,1,0,0,0,152,149,1,0,0,0,152,150,1,
        0,0,0,152,151,1,0,0,0,153,7,1,0,0,0,154,155,6,4,-1,0,155,156,3,10,
        5,0,156,162,1,0,0,0,157,158,10,2,0,0,158,159,5,27,0,0,159,161,3,
        10,5,0,160,157,1,0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,1,
        0,0,0,163,9,1,0,0,0,164,162,1,0,0,0,165,166,6,5,-1,0,166,167,3,12,
        6,0,167,173,1,0,0,0,168,169,10,2,0,0,169,170,5,26,0,0,170,172,3,
        12,6,0,171,168,1,0,0,0,172,175,1,0,0,0,173,171,1,0,0,0,173,174,1,
        0,0,0,174,11,1,0,0,0,175,173,1,0,0,0,176,177,6,6,-1,0,177,178,3,
        14,7,0,178,184,1,0,0,0,179,180,10,2,0,0,180,181,5,25,0,0,181,183,
        3,14,7,0,182,179,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,184,185,
        1,0,0,0,185,13,1,0,0,0,186,184,1,0,0,0,187,188,6,7,-1,0,188,189,
        3,16,8,0,189,198,1,0,0,0,190,191,10,3,0,0,191,192,5,33,0,0,192,197,
        3,16,8,0,193,194,10,2,0,0,194,195,5,34,0,0,195,197,3,16,8,0,196,
        190,1,0,0,0,196,193,1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,
        199,1,0,0,0,199,15,1,0,0,0,200,198,1,0,0,0,201,202,6,8,-1,0,202,
        203,3,18,9,0,203,215,1,0,0,0,204,205,10,4,0,0,205,206,5,35,0,0,206,
        214,3,18,9,0,207,208,10,3,0,0,208,209,5,36,0,0,209,214,3,18,9,0,
        210,211,10,2,0,0,211,212,5,37,0,0,212,214,3,18,9,0,213,204,1,0,0,
        0,213,207,1,0,0,0,213,210,1,0,0,0,214,217,1,0,0,0,215,213,1,0,0,
        0,215,216,1,0,0,0,216,17,1,0,0,0,217,215,1,0,0,0,218,219,5,28,0,
        0,219,224,3,20,10,0,220,221,5,34,0,0,221,224,3,20,10,0,222,224,3,
        20,10,0,223,218,1,0,0,0,223,220,1,0,0,0,223,222,1,0,0,0,224,19,1,
        0,0,0,225,226,6,10,-1,0,226,227,3,22,11,0,227,243,1,0,0,0,228,229,
        10,4,0,0,229,230,5,31,0,0,230,242,5,50,0,0,231,232,10,3,0,0,232,
        233,5,40,0,0,233,234,3,8,4,0,234,235,5,41,0,0,235,242,1,0,0,0,236,
        237,10,2,0,0,237,238,5,38,0,0,238,239,3,24,12,0,239,240,5,39,0,0,
        240,242,1,0,0,0,241,228,1,0,0,0,241,231,1,0,0,0,241,236,1,0,0,0,
        242,245,1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,21,1,0,0,0,245,
        243,1,0,0,0,246,247,5,38,0,0,247,248,3,8,4,0,248,249,5,39,0,0,249,
        253,1,0,0,0,250,253,5,50,0,0,251,253,3,122,61,0,252,246,1,0,0,0,
        252,250,1,0,0,0,252,251,1,0,0,0,253,23,1,0,0,0,254,257,3,26,13,0,
        255,257,1,0,0,0,256,254,1,0,0,0,256,255,1,0,0,0,257,25,1,0,0,0,258,
        259,3,8,4,0,259,260,5,44,0,0,260,261,3,26,13,0,261,264,1,0,0,0,262,
        264,3,8,4,0,263,258,1,0,0,0,263,262,1,0,0,0,264,27,1,0,0,0,265,266,
        6,14,-1,0,266,267,5,50,0,0,267,278,1,0,0,0,268,269,10,3,0,0,269,
        270,5,31,0,0,270,277,5,50,0,0,271,272,10,2,0,0,272,273,5,40,0,0,
        273,274,3,8,4,0,274,275,5,41,0,0,275,277,1,0,0,0,276,268,1,0,0,0,
        276,271,1,0,0,0,277,280,1,0,0,0,278,276,1,0,0,0,278,279,1,0,0,0,
        279,29,1,0,0,0,280,278,1,0,0,0,281,282,3,28,14,0,282,283,3,96,48,
        0,283,284,3,8,4,0,284,285,3,124,62,0,285,31,1,0,0,0,286,287,5,18,
        0,0,287,288,5,50,0,0,288,289,3,118,59,0,289,290,3,124,62,0,290,305,
        1,0,0,0,291,292,5,18,0,0,292,293,5,50,0,0,293,294,5,32,0,0,294,295,
        3,8,4,0,295,296,3,124,62,0,296,305,1,0,0,0,297,298,5,18,0,0,298,
        299,5,50,0,0,299,300,3,118,59,0,300,301,5,32,0,0,301,302,3,8,4,0,
        302,303,3,124,62,0,303,305,1,0,0,0,304,286,1,0,0,0,304,291,1,0,0,
        0,304,297,1,0,0,0,305,33,1,0,0,0,306,307,5,17,0,0,307,308,5,50,0,
        0,308,309,5,32,0,0,309,310,3,8,4,0,310,311,3,124,62,0,311,35,1,0,
        0,0,312,313,5,18,0,0,313,314,5,50,0,0,314,315,3,38,19,0,315,316,
        3,118,59,0,316,317,3,124,62,0,317,327,1,0,0,0,318,319,5,18,0,0,319,
        320,5,50,0,0,320,321,3,38,19,0,321,322,3,118,59,0,322,323,5,32,0,
        0,323,324,3,102,51,0,324,325,3,124,62,0,325,327,1,0,0,0,326,312,
        1,0,0,0,326,318,1,0,0,0,327,37,1,0,0,0,328,329,3,40,20,0,329,330,
        3,38,19,0,330,333,1,0,0,0,331,333,3,40,20,0,332,328,1,0,0,0,332,
        331,1,0,0,0,333,39,1,0,0,0,334,335,5,40,0,0,335,336,3,8,4,0,336,
        337,5,41,0,0,337,41,1,0,0,0,338,340,5,9,0,0,339,341,3,52,26,0,340,
        339,1,0,0,0,340,341,1,0,0,0,341,342,1,0,0,0,342,343,5,50,0,0,343,
        345,3,44,22,0,344,346,3,118,59,0,345,344,1,0,0,0,345,346,1,0,0,0,
        346,347,1,0,0,0,347,348,3,98,49,0,348,349,3,124,62,0,349,43,1,0,
        0,0,350,351,5,38,0,0,351,352,3,46,23,0,352,353,5,39,0,0,353,45,1,
        0,0,0,354,357,3,48,24,0,355,357,1,0,0,0,356,354,1,0,0,0,356,355,
        1,0,0,0,357,47,1,0,0,0,358,359,3,50,25,0,359,360,5,44,0,0,360,361,
        3,48,24,0,361,364,1,0,0,0,362,364,3,50,25,0,363,358,1,0,0,0,363,
        362,1,0,0,0,364,49,1,0,0,0,365,366,3,54,27,0,366,367,3,118,59,0,
        367,51,1,0,0,0,368,369,5,38,0,0,369,370,5,50,0,0,370,371,5,50,0,
        0,371,372,5,39,0,0,372,53,1,0,0,0,373,374,5,50,0,0,374,375,5,44,
        0,0,375,378,3,54,27,0,376,378,5,50,0,0,377,373,1,0,0,0,377,376,1,
        0,0,0,378,55,1,0,0,0,379,380,5,10,0,0,380,381,5,50,0,0,381,382,5,
        11,0,0,382,383,3,58,29,0,383,384,3,124,62,0,384,57,1,0,0,0,385,386,
        5,42,0,0,386,387,3,60,30,0,387,388,5,43,0,0,388,59,1,0,0,0,389,390,
        3,62,31,0,390,391,3,60,30,0,391,394,1,0,0,0,392,394,1,0,0,0,393,
        389,1,0,0,0,393,392,1,0,0,0,394,61,1,0,0,0,395,396,5,50,0,0,396,
        398,3,118,59,0,397,399,3,38,19,0,398,397,1,0,0,0,398,399,1,0,0,0,
        399,400,1,0,0,0,400,401,3,124,62,0,401,409,1,0,0,0,402,403,5,50,
        0,0,403,404,5,50,0,0,404,409,3,124,62,0,405,406,5,50,0,0,406,407,
        5,12,0,0,407,409,3,124,62,0,408,395,1,0,0,0,408,402,1,0,0,0,408,
        405,1,0,0,0,409,63,1,0,0,0,410,411,5,10,0,0,411,412,5,50,0,0,412,
        413,5,12,0,0,413,414,3,66,33,0,414,415,3,124,62,0,415,65,1,0,0,0,
        416,417,5,42,0,0,417,418,3,68,34,0,418,419,5,43,0,0,419,67,1,0,0,
        0,420,421,3,70,35,0,421,422,3,68,34,0,422,425,1,0,0,0,423,425,1,
        0,0,0,424,420,1,0,0,0,424,423,1,0,0,0,425,69,1,0,0,0,426,427,5,50,
        0,0,427,429,3,44,22,0,428,430,3,118,59,0,429,428,1,0,0,0,429,430,
        1,0,0,0,430,431,1,0,0,0,431,432,3,124,62,0,432,71,1,0,0,0,433,434,
        3,74,37,0,434,435,3,78,39,0,435,436,3,80,40,0,436,437,3,124,62,0,
        437,73,1,0,0,0,438,439,5,5,0,0,439,440,3,82,41,0,440,442,3,98,49,
        0,441,443,3,124,62,0,442,441,1,0,0,0,442,443,1,0,0,0,443,75,1,0,
        0,0,444,445,5,6,0,0,445,446,5,5,0,0,446,447,3,82,41,0,447,449,3,
        98,49,0,448,450,3,124,62,0,449,448,1,0,0,0,449,450,1,0,0,0,450,77,
        1,0,0,0,451,452,3,76,38,0,452,453,3,78,39,0,453,456,1,0,0,0,454,
        456,1,0,0,0,455,451,1,0,0,0,455,454,1,0,0,0,456,79,1,0,0,0,457,458,
        5,6,0,0,458,461,3,98,49,0,459,461,1,0,0,0,460,457,1,0,0,0,460,459,
        1,0,0,0,461,81,1,0,0,0,462,463,5,38,0,0,463,464,3,8,4,0,464,465,
        5,39,0,0,465,83,1,0,0,0,466,467,5,7,0,0,467,468,3,8,4,0,468,469,
        3,98,49,0,469,470,3,124,62,0,470,495,1,0,0,0,471,472,5,7,0,0,472,
        473,5,50,0,0,473,474,5,30,0,0,474,475,3,8,4,0,475,476,5,45,0,0,476,
        477,3,8,4,0,477,478,5,45,0,0,478,479,5,50,0,0,479,480,5,29,0,0,480,
        481,3,8,4,0,481,482,3,98,49,0,482,483,3,124,62,0,483,495,1,0,0,0,
        484,485,5,7,0,0,485,486,5,50,0,0,486,487,5,44,0,0,487,488,5,50,0,
        0,488,489,5,30,0,0,489,490,5,21,0,0,490,491,3,86,43,0,491,492,3,
        98,49,0,492,493,3,124,62,0,493,495,1,0,0,0,494,466,1,0,0,0,494,471,
        1,0,0,0,494,484,1,0,0,0,495,85,1,0,0,0,496,499,5,50,0,0,497,499,
        3,102,51,0,498,496,1,0,0,0,498,497,1,0,0,0,499,87,1,0,0,0,500,501,
        5,20,0,0,501,502,3,124,62,0,502,89,1,0,0,0,503,504,5,19,0,0,504,
        505,3,124,62,0,505,91,1,0,0,0,506,507,3,20,10,0,507,508,5,38,0,0,
        508,509,3,24,12,0,509,510,5,39,0,0,510,511,3,124,62,0,511,93,1,0,
        0,0,512,513,5,8,0,0,513,519,3,124,62,0,514,515,5,8,0,0,515,516,3,
        8,4,0,516,517,3,124,62,0,517,519,1,0,0,0,518,512,1,0,0,0,518,514,
        1,0,0,0,519,95,1,0,0,0,520,521,7,0,0,0,521,97,1,0,0,0,522,523,5,
        42,0,0,523,524,3,100,50,0,524,525,5,43,0,0,525,99,1,0,0,0,526,527,
        3,6,3,0,527,528,3,100,50,0,528,531,1,0,0,0,529,531,1,0,0,0,530,526,
        1,0,0,0,530,529,1,0,0,0,531,101,1,0,0,0,532,533,3,38,19,0,533,534,
        3,118,59,0,534,535,3,104,52,0,535,103,1,0,0,0,536,537,5,42,0,0,537,
        538,3,106,53,0,538,539,5,43,0,0,539,105,1,0,0,0,540,541,3,108,54,
        0,541,542,5,44,0,0,542,543,3,106,53,0,543,546,1,0,0,0,544,546,3,
        108,54,0,545,540,1,0,0,0,545,544,1,0,0,0,546,107,1,0,0,0,547,550,
        3,8,4,0,548,550,3,104,52,0,549,547,1,0,0,0,549,548,1,0,0,0,550,109,
        1,0,0,0,551,552,5,50,0,0,552,553,5,42,0,0,553,554,3,112,56,0,554,
        555,5,43,0,0,555,111,1,0,0,0,556,559,3,114,57,0,557,559,1,0,0,0,
        558,556,1,0,0,0,558,557,1,0,0,0,559,113,1,0,0,0,560,561,3,116,58,
        0,561,562,5,44,0,0,562,563,3,114,57,0,563,566,1,0,0,0,564,566,3,
        116,58,0,565,560,1,0,0,0,565,564,1,0,0,0,566,115,1,0,0,0,567,568,
        5,50,0,0,568,569,5,46,0,0,569,570,3,122,61,0,570,117,1,0,0,0,571,
        574,3,120,60,0,572,574,5,50,0,0,573,571,1,0,0,0,573,572,1,0,0,0,
        574,119,1,0,0,0,575,576,7,1,0,0,576,121,1,0,0,0,577,585,5,48,0,0,
        578,585,5,47,0,0,579,585,5,49,0,0,580,585,5,23,0,0,581,585,5,24,
        0,0,582,585,3,110,55,0,583,585,3,102,51,0,584,577,1,0,0,0,584,578,
        1,0,0,0,584,579,1,0,0,0,584,580,1,0,0,0,584,581,1,0,0,0,584,582,
        1,0,0,0,584,583,1,0,0,0,585,123,1,0,0,0,586,587,7,2,0,0,587,125,
        1,0,0,0,45,133,140,152,162,173,184,196,198,213,215,223,241,243,252,
        256,263,276,278,304,326,332,340,345,356,363,377,393,398,408,424,
        429,442,449,455,460,494,498,518,530,545,549,558,565,573,584
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
                     "'false'", "<INVALID>", "'&&'", "'||'", "'!'", "<INVALID>", 
                     "':='", "'.'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "','", "';'", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "SINGLE_LINE_CMT", "MULTI_LINE_CMT", 
                      "NL", "WS", "IF_", "ELSE_", "FOR_", "RETURN_", "FUNC_", 
                      "TYPE_", "STRUCT_", "INTERFACE_", "STRING_", "INT_", 
                      "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
                      "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "COMPARISON_OP", 
                      "AND", "OR", "NOT", "UPT_ASSIGN", "ASSIGN", "DOT", 
                      "EQUAL", "ADD", "SUB", "MUL", "DIV", "MOD", "LP", 
                      "RP", "LSB", "RSB", "LCB", "RCB", "COMMA", "SEMICOLON", 
                      "COLON", "FLOAT", "INTEGER", "STRING", "ID", "ERROR_CHAR", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decllst = 1
    RULE_decl = 2
    RULE_statement = 3
    RULE_expr = 4
    RULE_expr1 = 5
    RULE_expr2 = 6
    RULE_expr3 = 7
    RULE_expr4 = 8
    RULE_expr5 = 9
    RULE_expr6 = 10
    RULE_expr7 = 11
    RULE_exprlst = 12
    RULE_exprlstprime = 13
    RULE_lhs = 14
    RULE_assigning = 15
    RULE_vardecl = 16
    RULE_constdecl = 17
    RULE_arraydecl = 18
    RULE_arridxlst = 19
    RULE_arridx = 20
    RULE_funcdecl = 21
    RULE_funcparam = 22
    RULE_paramlst = 23
    RULE_paramlstprime = 24
    RULE_param = 25
    RULE_receiver = 26
    RULE_idlst = 27
    RULE_structdecl = 28
    RULE_structfield = 29
    RULE_fielddecllst = 30
    RULE_fielddecl = 31
    RULE_interfdecl = 32
    RULE_interfmeth = 33
    RULE_interfmethlst = 34
    RULE_interfmethmem = 35
    RULE_ifelse_stat = 36
    RULE_if_ = 37
    RULE_elseif_ = 38
    RULE_elseif_lst = 39
    RULE_else_ = 40
    RULE_condition = 41
    RULE_forloop_stat = 42
    RULE_id__arr = 43
    RULE_break_stat = 44
    RULE_continue_stat = 45
    RULE_funccall_stat = 46
    RULE_return_stat = 47
    RULE_assign = 48
    RULE_blockcode = 49
    RULE_stmtlst = 50
    RULE_arr_literal = 51
    RULE_arrelemlst = 52
    RULE_arreleml = 53
    RULE_arrelem = 54
    RULE_struct_literal = 55
    RULE_structparamlst = 56
    RULE_structparamlstprime = 57
    RULE_structparam = 58
    RULE_data_type = 59
    RULE_primitive_datatype = 60
    RULE_literal = 61
    RULE_end_stm = 62

    ruleNames =  [ "program", "decllst", "decl", "statement", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "exprlst", "exprlstprime", "lhs", "assigning", "vardecl", 
                   "constdecl", "arraydecl", "arridxlst", "arridx", "funcdecl", 
                   "funcparam", "paramlst", "paramlstprime", "param", "receiver", 
                   "idlst", "structdecl", "structfield", "fielddecllst", 
                   "fielddecl", "interfdecl", "interfmeth", "interfmethlst", 
                   "interfmethmem", "ifelse_stat", "if_", "elseif_", "elseif_lst", 
                   "else_", "condition", "forloop_stat", "id__arr", "break_stat", 
                   "continue_stat", "funccall_stat", "return_stat", "assign", 
                   "blockcode", "stmtlst", "arr_literal", "arrelemlst", 
                   "arreleml", "arrelem", "struct_literal", "structparamlst", 
                   "structparamlstprime", "structparam", "data_type", "primitive_datatype", 
                   "literal", "end_stm" ]

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
    COMPARISON_OP=25
    AND=26
    OR=27
    NOT=28
    UPT_ASSIGN=29
    ASSIGN=30
    DOT=31
    EQUAL=32
    ADD=33
    SUB=34
    MUL=35
    DIV=36
    MOD=37
    LP=38
    RP=39
    LSB=40
    RSB=41
    LCB=42
    RCB=43
    COMMA=44
    SEMICOLON=45
    COLON=46
    FLOAT=47
    INTEGER=48
    STRING=49
    ID=50
    ERROR_CHAR=51
    ILLEGAL_ESCAPE=52
    UNCLOSE_STRING=53

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

        def decllst(self):
            return self.getTypedRuleContext(MiniGoParser.DecllstContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.decllst()
            self.state = 127
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def decllst(self):
            return self.getTypedRuleContext(MiniGoParser.DecllstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decllst




    def decllst(self):

        localctx = MiniGoParser.DecllstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllst)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.decl()
                self.state = 130
                self.decllst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
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

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def structdecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructdeclContext,0)


        def interfdecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfdeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.vardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self.funcdecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 138
                self.structdecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 139
                self.interfdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assigning(self):
            return self.getTypedRuleContext(MiniGoParser.AssigningContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(MiniGoParser.ArraydeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def ifelse_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Ifelse_statContext,0)


        def forloop_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Forloop_statContext,0)


        def continue_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statContext,0)


        def break_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statContext,0)


        def funccall_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Funccall_statContext,0)


        def return_stat(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.assigning()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.vardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 144
                self.arraydecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 145
                self.constdecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 146
                self.ifelse_stat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 147
                self.forloop_stat()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 148
                self.continue_stat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 149
                self.break_stat()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 150
                self.funccall_stat()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 151
                self.return_stat()
                pass


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
            self.state = 155
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 162
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 157
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 158
                    self.match(MiniGoParser.OR)
                    self.state = 159
                    self.expr1(0) 
                self.state = 164
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
            self.state = 166
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 173
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 168
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 169
                    self.match(MiniGoParser.AND)
                    self.state = 170
                    self.expr2(0) 
                self.state = 175
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


        def COMPARISON_OP(self):
            return self.getToken(MiniGoParser.COMPARISON_OP, 0)

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
            self.state = 177
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 184
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 179
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 180
                    self.match(MiniGoParser.COMPARISON_OP)
                    self.state = 181
                    self.expr3(0) 
                self.state = 186
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
            self.state = 188
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 198
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 196
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 190
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 191
                        self.match(MiniGoParser.ADD)
                        self.state = 192
                        self.expr4(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 193
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 194
                        self.match(MiniGoParser.SUB)
                        self.state = 195
                        self.expr4(0)
                        pass

             
                self.state = 200
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
            self.state = 202
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 213
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 204
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 205
                        self.match(MiniGoParser.MUL)
                        self.state = 206
                        self.expr5()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 207
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 208
                        self.match(MiniGoParser.DIV)
                        self.state = 209
                        self.expr5()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 210
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 211
                        self.match(MiniGoParser.MOD)
                        self.state = 212
                        self.expr5()
                        pass

             
                self.state = 217
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

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr5)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(MiniGoParser.NOT)
                self.state = 219
                self.expr6(0)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.match(MiniGoParser.SUB)
                self.state = 221
                self.expr6(0)
                pass
            elif token in [23, 24, 38, 40, 47, 48, 49, 50]:
                self.enterOuterAlt(localctx, 3)
                self.state = 222
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


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def exprlst(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlstContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

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
            self.state = 226
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 243
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 241
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 228
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 229
                        self.match(MiniGoParser.DOT)
                        self.state = 230
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 231
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 232
                        self.match(MiniGoParser.LSB)
                        self.state = 233
                        self.expr(0)
                        self.state = 234
                        self.match(MiniGoParser.RSB)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 236
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 237
                        self.match(MiniGoParser.LP)
                        self.state = 238
                        self.exprlst()
                        self.state = 239
                        self.match(MiniGoParser.RP)
                        pass

             
                self.state = 245
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr7)
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(MiniGoParser.LP)
                self.state = 247
                self.expr(0)
                self.state = 248
                self.match(MiniGoParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprlstprime(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprlst




    def exprlst(self):

        localctx = MiniGoParser.ExprlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exprlst)
        try:
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 28, 34, 38, 40, 47, 48, 49, 50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.exprlstprime()
                pass
            elif token in [39]:
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


    class ExprlstprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def exprlstprime(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprlstprime




    def exprlstprime(self):

        localctx = MiniGoParser.ExprlstprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exprlstprime)
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.expr(0)
                self.state = 259
                self.match(MiniGoParser.COMMA)
                self.state = 260
                self.exprlstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 276
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 268
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 269
                        self.match(MiniGoParser.DOT)
                        self.state = 270
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 271
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 272
                        self.match(MiniGoParser.LSB)
                        self.state = 273
                        self.expr(0)
                        self.state = 274
                        self.match(MiniGoParser.RSB)
                        pass

             
                self.state = 280
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssigningContext(ParserRuleContext):
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


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assigning




    def assigning(self):

        localctx = MiniGoParser.AssigningContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assigning)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.lhs(0)
            self.state = 282
            self.assign()
            self.state = 283
            self.expr(0)
            self.state = 284
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
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


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_vardecl)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.match(MiniGoParser.VAR_)
                self.state = 287
                self.match(MiniGoParser.ID)
                self.state = 288
                self.data_type()
                self.state = 289
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.match(MiniGoParser.VAR_)
                self.state = 292
                self.match(MiniGoParser.ID)
                self.state = 293
                self.match(MiniGoParser.EQUAL)
                self.state = 294
                self.expr(0)
                self.state = 295
                self.end_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 297
                self.match(MiniGoParser.VAR_)
                self.state = 298
                self.match(MiniGoParser.ID)
                self.state = 299
                self.data_type()
                self.state = 300
                self.match(MiniGoParser.EQUAL)
                self.state = 301
                self.expr(0)
                self.state = 302
                self.end_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
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


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constdecl




    def constdecl(self):

        localctx = MiniGoParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(MiniGoParser.CONST_)
            self.state = 307
            self.match(MiniGoParser.ID)
            self.state = 308
            self.match(MiniGoParser.EQUAL)
            self.state = 309
            self.expr(0)
            self.state = 310
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_(self):
            return self.getToken(MiniGoParser.VAR_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arridxlst(self):
            return self.getTypedRuleContext(MiniGoParser.ArridxlstContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def arr_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arraydecl




    def arraydecl(self):

        localctx = MiniGoParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arraydecl)
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.match(MiniGoParser.VAR_)
                self.state = 313
                self.match(MiniGoParser.ID)
                self.state = 314
                self.arridxlst()
                self.state = 315
                self.data_type()
                self.state = 316
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.match(MiniGoParser.VAR_)
                self.state = 319
                self.match(MiniGoParser.ID)
                self.state = 320
                self.arridxlst()
                self.state = 321
                self.data_type()
                self.state = 322
                self.match(MiniGoParser.EQUAL)
                self.state = 323
                self.arr_literal()
                self.state = 324
                self.end_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArridxlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arridx(self):
            return self.getTypedRuleContext(MiniGoParser.ArridxContext,0)


        def arridxlst(self):
            return self.getTypedRuleContext(MiniGoParser.ArridxlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arridxlst




    def arridxlst(self):

        localctx = MiniGoParser.ArridxlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arridxlst)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.arridx()
                self.state = 329
                self.arridxlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
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
        self.enterRule(localctx, 40, self.RULE_arridx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(MiniGoParser.LSB)
            self.state = 335
            self.expr(0)
            self.state = 336
            self.match(MiniGoParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
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


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(MiniGoParser.FUNC_)
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 339
                self.receiver()


            self.state = 342
            self.match(MiniGoParser.ID)
            self.state = 343
            self.funcparam()
            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1125899906965504) != 0):
                self.state = 344
                self.data_type()


            self.state = 347
            self.blockcode()
            self.state = 348
            self.end_stm()
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

        def paramlst(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlstContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcparam




    def funcparam(self):

        localctx = MiniGoParser.FuncparamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_funcparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(MiniGoParser.LP)
            self.state = 351
            self.paramlst()
            self.state = 352
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramlstprime(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramlst




    def paramlst(self):

        localctx = MiniGoParser.ParamlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_paramlst)
        try:
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.paramlstprime()
                pass
            elif token in [39]:
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


    class ParamlstprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def paramlstprime(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramlstprime




    def paramlstprime(self):

        localctx = MiniGoParser.ParamlstprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_paramlstprime)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.param()
                self.state = 359
                self.match(MiniGoParser.COMMA)
                self.state = 360
                self.paramlstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
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

        def idlst(self):
            return self.getTypedRuleContext(MiniGoParser.IdlstContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.idlst()
            self.state = 366
            self.data_type()
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
        self.enterRule(localctx, 52, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(MiniGoParser.LP)
            self.state = 369
            self.match(MiniGoParser.ID)
            self.state = 370
            self.match(MiniGoParser.ID)
            self.state = 371
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def idlst(self):
            return self.getTypedRuleContext(MiniGoParser.IdlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_idlst




    def idlst(self):

        localctx = MiniGoParser.IdlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_idlst)
        try:
            self.state = 377
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.match(MiniGoParser.ID)
                self.state = 374
                self.match(MiniGoParser.COMMA)
                self.state = 375
                self.idlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructdeclContext(ParserRuleContext):
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


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structdecl




    def structdecl(self):

        localctx = MiniGoParser.StructdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_structdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(MiniGoParser.TYPE_)
            self.state = 380
            self.match(MiniGoParser.ID)
            self.state = 381
            self.match(MiniGoParser.STRUCT_)
            self.state = 382
            self.structfield()
            self.state = 383
            self.end_stm()
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

        def fielddecllst(self):
            return self.getTypedRuleContext(MiniGoParser.FielddecllstContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structfield




    def structfield(self):

        localctx = MiniGoParser.StructfieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_structfield)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(MiniGoParser.LCB)
            self.state = 386
            self.fielddecllst()
            self.state = 387
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FielddecllstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fielddecl(self):
            return self.getTypedRuleContext(MiniGoParser.FielddeclContext,0)


        def fielddecllst(self):
            return self.getTypedRuleContext(MiniGoParser.FielddecllstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fielddecllst




    def fielddecllst(self):

        localctx = MiniGoParser.FielddecllstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_fielddecllst)
        try:
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.fielddecl()
                self.state = 390
                self.fielddecllst()
                pass
            elif token in [43]:
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


    class FielddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def arridxlst(self):
            return self.getTypedRuleContext(MiniGoParser.ArridxlstContext,0)


        def INTERFACE_(self):
            return self.getToken(MiniGoParser.INTERFACE_, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_fielddecl




    def fielddecl(self):

        localctx = MiniGoParser.FielddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_fielddecl)
        self._la = 0 # Token type
        try:
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.match(MiniGoParser.ID)
                self.state = 396
                self.data_type()
                self.state = 398
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==40:
                    self.state = 397
                    self.arridxlst()


                self.state = 400
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self.match(MiniGoParser.ID)
                self.state = 403
                self.match(MiniGoParser.ID)
                self.state = 404
                self.end_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 405
                self.match(MiniGoParser.ID)
                self.state = 406
                self.match(MiniGoParser.INTERFACE_)
                self.state = 407
                self.end_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfdeclContext(ParserRuleContext):
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

        def interfmeth(self):
            return self.getTypedRuleContext(MiniGoParser.InterfmethContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfdecl




    def interfdecl(self):

        localctx = MiniGoParser.InterfdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_interfdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(MiniGoParser.TYPE_)
            self.state = 411
            self.match(MiniGoParser.ID)
            self.state = 412
            self.match(MiniGoParser.INTERFACE_)
            self.state = 413
            self.interfmeth()
            self.state = 414
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfmethContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def interfmethlst(self):
            return self.getTypedRuleContext(MiniGoParser.InterfmethlstContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfmeth




    def interfmeth(self):

        localctx = MiniGoParser.InterfmethContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_interfmeth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(MiniGoParser.LCB)
            self.state = 417
            self.interfmethlst()
            self.state = 418
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfmethlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interfmethmem(self):
            return self.getTypedRuleContext(MiniGoParser.InterfmethmemContext,0)


        def interfmethlst(self):
            return self.getTypedRuleContext(MiniGoParser.InterfmethlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfmethlst




    def interfmethlst(self):

        localctx = MiniGoParser.InterfmethlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_interfmethlst)
        try:
            self.state = 424
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.interfmethmem()
                self.state = 421
                self.interfmethlst()
                pass
            elif token in [43]:
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


    class InterfmethmemContext(ParserRuleContext):
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
            return MiniGoParser.RULE_interfmethmem




    def interfmethmem(self):

        localctx = MiniGoParser.InterfmethmemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_interfmethmem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(MiniGoParser.ID)
            self.state = 427
            self.funcparam()
            self.state = 429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1125899906965504) != 0):
                self.state = 428
                self.data_type()


            self.state = 431
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ifelse_statContext(ParserRuleContext):
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


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifelse_stat




    def ifelse_stat(self):

        localctx = MiniGoParser.Ifelse_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_ifelse_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.if_()
            self.state = 434
            self.elseif_lst()
            self.state = 435
            self.else_()
            self.state = 436
            self.end_stm()
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
        self.enterRule(localctx, 74, self.RULE_if_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(MiniGoParser.IF_)
            self.state = 439
            self.condition()
            self.state = 440
            self.blockcode()
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 441
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
        self.enterRule(localctx, 76, self.RULE_elseif_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(MiniGoParser.ELSE_)
            self.state = 445
            self.match(MiniGoParser.IF_)
            self.state = 446
            self.condition()
            self.state = 447
            self.blockcode()
            self.state = 449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 448
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
        self.enterRule(localctx, 78, self.RULE_elseif_lst)
        try:
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 451
                self.elseif_()
                self.state = 452
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
        self.enterRule(localctx, 80, self.RULE_else_)
        try:
            self.state = 460
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.match(MiniGoParser.ELSE_)
                self.state = 458
                self.blockcode()
                pass
            elif token in [-1, 45]:
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
        self.enterRule(localctx, 82, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(MiniGoParser.LP)
            self.state = 463
            self.expr(0)
            self.state = 464
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forloop_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_(self):
            return self.getToken(MiniGoParser.FOR_, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def UPT_ASSIGN(self):
            return self.getToken(MiniGoParser.UPT_ASSIGN, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def RANGE_(self):
            return self.getToken(MiniGoParser.RANGE_, 0)

        def id__arr(self):
            return self.getTypedRuleContext(MiniGoParser.Id__arrContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forloop_stat




    def forloop_stat(self):

        localctx = MiniGoParser.Forloop_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_forloop_stat)
        try:
            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.match(MiniGoParser.FOR_)
                self.state = 467
                self.expr(0)
                self.state = 468
                self.blockcode()
                self.state = 469
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 471
                self.match(MiniGoParser.FOR_)
                self.state = 472
                self.match(MiniGoParser.ID)
                self.state = 473
                self.match(MiniGoParser.ASSIGN)
                self.state = 474
                self.expr(0)
                self.state = 475
                self.match(MiniGoParser.SEMICOLON)
                self.state = 476
                self.expr(0)
                self.state = 477
                self.match(MiniGoParser.SEMICOLON)
                self.state = 478
                self.match(MiniGoParser.ID)
                self.state = 479
                self.match(MiniGoParser.UPT_ASSIGN)
                self.state = 480
                self.expr(0)
                self.state = 481
                self.blockcode()
                self.state = 482
                self.end_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 484
                self.match(MiniGoParser.FOR_)
                self.state = 485
                self.match(MiniGoParser.ID)
                self.state = 486
                self.match(MiniGoParser.COMMA)
                self.state = 487
                self.match(MiniGoParser.ID)
                self.state = 488
                self.match(MiniGoParser.ASSIGN)
                self.state = 489
                self.match(MiniGoParser.RANGE_)
                self.state = 490
                self.id__arr()
                self.state = 491
                self.blockcode()
                self.state = 492
                self.end_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id__arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arr_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_id__arr




    def id__arr(self):

        localctx = MiniGoParser.Id__arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_id__arr)
        try:
            self.state = 498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 496
                self.match(MiniGoParser.ID)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 497
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


    class Break_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK_(self):
            return self.getToken(MiniGoParser.BREAK_, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stat




    def break_stat(self):

        localctx = MiniGoParser.Break_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_break_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(MiniGoParser.BREAK_)
            self.state = 501
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE_(self):
            return self.getToken(MiniGoParser.CONTINUE_, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stat




    def continue_stat(self):

        localctx = MiniGoParser.Continue_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_continue_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(MiniGoParser.CONTINUE_)
            self.state = 504
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funccall_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def exprlst(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlstContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funccall_stat




    def funccall_stat(self):

        localctx = MiniGoParser.Funccall_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_funccall_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.expr6(0)
            self.state = 507
            self.match(MiniGoParser.LP)
            self.state = 508
            self.exprlst()
            self.state = 509
            self.match(MiniGoParser.RP)
            self.state = 510
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_(self):
            return self.getToken(MiniGoParser.RETURN_, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stat




    def return_stat(self):

        localctx = MiniGoParser.Return_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_return_stat)
        try:
            self.state = 518
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 512
                self.match(MiniGoParser.RETURN_)
                self.state = 513
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 514
                self.match(MiniGoParser.RETURN_)
                self.state = 515
                self.expr(0)
                self.state = 516
                self.end_stm()
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

        def UPT_ASSIGN(self):
            return self.getToken(MiniGoParser.UPT_ASSIGN, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign




    def assign(self):

        localctx = MiniGoParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            _la = self._input.LA(1)
            if not(_la==29 or _la==30):
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

        def stmtlst(self):
            return self.getTypedRuleContext(MiniGoParser.StmtlstContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_blockcode




    def blockcode(self):

        localctx = MiniGoParser.BlockcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_blockcode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            self.match(MiniGoParser.LCB)
            self.state = 523
            self.stmtlst()
            self.state = 524
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def stmtlst(self):
            return self.getTypedRuleContext(MiniGoParser.StmtlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmtlst




    def stmtlst(self):

        localctx = MiniGoParser.StmtlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_stmtlst)
        try:
            self.state = 530
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 7, 8, 17, 18, 19, 20, 23, 24, 38, 40, 47, 48, 49, 50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
                self.statement()
                self.state = 527
                self.stmtlst()
                pass
            elif token in [43]:
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


    class Arr_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arridxlst(self):
            return self.getTypedRuleContext(MiniGoParser.ArridxlstContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def arrelemlst(self):
            return self.getTypedRuleContext(MiniGoParser.ArrelemlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_literal




    def arr_literal(self):

        localctx = MiniGoParser.Arr_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_arr_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.arridxlst()
            self.state = 533
            self.data_type()
            self.state = 534
            self.arrelemlst()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrelemlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def arreleml(self):
            return self.getTypedRuleContext(MiniGoParser.ArrelemlContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrelemlst




    def arrelemlst(self):

        localctx = MiniGoParser.ArrelemlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_arrelemlst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.match(MiniGoParser.LCB)
            self.state = 537
            self.arreleml()
            self.state = 538
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrelemlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrelem(self):
            return self.getTypedRuleContext(MiniGoParser.ArrelemContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def arreleml(self):
            return self.getTypedRuleContext(MiniGoParser.ArrelemlContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arreleml




    def arreleml(self):

        localctx = MiniGoParser.ArrelemlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_arreleml)
        try:
            self.state = 545
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 540
                self.arrelem()
                self.state = 541
                self.match(MiniGoParser.COMMA)
                self.state = 542
                self.arreleml()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 544
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


        def arrelemlst(self):
            return self.getTypedRuleContext(MiniGoParser.ArrelemlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrelem




    def arrelem(self):

        localctx = MiniGoParser.ArrelemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_arrelem)
        try:
            self.state = 549
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 28, 34, 38, 40, 47, 48, 49, 50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 547
                self.expr(0)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 548
                self.arrelemlst()
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

        def structparamlst(self):
            return self.getTypedRuleContext(MiniGoParser.StructparamlstContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self.match(MiniGoParser.ID)
            self.state = 552
            self.match(MiniGoParser.LCB)
            self.state = 553
            self.structparamlst()
            self.state = 554
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructparamlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structparamlstprime(self):
            return self.getTypedRuleContext(MiniGoParser.StructparamlstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structparamlst




    def structparamlst(self):

        localctx = MiniGoParser.StructparamlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_structparamlst)
        try:
            self.state = 558
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 556
                self.structparamlstprime()
                pass
            elif token in [43]:
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


    class StructparamlstprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structparam(self):
            return self.getTypedRuleContext(MiniGoParser.StructparamContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def structparamlstprime(self):
            return self.getTypedRuleContext(MiniGoParser.StructparamlstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structparamlstprime




    def structparamlstprime(self):

        localctx = MiniGoParser.StructparamlstprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_structparamlstprime)
        try:
            self.state = 565
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 560
                self.structparam()
                self.state = 561
                self.match(MiniGoParser.COMMA)
                self.state = 562
                self.structparamlstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 564
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

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structparam




    def structparam(self):

        localctx = MiniGoParser.StructparamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_structparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567
            self.match(MiniGoParser.ID)
            self.state = 568
            self.match(MiniGoParser.COLON)
            self.state = 569
            self.literal()
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

        def primitive_datatype(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_datatypeContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_data_type




    def data_type(self):

        localctx = MiniGoParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_data_type)
        try:
            self.state = 573
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 571
                self.primitive_datatype()
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 572
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
        self.enterRule(localctx, 120, self.RULE_primitive_datatype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
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

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def arr_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_literal)
        try:
            self.state = 584
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 577
                self.match(MiniGoParser.INTEGER)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 578
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 3)
                self.state = 579
                self.match(MiniGoParser.STRING)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 580
                self.match(MiniGoParser.TRUE_)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 581
                self.match(MiniGoParser.FALSE_)
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 6)
                self.state = 582
                self.struct_literal()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 7)
                self.state = 583
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
        self.enterRule(localctx, 124, self.RULE_end_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            _la = self._input.LA(1)
            if not(_la==-1 or _la==45):
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
        self._predicates[14] = self.lhs_sempred
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
                return self.precpred(self._ctx, 4)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         




