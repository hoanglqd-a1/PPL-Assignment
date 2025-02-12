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
        4,1,53,607,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,1,0,1,0,1,
        0,1,1,1,1,1,1,1,1,3,1,138,8,1,1,2,1,2,3,2,142,8,2,1,3,1,3,1,3,1,
        3,1,3,1,3,3,3,150,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,159,8,4,1,
        5,1,5,1,5,1,5,1,5,1,5,5,5,167,8,5,10,5,12,5,170,9,5,1,6,1,6,1,6,
        1,6,1,6,1,6,5,6,178,8,6,10,6,12,6,181,9,6,1,7,1,7,1,7,1,7,1,7,1,
        7,5,7,189,8,7,10,7,12,7,192,9,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,5,8,203,8,8,10,8,12,8,206,9,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,5,9,220,8,9,10,9,12,9,223,9,9,1,10,1,10,1,10,1,
        10,1,10,3,10,230,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,248,8,11,10,11,12,11,
        251,9,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,259,8,12,1,13,1,13,3,
        13,263,8,13,1,14,1,14,1,14,1,14,1,14,3,14,270,8,14,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,283,8,15,10,15,12,15,
        286,9,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,
        311,8,17,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,333,8,19,1,20,
        1,20,1,20,1,20,3,20,339,8,20,1,21,1,21,1,21,1,21,1,22,1,22,3,22,
        347,8,22,1,22,1,22,1,22,3,22,352,8,22,1,22,1,22,1,22,1,23,1,23,1,
        23,1,23,1,24,1,24,3,24,363,8,24,1,25,1,25,1,25,1,25,1,25,3,25,370,
        8,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,
        3,28,384,8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,
        1,31,1,31,1,31,1,31,3,31,400,8,31,1,32,1,32,1,32,3,32,405,8,32,1,
        32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,3,32,415,8,32,1,33,1,33,1,
        33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,3,35,431,
        8,35,1,36,1,36,1,36,3,36,436,8,36,1,36,1,36,1,37,1,37,1,37,1,37,
        1,37,1,38,1,38,1,38,1,38,3,38,449,8,38,1,39,1,39,1,39,1,39,1,39,
        3,39,456,8,39,1,40,1,40,1,40,1,40,3,40,462,8,40,1,41,1,41,1,41,3,
        41,467,8,41,1,42,1,42,1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,43,1,
        43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,
        43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,3,43,501,8,43,1,44,1,
        44,3,44,505,8,44,1,45,1,45,1,45,1,46,1,46,1,46,1,47,1,47,1,47,1,
        47,1,47,1,47,1,48,1,48,1,48,1,48,1,48,1,48,3,48,525,8,48,1,49,1,
        49,1,50,1,50,1,50,1,50,1,51,1,51,1,51,1,51,3,51,537,8,51,1,52,1,
        52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,3,52,549,8,52,1,53,1,
        53,1,53,1,53,1,54,1,54,1,54,1,54,1,55,1,55,1,55,1,55,1,55,3,55,564,
        8,55,1,56,1,56,3,56,568,8,56,1,57,1,57,1,57,1,57,1,57,1,58,1,58,
        3,58,577,8,58,1,59,1,59,1,59,1,59,1,59,3,59,584,8,59,1,60,1,60,1,
        60,1,60,1,61,1,61,3,61,592,8,61,1,62,1,62,1,63,1,63,1,63,1,63,1,
        63,1,63,1,63,3,63,603,8,63,1,64,1,64,1,64,0,7,10,12,14,16,18,22,
        30,65,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,
        86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,
        122,124,126,128,0,3,1,0,29,30,1,0,13,16,1,1,45,45,617,0,130,1,0,
        0,0,2,137,1,0,0,0,4,141,1,0,0,0,6,149,1,0,0,0,8,158,1,0,0,0,10,160,
        1,0,0,0,12,171,1,0,0,0,14,182,1,0,0,0,16,193,1,0,0,0,18,207,1,0,
        0,0,20,229,1,0,0,0,22,231,1,0,0,0,24,258,1,0,0,0,26,262,1,0,0,0,
        28,269,1,0,0,0,30,271,1,0,0,0,32,287,1,0,0,0,34,310,1,0,0,0,36,312,
        1,0,0,0,38,332,1,0,0,0,40,338,1,0,0,0,42,340,1,0,0,0,44,344,1,0,
        0,0,46,356,1,0,0,0,48,362,1,0,0,0,50,369,1,0,0,0,52,371,1,0,0,0,
        54,374,1,0,0,0,56,383,1,0,0,0,58,385,1,0,0,0,60,391,1,0,0,0,62,399,
        1,0,0,0,64,414,1,0,0,0,66,416,1,0,0,0,68,422,1,0,0,0,70,430,1,0,
        0,0,72,432,1,0,0,0,74,439,1,0,0,0,76,444,1,0,0,0,78,450,1,0,0,0,
        80,461,1,0,0,0,82,466,1,0,0,0,84,468,1,0,0,0,86,500,1,0,0,0,88,504,
        1,0,0,0,90,506,1,0,0,0,92,509,1,0,0,0,94,512,1,0,0,0,96,524,1,0,
        0,0,98,526,1,0,0,0,100,528,1,0,0,0,102,536,1,0,0,0,104,548,1,0,0,
        0,106,550,1,0,0,0,108,554,1,0,0,0,110,563,1,0,0,0,112,567,1,0,0,
        0,114,569,1,0,0,0,116,576,1,0,0,0,118,583,1,0,0,0,120,585,1,0,0,
        0,122,591,1,0,0,0,124,593,1,0,0,0,126,602,1,0,0,0,128,604,1,0,0,
        0,130,131,3,2,1,0,131,132,5,0,0,1,132,1,1,0,0,0,133,134,3,4,2,0,
        134,135,3,2,1,0,135,138,1,0,0,0,136,138,3,4,2,0,137,133,1,0,0,0,
        137,136,1,0,0,0,138,3,1,0,0,0,139,142,3,6,3,0,140,142,3,8,4,0,141,
        139,1,0,0,0,141,140,1,0,0,0,142,5,1,0,0,0,143,150,3,34,17,0,144,
        150,3,38,19,0,145,150,3,36,18,0,146,150,3,44,22,0,147,150,3,58,29,
        0,148,150,3,66,33,0,149,143,1,0,0,0,149,144,1,0,0,0,149,145,1,0,
        0,0,149,146,1,0,0,0,149,147,1,0,0,0,149,148,1,0,0,0,150,7,1,0,0,
        0,151,159,3,32,16,0,152,159,3,74,37,0,153,159,3,86,43,0,154,159,
        3,92,46,0,155,159,3,90,45,0,156,159,3,94,47,0,157,159,3,96,48,0,
        158,151,1,0,0,0,158,152,1,0,0,0,158,153,1,0,0,0,158,154,1,0,0,0,
        158,155,1,0,0,0,158,156,1,0,0,0,158,157,1,0,0,0,159,9,1,0,0,0,160,
        161,6,5,-1,0,161,162,3,12,6,0,162,168,1,0,0,0,163,164,10,2,0,0,164,
        165,5,27,0,0,165,167,3,12,6,0,166,163,1,0,0,0,167,170,1,0,0,0,168,
        166,1,0,0,0,168,169,1,0,0,0,169,11,1,0,0,0,170,168,1,0,0,0,171,172,
        6,6,-1,0,172,173,3,14,7,0,173,179,1,0,0,0,174,175,10,2,0,0,175,176,
        5,26,0,0,176,178,3,14,7,0,177,174,1,0,0,0,178,181,1,0,0,0,179,177,
        1,0,0,0,179,180,1,0,0,0,180,13,1,0,0,0,181,179,1,0,0,0,182,183,6,
        7,-1,0,183,184,3,16,8,0,184,190,1,0,0,0,185,186,10,2,0,0,186,187,
        5,25,0,0,187,189,3,16,8,0,188,185,1,0,0,0,189,192,1,0,0,0,190,188,
        1,0,0,0,190,191,1,0,0,0,191,15,1,0,0,0,192,190,1,0,0,0,193,194,6,
        8,-1,0,194,195,3,18,9,0,195,204,1,0,0,0,196,197,10,3,0,0,197,198,
        5,33,0,0,198,203,3,18,9,0,199,200,10,2,0,0,200,201,5,34,0,0,201,
        203,3,18,9,0,202,196,1,0,0,0,202,199,1,0,0,0,203,206,1,0,0,0,204,
        202,1,0,0,0,204,205,1,0,0,0,205,17,1,0,0,0,206,204,1,0,0,0,207,208,
        6,9,-1,0,208,209,3,20,10,0,209,221,1,0,0,0,210,211,10,4,0,0,211,
        212,5,35,0,0,212,220,3,20,10,0,213,214,10,3,0,0,214,215,5,36,0,0,
        215,220,3,20,10,0,216,217,10,2,0,0,217,218,5,37,0,0,218,220,3,20,
        10,0,219,210,1,0,0,0,219,213,1,0,0,0,219,216,1,0,0,0,220,223,1,0,
        0,0,221,219,1,0,0,0,221,222,1,0,0,0,222,19,1,0,0,0,223,221,1,0,0,
        0,224,225,5,28,0,0,225,230,3,22,11,0,226,227,5,34,0,0,227,230,3,
        22,11,0,228,230,3,22,11,0,229,224,1,0,0,0,229,226,1,0,0,0,229,228,
        1,0,0,0,230,21,1,0,0,0,231,232,6,11,-1,0,232,233,3,24,12,0,233,249,
        1,0,0,0,234,235,10,4,0,0,235,236,5,31,0,0,236,248,5,50,0,0,237,238,
        10,3,0,0,238,239,5,40,0,0,239,240,3,10,5,0,240,241,5,41,0,0,241,
        248,1,0,0,0,242,243,10,2,0,0,243,244,5,38,0,0,244,245,3,26,13,0,
        245,246,5,39,0,0,246,248,1,0,0,0,247,234,1,0,0,0,247,237,1,0,0,0,
        247,242,1,0,0,0,248,251,1,0,0,0,249,247,1,0,0,0,249,250,1,0,0,0,
        250,23,1,0,0,0,251,249,1,0,0,0,252,253,5,38,0,0,253,254,3,10,5,0,
        254,255,5,39,0,0,255,259,1,0,0,0,256,259,5,50,0,0,257,259,3,126,
        63,0,258,252,1,0,0,0,258,256,1,0,0,0,258,257,1,0,0,0,259,25,1,0,
        0,0,260,263,3,28,14,0,261,263,1,0,0,0,262,260,1,0,0,0,262,261,1,
        0,0,0,263,27,1,0,0,0,264,265,3,10,5,0,265,266,5,44,0,0,266,267,3,
        28,14,0,267,270,1,0,0,0,268,270,3,10,5,0,269,264,1,0,0,0,269,268,
        1,0,0,0,270,29,1,0,0,0,271,272,6,15,-1,0,272,273,5,50,0,0,273,284,
        1,0,0,0,274,275,10,3,0,0,275,276,5,31,0,0,276,283,5,50,0,0,277,278,
        10,2,0,0,278,279,5,40,0,0,279,280,3,10,5,0,280,281,5,41,0,0,281,
        283,1,0,0,0,282,274,1,0,0,0,282,277,1,0,0,0,283,286,1,0,0,0,284,
        282,1,0,0,0,284,285,1,0,0,0,285,31,1,0,0,0,286,284,1,0,0,0,287,288,
        3,30,15,0,288,289,3,98,49,0,289,290,3,10,5,0,290,291,3,128,64,0,
        291,33,1,0,0,0,292,293,5,18,0,0,293,294,5,50,0,0,294,295,3,122,61,
        0,295,296,3,128,64,0,296,311,1,0,0,0,297,298,5,18,0,0,298,299,5,
        50,0,0,299,300,5,32,0,0,300,301,3,10,5,0,301,302,3,128,64,0,302,
        311,1,0,0,0,303,304,5,18,0,0,304,305,5,50,0,0,305,306,3,122,61,0,
        306,307,5,32,0,0,307,308,3,10,5,0,308,309,3,128,64,0,309,311,1,0,
        0,0,310,292,1,0,0,0,310,297,1,0,0,0,310,303,1,0,0,0,311,35,1,0,0,
        0,312,313,5,17,0,0,313,314,5,50,0,0,314,315,5,32,0,0,315,316,3,10,
        5,0,316,317,3,128,64,0,317,37,1,0,0,0,318,319,5,18,0,0,319,320,5,
        50,0,0,320,321,3,40,20,0,321,322,3,122,61,0,322,323,3,128,64,0,323,
        333,1,0,0,0,324,325,5,18,0,0,325,326,5,50,0,0,326,327,3,40,20,0,
        327,328,3,122,61,0,328,329,5,32,0,0,329,330,3,106,53,0,330,331,3,
        128,64,0,331,333,1,0,0,0,332,318,1,0,0,0,332,324,1,0,0,0,333,39,
        1,0,0,0,334,335,3,42,21,0,335,336,3,40,20,0,336,339,1,0,0,0,337,
        339,3,42,21,0,338,334,1,0,0,0,338,337,1,0,0,0,339,41,1,0,0,0,340,
        341,5,40,0,0,341,342,3,10,5,0,342,343,5,41,0,0,343,43,1,0,0,0,344,
        346,5,9,0,0,345,347,3,54,27,0,346,345,1,0,0,0,346,347,1,0,0,0,347,
        348,1,0,0,0,348,349,5,50,0,0,349,351,3,46,23,0,350,352,3,122,61,
        0,351,350,1,0,0,0,351,352,1,0,0,0,352,353,1,0,0,0,353,354,3,100,
        50,0,354,355,3,128,64,0,355,45,1,0,0,0,356,357,5,38,0,0,357,358,
        3,48,24,0,358,359,5,39,0,0,359,47,1,0,0,0,360,363,3,50,25,0,361,
        363,1,0,0,0,362,360,1,0,0,0,362,361,1,0,0,0,363,49,1,0,0,0,364,365,
        3,52,26,0,365,366,5,44,0,0,366,367,3,50,25,0,367,370,1,0,0,0,368,
        370,3,52,26,0,369,364,1,0,0,0,369,368,1,0,0,0,370,51,1,0,0,0,371,
        372,3,56,28,0,372,373,3,122,61,0,373,53,1,0,0,0,374,375,5,38,0,0,
        375,376,5,50,0,0,376,377,5,50,0,0,377,378,5,39,0,0,378,55,1,0,0,
        0,379,380,5,50,0,0,380,381,5,44,0,0,381,384,3,56,28,0,382,384,5,
        50,0,0,383,379,1,0,0,0,383,382,1,0,0,0,384,57,1,0,0,0,385,386,5,
        10,0,0,386,387,5,50,0,0,387,388,5,11,0,0,388,389,3,60,30,0,389,390,
        3,128,64,0,390,59,1,0,0,0,391,392,5,42,0,0,392,393,3,62,31,0,393,
        394,5,43,0,0,394,61,1,0,0,0,395,396,3,64,32,0,396,397,3,62,31,0,
        397,400,1,0,0,0,398,400,1,0,0,0,399,395,1,0,0,0,399,398,1,0,0,0,
        400,63,1,0,0,0,401,402,5,50,0,0,402,404,3,122,61,0,403,405,3,40,
        20,0,404,403,1,0,0,0,404,405,1,0,0,0,405,406,1,0,0,0,406,407,3,128,
        64,0,407,415,1,0,0,0,408,409,5,50,0,0,409,410,5,50,0,0,410,415,3,
        128,64,0,411,412,5,50,0,0,412,413,5,12,0,0,413,415,3,128,64,0,414,
        401,1,0,0,0,414,408,1,0,0,0,414,411,1,0,0,0,415,65,1,0,0,0,416,417,
        5,10,0,0,417,418,5,50,0,0,418,419,5,12,0,0,419,420,3,68,34,0,420,
        421,3,128,64,0,421,67,1,0,0,0,422,423,5,42,0,0,423,424,3,70,35,0,
        424,425,5,43,0,0,425,69,1,0,0,0,426,427,3,72,36,0,427,428,3,70,35,
        0,428,431,1,0,0,0,429,431,1,0,0,0,430,426,1,0,0,0,430,429,1,0,0,
        0,431,71,1,0,0,0,432,433,5,50,0,0,433,435,3,46,23,0,434,436,3,122,
        61,0,435,434,1,0,0,0,435,436,1,0,0,0,436,437,1,0,0,0,437,438,3,128,
        64,0,438,73,1,0,0,0,439,440,3,76,38,0,440,441,3,80,40,0,441,442,
        3,82,41,0,442,443,3,128,64,0,443,75,1,0,0,0,444,445,5,5,0,0,445,
        446,3,84,42,0,446,448,3,100,50,0,447,449,3,128,64,0,448,447,1,0,
        0,0,448,449,1,0,0,0,449,77,1,0,0,0,450,451,5,6,0,0,451,452,5,5,0,
        0,452,453,3,84,42,0,453,455,3,100,50,0,454,456,3,128,64,0,455,454,
        1,0,0,0,455,456,1,0,0,0,456,79,1,0,0,0,457,458,3,78,39,0,458,459,
        3,80,40,0,459,462,1,0,0,0,460,462,1,0,0,0,461,457,1,0,0,0,461,460,
        1,0,0,0,462,81,1,0,0,0,463,464,5,6,0,0,464,467,3,100,50,0,465,467,
        1,0,0,0,466,463,1,0,0,0,466,465,1,0,0,0,467,83,1,0,0,0,468,469,5,
        38,0,0,469,470,3,10,5,0,470,471,5,39,0,0,471,85,1,0,0,0,472,473,
        5,7,0,0,473,474,3,10,5,0,474,475,3,100,50,0,475,476,3,128,64,0,476,
        501,1,0,0,0,477,478,5,7,0,0,478,479,5,50,0,0,479,480,5,30,0,0,480,
        481,3,10,5,0,481,482,5,45,0,0,482,483,3,10,5,0,483,484,5,45,0,0,
        484,485,5,50,0,0,485,486,5,29,0,0,486,487,3,10,5,0,487,488,3,100,
        50,0,488,489,3,128,64,0,489,501,1,0,0,0,490,491,5,7,0,0,491,492,
        5,50,0,0,492,493,5,44,0,0,493,494,5,50,0,0,494,495,5,30,0,0,495,
        496,5,21,0,0,496,497,3,88,44,0,497,498,3,100,50,0,498,499,3,128,
        64,0,499,501,1,0,0,0,500,472,1,0,0,0,500,477,1,0,0,0,500,490,1,0,
        0,0,501,87,1,0,0,0,502,505,5,50,0,0,503,505,3,106,53,0,504,502,1,
        0,0,0,504,503,1,0,0,0,505,89,1,0,0,0,506,507,5,20,0,0,507,508,3,
        128,64,0,508,91,1,0,0,0,509,510,5,19,0,0,510,511,3,128,64,0,511,
        93,1,0,0,0,512,513,3,22,11,0,513,514,5,38,0,0,514,515,3,26,13,0,
        515,516,5,39,0,0,516,517,3,128,64,0,517,95,1,0,0,0,518,519,5,8,0,
        0,519,525,3,128,64,0,520,521,5,8,0,0,521,522,3,10,5,0,522,523,3,
        128,64,0,523,525,1,0,0,0,524,518,1,0,0,0,524,520,1,0,0,0,525,97,
        1,0,0,0,526,527,7,0,0,0,527,99,1,0,0,0,528,529,5,42,0,0,529,530,
        3,102,51,0,530,531,5,43,0,0,531,101,1,0,0,0,532,533,3,104,52,0,533,
        534,3,102,51,0,534,537,1,0,0,0,535,537,1,0,0,0,536,532,1,0,0,0,536,
        535,1,0,0,0,537,103,1,0,0,0,538,549,3,32,16,0,539,549,3,34,17,0,
        540,549,3,38,19,0,541,549,3,36,18,0,542,549,3,74,37,0,543,549,3,
        86,43,0,544,549,3,92,46,0,545,549,3,90,45,0,546,549,3,94,47,0,547,
        549,3,96,48,0,548,538,1,0,0,0,548,539,1,0,0,0,548,540,1,0,0,0,548,
        541,1,0,0,0,548,542,1,0,0,0,548,543,1,0,0,0,548,544,1,0,0,0,548,
        545,1,0,0,0,548,546,1,0,0,0,548,547,1,0,0,0,549,105,1,0,0,0,550,
        551,3,40,20,0,551,552,3,122,61,0,552,553,3,108,54,0,553,107,1,0,
        0,0,554,555,5,42,0,0,555,556,3,110,55,0,556,557,5,43,0,0,557,109,
        1,0,0,0,558,559,3,112,56,0,559,560,5,44,0,0,560,561,3,110,55,0,561,
        564,1,0,0,0,562,564,3,112,56,0,563,558,1,0,0,0,563,562,1,0,0,0,564,
        111,1,0,0,0,565,568,3,10,5,0,566,568,3,108,54,0,567,565,1,0,0,0,
        567,566,1,0,0,0,568,113,1,0,0,0,569,570,5,50,0,0,570,571,5,42,0,
        0,571,572,3,116,58,0,572,573,5,43,0,0,573,115,1,0,0,0,574,577,3,
        118,59,0,575,577,1,0,0,0,576,574,1,0,0,0,576,575,1,0,0,0,577,117,
        1,0,0,0,578,579,3,120,60,0,579,580,5,44,0,0,580,581,3,118,59,0,581,
        584,1,0,0,0,582,584,3,120,60,0,583,578,1,0,0,0,583,582,1,0,0,0,584,
        119,1,0,0,0,585,586,5,50,0,0,586,587,5,46,0,0,587,588,3,126,63,0,
        588,121,1,0,0,0,589,592,3,124,62,0,590,592,5,50,0,0,591,589,1,0,
        0,0,591,590,1,0,0,0,592,123,1,0,0,0,593,594,7,1,0,0,594,125,1,0,
        0,0,595,603,5,48,0,0,596,603,5,47,0,0,597,603,5,49,0,0,598,603,5,
        23,0,0,599,603,5,24,0,0,600,603,3,114,57,0,601,603,3,106,53,0,602,
        595,1,0,0,0,602,596,1,0,0,0,602,597,1,0,0,0,602,598,1,0,0,0,602,
        599,1,0,0,0,602,600,1,0,0,0,602,601,1,0,0,0,603,127,1,0,0,0,604,
        605,7,2,0,0,605,129,1,0,0,0,47,137,141,149,158,168,179,190,202,204,
        219,221,229,247,249,258,262,269,282,284,310,332,338,346,351,362,
        369,383,399,404,414,430,435,448,455,461,466,500,504,524,536,548,
        563,567,576,583,591,602
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
    RULE_decl_stmtlst = 1
    RULE_decl_stmt = 2
    RULE_decl = 3
    RULE_stmt = 4
    RULE_expr = 5
    RULE_expr1 = 6
    RULE_expr2 = 7
    RULE_expr3 = 8
    RULE_expr4 = 9
    RULE_expr5 = 10
    RULE_expr6 = 11
    RULE_expr7 = 12
    RULE_exprlst = 13
    RULE_exprlstprime = 14
    RULE_lhs = 15
    RULE_assigning = 16
    RULE_vardecl = 17
    RULE_constdecl = 18
    RULE_arraydecl = 19
    RULE_arridxlst = 20
    RULE_arridx = 21
    RULE_funcdecl = 22
    RULE_funcparam = 23
    RULE_paramlst = 24
    RULE_paramlstprime = 25
    RULE_param = 26
    RULE_receiver = 27
    RULE_idlst = 28
    RULE_structdecl = 29
    RULE_structfield = 30
    RULE_fielddecllst = 31
    RULE_fielddecl = 32
    RULE_interfdecl = 33
    RULE_interfmeth = 34
    RULE_interfmethlst = 35
    RULE_interfmethmem = 36
    RULE_ifelse_stat = 37
    RULE_if_ = 38
    RULE_elseif_ = 39
    RULE_elseif_lst = 40
    RULE_else_ = 41
    RULE_condition = 42
    RULE_forloop_stat = 43
    RULE_id__arr = 44
    RULE_break_stat = 45
    RULE_continue_stat = 46
    RULE_funccall_stat = 47
    RULE_return_stat = 48
    RULE_assign = 49
    RULE_blockcode = 50
    RULE_blockcodestmtlst = 51
    RULE_blockcodestmt = 52
    RULE_arr_literal = 53
    RULE_arrelemlst = 54
    RULE_arreleml = 55
    RULE_arrelem = 56
    RULE_struct_literal = 57
    RULE_structparamlst = 58
    RULE_structparamlstprime = 59
    RULE_structparam = 60
    RULE_data_type = 61
    RULE_primitive_datatype = 62
    RULE_literal = 63
    RULE_end_stm = 64

    ruleNames =  [ "program", "decl_stmtlst", "decl_stmt", "decl", "stmt", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "exprlst", "exprlstprime", "lhs", "assigning", 
                   "vardecl", "constdecl", "arraydecl", "arridxlst", "arridx", 
                   "funcdecl", "funcparam", "paramlst", "paramlstprime", 
                   "param", "receiver", "idlst", "structdecl", "structfield", 
                   "fielddecllst", "fielddecl", "interfdecl", "interfmeth", 
                   "interfmethlst", "interfmethmem", "ifelse_stat", "if_", 
                   "elseif_", "elseif_lst", "else_", "condition", "forloop_stat", 
                   "id__arr", "break_stat", "continue_stat", "funccall_stat", 
                   "return_stat", "assign", "blockcode", "blockcodestmtlst", 
                   "blockcodestmt", "arr_literal", "arrelemlst", "arreleml", 
                   "arrelem", "struct_literal", "structparamlst", "structparamlstprime", 
                   "structparam", "data_type", "primitive_datatype", "literal", 
                   "end_stm" ]

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

        def decl_stmtlst(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_stmtlstContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.decl_stmtlst()
            self.state = 131
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_stmtlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_stmtContext,0)


        def decl_stmtlst(self):
            return self.getTypedRuleContext(MiniGoParser.Decl_stmtlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_stmtlst




    def decl_stmtlst(self):

        localctx = MiniGoParser.Decl_stmtlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_stmtlst)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.decl_stmt()
                self.state = 134
                self.decl_stmtlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.decl_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def stmt(self):
            return self.getTypedRuleContext(MiniGoParser.StmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl_stmt




    def decl_stmt(self):

        localctx = MiniGoParser.Decl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl_stmt)
        try:
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 17, 18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.decl()
                pass
            elif token in [5, 7, 8, 19, 20, 23, 24, 38, 40, 47, 48, 49, 50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.stmt()
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


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(MiniGoParser.ArraydeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


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
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.arraydecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
                self.constdecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 146
                self.funcdecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 147
                self.structdecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 148
                self.interfdecl()
                pass


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

        def assigning(self):
            return self.getTypedRuleContext(MiniGoParser.AssigningContext,0)


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
            return MiniGoParser.RULE_stmt




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stmt)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.assigning()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.ifelse_stat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.forloop_stat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 154
                self.continue_stat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 155
                self.break_stat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 156
                self.funccall_stat()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 157
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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 163
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 164
                    self.match(MiniGoParser.OR)
                    self.state = 165
                    self.expr1(0) 
                self.state = 170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 174
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 175
                    self.match(MiniGoParser.AND)
                    self.state = 176
                    self.expr2(0) 
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 190
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 185
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 186
                    self.match(MiniGoParser.COMPARISON_OP)
                    self.state = 187
                    self.expr3(0) 
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 204
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 202
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 196
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 197
                        self.match(MiniGoParser.ADD)
                        self.state = 198
                        self.expr4(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 199
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 200
                        self.match(MiniGoParser.SUB)
                        self.state = 201
                        self.expr4(0)
                        pass

             
                self.state = 206
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 219
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 210
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 211
                        self.match(MiniGoParser.MUL)
                        self.state = 212
                        self.expr5()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 213
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 214
                        self.match(MiniGoParser.DIV)
                        self.state = 215
                        self.expr5()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 216
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 217
                        self.match(MiniGoParser.MOD)
                        self.state = 218
                        self.expr5()
                        pass

             
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        self.enterRule(localctx, 20, self.RULE_expr5)
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(MiniGoParser.NOT)
                self.state = 225
                self.expr6(0)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(MiniGoParser.SUB)
                self.state = 227
                self.expr6(0)
                pass
            elif token in [23, 24, 38, 40, 47, 48, 49, 50]:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 249
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 247
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 234
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 235
                        self.match(MiniGoParser.DOT)
                        self.state = 236
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 237
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 238
                        self.match(MiniGoParser.LSB)
                        self.state = 239
                        self.expr(0)
                        self.state = 240
                        self.match(MiniGoParser.RSB)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 242
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 243
                        self.match(MiniGoParser.LP)
                        self.state = 244
                        self.exprlst()
                        self.state = 245
                        self.match(MiniGoParser.RP)
                        pass

             
                self.state = 251
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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr7)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.match(MiniGoParser.LP)
                self.state = 253
                self.expr(0)
                self.state = 254
                self.match(MiniGoParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
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
        self.enterRule(localctx, 26, self.RULE_exprlst)
        try:
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 28, 34, 38, 40, 47, 48, 49, 50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
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
        self.enterRule(localctx, 28, self.RULE_exprlstprime)
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.expr(0)
                self.state = 265
                self.match(MiniGoParser.COMMA)
                self.state = 266
                self.exprlstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 284
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 282
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 274
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 275
                        self.match(MiniGoParser.DOT)
                        self.state = 276
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 277
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 278
                        self.match(MiniGoParser.LSB)
                        self.state = 279
                        self.expr(0)
                        self.state = 280
                        self.match(MiniGoParser.RSB)
                        pass

             
                self.state = 286
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        self.enterRule(localctx, 32, self.RULE_assigning)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.lhs(0)
            self.state = 288
            self.assign()
            self.state = 289
            self.expr(0)
            self.state = 290
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
        self.enterRule(localctx, 34, self.RULE_vardecl)
        try:
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(MiniGoParser.VAR_)
                self.state = 293
                self.match(MiniGoParser.ID)
                self.state = 294
                self.data_type()
                self.state = 295
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.match(MiniGoParser.VAR_)
                self.state = 298
                self.match(MiniGoParser.ID)
                self.state = 299
                self.match(MiniGoParser.EQUAL)
                self.state = 300
                self.expr(0)
                self.state = 301
                self.end_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 303
                self.match(MiniGoParser.VAR_)
                self.state = 304
                self.match(MiniGoParser.ID)
                self.state = 305
                self.data_type()
                self.state = 306
                self.match(MiniGoParser.EQUAL)
                self.state = 307
                self.expr(0)
                self.state = 308
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
        self.enterRule(localctx, 36, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(MiniGoParser.CONST_)
            self.state = 313
            self.match(MiniGoParser.ID)
            self.state = 314
            self.match(MiniGoParser.EQUAL)
            self.state = 315
            self.expr(0)
            self.state = 316
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
        self.enterRule(localctx, 38, self.RULE_arraydecl)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(MiniGoParser.VAR_)
                self.state = 319
                self.match(MiniGoParser.ID)
                self.state = 320
                self.arridxlst()
                self.state = 321
                self.data_type()
                self.state = 322
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.match(MiniGoParser.VAR_)
                self.state = 325
                self.match(MiniGoParser.ID)
                self.state = 326
                self.arridxlst()
                self.state = 327
                self.data_type()
                self.state = 328
                self.match(MiniGoParser.EQUAL)
                self.state = 329
                self.arr_literal()
                self.state = 330
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
        self.enterRule(localctx, 40, self.RULE_arridxlst)
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.arridx()
                self.state = 335
                self.arridxlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
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
        self.enterRule(localctx, 42, self.RULE_arridx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(MiniGoParser.LSB)
            self.state = 341
            self.expr(0)
            self.state = 342
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
        self.enterRule(localctx, 44, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(MiniGoParser.FUNC_)
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 345
                self.receiver()


            self.state = 348
            self.match(MiniGoParser.ID)
            self.state = 349
            self.funcparam()
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1125899906965504) != 0):
                self.state = 350
                self.data_type()


            self.state = 353
            self.blockcode()
            self.state = 354
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
        self.enterRule(localctx, 46, self.RULE_funcparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(MiniGoParser.LP)
            self.state = 357
            self.paramlst()
            self.state = 358
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
        self.enterRule(localctx, 48, self.RULE_paramlst)
        try:
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
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
        self.enterRule(localctx, 50, self.RULE_paramlstprime)
        try:
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.param()
                self.state = 365
                self.match(MiniGoParser.COMMA)
                self.state = 366
                self.paramlstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
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
        self.enterRule(localctx, 52, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.idlst()
            self.state = 372
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
        self.enterRule(localctx, 54, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(MiniGoParser.LP)
            self.state = 375
            self.match(MiniGoParser.ID)
            self.state = 376
            self.match(MiniGoParser.ID)
            self.state = 377
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
        self.enterRule(localctx, 56, self.RULE_idlst)
        try:
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.match(MiniGoParser.ID)
                self.state = 380
                self.match(MiniGoParser.COMMA)
                self.state = 381
                self.idlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
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
        self.enterRule(localctx, 58, self.RULE_structdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(MiniGoParser.TYPE_)
            self.state = 386
            self.match(MiniGoParser.ID)
            self.state = 387
            self.match(MiniGoParser.STRUCT_)
            self.state = 388
            self.structfield()
            self.state = 389
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
        self.enterRule(localctx, 60, self.RULE_structfield)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(MiniGoParser.LCB)
            self.state = 392
            self.fielddecllst()
            self.state = 393
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
        self.enterRule(localctx, 62, self.RULE_fielddecllst)
        try:
            self.state = 399
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.fielddecl()
                self.state = 396
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
        self.enterRule(localctx, 64, self.RULE_fielddecl)
        self._la = 0 # Token type
        try:
            self.state = 414
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(MiniGoParser.ID)
                self.state = 402
                self.data_type()
                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==40:
                    self.state = 403
                    self.arridxlst()


                self.state = 406
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.match(MiniGoParser.ID)
                self.state = 409
                self.match(MiniGoParser.ID)
                self.state = 410
                self.end_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 411
                self.match(MiniGoParser.ID)
                self.state = 412
                self.match(MiniGoParser.INTERFACE_)
                self.state = 413
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
        self.enterRule(localctx, 66, self.RULE_interfdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(MiniGoParser.TYPE_)
            self.state = 417
            self.match(MiniGoParser.ID)
            self.state = 418
            self.match(MiniGoParser.INTERFACE_)
            self.state = 419
            self.interfmeth()
            self.state = 420
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
        self.enterRule(localctx, 68, self.RULE_interfmeth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(MiniGoParser.LCB)
            self.state = 423
            self.interfmethlst()
            self.state = 424
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
        self.enterRule(localctx, 70, self.RULE_interfmethlst)
        try:
            self.state = 430
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.interfmethmem()
                self.state = 427
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
        self.enterRule(localctx, 72, self.RULE_interfmethmem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(MiniGoParser.ID)
            self.state = 433
            self.funcparam()
            self.state = 435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1125899906965504) != 0):
                self.state = 434
                self.data_type()


            self.state = 437
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
        self.enterRule(localctx, 74, self.RULE_ifelse_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.if_()
            self.state = 440
            self.elseif_lst()
            self.state = 441
            self.else_()
            self.state = 442
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
        self.enterRule(localctx, 76, self.RULE_if_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(MiniGoParser.IF_)
            self.state = 445
            self.condition()
            self.state = 446
            self.blockcode()
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 447
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
        self.enterRule(localctx, 78, self.RULE_elseif_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(MiniGoParser.ELSE_)
            self.state = 451
            self.match(MiniGoParser.IF_)
            self.state = 452
            self.condition()
            self.state = 453
            self.blockcode()
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 454
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
        self.enterRule(localctx, 80, self.RULE_elseif_lst)
        try:
            self.state = 461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.elseif_()
                self.state = 458
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
        self.enterRule(localctx, 82, self.RULE_else_)
        try:
            self.state = 466
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.match(MiniGoParser.ELSE_)
                self.state = 464
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
        self.enterRule(localctx, 84, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(MiniGoParser.LP)
            self.state = 469
            self.expr(0)
            self.state = 470
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
        self.enterRule(localctx, 86, self.RULE_forloop_stat)
        try:
            self.state = 500
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.match(MiniGoParser.FOR_)
                self.state = 473
                self.expr(0)
                self.state = 474
                self.blockcode()
                self.state = 475
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 477
                self.match(MiniGoParser.FOR_)
                self.state = 478
                self.match(MiniGoParser.ID)
                self.state = 479
                self.match(MiniGoParser.ASSIGN)
                self.state = 480
                self.expr(0)
                self.state = 481
                self.match(MiniGoParser.SEMICOLON)
                self.state = 482
                self.expr(0)
                self.state = 483
                self.match(MiniGoParser.SEMICOLON)
                self.state = 484
                self.match(MiniGoParser.ID)
                self.state = 485
                self.match(MiniGoParser.UPT_ASSIGN)
                self.state = 486
                self.expr(0)
                self.state = 487
                self.blockcode()
                self.state = 488
                self.end_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 490
                self.match(MiniGoParser.FOR_)
                self.state = 491
                self.match(MiniGoParser.ID)
                self.state = 492
                self.match(MiniGoParser.COMMA)
                self.state = 493
                self.match(MiniGoParser.ID)
                self.state = 494
                self.match(MiniGoParser.ASSIGN)
                self.state = 495
                self.match(MiniGoParser.RANGE_)
                self.state = 496
                self.id__arr()
                self.state = 497
                self.blockcode()
                self.state = 498
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
        self.enterRule(localctx, 88, self.RULE_id__arr)
        try:
            self.state = 504
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 502
                self.match(MiniGoParser.ID)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
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
        self.enterRule(localctx, 90, self.RULE_break_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.match(MiniGoParser.BREAK_)
            self.state = 507
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
        self.enterRule(localctx, 92, self.RULE_continue_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.match(MiniGoParser.CONTINUE_)
            self.state = 510
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
        self.enterRule(localctx, 94, self.RULE_funccall_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.expr6(0)
            self.state = 513
            self.match(MiniGoParser.LP)
            self.state = 514
            self.exprlst()
            self.state = 515
            self.match(MiniGoParser.RP)
            self.state = 516
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
        self.enterRule(localctx, 96, self.RULE_return_stat)
        try:
            self.state = 524
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self.match(MiniGoParser.RETURN_)
                self.state = 519
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 520
                self.match(MiniGoParser.RETURN_)
                self.state = 521
                self.expr(0)
                self.state = 522
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
        self.enterRule(localctx, 98, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
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

        def blockcodestmtlst(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodestmtlstContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_blockcode




    def blockcode(self):

        localctx = MiniGoParser.BlockcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_blockcode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.match(MiniGoParser.LCB)
            self.state = 529
            self.blockcodestmtlst()
            self.state = 530
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockcodestmtlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockcodestmt(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodestmtContext,0)


        def blockcodestmtlst(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodestmtlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_blockcodestmtlst




    def blockcodestmtlst(self):

        localctx = MiniGoParser.BlockcodestmtlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_blockcodestmtlst)
        try:
            self.state = 536
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 7, 8, 17, 18, 19, 20, 23, 24, 38, 40, 47, 48, 49, 50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 532
                self.blockcodestmt()
                self.state = 533
                self.blockcodestmtlst()
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


    class BlockcodestmtContext(ParserRuleContext):
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
            return MiniGoParser.RULE_blockcodestmt




    def blockcodestmt(self):

        localctx = MiniGoParser.BlockcodestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_blockcodestmt)
        try:
            self.state = 548
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 538
                self.assigning()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 539
                self.vardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 540
                self.arraydecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 541
                self.constdecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 542
                self.ifelse_stat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 543
                self.forloop_stat()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 544
                self.continue_stat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 545
                self.break_stat()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 546
                self.funccall_stat()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 547
                self.return_stat()
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
        self.enterRule(localctx, 106, self.RULE_arr_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.arridxlst()
            self.state = 551
            self.data_type()
            self.state = 552
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
        self.enterRule(localctx, 108, self.RULE_arrelemlst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self.match(MiniGoParser.LCB)
            self.state = 555
            self.arreleml()
            self.state = 556
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
        self.enterRule(localctx, 110, self.RULE_arreleml)
        try:
            self.state = 563
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 558
                self.arrelem()
                self.state = 559
                self.match(MiniGoParser.COMMA)
                self.state = 560
                self.arreleml()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 562
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
        self.enterRule(localctx, 112, self.RULE_arrelem)
        try:
            self.state = 567
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 28, 34, 38, 40, 47, 48, 49, 50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 565
                self.expr(0)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 566
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
        self.enterRule(localctx, 114, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(MiniGoParser.ID)
            self.state = 570
            self.match(MiniGoParser.LCB)
            self.state = 571
            self.structparamlst()
            self.state = 572
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
        self.enterRule(localctx, 116, self.RULE_structparamlst)
        try:
            self.state = 576
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 574
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
        self.enterRule(localctx, 118, self.RULE_structparamlstprime)
        try:
            self.state = 583
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 578
                self.structparam()
                self.state = 579
                self.match(MiniGoParser.COMMA)
                self.state = 580
                self.structparamlstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 582
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
        self.enterRule(localctx, 120, self.RULE_structparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.match(MiniGoParser.ID)
            self.state = 586
            self.match(MiniGoParser.COLON)
            self.state = 587
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
        self.enterRule(localctx, 122, self.RULE_data_type)
        try:
            self.state = 591
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 589
                self.primitive_datatype()
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 590
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
        self.enterRule(localctx, 124, self.RULE_primitive_datatype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
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
        self.enterRule(localctx, 126, self.RULE_literal)
        try:
            self.state = 602
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 595
                self.match(MiniGoParser.INTEGER)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 596
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 3)
                self.state = 597
                self.match(MiniGoParser.STRING)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 598
                self.match(MiniGoParser.TRUE_)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 599
                self.match(MiniGoParser.FALSE_)
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 6)
                self.state = 600
                self.struct_literal()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 7)
                self.state = 601
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
        self.enterRule(localctx, 128, self.RULE_end_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
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
        self._predicates[5] = self.expr_sempred
        self._predicates[6] = self.expr1_sempred
        self._predicates[7] = self.expr2_sempred
        self._predicates[8] = self.expr3_sempred
        self._predicates[9] = self.expr4_sempred
        self._predicates[11] = self.expr6_sempred
        self._predicates[15] = self.lhs_sempred
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
         




