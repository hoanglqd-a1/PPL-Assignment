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
        4,0,62,570,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,1,0,1,0,1,0,1,0,5,0,144,8,
        0,10,0,12,0,147,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,156,8,1,10,1,
        12,1,159,9,1,1,1,1,1,1,1,1,1,1,1,1,2,3,2,167,8,2,1,2,1,2,1,2,1,3,
        4,3,173,8,3,11,3,12,3,174,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,
        1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,
        1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,
        1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,
        1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,
        1,35,1,35,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,38,
        1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,40,1,40,1,40,1,41,1,41,1,41,
        1,42,1,42,1,42,1,43,1,43,1,43,1,44,1,44,1,44,1,45,1,45,1,45,1,46,
        1,46,1,46,1,47,1,47,1,47,1,48,1,48,1,48,1,49,1,49,1,49,1,50,1,50,
        1,50,1,51,1,51,1,51,1,52,1,52,1,52,1,53,1,53,1,53,1,54,1,54,1,54,
        1,55,1,55,1,56,4,56,456,8,56,11,56,12,56,457,1,56,1,56,4,56,462,
        8,56,11,56,12,56,463,3,56,466,8,56,1,56,1,56,3,56,470,8,56,1,56,
        4,56,473,8,56,11,56,12,56,474,3,56,477,8,56,1,56,1,56,1,57,1,57,
        1,57,5,57,484,8,57,10,57,12,57,487,9,57,3,57,489,8,57,1,58,1,58,
        1,58,4,58,494,8,58,11,58,12,58,495,1,59,1,59,1,59,4,59,501,8,59,
        11,59,12,59,502,1,60,1,60,1,60,4,60,508,8,60,11,60,12,60,509,1,61,
        1,61,1,61,1,61,3,61,516,8,61,1,61,1,61,1,62,1,62,1,63,1,63,1,63,
        1,64,1,64,1,64,5,64,528,8,64,10,64,12,64,531,9,64,1,64,1,64,1,64,
        1,65,1,65,5,65,538,8,65,10,65,12,65,541,9,65,1,65,1,65,1,66,1,66,
        1,66,1,67,1,67,1,67,5,67,551,8,67,10,67,12,67,554,9,67,1,67,1,67,
        1,67,1,67,1,68,1,68,1,68,5,68,563,8,68,10,68,12,68,566,9,68,1,68,
        1,68,1,68,1,157,0,69,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,
        10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,
        21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,
        32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,
        43,87,44,89,45,91,46,93,47,95,48,97,49,99,50,101,51,103,52,105,53,
        107,54,109,55,111,0,113,56,115,0,117,0,119,0,121,0,123,57,125,0,
        127,0,129,58,131,59,133,60,135,61,137,62,1,0,16,1,0,10,10,3,0,9,
        9,12,13,32,32,1,0,48,57,2,0,69,69,101,101,2,0,43,43,45,45,1,0,49,
        57,2,0,66,66,98,98,1,0,48,49,2,0,79,79,111,111,1,0,48,55,2,0,88,
        88,120,120,3,0,48,57,65,70,97,102,3,0,10,10,34,34,92,92,5,0,34,34,
        92,92,110,110,114,114,116,116,3,0,65,90,95,95,97,122,4,0,48,57,65,
        90,95,95,97,122,588,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,
        0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,
        0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,
        0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,
        0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,
        0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,
        0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,
        0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,
        0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,
        0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,
        0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,
        1,0,0,0,0,109,1,0,0,0,0,113,1,0,0,0,0,123,1,0,0,0,0,129,1,0,0,0,
        0,131,1,0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,1,139,1,
        0,0,0,3,150,1,0,0,0,5,166,1,0,0,0,7,172,1,0,0,0,9,178,1,0,0,0,11,
        183,1,0,0,0,13,190,1,0,0,0,15,196,1,0,0,0,17,205,1,0,0,0,19,212,
        1,0,0,0,21,219,1,0,0,0,23,228,1,0,0,0,25,240,1,0,0,0,27,249,1,0,
        0,0,29,255,1,0,0,0,31,263,1,0,0,0,33,273,1,0,0,0,35,281,1,0,0,0,
        37,287,1,0,0,0,39,298,1,0,0,0,41,306,1,0,0,0,43,314,1,0,0,0,45,320,
        1,0,0,0,47,327,1,0,0,0,49,335,1,0,0,0,51,340,1,0,0,0,53,345,1,0,
        0,0,55,348,1,0,0,0,57,353,1,0,0,0,59,356,1,0,0,0,61,361,1,0,0,0,
        63,366,1,0,0,0,65,371,1,0,0,0,67,374,1,0,0,0,69,379,1,0,0,0,71,384,
        1,0,0,0,73,389,1,0,0,0,75,394,1,0,0,0,77,399,1,0,0,0,79,404,1,0,
        0,0,81,407,1,0,0,0,83,410,1,0,0,0,85,413,1,0,0,0,87,416,1,0,0,0,
        89,419,1,0,0,0,91,422,1,0,0,0,93,425,1,0,0,0,95,428,1,0,0,0,97,431,
        1,0,0,0,99,434,1,0,0,0,101,437,1,0,0,0,103,440,1,0,0,0,105,443,1,
        0,0,0,107,446,1,0,0,0,109,449,1,0,0,0,111,452,1,0,0,0,113,455,1,
        0,0,0,115,488,1,0,0,0,117,490,1,0,0,0,119,497,1,0,0,0,121,504,1,
        0,0,0,123,515,1,0,0,0,125,519,1,0,0,0,127,521,1,0,0,0,129,524,1,
        0,0,0,131,535,1,0,0,0,133,544,1,0,0,0,135,547,1,0,0,0,137,559,1,
        0,0,0,139,140,5,47,0,0,140,141,5,47,0,0,141,145,1,0,0,0,142,144,
        8,0,0,0,143,142,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,
        1,0,0,0,146,148,1,0,0,0,147,145,1,0,0,0,148,149,6,0,0,0,149,2,1,
        0,0,0,150,151,5,47,0,0,151,152,5,42,0,0,152,157,1,0,0,0,153,156,
        3,3,1,0,154,156,9,0,0,0,155,153,1,0,0,0,155,154,1,0,0,0,156,159,
        1,0,0,0,157,158,1,0,0,0,157,155,1,0,0,0,158,160,1,0,0,0,159,157,
        1,0,0,0,160,161,5,42,0,0,161,162,5,47,0,0,162,163,1,0,0,0,163,164,
        6,1,0,0,164,4,1,0,0,0,165,167,5,13,0,0,166,165,1,0,0,0,166,167,1,
        0,0,0,167,168,1,0,0,0,168,169,5,10,0,0,169,170,6,2,1,0,170,6,1,0,
        0,0,171,173,7,1,0,0,172,171,1,0,0,0,173,174,1,0,0,0,174,172,1,0,
        0,0,174,175,1,0,0,0,175,176,1,0,0,0,176,177,6,3,0,0,177,8,1,0,0,
        0,178,179,5,105,0,0,179,180,5,102,0,0,180,181,1,0,0,0,181,182,6,
        4,2,0,182,10,1,0,0,0,183,184,5,101,0,0,184,185,5,108,0,0,185,186,
        5,115,0,0,186,187,5,101,0,0,187,188,1,0,0,0,188,189,6,5,3,0,189,
        12,1,0,0,0,190,191,5,102,0,0,191,192,5,111,0,0,192,193,5,114,0,0,
        193,194,1,0,0,0,194,195,6,6,4,0,195,14,1,0,0,0,196,197,5,114,0,0,
        197,198,5,101,0,0,198,199,5,116,0,0,199,200,5,117,0,0,200,201,5,
        114,0,0,201,202,5,110,0,0,202,203,1,0,0,0,203,204,6,7,5,0,204,16,
        1,0,0,0,205,206,5,102,0,0,206,207,5,117,0,0,207,208,5,110,0,0,208,
        209,5,99,0,0,209,210,1,0,0,0,210,211,6,8,6,0,211,18,1,0,0,0,212,
        213,5,116,0,0,213,214,5,121,0,0,214,215,5,112,0,0,215,216,5,101,
        0,0,216,217,1,0,0,0,217,218,6,9,7,0,218,20,1,0,0,0,219,220,5,115,
        0,0,220,221,5,116,0,0,221,222,5,114,0,0,222,223,5,117,0,0,223,224,
        5,99,0,0,224,225,5,116,0,0,225,226,1,0,0,0,226,227,6,10,8,0,227,
        22,1,0,0,0,228,229,5,105,0,0,229,230,5,110,0,0,230,231,5,116,0,0,
        231,232,5,101,0,0,232,233,5,114,0,0,233,234,5,102,0,0,234,235,5,
        97,0,0,235,236,5,99,0,0,236,237,5,101,0,0,237,238,1,0,0,0,238,239,
        6,11,9,0,239,24,1,0,0,0,240,241,5,115,0,0,241,242,5,116,0,0,242,
        243,5,114,0,0,243,244,5,105,0,0,244,245,5,110,0,0,245,246,5,103,
        0,0,246,247,1,0,0,0,247,248,6,12,10,0,248,26,1,0,0,0,249,250,5,105,
        0,0,250,251,5,110,0,0,251,252,5,116,0,0,252,253,1,0,0,0,253,254,
        6,13,11,0,254,28,1,0,0,0,255,256,5,102,0,0,256,257,5,108,0,0,257,
        258,5,111,0,0,258,259,5,97,0,0,259,260,5,116,0,0,260,261,1,0,0,0,
        261,262,6,14,12,0,262,30,1,0,0,0,263,264,5,98,0,0,264,265,5,111,
        0,0,265,266,5,111,0,0,266,267,5,108,0,0,267,268,5,101,0,0,268,269,
        5,97,0,0,269,270,5,110,0,0,270,271,1,0,0,0,271,272,6,15,13,0,272,
        32,1,0,0,0,273,274,5,99,0,0,274,275,5,111,0,0,275,276,5,110,0,0,
        276,277,5,115,0,0,277,278,5,116,0,0,278,279,1,0,0,0,279,280,6,16,
        14,0,280,34,1,0,0,0,281,282,5,118,0,0,282,283,5,97,0,0,283,284,5,
        114,0,0,284,285,1,0,0,0,285,286,6,17,15,0,286,36,1,0,0,0,287,288,
        5,99,0,0,288,289,5,111,0,0,289,290,5,110,0,0,290,291,5,116,0,0,291,
        292,5,105,0,0,292,293,5,110,0,0,293,294,5,117,0,0,294,295,5,101,
        0,0,295,296,1,0,0,0,296,297,6,18,16,0,297,38,1,0,0,0,298,299,5,98,
        0,0,299,300,5,114,0,0,300,301,5,101,0,0,301,302,5,97,0,0,302,303,
        5,107,0,0,303,304,1,0,0,0,304,305,6,19,17,0,305,40,1,0,0,0,306,307,
        5,114,0,0,307,308,5,97,0,0,308,309,5,110,0,0,309,310,5,103,0,0,310,
        311,5,101,0,0,311,312,1,0,0,0,312,313,6,20,18,0,313,42,1,0,0,0,314,
        315,5,110,0,0,315,316,5,105,0,0,316,317,5,108,0,0,317,318,1,0,0,
        0,318,319,6,21,19,0,319,44,1,0,0,0,320,321,5,116,0,0,321,322,5,114,
        0,0,322,323,5,117,0,0,323,324,5,101,0,0,324,325,1,0,0,0,325,326,
        6,22,20,0,326,46,1,0,0,0,327,328,5,102,0,0,328,329,5,97,0,0,329,
        330,5,108,0,0,330,331,5,115,0,0,331,332,5,101,0,0,332,333,1,0,0,
        0,333,334,6,23,21,0,334,48,1,0,0,0,335,336,5,61,0,0,336,337,5,61,
        0,0,337,338,1,0,0,0,338,339,6,24,22,0,339,50,1,0,0,0,340,341,5,33,
        0,0,341,342,5,61,0,0,342,343,1,0,0,0,343,344,6,25,23,0,344,52,1,
        0,0,0,345,346,5,60,0,0,346,347,6,26,24,0,347,54,1,0,0,0,348,349,
        5,60,0,0,349,350,5,61,0,0,350,351,1,0,0,0,351,352,6,27,25,0,352,
        56,1,0,0,0,353,354,5,62,0,0,354,355,6,28,26,0,355,58,1,0,0,0,356,
        357,5,62,0,0,357,358,5,61,0,0,358,359,1,0,0,0,359,360,6,29,27,0,
        360,60,1,0,0,0,361,362,5,38,0,0,362,363,5,38,0,0,363,364,1,0,0,0,
        364,365,6,30,28,0,365,62,1,0,0,0,366,367,5,124,0,0,367,368,5,124,
        0,0,368,369,1,0,0,0,369,370,6,31,29,0,370,64,1,0,0,0,371,372,5,33,
        0,0,372,373,6,32,30,0,373,66,1,0,0,0,374,375,5,43,0,0,375,376,5,
        61,0,0,376,377,1,0,0,0,377,378,6,33,31,0,378,68,1,0,0,0,379,380,
        5,45,0,0,380,381,5,61,0,0,381,382,1,0,0,0,382,383,6,34,32,0,383,
        70,1,0,0,0,384,385,5,42,0,0,385,386,5,61,0,0,386,387,1,0,0,0,387,
        388,6,35,33,0,388,72,1,0,0,0,389,390,5,47,0,0,390,391,5,61,0,0,391,
        392,1,0,0,0,392,393,6,36,34,0,393,74,1,0,0,0,394,395,5,37,0,0,395,
        396,5,61,0,0,396,397,1,0,0,0,397,398,6,37,35,0,398,76,1,0,0,0,399,
        400,5,58,0,0,400,401,5,61,0,0,401,402,1,0,0,0,402,403,6,38,36,0,
        403,78,1,0,0,0,404,405,5,46,0,0,405,406,6,39,37,0,406,80,1,0,0,0,
        407,408,5,61,0,0,408,409,6,40,38,0,409,82,1,0,0,0,410,411,5,43,0,
        0,411,412,6,41,39,0,412,84,1,0,0,0,413,414,5,45,0,0,414,415,6,42,
        40,0,415,86,1,0,0,0,416,417,5,42,0,0,417,418,6,43,41,0,418,88,1,
        0,0,0,419,420,5,47,0,0,420,421,6,44,42,0,421,90,1,0,0,0,422,423,
        5,37,0,0,423,424,6,45,43,0,424,92,1,0,0,0,425,426,5,40,0,0,426,427,
        6,46,44,0,427,94,1,0,0,0,428,429,5,41,0,0,429,430,6,47,45,0,430,
        96,1,0,0,0,431,432,5,91,0,0,432,433,6,48,46,0,433,98,1,0,0,0,434,
        435,5,93,0,0,435,436,6,49,47,0,436,100,1,0,0,0,437,438,5,123,0,0,
        438,439,6,50,48,0,439,102,1,0,0,0,440,441,5,125,0,0,441,442,6,51,
        49,0,442,104,1,0,0,0,443,444,5,44,0,0,444,445,6,52,50,0,445,106,
        1,0,0,0,446,447,5,59,0,0,447,448,6,53,51,0,448,108,1,0,0,0,449,450,
        5,58,0,0,450,451,6,54,52,0,451,110,1,0,0,0,452,453,7,2,0,0,453,112,
        1,0,0,0,454,456,3,111,55,0,455,454,1,0,0,0,456,457,1,0,0,0,457,455,
        1,0,0,0,457,458,1,0,0,0,458,459,1,0,0,0,459,465,5,46,0,0,460,462,
        3,111,55,0,461,460,1,0,0,0,462,463,1,0,0,0,463,461,1,0,0,0,463,464,
        1,0,0,0,464,466,1,0,0,0,465,461,1,0,0,0,465,466,1,0,0,0,466,476,
        1,0,0,0,467,469,7,3,0,0,468,470,7,4,0,0,469,468,1,0,0,0,469,470,
        1,0,0,0,470,472,1,0,0,0,471,473,3,111,55,0,472,471,1,0,0,0,473,474,
        1,0,0,0,474,472,1,0,0,0,474,475,1,0,0,0,475,477,1,0,0,0,476,467,
        1,0,0,0,476,477,1,0,0,0,477,478,1,0,0,0,478,479,6,56,53,0,479,114,
        1,0,0,0,480,489,5,48,0,0,481,485,7,5,0,0,482,484,7,2,0,0,483,482,
        1,0,0,0,484,487,1,0,0,0,485,483,1,0,0,0,485,486,1,0,0,0,486,489,
        1,0,0,0,487,485,1,0,0,0,488,480,1,0,0,0,488,481,1,0,0,0,489,116,
        1,0,0,0,490,491,5,48,0,0,491,493,7,6,0,0,492,494,7,7,0,0,493,492,
        1,0,0,0,494,495,1,0,0,0,495,493,1,0,0,0,495,496,1,0,0,0,496,118,
        1,0,0,0,497,498,5,48,0,0,498,500,7,8,0,0,499,501,7,9,0,0,500,499,
        1,0,0,0,501,502,1,0,0,0,502,500,1,0,0,0,502,503,1,0,0,0,503,120,
        1,0,0,0,504,505,5,48,0,0,505,507,7,10,0,0,506,508,7,11,0,0,507,506,
        1,0,0,0,508,509,1,0,0,0,509,507,1,0,0,0,509,510,1,0,0,0,510,122,
        1,0,0,0,511,516,3,115,57,0,512,516,3,117,58,0,513,516,3,119,59,0,
        514,516,3,121,60,0,515,511,1,0,0,0,515,512,1,0,0,0,515,513,1,0,0,
        0,515,514,1,0,0,0,516,517,1,0,0,0,517,518,6,61,54,0,518,124,1,0,
        0,0,519,520,8,12,0,0,520,126,1,0,0,0,521,522,5,92,0,0,522,523,7,
        13,0,0,523,128,1,0,0,0,524,529,5,34,0,0,525,528,3,125,62,0,526,528,
        3,127,63,0,527,525,1,0,0,0,527,526,1,0,0,0,528,531,1,0,0,0,529,527,
        1,0,0,0,529,530,1,0,0,0,530,532,1,0,0,0,531,529,1,0,0,0,532,533,
        5,34,0,0,533,534,6,64,55,0,534,130,1,0,0,0,535,539,7,14,0,0,536,
        538,7,15,0,0,537,536,1,0,0,0,538,541,1,0,0,0,539,537,1,0,0,0,539,
        540,1,0,0,0,540,542,1,0,0,0,541,539,1,0,0,0,542,543,6,65,56,0,543,
        132,1,0,0,0,544,545,9,0,0,0,545,546,6,66,57,0,546,134,1,0,0,0,547,
        552,5,34,0,0,548,551,3,125,62,0,549,551,3,127,63,0,550,548,1,0,0,
        0,550,549,1,0,0,0,551,554,1,0,0,0,552,550,1,0,0,0,552,553,1,0,0,
        0,553,555,1,0,0,0,554,552,1,0,0,0,555,556,5,92,0,0,556,557,8,13,
        0,0,557,558,6,67,58,0,558,136,1,0,0,0,559,564,5,34,0,0,560,563,3,
        125,62,0,561,563,3,127,63,0,562,560,1,0,0,0,562,561,1,0,0,0,563,
        566,1,0,0,0,564,562,1,0,0,0,564,565,1,0,0,0,565,567,1,0,0,0,566,
        564,1,0,0,0,567,568,6,68,59,0,568,569,6,68,60,0,569,138,1,0,0,0,
        25,0,145,155,157,166,174,457,463,465,469,474,476,485,488,495,502,
        509,515,527,529,539,550,552,562,564,61,6,0,0,1,2,0,1,4,1,1,5,2,1,
        6,3,1,7,4,1,8,5,1,9,6,1,10,7,1,11,8,1,12,9,1,13,10,1,14,11,1,15,
        12,1,16,13,1,17,14,1,18,15,1,19,16,1,20,17,1,21,18,1,22,19,1,23,
        20,1,24,21,1,25,22,1,26,23,1,27,24,1,28,25,1,29,26,1,30,27,1,31,
        28,1,32,29,1,33,30,1,34,31,1,35,32,1,36,33,1,37,34,1,38,35,1,39,
        36,1,40,37,1,41,38,1,42,39,1,43,40,1,44,41,1,45,42,1,46,43,1,47,
        44,1,48,45,1,49,46,1,50,47,1,51,48,1,52,49,1,53,50,1,54,51,1,56,
        52,1,61,53,1,64,54,1,65,55,1,66,56,1,67,57,1,68,58,1,68,59
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
    EQCOM = 25
    DIFFCOM = 26
    LESSCOM = 27
    LEQCOM = 28
    GRECOM = 29
    GEQCOM = 30
    AND = 31
    OR = 32
    NOT = 33
    ADDASSIGN = 34
    SUBASSIGN = 35
    MULASSIGN = 36
    DIVASSIGN = 37
    MODASSIGN = 38
    ASSIGN = 39
    DOT = 40
    EQUAL = 41
    ADD = 42
    SUB = 43
    MUL = 44
    DIV = 45
    MOD = 46
    LP = 47
    RP = 48
    LSB = 49
    RSB = 50
    LCB = 51
    RCB = 52
    COMMA = 53
    SEMICOLON = 54
    COLON = 55
    FLOAT = 56
    INTEGER = 57
    STRING = 58
    ID = 59
    ERROR_CHAR = 60
    ILLEGAL_ESCAPE = 61
    UNCLOSE_STRING = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'&&'", "'||'", "'!'", "'+='", "'-='", "'*='", "'/='", "'%='", 
            "':='", "'.'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", 
            "')'", "'['", "']'", "'{'", "'}'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "SINGLE_LINE_CMT", "MULTI_LINE_CMT", "NL", "WS", "IF_", "ELSE_", 
            "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", "INTERFACE_", 
            "STRING_", "INT_", "FLOAT_", "BOOLEAN_", "CONST_", "VAR_", "CONTINUE_", 
            "BREAK_", "RANGE_", "NIL_", "TRUE_", "FALSE_", "EQCOM", "DIFFCOM", 
            "LESSCOM", "LEQCOM", "GRECOM", "GEQCOM", "AND", "OR", "NOT", 
            "ADDASSIGN", "SUBASSIGN", "MULASSIGN", "DIVASSIGN", "MODASSIGN", 
            "ASSIGN", "DOT", "EQUAL", "ADD", "SUB", "MUL", "DIV", "MOD", 
            "LP", "RP", "LSB", "RSB", "LCB", "RCB", "COMMA", "SEMICOLON", 
            "COLON", "FLOAT", "INTEGER", "STRING", "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING" ]

    ruleNames = [ "SINGLE_LINE_CMT", "MULTI_LINE_CMT", "NL", "WS", "IF_", 
                  "ELSE_", "FOR_", "RETURN_", "FUNC_", "TYPE_", "STRUCT_", 
                  "INTERFACE_", "STRING_", "INT_", "FLOAT_", "BOOLEAN_", 
                  "CONST_", "VAR_", "CONTINUE_", "BREAK_", "RANGE_", "NIL_", 
                  "TRUE_", "FALSE_", "EQCOM", "DIFFCOM", "LESSCOM", "LEQCOM", 
                  "GRECOM", "GEQCOM", "AND", "OR", "NOT", "ADDASSIGN", "SUBASSIGN", 
                  "MULASSIGN", "DIVASSIGN", "MODASSIGN", "ASSIGN", "DOT", 
                  "EQUAL", "ADD", "SUB", "MUL", "DIV", "MOD", "LP", "RP", 
                  "LSB", "RSB", "LCB", "RCB", "COMMA", "SEMICOLON", "COLON", 
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
            actions[24] = self.EQCOM_action 
            actions[25] = self.DIFFCOM_action 
            actions[26] = self.LESSCOM_action 
            actions[27] = self.LEQCOM_action 
            actions[28] = self.GRECOM_action 
            actions[29] = self.GEQCOM_action 
            actions[30] = self.AND_action 
            actions[31] = self.OR_action 
            actions[32] = self.NOT_action 
            actions[33] = self.ADDASSIGN_action 
            actions[34] = self.SUBASSIGN_action 
            actions[35] = self.MULASSIGN_action 
            actions[36] = self.DIVASSIGN_action 
            actions[37] = self.MODASSIGN_action 
            actions[38] = self.ASSIGN_action 
            actions[39] = self.DOT_action 
            actions[40] = self.EQUAL_action 
            actions[41] = self.ADD_action 
            actions[42] = self.SUB_action 
            actions[43] = self.MUL_action 
            actions[44] = self.DIV_action 
            actions[45] = self.MOD_action 
            actions[46] = self.LP_action 
            actions[47] = self.RP_action 
            actions[48] = self.LSB_action 
            actions[49] = self.RSB_action 
            actions[50] = self.LCB_action 
            actions[51] = self.RCB_action 
            actions[52] = self.COMMA_action 
            actions[53] = self.SEMICOLON_action 
            actions[54] = self.COLON_action 
            actions[56] = self.FLOAT_action 
            actions[61] = self.INTEGER_action 
            actions[64] = self.STRING_action 
            actions[65] = self.ID_action 
            actions[66] = self.ERROR_CHAR_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
            actions[68] = self.UNCLOSE_STRING_action 
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
     

    def EQCOM_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 21:
            self.lastTokenType = 'EQCOM'
     

    def DIFFCOM_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 22:
            self.lastTokenType = 'DIFFCOM'
     

    def LESSCOM_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 23:
            self.lastTokenType = 'LESSCOM'
     

    def LEQCOM_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 24:
            self.lastTokenType = 'LEQCOM'
     

    def GRECOM_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 25:
            self.lastTokenType = 'GRECOM'
     

    def GEQCOM_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 26:
            self.lastTokenType = 'GEQCOM'
     

    def AND_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 27:
            self.lastTokenType = 'AND'
     

    def OR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 28:
            self.lastTokenType = 'OR'
     

    def NOT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 29:
            self.lastTokenType = 'NOT'
     

    def ADDASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 30:
            self.lastTokenType = 'ADDASSIGN'
     

    def SUBASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 31:
            self.lastTokenType = 'SUBASSIGN'
     

    def MULASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 32:
            self.lastTokenType = 'MULASSIGN'
     

    def DIVASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 33:
            self.lastTokenType = 'DIVASSIGN'
     

    def MODASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 34:
            self.lastTokenType = 'MODASSIGN'
     

    def ASSIGN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 35:
            self.lastTokenType = 'ASSIGN'
     

    def DOT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 36:
            self.lastTokenType = 'DOT'
     

    def EQUAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 37:
            self.lastTokenType = 'EQUAL'
     

    def ADD_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 38:
            self.lastTokenType = 'ADD'
     

    def SUB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 39:
            self.lastTokenType = 'SUB'
     

    def MUL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 40:
            self.lastTokenType = 'MUL'
     

    def DIV_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 41:
            self.lastTokenType = 'DIV'
     

    def MOD_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 42:
            self.lastTokenType = 'MOD'
     

    def LP_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 43:
            self.lastTokenType = 'LP'
     

    def RP_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 44:
            self.lastTokenType = 'RP'
     

    def LSB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 45:
            self.lastTokenType = 'LSB'
     

    def RSB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 46:
            self.lastTokenType = 'RSB'
     

    def LCB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 47:
            self.lastTokenType = 'LCB'
     

    def RCB_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 48:
            self.lastTokenType = 'RCB'
     

    def COMMA_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 49:
            self.lastTokenType = 'COMMA'
     

    def SEMICOLON_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 50:
            self.lastTokenType = 'SEMICOLON'
     

    def COLON_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 51:
            self.lastTokenType = 'COLON'
     

    def FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 52:
            self.lastTokenType = 'FLOAT'
     

    def INTEGER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 53:
            self.lastTokenType = 'INTEGER'
     

    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 54:
            self.lastTokenType = 'STRING'
     

    def ID_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 55:
            self.lastTokenType = 'ID'
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 56:
            self.lastTokenType = 'ERROR_CHAR'
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 57:
            self.lastTokenType = 'ILLEGAL_ESCAPE'
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 58:
            self.text = self.text.replace('\r','\n').split('\n')[0]
     

        if actionIndex == 59:
            self.lastTokenType = 'UNCLOSE_STRING'
     


