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
        4,1,62,568,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,65,
        2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,3,1,150,8,1,1,2,1,2,1,2,1,2,1,2,3,2,157,8,2,1,2,1,
        2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,170,8,3,1,3,1,3,1,4,1,
        4,1,4,1,4,1,4,1,4,5,4,180,8,4,10,4,12,4,183,9,4,1,5,1,5,1,5,1,5,
        1,5,1,5,5,5,191,8,5,10,5,12,5,194,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,5,6,203,8,6,10,6,12,6,206,9,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,5,7,217,8,7,10,7,12,7,220,9,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,5,8,234,8,8,10,8,12,8,237,9,8,1,9,1,9,1,9,1,9,
        1,9,3,9,244,8,9,1,10,1,10,1,10,1,10,1,10,5,10,251,8,10,10,10,12,
        10,254,9,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,262,8,11,1,12,1,12,
        1,12,3,12,267,8,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,
        1,15,1,15,1,16,1,16,3,16,282,8,16,1,17,1,17,1,17,1,17,1,17,3,17,
        289,8,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,298,8,18,1,19,1,
        19,3,19,302,8,19,1,20,1,20,1,20,3,20,307,8,20,1,20,1,20,1,20,1,21,
        1,21,1,21,1,21,1,22,1,22,1,22,3,22,319,8,22,1,22,1,22,1,22,1,23,
        1,23,3,23,326,8,23,1,23,1,23,1,23,3,23,331,8,23,1,23,1,23,1,24,1,
        24,1,24,1,24,1,25,1,25,3,25,341,8,25,1,26,1,26,1,26,1,26,1,26,3,
        26,348,8,26,1,27,1,27,1,27,1,28,1,28,1,28,1,28,3,28,357,8,28,1,29,
        1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,
        1,32,1,32,1,32,1,32,3,32,377,8,32,1,33,1,33,1,33,1,33,1,34,1,34,
        1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,3,36,396,
        8,36,1,37,1,37,1,37,3,37,401,8,37,1,37,1,37,1,38,1,38,1,38,1,38,
        1,39,1,39,1,39,3,39,412,8,39,1,40,1,40,1,40,1,40,3,40,418,8,40,1,
        41,1,41,1,41,1,41,1,41,3,41,425,8,41,1,42,1,42,1,42,1,42,3,42,431,
        8,42,1,43,1,43,1,43,1,44,1,44,1,44,1,44,1,45,1,45,1,45,1,45,1,45,
        1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,
        1,45,1,45,1,45,3,45,461,8,45,1,46,1,46,3,46,465,8,46,1,47,1,47,1,
        48,1,48,1,49,1,49,1,49,1,50,1,50,3,50,476,8,50,1,51,1,51,3,51,480,
        8,51,1,52,1,52,1,52,1,52,1,53,1,53,1,53,1,53,3,53,490,8,53,1,54,
        1,54,1,54,1,54,1,55,1,55,1,55,1,55,3,55,500,8,55,1,56,1,56,1,56,
        1,56,1,57,1,57,1,57,1,57,1,58,1,58,1,58,1,58,1,58,3,58,515,8,58,
        1,59,1,59,3,59,519,8,59,1,60,1,60,1,60,1,60,1,60,1,61,1,61,3,61,
        528,8,61,1,62,1,62,1,62,1,62,1,62,3,62,535,8,62,1,63,1,63,1,63,1,
        63,1,64,3,64,542,8,64,1,64,1,64,1,65,1,65,3,65,548,8,65,1,66,1,66,
        1,67,1,67,1,67,1,67,1,67,1,67,1,67,1,67,3,67,560,8,67,1,68,1,68,
        1,69,1,69,1,70,1,70,1,70,0,6,8,10,12,14,16,20,71,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,
        102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,
        134,136,138,140,0,4,1,0,13,16,1,0,34,38,1,0,25,30,1,1,54,54,563,
        0,142,1,0,0,0,2,149,1,0,0,0,4,156,1,0,0,0,6,169,1,0,0,0,8,173,1,
        0,0,0,10,184,1,0,0,0,12,195,1,0,0,0,14,207,1,0,0,0,16,221,1,0,0,
        0,18,243,1,0,0,0,20,245,1,0,0,0,22,261,1,0,0,0,24,266,1,0,0,0,26,
        268,1,0,0,0,28,271,1,0,0,0,30,275,1,0,0,0,32,281,1,0,0,0,34,288,
        1,0,0,0,36,297,1,0,0,0,38,301,1,0,0,0,40,303,1,0,0,0,42,311,1,0,
        0,0,44,315,1,0,0,0,46,323,1,0,0,0,48,334,1,0,0,0,50,340,1,0,0,0,
        52,347,1,0,0,0,54,349,1,0,0,0,56,356,1,0,0,0,58,358,1,0,0,0,60,363,
        1,0,0,0,62,368,1,0,0,0,64,376,1,0,0,0,66,378,1,0,0,0,68,382,1,0,
        0,0,70,387,1,0,0,0,72,395,1,0,0,0,74,397,1,0,0,0,76,404,1,0,0,0,
        78,408,1,0,0,0,80,413,1,0,0,0,82,419,1,0,0,0,84,430,1,0,0,0,86,432,
        1,0,0,0,88,435,1,0,0,0,90,460,1,0,0,0,92,464,1,0,0,0,94,466,1,0,
        0,0,96,468,1,0,0,0,98,470,1,0,0,0,100,473,1,0,0,0,102,479,1,0,0,
        0,104,481,1,0,0,0,106,489,1,0,0,0,108,491,1,0,0,0,110,499,1,0,0,
        0,112,501,1,0,0,0,114,505,1,0,0,0,116,514,1,0,0,0,118,518,1,0,0,
        0,120,520,1,0,0,0,122,527,1,0,0,0,124,534,1,0,0,0,126,536,1,0,0,
        0,128,541,1,0,0,0,130,547,1,0,0,0,132,549,1,0,0,0,134,559,1,0,0,
        0,136,561,1,0,0,0,138,563,1,0,0,0,140,565,1,0,0,0,142,143,3,2,1,
        0,143,144,5,0,0,1,144,1,1,0,0,0,145,146,3,4,2,0,146,147,3,2,1,0,
        147,150,1,0,0,0,148,150,3,4,2,0,149,145,1,0,0,0,149,148,1,0,0,0,
        150,3,1,0,0,0,151,157,3,38,19,0,152,157,3,44,22,0,153,157,3,46,23,
        0,154,157,3,60,30,0,155,157,3,68,34,0,156,151,1,0,0,0,156,152,1,
        0,0,0,156,153,1,0,0,0,156,154,1,0,0,0,156,155,1,0,0,0,157,158,1,
        0,0,0,158,159,3,140,70,0,159,5,1,0,0,0,160,170,3,38,19,0,161,170,
        3,44,22,0,162,170,3,76,38,0,163,170,3,78,39,0,164,170,3,90,45,0,
        165,170,3,94,47,0,166,170,3,96,48,0,167,170,3,98,49,0,168,170,3,
        100,50,0,169,160,1,0,0,0,169,161,1,0,0,0,169,162,1,0,0,0,169,163,
        1,0,0,0,169,164,1,0,0,0,169,165,1,0,0,0,169,166,1,0,0,0,169,167,
        1,0,0,0,169,168,1,0,0,0,170,171,1,0,0,0,171,172,3,140,70,0,172,7,
        1,0,0,0,173,174,6,4,-1,0,174,175,3,10,5,0,175,181,1,0,0,0,176,177,
        10,2,0,0,177,178,5,32,0,0,178,180,3,10,5,0,179,176,1,0,0,0,180,183,
        1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,9,1,0,0,0,183,181,1,
        0,0,0,184,185,6,5,-1,0,185,186,3,12,6,0,186,192,1,0,0,0,187,188,
        10,2,0,0,188,189,5,31,0,0,189,191,3,12,6,0,190,187,1,0,0,0,191,194,
        1,0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,11,1,0,0,0,194,192,1,
        0,0,0,195,196,6,6,-1,0,196,197,3,14,7,0,197,204,1,0,0,0,198,199,
        10,2,0,0,199,200,3,138,69,0,200,201,3,14,7,0,201,203,1,0,0,0,202,
        198,1,0,0,0,203,206,1,0,0,0,204,202,1,0,0,0,204,205,1,0,0,0,205,
        13,1,0,0,0,206,204,1,0,0,0,207,208,6,7,-1,0,208,209,3,16,8,0,209,
        218,1,0,0,0,210,211,10,3,0,0,211,212,5,42,0,0,212,217,3,16,8,0,213,
        214,10,2,0,0,214,215,5,43,0,0,215,217,3,16,8,0,216,210,1,0,0,0,216,
        213,1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,
        15,1,0,0,0,220,218,1,0,0,0,221,222,6,8,-1,0,222,223,3,18,9,0,223,
        235,1,0,0,0,224,225,10,4,0,0,225,226,5,44,0,0,226,234,3,18,9,0,227,
        228,10,3,0,0,228,229,5,45,0,0,229,234,3,18,9,0,230,231,10,2,0,0,
        231,232,5,46,0,0,232,234,3,18,9,0,233,224,1,0,0,0,233,227,1,0,0,
        0,233,230,1,0,0,0,234,237,1,0,0,0,235,233,1,0,0,0,235,236,1,0,0,
        0,236,17,1,0,0,0,237,235,1,0,0,0,238,239,5,33,0,0,239,244,3,18,9,
        0,240,241,5,43,0,0,241,244,3,18,9,0,242,244,3,20,10,0,243,238,1,
        0,0,0,243,240,1,0,0,0,243,242,1,0,0,0,244,19,1,0,0,0,245,246,6,10,
        -1,0,246,247,3,22,11,0,247,252,1,0,0,0,248,249,10,2,0,0,249,251,
        3,24,12,0,250,248,1,0,0,0,251,254,1,0,0,0,252,250,1,0,0,0,252,253,
        1,0,0,0,253,21,1,0,0,0,254,252,1,0,0,0,255,256,5,47,0,0,256,257,
        3,8,4,0,257,258,5,48,0,0,258,262,1,0,0,0,259,262,3,134,67,0,260,
        262,5,59,0,0,261,255,1,0,0,0,261,259,1,0,0,0,261,260,1,0,0,0,262,
        23,1,0,0,0,263,267,3,26,13,0,264,267,3,28,14,0,265,267,3,30,15,0,
        266,263,1,0,0,0,266,264,1,0,0,0,266,265,1,0,0,0,267,25,1,0,0,0,268,
        269,5,40,0,0,269,270,5,59,0,0,270,27,1,0,0,0,271,272,5,49,0,0,272,
        273,3,8,4,0,273,274,5,50,0,0,274,29,1,0,0,0,275,276,5,47,0,0,276,
        277,3,32,16,0,277,278,5,48,0,0,278,31,1,0,0,0,279,282,3,34,17,0,
        280,282,1,0,0,0,281,279,1,0,0,0,281,280,1,0,0,0,282,33,1,0,0,0,283,
        284,3,8,4,0,284,285,5,53,0,0,285,286,3,34,17,0,286,289,1,0,0,0,287,
        289,3,8,4,0,288,283,1,0,0,0,288,287,1,0,0,0,289,35,1,0,0,0,290,291,
        3,20,10,0,291,292,3,26,13,0,292,298,1,0,0,0,293,294,3,20,10,0,294,
        295,3,28,14,0,295,298,1,0,0,0,296,298,5,59,0,0,297,290,1,0,0,0,297,
        293,1,0,0,0,297,296,1,0,0,0,298,37,1,0,0,0,299,302,3,40,20,0,300,
        302,3,42,21,0,301,299,1,0,0,0,301,300,1,0,0,0,302,39,1,0,0,0,303,
        304,5,18,0,0,304,306,5,59,0,0,305,307,3,128,64,0,306,305,1,0,0,0,
        306,307,1,0,0,0,307,308,1,0,0,0,308,309,5,41,0,0,309,310,3,8,4,0,
        310,41,1,0,0,0,311,312,5,18,0,0,312,313,5,59,0,0,313,314,3,128,64,
        0,314,43,1,0,0,0,315,316,5,17,0,0,316,318,5,59,0,0,317,319,3,128,
        64,0,318,317,1,0,0,0,318,319,1,0,0,0,319,320,1,0,0,0,320,321,5,41,
        0,0,321,322,3,8,4,0,322,45,1,0,0,0,323,325,5,9,0,0,324,326,3,58,
        29,0,325,324,1,0,0,0,325,326,1,0,0,0,326,327,1,0,0,0,327,328,5,59,
        0,0,328,330,3,48,24,0,329,331,3,128,64,0,330,329,1,0,0,0,330,331,
        1,0,0,0,331,332,1,0,0,0,332,333,3,104,52,0,333,47,1,0,0,0,334,335,
        5,47,0,0,335,336,3,50,25,0,336,337,5,48,0,0,337,49,1,0,0,0,338,341,
        3,52,26,0,339,341,1,0,0,0,340,338,1,0,0,0,340,339,1,0,0,0,341,51,
        1,0,0,0,342,343,3,54,27,0,343,344,5,53,0,0,344,345,3,52,26,0,345,
        348,1,0,0,0,346,348,3,54,27,0,347,342,1,0,0,0,347,346,1,0,0,0,348,
        53,1,0,0,0,349,350,3,56,28,0,350,351,3,128,64,0,351,55,1,0,0,0,352,
        353,5,59,0,0,353,354,5,53,0,0,354,357,3,56,28,0,355,357,5,59,0,0,
        356,352,1,0,0,0,356,355,1,0,0,0,357,57,1,0,0,0,358,359,5,47,0,0,
        359,360,5,59,0,0,360,361,5,59,0,0,361,362,5,48,0,0,362,59,1,0,0,
        0,363,364,5,10,0,0,364,365,5,59,0,0,365,366,5,11,0,0,366,367,3,62,
        31,0,367,61,1,0,0,0,368,369,5,51,0,0,369,370,3,64,32,0,370,371,5,
        52,0,0,371,63,1,0,0,0,372,373,3,66,33,0,373,374,3,64,32,0,374,377,
        1,0,0,0,375,377,3,66,33,0,376,372,1,0,0,0,376,375,1,0,0,0,377,65,
        1,0,0,0,378,379,5,59,0,0,379,380,3,128,64,0,380,381,3,140,70,0,381,
        67,1,0,0,0,382,383,5,10,0,0,383,384,5,59,0,0,384,385,5,12,0,0,385,
        386,3,70,35,0,386,69,1,0,0,0,387,388,5,51,0,0,388,389,3,72,36,0,
        389,390,5,52,0,0,390,71,1,0,0,0,391,392,3,74,37,0,392,393,3,72,36,
        0,393,396,1,0,0,0,394,396,3,74,37,0,395,391,1,0,0,0,395,394,1,0,
        0,0,396,73,1,0,0,0,397,398,5,59,0,0,398,400,3,48,24,0,399,401,3,
        128,64,0,400,399,1,0,0,0,400,401,1,0,0,0,401,402,1,0,0,0,402,403,
        3,140,70,0,403,75,1,0,0,0,404,405,3,36,18,0,405,406,3,102,51,0,406,
        407,3,8,4,0,407,77,1,0,0,0,408,409,3,80,40,0,409,411,3,84,42,0,410,
        412,3,86,43,0,411,410,1,0,0,0,411,412,1,0,0,0,412,79,1,0,0,0,413,
        414,5,5,0,0,414,415,3,88,44,0,415,417,3,104,52,0,416,418,3,140,70,
        0,417,416,1,0,0,0,417,418,1,0,0,0,418,81,1,0,0,0,419,420,5,6,0,0,
        420,421,5,5,0,0,421,422,3,88,44,0,422,424,3,104,52,0,423,425,3,140,
        70,0,424,423,1,0,0,0,424,425,1,0,0,0,425,83,1,0,0,0,426,427,3,82,
        41,0,427,428,3,84,42,0,428,431,1,0,0,0,429,431,1,0,0,0,430,426,1,
        0,0,0,430,429,1,0,0,0,431,85,1,0,0,0,432,433,5,6,0,0,433,434,3,104,
        52,0,434,87,1,0,0,0,435,436,5,47,0,0,436,437,3,8,4,0,437,438,5,48,
        0,0,438,89,1,0,0,0,439,440,5,7,0,0,440,441,3,8,4,0,441,442,3,104,
        52,0,442,461,1,0,0,0,443,444,5,7,0,0,444,445,3,92,46,0,445,446,5,
        54,0,0,446,447,3,8,4,0,447,448,5,54,0,0,448,449,3,76,38,0,449,450,
        3,104,52,0,450,461,1,0,0,0,451,452,5,7,0,0,452,453,5,59,0,0,453,
        454,5,53,0,0,454,455,5,59,0,0,455,456,5,39,0,0,456,457,5,21,0,0,
        457,458,3,8,4,0,458,459,3,104,52,0,459,461,1,0,0,0,460,439,1,0,0,
        0,460,443,1,0,0,0,460,451,1,0,0,0,461,91,1,0,0,0,462,465,3,40,20,
        0,463,465,3,76,38,0,464,462,1,0,0,0,464,463,1,0,0,0,465,93,1,0,0,
        0,466,467,5,20,0,0,467,95,1,0,0,0,468,469,5,19,0,0,469,97,1,0,0,
        0,470,471,3,20,10,0,471,472,3,30,15,0,472,99,1,0,0,0,473,475,5,8,
        0,0,474,476,3,8,4,0,475,474,1,0,0,0,475,476,1,0,0,0,476,101,1,0,
        0,0,477,480,3,136,68,0,478,480,5,39,0,0,479,477,1,0,0,0,479,478,
        1,0,0,0,480,103,1,0,0,0,481,482,5,51,0,0,482,483,3,106,53,0,483,
        484,5,52,0,0,484,105,1,0,0,0,485,486,3,6,3,0,486,487,3,106,53,0,
        487,490,1,0,0,0,488,490,3,6,3,0,489,485,1,0,0,0,489,488,1,0,0,0,
        490,107,1,0,0,0,491,492,3,110,55,0,492,493,3,130,65,0,493,494,3,
        114,57,0,494,109,1,0,0,0,495,496,3,112,56,0,496,497,3,110,55,0,497,
        500,1,0,0,0,498,500,3,112,56,0,499,495,1,0,0,0,499,498,1,0,0,0,500,
        111,1,0,0,0,501,502,5,49,0,0,502,503,3,8,4,0,503,504,5,50,0,0,504,
        113,1,0,0,0,505,506,5,51,0,0,506,507,3,116,58,0,507,508,5,52,0,0,
        508,115,1,0,0,0,509,510,3,118,59,0,510,511,5,53,0,0,511,512,3,116,
        58,0,512,515,1,0,0,0,513,515,3,118,59,0,514,509,1,0,0,0,514,513,
        1,0,0,0,515,117,1,0,0,0,516,519,3,8,4,0,517,519,3,114,57,0,518,516,
        1,0,0,0,518,517,1,0,0,0,519,119,1,0,0,0,520,521,5,59,0,0,521,522,
        5,51,0,0,522,523,3,122,61,0,523,524,5,52,0,0,524,121,1,0,0,0,525,
        528,3,124,62,0,526,528,1,0,0,0,527,525,1,0,0,0,527,526,1,0,0,0,528,
        123,1,0,0,0,529,530,3,126,63,0,530,531,5,53,0,0,531,532,3,124,62,
        0,532,535,1,0,0,0,533,535,3,126,63,0,534,529,1,0,0,0,534,533,1,0,
        0,0,535,125,1,0,0,0,536,537,5,59,0,0,537,538,5,55,0,0,538,539,3,
        8,4,0,539,127,1,0,0,0,540,542,3,110,55,0,541,540,1,0,0,0,541,542,
        1,0,0,0,542,543,1,0,0,0,543,544,3,130,65,0,544,129,1,0,0,0,545,548,
        3,132,66,0,546,548,5,59,0,0,547,545,1,0,0,0,547,546,1,0,0,0,548,
        131,1,0,0,0,549,550,7,0,0,0,550,133,1,0,0,0,551,560,5,57,0,0,552,
        560,5,56,0,0,553,560,5,58,0,0,554,560,5,23,0,0,555,560,5,24,0,0,
        556,560,5,22,0,0,557,560,3,120,60,0,558,560,3,108,54,0,559,551,1,
        0,0,0,559,552,1,0,0,0,559,553,1,0,0,0,559,554,1,0,0,0,559,555,1,
        0,0,0,559,556,1,0,0,0,559,557,1,0,0,0,559,558,1,0,0,0,560,135,1,
        0,0,0,561,562,7,1,0,0,562,137,1,0,0,0,563,564,7,2,0,0,564,139,1,
        0,0,0,565,566,7,3,0,0,566,141,1,0,0,0,45,149,156,169,181,192,204,
        216,218,233,235,243,252,261,266,281,288,297,301,306,318,325,330,
        340,347,356,376,395,400,411,417,424,430,460,464,475,479,489,499,
        514,518,527,534,541,547,559
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
    RULE_break_stmt = 47
    RULE_continue_stmt = 48
    RULE_funccall_stmt = 49
    RULE_return_stmt = 50
    RULE_assign = 51
    RULE_blockcode = 52
    RULE_stmt_nnlst = 53
    RULE_arr_literal = 54
    RULE_arridx_lst = 55
    RULE_arridx = 56
    RULE_arrvalue = 57
    RULE_arrelem_lst = 58
    RULE_arrelem = 59
    RULE_struct_literal = 60
    RULE_structparam_lst = 61
    RULE_structparam_lstprime = 62
    RULE_structparam = 63
    RULE_data_type = 64
    RULE_prime_datatype = 65
    RULE_primitive_datatype = 66
    RULE_literal = 67
    RULE_uptassign = 68
    RULE_compare_op = 69
    RULE_end_stm = 70

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
                   "forloop_stmt", "forloop_init", "break_stmt", "continue_stmt", 
                   "funccall_stmt", "return_stmt", "assign", "blockcode", 
                   "stmt_nnlst", "arr_literal", "arridx_lst", "arridx", 
                   "arrvalue", "arrelem_lst", "arrelem", "struct_literal", 
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
            self.state = 142
            self.decl_lst()
            self.state = 143
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
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.decl()
                self.state = 146
                self.decl_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
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
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 151
                self.var_decl()
                pass

            elif la_ == 2:
                self.state = 152
                self.const_decl()
                pass

            elif la_ == 3:
                self.state = 153
                self.func_decl()
                pass

            elif la_ == 4:
                self.state = 154
                self.struct_decl()
                pass

            elif la_ == 5:
                self.state = 155
                self.interface_decl()
                pass


            self.state = 158
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
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 160
                self.var_decl()
                pass

            elif la_ == 2:
                self.state = 161
                self.const_decl()
                pass

            elif la_ == 3:
                self.state = 162
                self.assigning_stmt()
                pass

            elif la_ == 4:
                self.state = 163
                self.ifelse_stmt()
                pass

            elif la_ == 5:
                self.state = 164
                self.forloop_stmt()
                pass

            elif la_ == 6:
                self.state = 165
                self.break_stmt()
                pass

            elif la_ == 7:
                self.state = 166
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.state = 167
                self.funccall_stmt()
                pass

            elif la_ == 9:
                self.state = 168
                self.return_stmt()
                pass


            self.state = 171
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
            self.state = 174
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 176
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 177
                    self.match(MiniGoParser.OR)
                    self.state = 178
                    self.expr1(0) 
                self.state = 183
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
            self.state = 185
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 192
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 187
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 188
                    self.match(MiniGoParser.AND)
                    self.state = 189
                    self.expr2(0) 
                self.state = 194
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
            self.state = 196
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 204
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 198
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 199
                    self.compare_op()
                    self.state = 200
                    self.expr3(0) 
                self.state = 206
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
            self.state = 208
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 218
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 216
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 210
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 211
                        self.match(MiniGoParser.ADD)
                        self.state = 212
                        self.expr4(0)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                        self.state = 213
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 214
                        self.match(MiniGoParser.SUB)
                        self.state = 215
                        self.expr4(0)
                        pass

             
                self.state = 220
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
            self.state = 222
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 233
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 224
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 225
                        self.match(MiniGoParser.MUL)
                        self.state = 226
                        self.expr5()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 227
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 228
                        self.match(MiniGoParser.DIV)
                        self.state = 229
                        self.expr5()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                        self.state = 230
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 231
                        self.match(MiniGoParser.MOD)
                        self.state = 232
                        self.expr5()
                        pass

             
                self.state = 237
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
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(MiniGoParser.NOT)
                self.state = 239
                self.expr5()
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.match(MiniGoParser.SUB)
                self.state = 241
                self.expr5()
                pass
            elif token in [22, 23, 24, 47, 49, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
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
            self.state = 246
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 252
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 248
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 249
                    self.tail() 
                self.state = 254
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
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(MiniGoParser.LP)
                self.state = 256
                self.expr(0)
                self.state = 257
                self.match(MiniGoParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 260
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
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.field_access_tail()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.arr_elem_access()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 3)
                self.state = 265
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
            self.state = 268
            self.match(MiniGoParser.DOT)
            self.state = 269
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
            self.state = 271
            self.match(MiniGoParser.LSB)
            self.state = 272
            self.expr(0)
            self.state = 273
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
            self.state = 275
            self.match(MiniGoParser.LP)
            self.state = 276
            self.expr_lst()
            self.state = 277
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
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23, 24, 33, 43, 47, 49, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
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
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.expr(0)
                self.state = 284
                self.match(MiniGoParser.COMMA)
                self.state = 285
                self.expr_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
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
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.expr6(0)
                self.state = 291
                self.field_access_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.expr6(0)
                self.state = 294
                self.arr_elem_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 296
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
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.withInit_var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
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
            self.state = 303
            self.match(MiniGoParser.VAR_)
            self.state = 304
            self.match(MiniGoParser.ID)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 577023702256967680) != 0):
                self.state = 305
                self.data_type()


            self.state = 308
            self.match(MiniGoParser.EQUAL)
            self.state = 309
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
            self.state = 311
            self.match(MiniGoParser.VAR_)
            self.state = 312
            self.match(MiniGoParser.ID)
            self.state = 313
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
            self.state = 315
            self.match(MiniGoParser.CONST_)
            self.state = 316
            self.match(MiniGoParser.ID)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 577023702256967680) != 0):
                self.state = 317
                self.data_type()


            self.state = 320
            self.match(MiniGoParser.EQUAL)
            self.state = 321
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
            self.state = 323
            self.match(MiniGoParser.FUNC_)
            self.state = 325
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 324
                self.receiver()


            self.state = 327
            self.match(MiniGoParser.ID)
            self.state = 328
            self.funcparam()
            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 577023702256967680) != 0):
                self.state = 329
                self.data_type()


            self.state = 332
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
            self.state = 334
            self.match(MiniGoParser.LP)
            self.state = 335
            self.param_lst()
            self.state = 336
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
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
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
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.param()
                self.state = 343
                self.match(MiniGoParser.COMMA)
                self.state = 344
                self.param_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
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
            self.state = 349
            self.id_nnlst()
            self.state = 350
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
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.match(MiniGoParser.ID)
                self.state = 353
                self.match(MiniGoParser.COMMA)
                self.state = 354
                self.id_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
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
            self.state = 358
            self.match(MiniGoParser.LP)
            self.state = 359
            self.match(MiniGoParser.ID)
            self.state = 360
            self.match(MiniGoParser.ID)
            self.state = 361
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
            self.state = 363
            self.match(MiniGoParser.TYPE_)
            self.state = 364
            self.match(MiniGoParser.ID)
            self.state = 365
            self.match(MiniGoParser.STRUCT_)
            self.state = 366
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
            self.state = 368
            self.match(MiniGoParser.LCB)
            self.state = 369
            self.fielddecl_nnlst()
            self.state = 370
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
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.fielddecl()
                self.state = 373
                self.fielddecl_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
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
            self.state = 378
            self.match(MiniGoParser.ID)
            self.state = 379
            self.data_type()
            self.state = 380
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
            self.state = 382
            self.match(MiniGoParser.TYPE_)
            self.state = 383
            self.match(MiniGoParser.ID)
            self.state = 384
            self.match(MiniGoParser.INTERFACE_)
            self.state = 385
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
            self.state = 387
            self.match(MiniGoParser.LCB)
            self.state = 388
            self.interfacemeth_nnlst()
            self.state = 389
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
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.interfacemethmem()
                self.state = 392
                self.interfacemeth_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
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
            self.state = 397
            self.match(MiniGoParser.ID)
            self.state = 398
            self.funcparam()
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 577023702256967680) != 0):
                self.state = 399
                self.data_type()


            self.state = 402
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
            self.state = 404
            self.lhs()
            self.state = 405
            self.assign()
            self.state = 406
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
            self.state = 408
            self.if_()
            self.state = 409
            self.elseif_lst()
            self.state = 411
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 410
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
            self.state = 413
            self.match(MiniGoParser.IF_)
            self.state = 414
            self.condition()
            self.state = 415
            self.blockcode()
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 416
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
            self.state = 419
            self.match(MiniGoParser.ELSE_)
            self.state = 420
            self.match(MiniGoParser.IF_)
            self.state = 421
            self.condition()
            self.state = 422
            self.blockcode()
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 423
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
            self.state = 430
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.elseif_()
                self.state = 427
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
            self.state = 432
            self.match(MiniGoParser.ELSE_)
            self.state = 433
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
            self.state = 435
            self.match(MiniGoParser.LP)
            self.state = 436
            self.expr(0)
            self.state = 437
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
            self.state = 460
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                localctx = MiniGoParser.ForBasicContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.match(MiniGoParser.FOR_)
                self.state = 440
                self.expr(0)
                self.state = 441
                self.blockcode()
                pass

            elif la_ == 2:
                localctx = MiniGoParser.ForStepContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 443
                self.match(MiniGoParser.FOR_)
                self.state = 444
                self.forloop_init()
                self.state = 445
                self.match(MiniGoParser.SEMICOLON)
                self.state = 446
                self.expr(0)
                self.state = 447
                self.match(MiniGoParser.SEMICOLON)
                self.state = 448
                self.assigning_stmt()
                self.state = 449
                self.blockcode()
                pass

            elif la_ == 3:
                localctx = MiniGoParser.ForEachContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 451
                self.match(MiniGoParser.FOR_)
                self.state = 452
                self.match(MiniGoParser.ID)
                self.state = 453
                self.match(MiniGoParser.COMMA)
                self.state = 454
                self.match(MiniGoParser.ID)
                self.state = 455
                self.match(MiniGoParser.ASSIGN)
                self.state = 456
                self.match(MiniGoParser.RANGE_)
                self.state = 457
                self.expr(0)
                self.state = 458
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
            self.state = 464
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.withInit_var_decl()
                pass
            elif token in [22, 23, 24, 47, 49, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
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
            self.state = 466
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
            self.state = 468
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
        self.enterRule(localctx, 98, self.RULE_funccall_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.expr6(0)
            self.state = 471
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
        self.enterRule(localctx, 100, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(MiniGoParser.RETURN_)
            self.state = 475
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1081576402723012608) != 0):
                self.state = 474
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

        def uptassign(self):
            return self.getTypedRuleContext(MiniGoParser.UptassignContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign




    def assign(self):

        localctx = MiniGoParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_assign)
        try:
            self.state = 479
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34, 35, 36, 37, 38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.uptassign()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
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
        self.enterRule(localctx, 104, self.RULE_blockcode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.match(MiniGoParser.LCB)
            self.state = 482
            self.stmt_nnlst()
            self.state = 483
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
            self.state = 489
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.stmt()
                self.state = 486
                self.stmt_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 488
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
        self.enterRule(localctx, 108, self.RULE_arr_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.arridx_lst()
            self.state = 492
            self.prime_datatype()
            self.state = 493
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
        self.enterRule(localctx, 110, self.RULE_arridx_lst)
        try:
            self.state = 499
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.arridx()
                self.state = 496
                self.arridx_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 498
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
        self.enterRule(localctx, 112, self.RULE_arridx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(MiniGoParser.LSB)
            self.state = 502
            self.expr(0)
            self.state = 503
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
        self.enterRule(localctx, 114, self.RULE_arrvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(MiniGoParser.LCB)
            self.state = 506
            self.arrelem_lst()
            self.state = 507
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
        self.enterRule(localctx, 116, self.RULE_arrelem_lst)
        try:
            self.state = 514
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.arrelem()
                self.state = 510
                self.match(MiniGoParser.COMMA)
                self.state = 511
                self.arrelem_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 513
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
        self.enterRule(localctx, 118, self.RULE_arrelem)
        try:
            self.state = 518
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23, 24, 33, 43, 47, 49, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                self.expr(0)
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
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
        self.enterRule(localctx, 120, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(MiniGoParser.ID)
            self.state = 521
            self.match(MiniGoParser.LCB)
            self.state = 522
            self.structparam_lst()
            self.state = 523
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
        self.enterRule(localctx, 122, self.RULE_structparam_lst)
        try:
            self.state = 527
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
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
        self.enterRule(localctx, 124, self.RULE_structparam_lstprime)
        try:
            self.state = 534
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 529
                self.structparam()
                self.state = 530
                self.match(MiniGoParser.COMMA)
                self.state = 531
                self.structparam_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 533
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
        self.enterRule(localctx, 126, self.RULE_structparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.match(MiniGoParser.ID)
            self.state = 537
            self.match(MiniGoParser.COLON)
            self.state = 538
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
        self.enterRule(localctx, 128, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 540
                self.arridx_lst()


            self.state = 543
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
        self.enterRule(localctx, 130, self.RULE_prime_datatype)
        try:
            self.state = 547
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 545
                self.primitive_datatype()
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 546
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
        self.enterRule(localctx, 132, self.RULE_primitive_datatype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
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
        self.enterRule(localctx, 134, self.RULE_literal)
        try:
            self.state = 559
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.match(MiniGoParser.INTEGER)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 552
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 3)
                self.state = 553
                self.match(MiniGoParser.STRING)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 554
                self.match(MiniGoParser.TRUE_)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 555
                self.match(MiniGoParser.FALSE_)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 6)
                self.state = 556
                self.match(MiniGoParser.NIL_)
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 7)
                self.state = 557
                self.struct_literal()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 8)
                self.state = 558
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
        self.enterRule(localctx, 136, self.RULE_uptassign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
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
        self.enterRule(localctx, 138, self.RULE_compare_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
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
        self.enterRule(localctx, 140, self.RULE_end_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
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
         




