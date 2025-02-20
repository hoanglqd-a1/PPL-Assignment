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
        4,1,62,611,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
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
        1,1,1,1,1,1,1,3,1,150,8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,158,8,2,1,
        3,1,3,1,3,1,3,1,3,1,3,5,3,166,8,3,10,3,12,3,169,9,3,1,4,1,4,1,4,
        1,4,1,4,1,4,5,4,177,8,4,10,4,12,4,180,9,4,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,5,5,189,8,5,10,5,12,5,192,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,5,6,203,8,6,10,6,12,6,206,9,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,5,7,220,8,7,10,7,12,7,223,9,7,1,8,1,8,1,8,
        1,8,1,8,3,8,230,8,8,1,9,1,9,1,9,1,9,1,9,5,9,237,8,9,10,9,12,9,240,
        9,9,1,10,1,10,1,10,1,10,1,10,1,10,3,10,248,8,10,1,11,1,11,1,11,3,
        11,253,8,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,
        14,1,15,1,15,3,15,268,8,15,1,16,1,16,1,16,1,16,1,16,3,16,275,8,16,
        1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,
        289,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,309,8,19,1,20,1,20,1,20,
        3,20,314,8,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,334,8,21,1,22,1,22,
        1,22,1,22,3,22,340,8,22,1,23,1,23,1,23,1,23,1,24,1,24,3,24,348,8,
        24,1,24,1,24,1,24,3,24,353,8,24,1,24,1,24,1,24,1,25,1,25,1,25,1,
        25,1,26,1,26,3,26,364,8,26,1,27,1,27,1,27,1,27,1,27,3,27,371,8,27,
        1,28,1,28,1,28,1,29,1,29,1,29,1,29,3,29,380,8,29,1,30,1,30,1,30,
        1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,33,
        1,33,1,33,1,33,3,33,401,8,33,1,34,1,34,1,34,1,34,1,35,1,35,1,35,
        1,35,1,35,1,36,1,36,3,36,414,8,36,1,37,1,37,1,37,1,37,1,37,3,37,
        421,8,37,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,39,1,40,
        1,40,1,40,1,40,1,41,1,41,1,41,1,41,3,41,441,8,41,1,42,1,42,1,42,
        3,42,446,8,42,1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,44,
        1,44,3,44,459,8,44,1,45,1,45,1,45,1,45,1,45,3,45,466,8,45,1,46,1,
        46,1,46,1,46,3,46,472,8,46,1,47,1,47,1,47,3,47,477,8,47,1,48,1,48,
        1,48,1,48,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,
        1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,1,49,
        3,49,507,8,49,1,50,1,50,1,50,1,50,1,51,1,51,1,51,1,51,1,52,1,52,
        3,52,519,8,52,1,53,1,53,1,53,1,54,1,54,1,54,1,55,1,55,1,55,1,55,
        1,56,1,56,1,56,1,56,1,56,1,56,3,56,537,8,56,1,57,1,57,3,57,541,8,
        57,1,58,1,58,1,58,1,58,1,59,1,59,1,59,1,59,3,59,551,8,59,1,60,1,
        60,1,60,1,60,1,60,1,60,1,60,1,60,1,60,1,60,3,60,563,8,60,1,61,1,
        61,1,61,1,61,1,62,1,62,1,62,1,62,1,63,1,63,1,63,1,63,1,63,3,63,578,
        8,63,1,64,1,64,3,64,582,8,64,1,65,3,65,585,8,65,1,65,1,65,3,65,589,
        8,65,1,65,3,65,592,8,65,1,66,1,66,1,67,1,67,1,67,1,67,1,67,1,67,
        1,67,3,67,603,8,67,1,68,1,68,1,69,1,69,1,70,1,70,1,70,0,6,6,8,10,
        12,14,18,71,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,
        82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,
        120,122,124,126,128,130,132,134,136,138,140,0,4,1,0,13,16,1,0,34,
        38,1,0,25,30,1,1,54,54,609,0,142,1,0,0,0,2,149,1,0,0,0,4,157,1,0,
        0,0,6,159,1,0,0,0,8,170,1,0,0,0,10,181,1,0,0,0,12,193,1,0,0,0,14,
        207,1,0,0,0,16,229,1,0,0,0,18,231,1,0,0,0,20,247,1,0,0,0,22,252,
        1,0,0,0,24,254,1,0,0,0,26,257,1,0,0,0,28,261,1,0,0,0,30,267,1,0,
        0,0,32,274,1,0,0,0,34,276,1,0,0,0,36,288,1,0,0,0,38,308,1,0,0,0,
        40,310,1,0,0,0,42,333,1,0,0,0,44,339,1,0,0,0,46,341,1,0,0,0,48,345,
        1,0,0,0,50,357,1,0,0,0,52,363,1,0,0,0,54,370,1,0,0,0,56,372,1,0,
        0,0,58,379,1,0,0,0,60,381,1,0,0,0,62,386,1,0,0,0,64,392,1,0,0,0,
        66,400,1,0,0,0,68,402,1,0,0,0,70,406,1,0,0,0,72,413,1,0,0,0,74,420,
        1,0,0,0,76,422,1,0,0,0,78,426,1,0,0,0,80,432,1,0,0,0,82,440,1,0,
        0,0,84,442,1,0,0,0,86,449,1,0,0,0,88,454,1,0,0,0,90,460,1,0,0,0,
        92,471,1,0,0,0,94,476,1,0,0,0,96,478,1,0,0,0,98,506,1,0,0,0,100,
        508,1,0,0,0,102,512,1,0,0,0,104,518,1,0,0,0,106,520,1,0,0,0,108,
        523,1,0,0,0,110,526,1,0,0,0,112,536,1,0,0,0,114,540,1,0,0,0,116,
        542,1,0,0,0,118,550,1,0,0,0,120,562,1,0,0,0,122,564,1,0,0,0,124,
        568,1,0,0,0,126,577,1,0,0,0,128,581,1,0,0,0,130,591,1,0,0,0,132,
        593,1,0,0,0,134,602,1,0,0,0,136,604,1,0,0,0,138,606,1,0,0,0,140,
        608,1,0,0,0,142,143,3,2,1,0,143,144,5,0,0,1,144,1,1,0,0,0,145,146,
        3,4,2,0,146,147,3,2,1,0,147,150,1,0,0,0,148,150,3,4,2,0,149,145,
        1,0,0,0,149,148,1,0,0,0,150,3,1,0,0,0,151,158,3,38,19,0,152,158,
        3,42,21,0,153,158,3,40,20,0,154,158,3,48,24,0,155,158,3,62,31,0,
        156,158,3,78,39,0,157,151,1,0,0,0,157,152,1,0,0,0,157,153,1,0,0,
        0,157,154,1,0,0,0,157,155,1,0,0,0,157,156,1,0,0,0,158,5,1,0,0,0,
        159,160,6,3,-1,0,160,161,3,8,4,0,161,167,1,0,0,0,162,163,10,2,0,
        0,163,164,5,32,0,0,164,166,3,8,4,0,165,162,1,0,0,0,166,169,1,0,0,
        0,167,165,1,0,0,0,167,168,1,0,0,0,168,7,1,0,0,0,169,167,1,0,0,0,
        170,171,6,4,-1,0,171,172,3,10,5,0,172,178,1,0,0,0,173,174,10,2,0,
        0,174,175,5,31,0,0,175,177,3,10,5,0,176,173,1,0,0,0,177,180,1,0,
        0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,9,1,0,0,0,180,178,1,0,0,
        0,181,182,6,5,-1,0,182,183,3,12,6,0,183,190,1,0,0,0,184,185,10,2,
        0,0,185,186,3,138,69,0,186,187,3,12,6,0,187,189,1,0,0,0,188,184,
        1,0,0,0,189,192,1,0,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,11,1,
        0,0,0,192,190,1,0,0,0,193,194,6,6,-1,0,194,195,3,14,7,0,195,204,
        1,0,0,0,196,197,10,3,0,0,197,198,5,42,0,0,198,203,3,14,7,0,199,200,
        10,2,0,0,200,201,5,43,0,0,201,203,3,14,7,0,202,196,1,0,0,0,202,199,
        1,0,0,0,203,206,1,0,0,0,204,202,1,0,0,0,204,205,1,0,0,0,205,13,1,
        0,0,0,206,204,1,0,0,0,207,208,6,7,-1,0,208,209,3,16,8,0,209,221,
        1,0,0,0,210,211,10,4,0,0,211,212,5,44,0,0,212,220,3,16,8,0,213,214,
        10,3,0,0,214,215,5,45,0,0,215,220,3,16,8,0,216,217,10,2,0,0,217,
        218,5,46,0,0,218,220,3,16,8,0,219,210,1,0,0,0,219,213,1,0,0,0,219,
        216,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,221,222,1,0,0,0,222,
        15,1,0,0,0,223,221,1,0,0,0,224,225,5,33,0,0,225,230,3,16,8,0,226,
        227,5,43,0,0,227,230,3,16,8,0,228,230,3,18,9,0,229,224,1,0,0,0,229,
        226,1,0,0,0,229,228,1,0,0,0,230,17,1,0,0,0,231,232,6,9,-1,0,232,
        233,3,20,10,0,233,238,1,0,0,0,234,235,10,2,0,0,235,237,3,22,11,0,
        236,234,1,0,0,0,237,240,1,0,0,0,238,236,1,0,0,0,238,239,1,0,0,0,
        239,19,1,0,0,0,240,238,1,0,0,0,241,242,5,47,0,0,242,243,3,6,3,0,
        243,244,5,48,0,0,244,248,1,0,0,0,245,248,3,134,67,0,246,248,5,59,
        0,0,247,241,1,0,0,0,247,245,1,0,0,0,247,246,1,0,0,0,248,21,1,0,0,
        0,249,253,3,24,12,0,250,253,3,26,13,0,251,253,3,28,14,0,252,249,
        1,0,0,0,252,250,1,0,0,0,252,251,1,0,0,0,253,23,1,0,0,0,254,255,5,
        40,0,0,255,256,5,59,0,0,256,25,1,0,0,0,257,258,5,49,0,0,258,259,
        3,6,3,0,259,260,5,50,0,0,260,27,1,0,0,0,261,262,5,47,0,0,262,263,
        3,30,15,0,263,264,5,48,0,0,264,29,1,0,0,0,265,268,3,32,16,0,266,
        268,1,0,0,0,267,265,1,0,0,0,267,266,1,0,0,0,268,31,1,0,0,0,269,270,
        3,6,3,0,270,271,5,53,0,0,271,272,3,32,16,0,272,275,1,0,0,0,273,275,
        3,6,3,0,274,269,1,0,0,0,274,273,1,0,0,0,275,33,1,0,0,0,276,277,3,
        36,18,0,277,278,3,114,57,0,278,279,3,6,3,0,279,280,3,140,70,0,280,
        35,1,0,0,0,281,282,3,18,9,0,282,283,3,24,12,0,283,289,1,0,0,0,284,
        285,3,18,9,0,285,286,3,26,13,0,286,289,1,0,0,0,287,289,5,59,0,0,
        288,281,1,0,0,0,288,284,1,0,0,0,288,287,1,0,0,0,289,37,1,0,0,0,290,
        291,5,18,0,0,291,292,5,59,0,0,292,293,3,130,65,0,293,294,3,140,70,
        0,294,309,1,0,0,0,295,296,5,18,0,0,296,297,5,59,0,0,297,298,5,41,
        0,0,298,299,3,6,3,0,299,300,3,140,70,0,300,309,1,0,0,0,301,302,5,
        18,0,0,302,303,5,59,0,0,303,304,3,130,65,0,304,305,5,41,0,0,305,
        306,3,6,3,0,306,307,3,140,70,0,307,309,1,0,0,0,308,290,1,0,0,0,308,
        295,1,0,0,0,308,301,1,0,0,0,309,39,1,0,0,0,310,311,5,17,0,0,311,
        313,5,59,0,0,312,314,3,130,65,0,313,312,1,0,0,0,313,314,1,0,0,0,
        314,315,1,0,0,0,315,316,5,41,0,0,316,317,3,6,3,0,317,318,3,140,70,
        0,318,41,1,0,0,0,319,320,5,18,0,0,320,321,5,59,0,0,321,322,3,44,
        22,0,322,323,3,130,65,0,323,324,3,140,70,0,324,334,1,0,0,0,325,326,
        5,18,0,0,326,327,5,59,0,0,327,328,3,44,22,0,328,329,3,130,65,0,329,
        330,5,41,0,0,330,331,3,122,61,0,331,332,3,140,70,0,332,334,1,0,0,
        0,333,319,1,0,0,0,333,325,1,0,0,0,334,43,1,0,0,0,335,336,3,46,23,
        0,336,337,3,44,22,0,337,340,1,0,0,0,338,340,3,46,23,0,339,335,1,
        0,0,0,339,338,1,0,0,0,340,45,1,0,0,0,341,342,5,49,0,0,342,343,3,
        6,3,0,343,344,5,50,0,0,344,47,1,0,0,0,345,347,5,9,0,0,346,348,3,
        60,30,0,347,346,1,0,0,0,347,348,1,0,0,0,348,349,1,0,0,0,349,350,
        5,59,0,0,350,352,3,50,25,0,351,353,3,130,65,0,352,351,1,0,0,0,352,
        353,1,0,0,0,353,354,1,0,0,0,354,355,3,116,58,0,355,356,3,140,70,
        0,356,49,1,0,0,0,357,358,5,47,0,0,358,359,3,52,26,0,359,360,5,48,
        0,0,360,51,1,0,0,0,361,364,3,54,27,0,362,364,1,0,0,0,363,361,1,0,
        0,0,363,362,1,0,0,0,364,53,1,0,0,0,365,366,3,56,28,0,366,367,5,53,
        0,0,367,368,3,54,27,0,368,371,1,0,0,0,369,371,3,56,28,0,370,365,
        1,0,0,0,370,369,1,0,0,0,371,55,1,0,0,0,372,373,3,58,29,0,373,374,
        3,130,65,0,374,57,1,0,0,0,375,376,5,59,0,0,376,377,5,53,0,0,377,
        380,3,58,29,0,378,380,5,59,0,0,379,375,1,0,0,0,379,378,1,0,0,0,380,
        59,1,0,0,0,381,382,5,47,0,0,382,383,5,59,0,0,383,384,5,59,0,0,384,
        385,5,48,0,0,385,61,1,0,0,0,386,387,5,10,0,0,387,388,5,59,0,0,388,
        389,5,11,0,0,389,390,3,64,32,0,390,391,3,140,70,0,391,63,1,0,0,0,
        392,393,5,51,0,0,393,394,3,66,33,0,394,395,5,52,0,0,395,65,1,0,0,
        0,396,397,3,68,34,0,397,398,3,66,33,0,398,401,1,0,0,0,399,401,3,
        68,34,0,400,396,1,0,0,0,400,399,1,0,0,0,401,67,1,0,0,0,402,403,5,
        59,0,0,403,404,3,130,65,0,404,405,3,140,70,0,405,69,1,0,0,0,406,
        407,5,59,0,0,407,408,5,51,0,0,408,409,3,72,36,0,409,410,5,52,0,0,
        410,71,1,0,0,0,411,414,3,74,37,0,412,414,1,0,0,0,413,411,1,0,0,0,
        413,412,1,0,0,0,414,73,1,0,0,0,415,416,3,76,38,0,416,417,5,53,0,
        0,417,418,3,74,37,0,418,421,1,0,0,0,419,421,3,76,38,0,420,415,1,
        0,0,0,420,419,1,0,0,0,421,75,1,0,0,0,422,423,5,59,0,0,423,424,5,
        55,0,0,424,425,3,6,3,0,425,77,1,0,0,0,426,427,5,10,0,0,427,428,5,
        59,0,0,428,429,5,12,0,0,429,430,3,80,40,0,430,431,3,140,70,0,431,
        79,1,0,0,0,432,433,5,51,0,0,433,434,3,82,41,0,434,435,5,52,0,0,435,
        81,1,0,0,0,436,437,3,84,42,0,437,438,3,82,41,0,438,441,1,0,0,0,439,
        441,3,84,42,0,440,436,1,0,0,0,440,439,1,0,0,0,441,83,1,0,0,0,442,
        443,5,59,0,0,443,445,3,50,25,0,444,446,3,130,65,0,445,444,1,0,0,
        0,445,446,1,0,0,0,446,447,1,0,0,0,447,448,3,140,70,0,448,85,1,0,
        0,0,449,450,3,88,44,0,450,451,3,92,46,0,451,452,3,94,47,0,452,453,
        3,140,70,0,453,87,1,0,0,0,454,455,5,5,0,0,455,456,3,96,48,0,456,
        458,3,116,58,0,457,459,3,140,70,0,458,457,1,0,0,0,458,459,1,0,0,
        0,459,89,1,0,0,0,460,461,5,6,0,0,461,462,5,5,0,0,462,463,3,96,48,
        0,463,465,3,116,58,0,464,466,3,140,70,0,465,464,1,0,0,0,465,466,
        1,0,0,0,466,91,1,0,0,0,467,468,3,90,45,0,468,469,3,92,46,0,469,472,
        1,0,0,0,470,472,1,0,0,0,471,467,1,0,0,0,471,470,1,0,0,0,472,93,1,
        0,0,0,473,474,5,6,0,0,474,477,3,116,58,0,475,477,1,0,0,0,476,473,
        1,0,0,0,476,475,1,0,0,0,477,95,1,0,0,0,478,479,5,47,0,0,479,480,
        3,6,3,0,480,481,5,48,0,0,481,97,1,0,0,0,482,483,5,7,0,0,483,484,
        3,6,3,0,484,485,3,116,58,0,485,486,3,140,70,0,486,507,1,0,0,0,487,
        488,5,7,0,0,488,489,3,100,50,0,489,490,5,54,0,0,490,491,3,6,3,0,
        491,492,5,54,0,0,492,493,3,102,51,0,493,494,3,116,58,0,494,495,3,
        140,70,0,495,507,1,0,0,0,496,497,5,7,0,0,497,498,5,59,0,0,498,499,
        5,53,0,0,499,500,5,59,0,0,500,501,5,39,0,0,501,502,5,21,0,0,502,
        503,3,104,52,0,503,504,3,116,58,0,504,505,3,140,70,0,505,507,1,0,
        0,0,506,482,1,0,0,0,506,487,1,0,0,0,506,496,1,0,0,0,507,99,1,0,0,
        0,508,509,5,59,0,0,509,510,5,39,0,0,510,511,3,6,3,0,511,101,1,0,
        0,0,512,513,5,59,0,0,513,514,3,136,68,0,514,515,3,6,3,0,515,103,
        1,0,0,0,516,519,5,59,0,0,517,519,3,122,61,0,518,516,1,0,0,0,518,
        517,1,0,0,0,519,105,1,0,0,0,520,521,5,20,0,0,521,522,3,140,70,0,
        522,107,1,0,0,0,523,524,5,19,0,0,524,525,3,140,70,0,525,109,1,0,
        0,0,526,527,3,18,9,0,527,528,3,28,14,0,528,529,3,140,70,0,529,111,
        1,0,0,0,530,531,5,8,0,0,531,537,3,140,70,0,532,533,5,8,0,0,533,534,
        3,6,3,0,534,535,3,140,70,0,535,537,1,0,0,0,536,530,1,0,0,0,536,532,
        1,0,0,0,537,113,1,0,0,0,538,541,3,136,68,0,539,541,5,39,0,0,540,
        538,1,0,0,0,540,539,1,0,0,0,541,115,1,0,0,0,542,543,5,51,0,0,543,
        544,3,118,59,0,544,545,5,52,0,0,545,117,1,0,0,0,546,547,3,120,60,
        0,547,548,3,118,59,0,548,551,1,0,0,0,549,551,3,120,60,0,550,546,
        1,0,0,0,550,549,1,0,0,0,551,119,1,0,0,0,552,563,3,34,17,0,553,563,
        3,38,19,0,554,563,3,42,21,0,555,563,3,40,20,0,556,563,3,86,43,0,
        557,563,3,98,49,0,558,563,3,108,54,0,559,563,3,106,53,0,560,563,
        3,110,55,0,561,563,3,112,56,0,562,552,1,0,0,0,562,553,1,0,0,0,562,
        554,1,0,0,0,562,555,1,0,0,0,562,556,1,0,0,0,562,557,1,0,0,0,562,
        558,1,0,0,0,562,559,1,0,0,0,562,560,1,0,0,0,562,561,1,0,0,0,563,
        121,1,0,0,0,564,565,3,44,22,0,565,566,3,130,65,0,566,567,3,124,62,
        0,567,123,1,0,0,0,568,569,5,51,0,0,569,570,3,126,63,0,570,571,5,
        52,0,0,571,125,1,0,0,0,572,573,3,128,64,0,573,574,5,53,0,0,574,575,
        3,126,63,0,575,578,1,0,0,0,576,578,3,128,64,0,577,572,1,0,0,0,577,
        576,1,0,0,0,578,127,1,0,0,0,579,582,3,6,3,0,580,582,3,124,62,0,581,
        579,1,0,0,0,581,580,1,0,0,0,582,129,1,0,0,0,583,585,3,44,22,0,584,
        583,1,0,0,0,584,585,1,0,0,0,585,586,1,0,0,0,586,592,3,132,66,0,587,
        589,3,44,22,0,588,587,1,0,0,0,588,589,1,0,0,0,589,590,1,0,0,0,590,
        592,5,59,0,0,591,584,1,0,0,0,591,588,1,0,0,0,592,131,1,0,0,0,593,
        594,7,0,0,0,594,133,1,0,0,0,595,603,5,57,0,0,596,603,5,56,0,0,597,
        603,5,58,0,0,598,603,5,23,0,0,599,603,5,24,0,0,600,603,3,70,35,0,
        601,603,3,122,61,0,602,595,1,0,0,0,602,596,1,0,0,0,602,597,1,0,0,
        0,602,598,1,0,0,0,602,599,1,0,0,0,602,600,1,0,0,0,602,601,1,0,0,
        0,603,135,1,0,0,0,604,605,7,1,0,0,605,137,1,0,0,0,606,607,7,2,0,
        0,607,139,1,0,0,0,608,609,7,3,0,0,609,141,1,0,0,0,46,149,157,167,
        178,190,202,204,219,221,229,238,247,252,267,274,288,308,313,333,
        339,347,352,363,370,379,400,413,420,440,445,458,465,471,476,506,
        518,536,540,550,562,577,581,584,588,591,602
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
    RULE_expr = 3
    RULE_expr1 = 4
    RULE_expr2 = 5
    RULE_expr3 = 6
    RULE_expr4 = 7
    RULE_expr5 = 8
    RULE_expr6 = 9
    RULE_expr7 = 10
    RULE_tail = 11
    RULE_field_access_tail = 12
    RULE_arr_elem_access = 13
    RULE_funccall_tail = 14
    RULE_expr_lst = 15
    RULE_expr_lstprime = 16
    RULE_assigning_stmt = 17
    RULE_lhs = 18
    RULE_var_decl = 19
    RULE_const_decl = 20
    RULE_array_decl = 21
    RULE_arridx_lst = 22
    RULE_arridx = 23
    RULE_func_decl = 24
    RULE_funcparam = 25
    RULE_paramlst = 26
    RULE_param_lstprime = 27
    RULE_param = 28
    RULE_id_nnlst = 29
    RULE_receiver = 30
    RULE_struct_decl = 31
    RULE_structfield = 32
    RULE_fielddecl_nnlst = 33
    RULE_fielddecl = 34
    RULE_struct_literal = 35
    RULE_structparam_lst = 36
    RULE_structparam_lstprime = 37
    RULE_structparam = 38
    RULE_interf_decl = 39
    RULE_interfmeth = 40
    RULE_interfmeth_nnlst = 41
    RULE_interfmethmem = 42
    RULE_ifelse_stmt = 43
    RULE_if_ = 44
    RULE_elseif_ = 45
    RULE_elseif_lst = 46
    RULE_else_ = 47
    RULE_condition = 48
    RULE_forloop_stmt = 49
    RULE_forloop_init = 50
    RULE_forloop_update = 51
    RULE_id__arr = 52
    RULE_break_stmt = 53
    RULE_continue_stmt = 54
    RULE_funccall_stmt = 55
    RULE_return_stmt = 56
    RULE_assign = 57
    RULE_blockcode = 58
    RULE_blockcodestmt_nnlst = 59
    RULE_blockcodestmt = 60
    RULE_arr_literal = 61
    RULE_arrvalue = 62
    RULE_arrelem_lst = 63
    RULE_arrelem = 64
    RULE_data_type = 65
    RULE_primitive_datatype = 66
    RULE_literal = 67
    RULE_uptassign = 68
    RULE_compare_op = 69
    RULE_end_stm = 70

    ruleNames =  [ "program", "decl_lst", "decl", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "tail", 
                   "field_access_tail", "arr_elem_access", "funccall_tail", 
                   "expr_lst", "expr_lstprime", "assigning_stmt", "lhs", 
                   "var_decl", "const_decl", "array_decl", "arridx_lst", 
                   "arridx", "func_decl", "funcparam", "paramlst", "param_lstprime", 
                   "param", "id_nnlst", "receiver", "struct_decl", "structfield", 
                   "fielddecl_nnlst", "fielddecl", "struct_literal", "structparam_lst", 
                   "structparam_lstprime", "structparam", "interf_decl", 
                   "interfmeth", "interfmeth_nnlst", "interfmethmem", "ifelse_stmt", 
                   "if_", "elseif_", "elseif_lst", "else_", "condition", 
                   "forloop_stmt", "forloop_init", "forloop_update", "id__arr", 
                   "break_stmt", "continue_stmt", "funccall_stmt", "return_stmt", 
                   "assign", "blockcode", "blockcodestmt_nnlst", "blockcodestmt", 
                   "arr_literal", "arrvalue", "arrelem_lst", "arrelem", 
                   "data_type", "primitive_datatype", "literal", "uptassign", 
                   "compare_op", "end_stm" ]

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

        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def array_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declContext,0)


        def struct_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declContext,0)


        def interf_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Interf_declContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.array_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.const_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 154
                self.func_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 155
                self.struct_decl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 156
                self.interf_decl()
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
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 167
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 162
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 163
                    self.match(MiniGoParser.OR)
                    self.state = 164
                    self.expr1(0) 
                self.state = 169
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 173
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 174
                    self.match(MiniGoParser.AND)
                    self.state = 175
                    self.expr2(0) 
                self.state = 180
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 190
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 184
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 185
                    self.compare_op()
                    self.state = 186
                    self.expr3(0) 
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 204
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 202
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
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
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 219
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
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
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
        self.enterRule(localctx, 16, self.RULE_expr5)
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(MiniGoParser.NOT)
                self.state = 225
                self.expr5()
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(MiniGoParser.SUB)
                self.state = 227
                self.expr5()
                pass
            elif token in [23, 24, 47, 49, 56, 57, 58, 59]:
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


        def tail(self):
            return self.getTypedRuleContext(MiniGoParser.TailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 238
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 234
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 235
                    self.tail() 
                self.state = 240
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        self.enterRule(localctx, 20, self.RULE_expr7)
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(MiniGoParser.LP)
                self.state = 242
                self.expr(0)
                self.state = 243
                self.match(MiniGoParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 246
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
        self.enterRule(localctx, 22, self.RULE_tail)
        try:
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.field_access_tail()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.arr_elem_access()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
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
        self.enterRule(localctx, 24, self.RULE_field_access_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(MiniGoParser.DOT)
            self.state = 255
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
        self.enterRule(localctx, 26, self.RULE_arr_elem_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(MiniGoParser.LSB)
            self.state = 258
            self.expr(0)
            self.state = 259
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
        self.enterRule(localctx, 28, self.RULE_funccall_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(MiniGoParser.LP)
            self.state = 262
            self.expr_lst()
            self.state = 263
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
        self.enterRule(localctx, 30, self.RULE_expr_lst)
        try:
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 33, 43, 47, 49, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
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
        self.enterRule(localctx, 32, self.RULE_expr_lstprime)
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.expr(0)
                self.state = 270
                self.match(MiniGoParser.COMMA)
                self.state = 271
                self.expr_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.expr(0)
                pass


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


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assigning_stmt




    def assigning_stmt(self):

        localctx = MiniGoParser.Assigning_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assigning_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.lhs()
            self.state = 277
            self.assign()
            self.state = 278
            self.expr(0)
            self.state = 279
            self.end_stm()
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
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.expr6(0)
                self.state = 282
                self.field_access_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                self.expr6(0)
                self.state = 285
                self.arr_elem_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 287
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_decl

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Type_Var_declContext(Var_declContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Var_declContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR_(self):
            return self.getToken(MiniGoParser.VAR_, 0)
        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)
        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)



    class Value_Var_declContext(Var_declContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Var_declContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR_(self):
            return self.getToken(MiniGoParser.VAR_, 0)
        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)
        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)



    class TypeValue_Var_declContext(Var_declContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniGoParser.Var_declContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR_(self):
            return self.getToken(MiniGoParser.VAR_, 0)
        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)
        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)




    def var_decl(self):

        localctx = MiniGoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_decl)
        try:
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = MiniGoParser.Type_Var_declContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.match(MiniGoParser.VAR_)
                self.state = 291
                self.match(MiniGoParser.ID)
                self.state = 292
                self.data_type()
                self.state = 293
                self.end_stm()
                pass

            elif la_ == 2:
                localctx = MiniGoParser.Value_Var_declContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(MiniGoParser.VAR_)
                self.state = 296
                self.match(MiniGoParser.ID)
                self.state = 297
                self.match(MiniGoParser.EQUAL)
                self.state = 298
                self.expr(0)
                self.state = 299
                self.end_stm()
                pass

            elif la_ == 3:
                localctx = MiniGoParser.TypeValue_Var_declContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 301
                self.match(MiniGoParser.VAR_)
                self.state = 302
                self.match(MiniGoParser.ID)
                self.state = 303
                self.data_type()
                self.state = 304
                self.match(MiniGoParser.EQUAL)
                self.state = 305
                self.expr(0)
                self.state = 306
                self.end_stm()
                pass


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


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_decl




    def const_decl(self):

        localctx = MiniGoParser.Const_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_const_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(MiniGoParser.CONST_)
            self.state = 311
            self.match(MiniGoParser.ID)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 577023702256967680) != 0):
                self.state = 312
                self.data_type()


            self.state = 315
            self.match(MiniGoParser.EQUAL)
            self.state = 316
            self.expr(0)
            self.state = 317
            self.end_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_(self):
            return self.getToken(MiniGoParser.VAR_, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arridx_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Arridx_lstContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def arr_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_decl




    def array_decl(self):

        localctx = MiniGoParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_array_decl)
        try:
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.match(MiniGoParser.VAR_)
                self.state = 320
                self.match(MiniGoParser.ID)
                self.state = 321
                self.arridx_lst()
                self.state = 322
                self.data_type()
                self.state = 323
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.match(MiniGoParser.VAR_)
                self.state = 326
                self.match(MiniGoParser.ID)
                self.state = 327
                self.arridx_lst()
                self.state = 328
                self.data_type()
                self.state = 329
                self.match(MiniGoParser.EQUAL)
                self.state = 330
                self.arr_literal()
                self.state = 331
                self.end_stm()
                pass


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
        self.enterRule(localctx, 44, self.RULE_arridx_lst)
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.arridx()
                self.state = 336
                self.arridx_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
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
        self.enterRule(localctx, 46, self.RULE_arridx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(MiniGoParser.LSB)
            self.state = 342
            self.expr(0)
            self.state = 343
            self.match(MiniGoParser.RSB)
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


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_decl




    def func_decl(self):

        localctx = MiniGoParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(MiniGoParser.FUNC_)
            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 346
                self.receiver()


            self.state = 349
            self.match(MiniGoParser.ID)
            self.state = 350
            self.funcparam()
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 577023702256967680) != 0):
                self.state = 351
                self.data_type()


            self.state = 354
            self.blockcode()
            self.state = 355
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
        self.enterRule(localctx, 50, self.RULE_funcparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(MiniGoParser.LP)
            self.state = 358
            self.paramlst()
            self.state = 359
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

        def param_lstprime(self):
            return self.getTypedRuleContext(MiniGoParser.Param_lstprimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramlst




    def paramlst(self):

        localctx = MiniGoParser.ParamlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_paramlst)
        try:
            self.state = 363
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
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
        self.enterRule(localctx, 54, self.RULE_param_lstprime)
        try:
            self.state = 370
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.param()
                self.state = 366
                self.match(MiniGoParser.COMMA)
                self.state = 367
                self.param_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
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
        self.enterRule(localctx, 56, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.id_nnlst()
            self.state = 373
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
        self.enterRule(localctx, 58, self.RULE_id_nnlst)
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.match(MiniGoParser.ID)
                self.state = 376
                self.match(MiniGoParser.COMMA)
                self.state = 377
                self.id_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
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
        self.enterRule(localctx, 60, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(MiniGoParser.LP)
            self.state = 382
            self.match(MiniGoParser.ID)
            self.state = 383
            self.match(MiniGoParser.ID)
            self.state = 384
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


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_decl




    def struct_decl(self):

        localctx = MiniGoParser.Struct_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_struct_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(MiniGoParser.TYPE_)
            self.state = 387
            self.match(MiniGoParser.ID)
            self.state = 388
            self.match(MiniGoParser.STRUCT_)
            self.state = 389
            self.structfield()
            self.state = 390
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

        def fielddecl_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Fielddecl_nnlstContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structfield




    def structfield(self):

        localctx = MiniGoParser.StructfieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_structfield)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(MiniGoParser.LCB)
            self.state = 393
            self.fielddecl_nnlst()
            self.state = 394
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
        self.enterRule(localctx, 66, self.RULE_fielddecl_nnlst)
        try:
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.fielddecl()
                self.state = 397
                self.fielddecl_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
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
        self.enterRule(localctx, 68, self.RULE_fielddecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(MiniGoParser.ID)
            self.state = 403
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
        self.enterRule(localctx, 70, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(MiniGoParser.ID)
            self.state = 407
            self.match(MiniGoParser.LCB)
            self.state = 408
            self.structparam_lst()
            self.state = 409
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
        self.enterRule(localctx, 72, self.RULE_structparam_lst)
        try:
            self.state = 413
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
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
        self.enterRule(localctx, 74, self.RULE_structparam_lstprime)
        try:
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.structparam()
                self.state = 416
                self.match(MiniGoParser.COMMA)
                self.state = 417
                self.structparam_lstprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
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
        self.enterRule(localctx, 76, self.RULE_structparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(MiniGoParser.ID)
            self.state = 423
            self.match(MiniGoParser.COLON)
            self.state = 424
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interf_declContext(ParserRuleContext):
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
            return MiniGoParser.RULE_interf_decl




    def interf_decl(self):

        localctx = MiniGoParser.Interf_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_interf_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(MiniGoParser.TYPE_)
            self.state = 427
            self.match(MiniGoParser.ID)
            self.state = 428
            self.match(MiniGoParser.INTERFACE_)
            self.state = 429
            self.interfmeth()
            self.state = 430
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

        def interfmeth_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Interfmeth_nnlstContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfmeth




    def interfmeth(self):

        localctx = MiniGoParser.InterfmethContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_interfmeth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(MiniGoParser.LCB)
            self.state = 433
            self.interfmeth_nnlst()
            self.state = 434
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interfmeth_nnlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interfmethmem(self):
            return self.getTypedRuleContext(MiniGoParser.InterfmethmemContext,0)


        def interfmeth_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Interfmeth_nnlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfmeth_nnlst




    def interfmeth_nnlst(self):

        localctx = MiniGoParser.Interfmeth_nnlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_interfmeth_nnlst)
        try:
            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.interfmethmem()
                self.state = 437
                self.interfmeth_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
                self.interfmethmem()
                pass


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
        self.enterRule(localctx, 84, self.RULE_interfmethmem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(MiniGoParser.ID)
            self.state = 443
            self.funcparam()
            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 577023702256967680) != 0):
                self.state = 444
                self.data_type()


            self.state = 447
            self.end_stm()
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


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifelse_stmt




    def ifelse_stmt(self):

        localctx = MiniGoParser.Ifelse_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_ifelse_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.if_()
            self.state = 450
            self.elseif_lst()
            self.state = 451
            self.else_()
            self.state = 452
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
        self.enterRule(localctx, 88, self.RULE_if_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(MiniGoParser.IF_)
            self.state = 455
            self.condition()
            self.state = 456
            self.blockcode()
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 457
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
        self.enterRule(localctx, 90, self.RULE_elseif_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(MiniGoParser.ELSE_)
            self.state = 461
            self.match(MiniGoParser.IF_)
            self.state = 462
            self.condition()
            self.state = 463
            self.blockcode()
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 464
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
        self.enterRule(localctx, 92, self.RULE_elseif_lst)
        try:
            self.state = 471
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.elseif_()
                self.state = 468
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
        self.enterRule(localctx, 94, self.RULE_else_)
        try:
            self.state = 476
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(MiniGoParser.ELSE_)
                self.state = 474
                self.blockcode()
                pass
            elif token in [-1, 54]:
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
        self.enterRule(localctx, 96, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(MiniGoParser.LP)
            self.state = 479
            self.expr(0)
            self.state = 480
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

        def FOR_(self):
            return self.getToken(MiniGoParser.FOR_, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def blockcode(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodeContext,0)


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def forloop_init(self):
            return self.getTypedRuleContext(MiniGoParser.Forloop_initContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def forloop_update(self):
            return self.getTypedRuleContext(MiniGoParser.Forloop_updateContext,0)


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

        def id__arr(self):
            return self.getTypedRuleContext(MiniGoParser.Id__arrContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forloop_stmt




    def forloop_stmt(self):

        localctx = MiniGoParser.Forloop_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_forloop_stmt)
        try:
            self.state = 506
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.match(MiniGoParser.FOR_)
                self.state = 483
                self.expr(0)
                self.state = 484
                self.blockcode()
                self.state = 485
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.match(MiniGoParser.FOR_)
                self.state = 488
                self.forloop_init()
                self.state = 489
                self.match(MiniGoParser.SEMICOLON)
                self.state = 490
                self.expr(0)
                self.state = 491
                self.match(MiniGoParser.SEMICOLON)
                self.state = 492
                self.forloop_update()
                self.state = 493
                self.blockcode()
                self.state = 494
                self.end_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 496
                self.match(MiniGoParser.FOR_)
                self.state = 497
                self.match(MiniGoParser.ID)
                self.state = 498
                self.match(MiniGoParser.COMMA)
                self.state = 499
                self.match(MiniGoParser.ID)
                self.state = 500
                self.match(MiniGoParser.ASSIGN)
                self.state = 501
                self.match(MiniGoParser.RANGE_)
                self.state = 502
                self.id__arr()
                self.state = 503
                self.blockcode()
                self.state = 504
                self.end_stm()
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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forloop_init




    def forloop_init(self):

        localctx = MiniGoParser.Forloop_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_forloop_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.match(MiniGoParser.ID)
            self.state = 509
            self.match(MiniGoParser.ASSIGN)
            self.state = 510
            self.expr(0)
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
        self.enterRule(localctx, 102, self.RULE_forloop_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.match(MiniGoParser.ID)
            self.state = 513
            self.uptassign()
            self.state = 514
            self.expr(0)
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
        self.enterRule(localctx, 104, self.RULE_id__arr)
        try:
            self.state = 518
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                self.match(MiniGoParser.ID)
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
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


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK_(self):
            return self.getToken(MiniGoParser.BREAK_, 0)

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(MiniGoParser.BREAK_)
            self.state = 521
            self.end_stm()
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

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(MiniGoParser.CONTINUE_)
            self.state = 524
            self.end_stm()
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


        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funccall_stmt




    def funccall_stmt(self):

        localctx = MiniGoParser.Funccall_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_funccall_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.expr6(0)
            self.state = 527
            self.funccall_tail()
            self.state = 528
            self.end_stm()
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

        def end_stm(self):
            return self.getTypedRuleContext(MiniGoParser.End_stmContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_return_stmt)
        try:
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.match(MiniGoParser.RETURN_)
                self.state = 531
                self.end_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 532
                self.match(MiniGoParser.RETURN_)
                self.state = 533
                self.expr(0)
                self.state = 534
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

        def uptassign(self):
            return self.getTypedRuleContext(MiniGoParser.UptassignContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign




    def assign(self):

        localctx = MiniGoParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_assign)
        try:
            self.state = 540
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34, 35, 36, 37, 38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 538
                self.uptassign()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 539
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

        def blockcodestmt_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Blockcodestmt_nnlstContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_blockcode




    def blockcode(self):

        localctx = MiniGoParser.BlockcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_blockcode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(MiniGoParser.LCB)
            self.state = 543
            self.blockcodestmt_nnlst()
            self.state = 544
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Blockcodestmt_nnlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockcodestmt(self):
            return self.getTypedRuleContext(MiniGoParser.BlockcodestmtContext,0)


        def blockcodestmt_nnlst(self):
            return self.getTypedRuleContext(MiniGoParser.Blockcodestmt_nnlstContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_blockcodestmt_nnlst




    def blockcodestmt_nnlst(self):

        localctx = MiniGoParser.Blockcodestmt_nnlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_blockcodestmt_nnlst)
        try:
            self.state = 550
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 546
                self.blockcodestmt()
                self.state = 547
                self.blockcodestmt_nnlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 549
                self.blockcodestmt()
                pass


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

        def assigning_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Assigning_stmtContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declContext,0)


        def array_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Array_declContext,0)


        def const_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declContext,0)


        def ifelse_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Ifelse_stmtContext,0)


        def forloop_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Forloop_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def funccall_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Funccall_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_blockcodestmt




    def blockcodestmt(self):

        localctx = MiniGoParser.BlockcodestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_blockcodestmt)
        try:
            self.state = 562
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 552
                self.assigning_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 553
                self.var_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 554
                self.array_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 555
                self.const_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 556
                self.ifelse_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 557
                self.forloop_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 558
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 559
                self.break_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 560
                self.funccall_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 561
                self.return_stmt()
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


        def data_type(self):
            return self.getTypedRuleContext(MiniGoParser.Data_typeContext,0)


        def arrvalue(self):
            return self.getTypedRuleContext(MiniGoParser.ArrvalueContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_literal




    def arr_literal(self):

        localctx = MiniGoParser.Arr_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_arr_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self.arridx_lst()
            self.state = 565
            self.data_type()
            self.state = 566
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
        self.enterRule(localctx, 124, self.RULE_arrvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.match(MiniGoParser.LCB)
            self.state = 569
            self.arrelem_lst()
            self.state = 570
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
        self.enterRule(localctx, 126, self.RULE_arrelem_lst)
        try:
            self.state = 577
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 572
                self.arrelem()
                self.state = 573
                self.match(MiniGoParser.COMMA)
                self.state = 574
                self.arrelem_lst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 576
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
        self.enterRule(localctx, 128, self.RULE_arrelem)
        try:
            self.state = 581
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 33, 43, 47, 49, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 579
                self.expr(0)
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 580
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


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_datatype(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_datatypeContext,0)


        def arridx_lst(self):
            return self.getTypedRuleContext(MiniGoParser.Arridx_lstContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_data_type




    def data_type(self):

        localctx = MiniGoParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.state = 591
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 584
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 583
                    self.arridx_lst()


                self.state = 586
                self.primitive_datatype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 588
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 587
                    self.arridx_lst()


                self.state = 590
                self.match(MiniGoParser.ID)
                pass


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
        self.enterRule(localctx, 134, self.RULE_literal)
        try:
            self.state = 602
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 595
                self.match(MiniGoParser.INTEGER)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 596
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [58]:
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
            elif token in [59]:
                self.enterOuterAlt(localctx, 6)
                self.state = 600
                self.struct_literal()
                pass
            elif token in [49]:
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
            self.state = 604
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
            self.state = 606
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
            self.state = 608
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
        self._predicates[3] = self.expr_sempred
        self._predicates[4] = self.expr1_sempred
        self._predicates[5] = self.expr2_sempred
        self._predicates[6] = self.expr3_sempred
        self._predicates[7] = self.expr4_sempred
        self._predicates[9] = self.expr6_sempred
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
         




