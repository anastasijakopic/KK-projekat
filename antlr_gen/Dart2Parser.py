# Generated from grammar/Dart2Parser.g4 by ANTLR 4.13.2
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
        4,1,88,532,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,1,0,5,0,96,8,0,10,0,12,0,99,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,121,8,1,
        1,2,1,2,1,2,3,2,126,8,2,1,2,1,2,3,2,130,8,2,1,3,1,3,3,3,134,8,3,
        1,3,1,3,1,3,3,3,139,8,3,1,3,1,3,1,3,1,3,1,3,3,3,146,8,3,3,3,148,
        8,3,1,4,1,4,1,4,5,4,153,8,4,10,4,12,4,156,9,4,1,5,1,5,1,5,1,5,3,
        5,162,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,173,8,6,10,6,12,
        6,176,9,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,3,6,194,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,203,8,7,1,
        8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,218,8,9,1,
        10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,3,11,228,8,11,1,11,3,11,231,
        8,11,1,11,1,11,3,11,235,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        3,11,244,8,11,1,12,1,12,1,12,1,12,5,12,250,8,12,10,12,12,12,253,
        9,12,1,12,3,12,256,8,12,3,12,258,8,12,1,13,1,13,1,13,1,13,1,13,1,
        13,5,13,266,8,13,10,13,12,13,269,9,13,1,13,3,13,272,8,13,1,13,1,
        13,1,14,1,14,1,14,1,14,5,14,280,8,14,10,14,12,14,283,9,14,1,15,1,
        15,1,15,5,15,288,8,15,10,15,12,15,291,9,15,1,16,1,16,1,16,1,16,5,
        16,297,8,16,10,16,12,16,300,9,16,1,16,3,16,303,8,16,1,17,1,17,1,
        17,1,17,1,18,1,18,1,18,1,18,1,18,3,18,314,8,18,1,18,1,18,1,18,1,
        19,1,19,1,19,1,20,1,20,3,20,324,8,20,1,20,3,20,327,8,20,1,21,1,21,
        1,21,1,21,3,21,333,8,21,1,21,3,21,336,8,21,1,22,1,22,1,22,1,22,3,
        22,342,8,22,1,22,3,22,345,8,22,1,23,1,23,1,23,1,23,3,23,351,8,23,
        1,23,3,23,354,8,23,1,24,1,24,1,24,1,24,3,24,360,8,24,1,24,3,24,363,
        8,24,1,25,1,25,1,25,1,25,3,25,369,8,25,1,25,3,25,372,8,25,1,26,1,
        26,1,26,1,27,1,27,3,27,379,8,27,1,28,1,28,5,28,383,8,28,10,28,12,
        28,386,9,28,1,28,1,28,1,29,1,29,3,29,392,8,29,1,30,1,30,3,30,396,
        8,30,1,31,1,31,1,31,3,31,401,8,31,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,3,32,417,8,32,1,32,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        3,32,434,8,32,1,32,1,32,1,32,1,32,3,32,440,8,32,1,32,1,32,1,32,1,
        32,1,32,1,32,1,32,1,32,5,32,450,8,32,10,32,12,32,453,9,32,1,33,1,
        33,3,33,457,8,33,1,33,1,33,1,34,1,34,1,34,5,34,464,8,34,10,34,12,
        34,467,9,34,1,35,1,35,5,35,471,8,35,10,35,12,35,474,9,35,1,36,1,
        36,1,36,1,36,3,36,480,8,36,1,37,1,37,3,37,484,8,37,1,37,1,37,3,37,
        488,8,37,1,38,1,38,1,38,3,38,493,8,38,1,39,1,39,1,39,1,39,1,40,1,
        40,1,40,5,40,502,8,40,10,40,12,40,505,9,40,1,41,1,41,1,41,3,41,510,
        8,41,3,41,512,8,41,1,41,1,41,1,42,1,42,1,42,5,42,519,8,42,10,42,
        12,42,522,9,42,1,43,1,43,1,44,1,44,1,45,1,45,1,46,1,46,1,46,0,1,
        64,47,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,
        86,88,90,92,0,6,3,0,8,8,16,16,32,32,1,0,60,64,4,0,15,15,23,23,30,
        30,83,85,3,0,65,69,72,77,79,80,3,0,65,66,70,71,81,81,1,0,70,71,580,
        0,97,1,0,0,0,2,120,1,0,0,0,4,122,1,0,0,0,6,133,1,0,0,0,8,149,1,0,
        0,0,10,161,1,0,0,0,12,193,1,0,0,0,14,195,1,0,0,0,16,204,1,0,0,0,
        18,210,1,0,0,0,20,219,1,0,0,0,22,243,1,0,0,0,24,257,1,0,0,0,26,259,
        1,0,0,0,28,275,1,0,0,0,30,284,1,0,0,0,32,292,1,0,0,0,34,304,1,0,
        0,0,36,308,1,0,0,0,38,318,1,0,0,0,40,321,1,0,0,0,42,328,1,0,0,0,
        44,337,1,0,0,0,46,346,1,0,0,0,48,355,1,0,0,0,50,364,1,0,0,0,52,373,
        1,0,0,0,54,376,1,0,0,0,56,380,1,0,0,0,58,389,1,0,0,0,60,393,1,0,
        0,0,62,397,1,0,0,0,64,416,1,0,0,0,66,454,1,0,0,0,68,460,1,0,0,0,
        70,472,1,0,0,0,72,479,1,0,0,0,74,481,1,0,0,0,76,489,1,0,0,0,78,494,
        1,0,0,0,80,498,1,0,0,0,82,506,1,0,0,0,84,515,1,0,0,0,86,523,1,0,
        0,0,88,525,1,0,0,0,90,527,1,0,0,0,92,529,1,0,0,0,94,96,3,2,1,0,95,
        94,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,100,1,0,
        0,0,99,97,1,0,0,0,100,101,5,0,0,1,101,1,1,0,0,0,102,121,3,4,2,0,
        103,121,3,42,21,0,104,121,3,46,23,0,105,121,3,44,22,0,106,121,3,
        6,3,0,107,121,3,14,7,0,108,121,3,16,8,0,109,121,3,18,9,0,110,121,
        3,20,10,0,111,121,3,32,16,0,112,121,3,40,20,0,113,121,3,54,27,0,
        114,121,3,56,28,0,115,121,3,58,29,0,116,121,3,60,30,0,117,121,3,
        62,31,0,118,121,3,26,13,0,119,121,3,48,24,0,120,102,1,0,0,0,120,
        103,1,0,0,0,120,104,1,0,0,0,120,105,1,0,0,0,120,106,1,0,0,0,120,
        107,1,0,0,0,120,108,1,0,0,0,120,109,1,0,0,0,120,110,1,0,0,0,120,
        111,1,0,0,0,120,112,1,0,0,0,120,113,1,0,0,0,120,114,1,0,0,0,120,
        115,1,0,0,0,120,116,1,0,0,0,120,117,1,0,0,0,120,118,1,0,0,0,120,
        119,1,0,0,0,121,3,1,0,0,0,122,123,5,37,0,0,123,125,5,47,0,0,124,
        126,3,64,32,0,125,124,1,0,0,0,125,126,1,0,0,0,126,127,1,0,0,0,127,
        129,5,48,0,0,128,130,5,53,0,0,129,128,1,0,0,0,129,130,1,0,0,0,130,
        5,1,0,0,0,131,134,3,12,6,0,132,134,5,33,0,0,133,131,1,0,0,0,133,
        132,1,0,0,0,133,134,1,0,0,0,134,135,1,0,0,0,135,136,5,82,0,0,136,
        138,5,47,0,0,137,139,3,8,4,0,138,137,1,0,0,0,138,139,1,0,0,0,139,
        140,1,0,0,0,140,147,5,48,0,0,141,148,3,56,28,0,142,143,5,58,0,0,
        143,145,3,64,32,0,144,146,5,53,0,0,145,144,1,0,0,0,145,146,1,0,0,
        0,146,148,1,0,0,0,147,141,1,0,0,0,147,142,1,0,0,0,148,7,1,0,0,0,
        149,154,3,10,5,0,150,151,5,55,0,0,151,153,3,10,5,0,152,150,1,0,0,
        0,153,156,1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,9,1,0,0,0,
        156,154,1,0,0,0,157,158,5,82,0,0,158,159,5,54,0,0,159,162,3,12,6,
        0,160,162,5,82,0,0,161,157,1,0,0,0,161,160,1,0,0,0,162,11,1,0,0,
        0,163,194,5,39,0,0,164,194,5,40,0,0,165,194,5,41,0,0,166,194,5,42,
        0,0,167,168,5,43,0,0,168,169,5,74,0,0,169,174,3,12,6,0,170,171,5,
        55,0,0,171,173,3,12,6,0,172,170,1,0,0,0,173,176,1,0,0,0,174,172,
        1,0,0,0,174,175,1,0,0,0,175,177,1,0,0,0,176,174,1,0,0,0,177,178,
        5,75,0,0,178,194,1,0,0,0,179,180,5,44,0,0,180,181,5,74,0,0,181,182,
        3,12,6,0,182,183,5,55,0,0,183,184,3,12,6,0,184,185,5,75,0,0,185,
        194,1,0,0,0,186,187,5,45,0,0,187,188,5,74,0,0,188,189,3,12,6,0,189,
        190,5,75,0,0,190,194,1,0,0,0,191,194,5,46,0,0,192,194,5,82,0,0,193,
        163,1,0,0,0,193,164,1,0,0,0,193,165,1,0,0,0,193,166,1,0,0,0,193,
        167,1,0,0,0,193,179,1,0,0,0,193,186,1,0,0,0,193,191,1,0,0,0,193,
        192,1,0,0,0,194,13,1,0,0,0,195,196,5,19,0,0,196,197,5,47,0,0,197,
        198,3,64,32,0,198,199,5,48,0,0,199,202,3,56,28,0,200,201,5,12,0,
        0,201,203,3,56,28,0,202,200,1,0,0,0,202,203,1,0,0,0,203,15,1,0,0,
        0,204,205,5,34,0,0,205,206,5,47,0,0,206,207,3,64,32,0,207,208,5,
        48,0,0,208,209,3,56,28,0,209,17,1,0,0,0,210,211,5,11,0,0,211,212,
        3,56,28,0,212,213,5,34,0,0,213,214,5,47,0,0,214,215,3,64,32,0,215,
        217,5,48,0,0,216,218,5,53,0,0,217,216,1,0,0,0,217,218,1,0,0,0,218,
        19,1,0,0,0,219,220,5,18,0,0,220,221,5,47,0,0,221,222,3,22,11,0,222,
        223,5,48,0,0,223,224,3,56,28,0,224,21,1,0,0,0,225,228,3,24,12,0,
        226,228,1,0,0,0,227,225,1,0,0,0,227,226,1,0,0,0,228,230,1,0,0,0,
        229,231,3,64,32,0,230,229,1,0,0,0,230,231,1,0,0,0,231,232,1,0,0,
        0,232,234,5,53,0,0,233,235,3,68,34,0,234,233,1,0,0,0,234,235,1,0,
        0,0,235,244,1,0,0,0,236,237,3,52,26,0,237,238,5,20,0,0,238,239,3,
        64,32,0,239,244,1,0,0,0,240,241,5,82,0,0,241,242,5,20,0,0,242,244,
        3,64,32,0,243,227,1,0,0,0,243,236,1,0,0,0,243,240,1,0,0,0,244,23,
        1,0,0,0,245,258,3,50,25,0,246,251,3,64,32,0,247,248,5,55,0,0,248,
        250,3,64,32,0,249,247,1,0,0,0,250,253,1,0,0,0,251,249,1,0,0,0,251,
        252,1,0,0,0,252,255,1,0,0,0,253,251,1,0,0,0,254,256,5,53,0,0,255,
        254,1,0,0,0,255,256,1,0,0,0,256,258,1,0,0,0,257,245,1,0,0,0,257,
        246,1,0,0,0,258,25,1,0,0,0,259,260,5,27,0,0,260,261,5,47,0,0,261,
        262,3,64,32,0,262,263,5,48,0,0,263,267,5,49,0,0,264,266,3,28,14,
        0,265,264,1,0,0,0,266,269,1,0,0,0,267,265,1,0,0,0,267,268,1,0,0,
        0,268,271,1,0,0,0,269,267,1,0,0,0,270,272,3,30,15,0,271,270,1,0,
        0,0,271,272,1,0,0,0,272,273,1,0,0,0,273,274,5,50,0,0,274,27,1,0,
        0,0,275,276,5,5,0,0,276,277,3,64,32,0,277,281,5,54,0,0,278,280,3,
        2,1,0,279,278,1,0,0,0,280,283,1,0,0,0,281,279,1,0,0,0,281,282,1,
        0,0,0,282,29,1,0,0,0,283,281,1,0,0,0,284,285,5,10,0,0,285,289,5,
        54,0,0,286,288,3,2,1,0,287,286,1,0,0,0,288,291,1,0,0,0,289,287,1,
        0,0,0,289,290,1,0,0,0,290,31,1,0,0,0,291,289,1,0,0,0,292,293,5,31,
        0,0,293,298,3,56,28,0,294,297,3,36,18,0,295,297,3,34,17,0,296,294,
        1,0,0,0,296,295,1,0,0,0,297,300,1,0,0,0,298,296,1,0,0,0,298,299,
        1,0,0,0,299,302,1,0,0,0,300,298,1,0,0,0,301,303,3,38,19,0,302,301,
        1,0,0,0,302,303,1,0,0,0,303,33,1,0,0,0,304,305,5,38,0,0,305,306,
        3,12,6,0,306,307,3,56,28,0,307,35,1,0,0,0,308,309,5,6,0,0,309,310,
        5,47,0,0,310,313,5,82,0,0,311,312,5,54,0,0,312,314,3,12,6,0,313,
        311,1,0,0,0,313,314,1,0,0,0,314,315,1,0,0,0,315,316,5,48,0,0,316,
        317,3,56,28,0,317,37,1,0,0,0,318,319,5,17,0,0,319,320,3,56,28,0,
        320,39,1,0,0,0,321,323,5,25,0,0,322,324,3,64,32,0,323,322,1,0,0,
        0,323,324,1,0,0,0,324,326,1,0,0,0,325,327,5,53,0,0,326,325,1,0,0,
        0,326,327,1,0,0,0,327,41,1,0,0,0,328,329,5,32,0,0,329,332,5,82,0,
        0,330,331,5,78,0,0,331,333,3,64,32,0,332,330,1,0,0,0,332,333,1,0,
        0,0,333,335,1,0,0,0,334,336,5,53,0,0,335,334,1,0,0,0,335,336,1,0,
        0,0,336,43,1,0,0,0,337,338,5,16,0,0,338,341,5,82,0,0,339,340,5,78,
        0,0,340,342,3,64,32,0,341,339,1,0,0,0,341,342,1,0,0,0,342,344,1,
        0,0,0,343,345,5,53,0,0,344,343,1,0,0,0,344,345,1,0,0,0,345,45,1,
        0,0,0,346,347,5,8,0,0,347,350,5,82,0,0,348,349,5,78,0,0,349,351,
        3,64,32,0,350,348,1,0,0,0,350,351,1,0,0,0,351,353,1,0,0,0,352,354,
        5,53,0,0,353,352,1,0,0,0,353,354,1,0,0,0,354,47,1,0,0,0,355,356,
        3,12,6,0,356,359,5,82,0,0,357,358,5,78,0,0,358,360,3,64,32,0,359,
        357,1,0,0,0,359,360,1,0,0,0,360,362,1,0,0,0,361,363,5,53,0,0,362,
        361,1,0,0,0,362,363,1,0,0,0,363,49,1,0,0,0,364,365,7,0,0,0,365,368,
        5,82,0,0,366,367,5,78,0,0,367,369,3,64,32,0,368,366,1,0,0,0,368,
        369,1,0,0,0,369,371,1,0,0,0,370,372,5,53,0,0,371,370,1,0,0,0,371,
        372,1,0,0,0,372,51,1,0,0,0,373,374,7,0,0,0,374,375,5,82,0,0,375,
        53,1,0,0,0,376,378,3,64,32,0,377,379,5,53,0,0,378,377,1,0,0,0,378,
        379,1,0,0,0,379,55,1,0,0,0,380,384,5,49,0,0,381,383,3,2,1,0,382,
        381,1,0,0,0,383,386,1,0,0,0,384,382,1,0,0,0,384,385,1,0,0,0,385,
        387,1,0,0,0,386,384,1,0,0,0,387,388,5,50,0,0,388,57,1,0,0,0,389,
        391,5,4,0,0,390,392,5,53,0,0,391,390,1,0,0,0,391,392,1,0,0,0,392,
        59,1,0,0,0,393,395,5,9,0,0,394,396,5,53,0,0,395,394,1,0,0,0,395,
        396,1,0,0,0,396,61,1,0,0,0,397,398,5,29,0,0,398,400,3,64,32,0,399,
        401,5,53,0,0,400,399,1,0,0,0,400,401,1,0,0,0,401,63,1,0,0,0,402,
        403,6,32,-1,0,403,417,3,86,43,0,404,417,5,82,0,0,405,417,3,66,33,
        0,406,407,5,82,0,0,407,408,5,78,0,0,408,417,3,64,32,10,409,410,3,
        90,45,0,410,411,3,64,32,4,411,417,1,0,0,0,412,413,5,47,0,0,413,414,
        3,64,32,0,414,415,5,48,0,0,415,417,1,0,0,0,416,402,1,0,0,0,416,404,
        1,0,0,0,416,405,1,0,0,0,416,406,1,0,0,0,416,409,1,0,0,0,416,412,
        1,0,0,0,417,451,1,0,0,0,418,419,10,9,0,0,419,420,7,1,0,0,420,450,
        3,64,32,10,421,422,10,5,0,0,422,423,3,88,44,0,423,424,3,64,32,6,
        424,450,1,0,0,0,425,426,10,8,0,0,426,427,5,56,0,0,427,450,5,82,0,
        0,428,429,10,7,0,0,429,430,5,56,0,0,430,431,5,82,0,0,431,433,5,47,
        0,0,432,434,3,84,42,0,433,432,1,0,0,0,433,434,1,0,0,0,434,435,1,
        0,0,0,435,450,5,48,0,0,436,437,10,6,0,0,437,439,5,47,0,0,438,440,
        3,84,42,0,439,438,1,0,0,0,439,440,1,0,0,0,440,441,1,0,0,0,441,450,
        5,48,0,0,442,443,10,3,0,0,443,450,3,92,46,0,444,445,10,1,0,0,445,
        446,5,51,0,0,446,447,3,64,32,0,447,448,5,52,0,0,448,450,1,0,0,0,
        449,418,1,0,0,0,449,421,1,0,0,0,449,425,1,0,0,0,449,428,1,0,0,0,
        449,436,1,0,0,0,449,442,1,0,0,0,449,444,1,0,0,0,450,453,1,0,0,0,
        451,449,1,0,0,0,451,452,1,0,0,0,452,65,1,0,0,0,453,451,1,0,0,0,454,
        456,5,51,0,0,455,457,3,68,34,0,456,455,1,0,0,0,456,457,1,0,0,0,457,
        458,1,0,0,0,458,459,5,52,0,0,459,67,1,0,0,0,460,465,3,64,32,0,461,
        462,5,55,0,0,462,464,3,64,32,0,463,461,1,0,0,0,464,467,1,0,0,0,465,
        463,1,0,0,0,465,466,1,0,0,0,466,69,1,0,0,0,467,465,1,0,0,0,468,469,
        5,59,0,0,469,471,3,72,36,0,470,468,1,0,0,0,471,474,1,0,0,0,472,470,
        1,0,0,0,472,473,1,0,0,0,473,71,1,0,0,0,474,472,1,0,0,0,475,480,5,
        82,0,0,476,477,3,74,37,0,477,478,3,82,41,0,478,480,1,0,0,0,479,475,
        1,0,0,0,479,476,1,0,0,0,480,73,1,0,0,0,481,483,3,76,38,0,482,484,
        3,78,39,0,483,482,1,0,0,0,483,484,1,0,0,0,484,485,1,0,0,0,485,487,
        5,56,0,0,486,488,5,82,0,0,487,486,1,0,0,0,487,488,1,0,0,0,488,75,
        1,0,0,0,489,492,5,82,0,0,490,491,5,56,0,0,491,493,5,82,0,0,492,490,
        1,0,0,0,492,493,1,0,0,0,493,77,1,0,0,0,494,495,5,74,0,0,495,496,
        3,80,40,0,496,497,5,75,0,0,497,79,1,0,0,0,498,503,3,12,6,0,499,500,
        5,55,0,0,500,502,3,12,6,0,501,499,1,0,0,0,502,505,1,0,0,0,503,501,
        1,0,0,0,503,504,1,0,0,0,504,81,1,0,0,0,505,503,1,0,0,0,506,511,5,
        47,0,0,507,509,3,84,42,0,508,510,5,55,0,0,509,508,1,0,0,0,509,510,
        1,0,0,0,510,512,1,0,0,0,511,507,1,0,0,0,511,512,1,0,0,0,512,513,
        1,0,0,0,513,514,5,48,0,0,514,83,1,0,0,0,515,520,3,64,32,0,516,517,
        5,55,0,0,517,519,3,64,32,0,518,516,1,0,0,0,519,522,1,0,0,0,520,518,
        1,0,0,0,520,521,1,0,0,0,521,85,1,0,0,0,522,520,1,0,0,0,523,524,7,
        2,0,0,524,87,1,0,0,0,525,526,7,3,0,0,526,89,1,0,0,0,527,528,7,4,
        0,0,528,91,1,0,0,0,529,530,7,5,0,0,530,93,1,0,0,0,62,97,120,125,
        129,133,138,145,147,154,161,174,193,202,217,227,230,234,243,251,
        255,257,267,271,281,289,296,298,302,313,323,326,332,335,341,344,
        350,353,359,362,368,371,378,384,391,395,400,416,433,439,449,451,
        456,465,472,479,483,487,492,503,509,511,520
    ]

class Dart2Parser ( Parser ):

    grammarFileName = "Dart2Parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'abstract'", "'as'", "'assert'", "'break'", 
                     "'case'", "'catch'", "'class'", "'const'", "'continue'", 
                     "'default'", "'do'", "'else'", "'enum'", "'extends'", 
                     "'false'", "'final'", "'finally'", "'for'", "'if'", 
                     "'in'", "'is'", "'new'", "'null'", "'rethrow'", "'return'", 
                     "'super'", "'switch'", "'this'", "'throw'", "'true'", 
                     "'try'", "'var'", "'void'", "'while'", "'with'", "'yield'", 
                     "'print'", "'on'", "'int'", "'double'", "'String'", 
                     "'bool'", "'List'", "'Map'", "'Set'", "'dynamic'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "':'", 
                     "','", "'.'", "'?'", "'=>'", "'@'", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'++'", "'--'", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "'='", "'&&'", "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "ABSTRACT", "AS", "ASSERT", "BREAK", 
                      "CASE", "CATCH", "CLASS", "CONST", "CONTINUE", "DEFAULT", 
                      "DO", "ELSE", "ENUM", "EXTENDS", "FALSE", "FINAL", 
                      "FINALLY", "FOR", "IF", "IN", "IS", "NEW", "NULL", 
                      "RETHROW", "RETURN", "SUPER", "SWITCH", "THIS", "THROW", 
                      "TRUE", "TRY", "VAR", "VOID", "WHILE", "WITH", "YIELD", 
                      "PRINT", "ON", "INT_TYPE", "DOUBLE_TYPE", "STRING_TYPE", 
                      "BOOL_TYPE", "LIST_TYPE", "MAP_TYPE", "SET_TYPE", 
                      "DYNAMIC", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACK", "RBRACK", "SEMI", "COLON", "COMMA", "DOT", 
                      "QMARK", "ARROW", "AT", "PLUSEQ", "MINUSEQ", "MULEQ", 
                      "DIVEQ", "MODEQ", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
                      "INC", "DEC", "EQ", "NEQ", "LT", "GT", "LEQ", "GEQ", 
                      "ASSIGN", "AND", "OR", "NOT", "ID", "INT_LITERAL", 
                      "DOUBLE_LITERAL", "STRING", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_printStatement = 2
    RULE_functionDecl = 3
    RULE_parameterList = 4
    RULE_parameter = 5
    RULE_type = 6
    RULE_ifStatement = 7
    RULE_whileStatement = 8
    RULE_doWhileStatement = 9
    RULE_forStatement = 10
    RULE_forLoopParts = 11
    RULE_forInitializerStatement = 12
    RULE_switchStatement = 13
    RULE_switchCase = 14
    RULE_defaultCase = 15
    RULE_tryStatement = 16
    RULE_onClause = 17
    RULE_catchClause = 18
    RULE_finallyClause = 19
    RULE_returnStatement = 20
    RULE_varDecl = 21
    RULE_finalDecl = 22
    RULE_constDecl = 23
    RULE_typedVarDecl = 24
    RULE_localVariableDeclaration = 25
    RULE_declaredIdentifier = 26
    RULE_exprStatement = 27
    RULE_block = 28
    RULE_breakStatement = 29
    RULE_continueStatement = 30
    RULE_throwStatement = 31
    RULE_expression = 32
    RULE_listLiteral = 33
    RULE_expressionList = 34
    RULE_metadata = 35
    RULE_metadatum = 36
    RULE_constructorDesignation = 37
    RULE_typeName = 38
    RULE_typeArguments = 39
    RULE_typeList = 40
    RULE_arguments = 41
    RULE_argumentList = 42
    RULE_literal = 43
    RULE_binaryOp = 44
    RULE_unaryOp = 45
    RULE_unaryPostfixOp = 46

    ruleNames =  [ "program", "statement", "printStatement", "functionDecl", 
                   "parameterList", "parameter", "type", "ifStatement", 
                   "whileStatement", "doWhileStatement", "forStatement", 
                   "forLoopParts", "forInitializerStatement", "switchStatement", 
                   "switchCase", "defaultCase", "tryStatement", "onClause", 
                   "catchClause", "finallyClause", "returnStatement", "varDecl", 
                   "finalDecl", "constDecl", "typedVarDecl", "localVariableDeclaration", 
                   "declaredIdentifier", "exprStatement", "block", "breakStatement", 
                   "continueStatement", "throwStatement", "expression", 
                   "listLiteral", "expressionList", "metadata", "metadatum", 
                   "constructorDesignation", "typeName", "typeArguments", 
                   "typeList", "arguments", "argumentList", "literal", "binaryOp", 
                   "unaryOp", "unaryPostfixOp" ]

    EOF = Token.EOF
    ABSTRACT=1
    AS=2
    ASSERT=3
    BREAK=4
    CASE=5
    CATCH=6
    CLASS=7
    CONST=8
    CONTINUE=9
    DEFAULT=10
    DO=11
    ELSE=12
    ENUM=13
    EXTENDS=14
    FALSE=15
    FINAL=16
    FINALLY=17
    FOR=18
    IF=19
    IN=20
    IS=21
    NEW=22
    NULL=23
    RETHROW=24
    RETURN=25
    SUPER=26
    SWITCH=27
    THIS=28
    THROW=29
    TRUE=30
    TRY=31
    VAR=32
    VOID=33
    WHILE=34
    WITH=35
    YIELD=36
    PRINT=37
    ON=38
    INT_TYPE=39
    DOUBLE_TYPE=40
    STRING_TYPE=41
    BOOL_TYPE=42
    LIST_TYPE=43
    MAP_TYPE=44
    SET_TYPE=45
    DYNAMIC=46
    LPAREN=47
    RPAREN=48
    LBRACE=49
    RBRACE=50
    LBRACK=51
    RBRACK=52
    SEMI=53
    COLON=54
    COMMA=55
    DOT=56
    QMARK=57
    ARROW=58
    AT=59
    PLUSEQ=60
    MINUSEQ=61
    MULEQ=62
    DIVEQ=63
    MODEQ=64
    PLUS=65
    MINUS=66
    MUL=67
    DIV=68
    MOD=69
    INC=70
    DEC=71
    EQ=72
    NEQ=73
    LT=74
    GT=75
    LEQ=76
    GEQ=77
    ASSIGN=78
    AND=79
    OR=80
    NOT=81
    ID=82
    INT_LITERAL=83
    DOUBLE_LITERAL=84
    STRING=85
    LINE_COMMENT=86
    BLOCK_COMMENT=87
    WS=88

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Dart2Parser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.StatementContext,i)


        def getRuleIndex(self):
            return Dart2Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = Dart2Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3095846426872592) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2031715) != 0):
                self.state = 94
                self.statement()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
            self.match(Dart2Parser.EOF)
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

        def printStatement(self):
            return self.getTypedRuleContext(Dart2Parser.PrintStatementContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(Dart2Parser.VarDeclContext,0)


        def constDecl(self):
            return self.getTypedRuleContext(Dart2Parser.ConstDeclContext,0)


        def finalDecl(self):
            return self.getTypedRuleContext(Dart2Parser.FinalDeclContext,0)


        def functionDecl(self):
            return self.getTypedRuleContext(Dart2Parser.FunctionDeclContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(Dart2Parser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(Dart2Parser.WhileStatementContext,0)


        def doWhileStatement(self):
            return self.getTypedRuleContext(Dart2Parser.DoWhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(Dart2Parser.ForStatementContext,0)


        def tryStatement(self):
            return self.getTypedRuleContext(Dart2Parser.TryStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(Dart2Parser.ReturnStatementContext,0)


        def exprStatement(self):
            return self.getTypedRuleContext(Dart2Parser.ExprStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(Dart2Parser.BlockContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(Dart2Parser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(Dart2Parser.ContinueStatementContext,0)


        def throwStatement(self):
            return self.getTypedRuleContext(Dart2Parser.ThrowStatementContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(Dart2Parser.SwitchStatementContext,0)


        def typedVarDecl(self):
            return self.getTypedRuleContext(Dart2Parser.TypedVarDeclContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = Dart2Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.printStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.varDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.constDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 105
                self.finalDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 106
                self.functionDecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 107
                self.ifStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 108
                self.whileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 109
                self.doWhileStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 110
                self.forStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 111
                self.tryStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 112
                self.returnStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 113
                self.exprStatement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 114
                self.block()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 115
                self.breakStatement()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 116
                self.continueStatement()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 117
                self.throwStatement()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 118
                self.switchStatement()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 119
                self.typedVarDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(Dart2Parser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(Dart2Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Dart2Parser.RPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(Dart2Parser.SEMI, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)




    def printStatement(self):

        localctx = Dart2Parser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_printStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(Dart2Parser.PRINT)
            self.state = 123
            self.match(Dart2Parser.LPAREN)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2392538384203776) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2031715) != 0):
                self.state = 124
                self.expression(0)


            self.state = 127
            self.match(Dart2Parser.RPAREN)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 128
                self.match(Dart2Parser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def LPAREN(self):
            return self.getToken(Dart2Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Dart2Parser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(Dart2Parser.BlockContext,0)


        def ARROW(self):
            return self.getToken(Dart2Parser.ARROW, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def type_(self):
            return self.getTypedRuleContext(Dart2Parser.TypeContext,0)


        def VOID(self):
            return self.getToken(Dart2Parser.VOID, 0)

        def parameterList(self):
            return self.getTypedRuleContext(Dart2Parser.ParameterListContext,0)


        def SEMI(self):
            return self.getToken(Dart2Parser.SEMI, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)




    def functionDecl(self):

        localctx = Dart2Parser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 131
                self.type_()

            elif la_ == 2:
                self.state = 132
                self.match(Dart2Parser.VOID)


            self.state = 135
            self.match(Dart2Parser.ID)
            self.state = 136
            self.match(Dart2Parser.LPAREN)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==82:
                self.state = 137
                self.parameterList()


            self.state = 140
            self.match(Dart2Parser.RPAREN)
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.state = 141
                self.block()
                pass
            elif token in [58]:
                self.state = 142
                self.match(Dart2Parser.ARROW)
                self.state = 143
                self.expression(0)
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==53:
                    self.state = 144
                    self.match(Dart2Parser.SEMI)


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


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.ParameterContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Dart2Parser.COMMA)
            else:
                return self.getToken(Dart2Parser.COMMA, i)

        def getRuleIndex(self):
            return Dart2Parser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)




    def parameterList(self):

        localctx = Dart2Parser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.parameter()
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 150
                self.match(Dart2Parser.COMMA)
                self.state = 151
                self.parameter()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def COLON(self):
            return self.getToken(Dart2Parser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(Dart2Parser.TypeContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = Dart2Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parameter)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.match(Dart2Parser.ID)
                self.state = 158
                self.match(Dart2Parser.COLON)
                self.state = 159
                self.type_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.match(Dart2Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(Dart2Parser.INT_TYPE, 0)

        def DOUBLE_TYPE(self):
            return self.getToken(Dart2Parser.DOUBLE_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(Dart2Parser.STRING_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(Dart2Parser.BOOL_TYPE, 0)

        def LIST_TYPE(self):
            return self.getToken(Dart2Parser.LIST_TYPE, 0)

        def LT(self):
            return self.getToken(Dart2Parser.LT, 0)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.TypeContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.TypeContext,i)


        def GT(self):
            return self.getToken(Dart2Parser.GT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Dart2Parser.COMMA)
            else:
                return self.getToken(Dart2Parser.COMMA, i)

        def MAP_TYPE(self):
            return self.getToken(Dart2Parser.MAP_TYPE, 0)

        def SET_TYPE(self):
            return self.getToken(Dart2Parser.SET_TYPE, 0)

        def DYNAMIC(self):
            return self.getToken(Dart2Parser.DYNAMIC, 0)

        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = Dart2Parser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.match(Dart2Parser.INT_TYPE)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(Dart2Parser.DOUBLE_TYPE)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.match(Dart2Parser.STRING_TYPE)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 4)
                self.state = 166
                self.match(Dart2Parser.BOOL_TYPE)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 5)
                self.state = 167
                self.match(Dart2Parser.LIST_TYPE)
                self.state = 168
                self.match(Dart2Parser.LT)
                self.state = 169
                self.type_()
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==55:
                    self.state = 170
                    self.match(Dart2Parser.COMMA)
                    self.state = 171
                    self.type_()
                    self.state = 176
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 177
                self.match(Dart2Parser.GT)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 6)
                self.state = 179
                self.match(Dart2Parser.MAP_TYPE)
                self.state = 180
                self.match(Dart2Parser.LT)
                self.state = 181
                self.type_()
                self.state = 182
                self.match(Dart2Parser.COMMA)
                self.state = 183
                self.type_()
                self.state = 184
                self.match(Dart2Parser.GT)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 7)
                self.state = 186
                self.match(Dart2Parser.SET_TYPE)
                self.state = 187
                self.match(Dart2Parser.LT)
                self.state = 188
                self.type_()
                self.state = 189
                self.match(Dart2Parser.GT)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 8)
                self.state = 191
                self.match(Dart2Parser.DYNAMIC)
                pass
            elif token in [82]:
                self.enterOuterAlt(localctx, 9)
                self.state = 192
                self.match(Dart2Parser.ID)
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


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(Dart2Parser.IF, 0)

        def LPAREN(self):
            return self.getToken(Dart2Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Dart2Parser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.BlockContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.BlockContext,i)


        def ELSE(self):
            return self.getToken(Dart2Parser.ELSE, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = Dart2Parser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(Dart2Parser.IF)
            self.state = 196
            self.match(Dart2Parser.LPAREN)
            self.state = 197
            self.expression(0)
            self.state = 198
            self.match(Dart2Parser.RPAREN)
            self.state = 199
            self.block()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 200
                self.match(Dart2Parser.ELSE)
                self.state = 201
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(Dart2Parser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(Dart2Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Dart2Parser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(Dart2Parser.BlockContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = Dart2Parser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(Dart2Parser.WHILE)
            self.state = 205
            self.match(Dart2Parser.LPAREN)
            self.state = 206
            self.expression(0)
            self.state = 207
            self.match(Dart2Parser.RPAREN)
            self.state = 208
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(Dart2Parser.DO, 0)

        def block(self):
            return self.getTypedRuleContext(Dart2Parser.BlockContext,0)


        def WHILE(self):
            return self.getToken(Dart2Parser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(Dart2Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Dart2Parser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(Dart2Parser.SEMI, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_doWhileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhileStatement" ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhileStatement" ):
                listener.exitDoWhileStatement(self)




    def doWhileStatement(self):

        localctx = Dart2Parser.DoWhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_doWhileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(Dart2Parser.DO)
            self.state = 211
            self.block()
            self.state = 212
            self.match(Dart2Parser.WHILE)
            self.state = 213
            self.match(Dart2Parser.LPAREN)
            self.state = 214
            self.expression(0)
            self.state = 215
            self.match(Dart2Parser.RPAREN)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 216
                self.match(Dart2Parser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(Dart2Parser.FOR, 0)

        def LPAREN(self):
            return self.getToken(Dart2Parser.LPAREN, 0)

        def forLoopParts(self):
            return self.getTypedRuleContext(Dart2Parser.ForLoopPartsContext,0)


        def RPAREN(self):
            return self.getToken(Dart2Parser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(Dart2Parser.BlockContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)




    def forStatement(self):

        localctx = Dart2Parser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(Dart2Parser.FOR)
            self.state = 220
            self.match(Dart2Parser.LPAREN)
            self.state = 221
            self.forLoopParts()
            self.state = 222
            self.match(Dart2Parser.RPAREN)
            self.state = 223
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopPartsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(Dart2Parser.SEMI, 0)

        def forInitializerStatement(self):
            return self.getTypedRuleContext(Dart2Parser.ForInitializerStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def expressionList(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionListContext,0)


        def declaredIdentifier(self):
            return self.getTypedRuleContext(Dart2Parser.DeclaredIdentifierContext,0)


        def IN(self):
            return self.getToken(Dart2Parser.IN, 0)

        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_forLoopParts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoopParts" ):
                listener.enterForLoopParts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoopParts" ):
                listener.exitForLoopParts(self)




    def forLoopParts(self):

        localctx = Dart2Parser.ForLoopPartsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forLoopParts)
        self._la = 0 # Token type
        try:
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 225
                    self.forInitializerStatement()
                    pass

                elif la_ == 2:
                    pass


                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2392538384203776) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2031715) != 0):
                    self.state = 229
                    self.expression(0)


                self.state = 232
                self.match(Dart2Parser.SEMI)
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2392538384203776) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2031715) != 0):
                    self.state = 233
                    self.expressionList()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.declaredIdentifier()
                self.state = 237
                self.match(Dart2Parser.IN)
                self.state = 238
                self.expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.match(Dart2Parser.ID)
                self.state = 241
                self.match(Dart2Parser.IN)
                self.state = 242
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitializerStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def localVariableDeclaration(self):
            return self.getTypedRuleContext(Dart2Parser.LocalVariableDeclarationContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Dart2Parser.COMMA)
            else:
                return self.getToken(Dart2Parser.COMMA, i)

        def SEMI(self):
            return self.getToken(Dart2Parser.SEMI, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_forInitializerStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInitializerStatement" ):
                listener.enterForInitializerStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInitializerStatement" ):
                listener.exitForInitializerStatement(self)




    def forInitializerStatement(self):

        localctx = Dart2Parser.ForInitializerStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_forInitializerStatement)
        self._la = 0 # Token type
        try:
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 16, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.localVariableDeclaration()
                pass
            elif token in [15, 23, 30, 47, 51, 65, 66, 70, 71, 81, 82, 83, 84, 85]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.expression(0)
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==55:
                    self.state = 247
                    self.match(Dart2Parser.COMMA)
                    self.state = 248
                    self.expression(0)
                    self.state = 253
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 255
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 254
                    self.match(Dart2Parser.SEMI)


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


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(Dart2Parser.SWITCH, 0)

        def LPAREN(self):
            return self.getToken(Dart2Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(Dart2Parser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(Dart2Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Dart2Parser.RBRACE, 0)

        def switchCase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.SwitchCaseContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.SwitchCaseContext,i)


        def defaultCase(self):
            return self.getTypedRuleContext(Dart2Parser.DefaultCaseContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)




    def switchStatement(self):

        localctx = Dart2Parser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(Dart2Parser.SWITCH)
            self.state = 260
            self.match(Dart2Parser.LPAREN)
            self.state = 261
            self.expression(0)
            self.state = 262
            self.match(Dart2Parser.RPAREN)
            self.state = 263
            self.match(Dart2Parser.LBRACE)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 264
                self.switchCase()
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 270
                self.defaultCase()


            self.state = 273
            self.match(Dart2Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(Dart2Parser.CASE, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(Dart2Parser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.StatementContext,i)


        def getRuleIndex(self):
            return Dart2Parser.RULE_switchCase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchCase" ):
                listener.enterSwitchCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchCase" ):
                listener.exitSwitchCase(self)




    def switchCase(self):

        localctx = Dart2Parser.SwitchCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_switchCase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(Dart2Parser.CASE)
            self.state = 276
            self.expression(0)
            self.state = 277
            self.match(Dart2Parser.COLON)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3095846426872592) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2031715) != 0):
                self.state = 278
                self.statement()
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(Dart2Parser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(Dart2Parser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.StatementContext,i)


        def getRuleIndex(self):
            return Dart2Parser.RULE_defaultCase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultCase" ):
                listener.enterDefaultCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultCase" ):
                listener.exitDefaultCase(self)




    def defaultCase(self):

        localctx = Dart2Parser.DefaultCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_defaultCase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(Dart2Parser.DEFAULT)
            self.state = 285
            self.match(Dart2Parser.COLON)
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3095846426872592) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2031715) != 0):
                self.state = 286
                self.statement()
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TryStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRY(self):
            return self.getToken(Dart2Parser.TRY, 0)

        def block(self):
            return self.getTypedRuleContext(Dart2Parser.BlockContext,0)


        def catchClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.CatchClauseContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.CatchClauseContext,i)


        def onClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.OnClauseContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.OnClauseContext,i)


        def finallyClause(self):
            return self.getTypedRuleContext(Dart2Parser.FinallyClauseContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_tryStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryStatement" ):
                listener.enterTryStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryStatement" ):
                listener.exitTryStatement(self)




    def tryStatement(self):

        localctx = Dart2Parser.TryStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_tryStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(Dart2Parser.TRY)
            self.state = 293
            self.block()
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==38:
                self.state = 296
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 294
                    self.catchClause()
                    pass
                elif token in [38]:
                    self.state = 295
                    self.onClause()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 300
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 301
                self.finallyClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OnClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ON(self):
            return self.getToken(Dart2Parser.ON, 0)

        def type_(self):
            return self.getTypedRuleContext(Dart2Parser.TypeContext,0)


        def block(self):
            return self.getTypedRuleContext(Dart2Parser.BlockContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_onClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOnClause" ):
                listener.enterOnClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOnClause" ):
                listener.exitOnClause(self)




    def onClause(self):

        localctx = Dart2Parser.OnClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_onClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(Dart2Parser.ON)
            self.state = 305
            self.type_()
            self.state = 306
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CatchClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CATCH(self):
            return self.getToken(Dart2Parser.CATCH, 0)

        def LPAREN(self):
            return self.getToken(Dart2Parser.LPAREN, 0)

        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def RPAREN(self):
            return self.getToken(Dart2Parser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(Dart2Parser.BlockContext,0)


        def COLON(self):
            return self.getToken(Dart2Parser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(Dart2Parser.TypeContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_catchClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatchClause" ):
                listener.enterCatchClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatchClause" ):
                listener.exitCatchClause(self)




    def catchClause(self):

        localctx = Dart2Parser.CatchClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_catchClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(Dart2Parser.CATCH)
            self.state = 309
            self.match(Dart2Parser.LPAREN)
            self.state = 310
            self.match(Dart2Parser.ID)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 311
                self.match(Dart2Parser.COLON)
                self.state = 312
                self.type_()


            self.state = 315
            self.match(Dart2Parser.RPAREN)
            self.state = 316
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FinallyClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINALLY(self):
            return self.getToken(Dart2Parser.FINALLY, 0)

        def block(self):
            return self.getTypedRuleContext(Dart2Parser.BlockContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_finallyClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinallyClause" ):
                listener.enterFinallyClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinallyClause" ):
                listener.exitFinallyClause(self)




    def finallyClause(self):

        localctx = Dart2Parser.FinallyClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_finallyClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(Dart2Parser.FINALLY)
            self.state = 319
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(Dart2Parser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(Dart2Parser.SEMI, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = Dart2Parser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(Dart2Parser.RETURN)
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 322
                self.expression(0)


            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 325
                self.match(Dart2Parser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(Dart2Parser.VAR, 0)

        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def ASSIGN(self):
            return self.getToken(Dart2Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(Dart2Parser.SEMI, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)




    def varDecl(self):

        localctx = Dart2Parser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(Dart2Parser.VAR)
            self.state = 329
            self.match(Dart2Parser.ID)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==78:
                self.state = 330
                self.match(Dart2Parser.ASSIGN)
                self.state = 331
                self.expression(0)


            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 334
                self.match(Dart2Parser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FinalDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(Dart2Parser.FINAL, 0)

        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def ASSIGN(self):
            return self.getToken(Dart2Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(Dart2Parser.SEMI, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_finalDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinalDecl" ):
                listener.enterFinalDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinalDecl" ):
                listener.exitFinalDecl(self)




    def finalDecl(self):

        localctx = Dart2Parser.FinalDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_finalDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(Dart2Parser.FINAL)
            self.state = 338
            self.match(Dart2Parser.ID)
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==78:
                self.state = 339
                self.match(Dart2Parser.ASSIGN)
                self.state = 340
                self.expression(0)


            self.state = 344
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 343
                self.match(Dart2Parser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(Dart2Parser.CONST, 0)

        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def ASSIGN(self):
            return self.getToken(Dart2Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(Dart2Parser.SEMI, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_constDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstDecl" ):
                listener.enterConstDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstDecl" ):
                listener.exitConstDecl(self)




    def constDecl(self):

        localctx = Dart2Parser.ConstDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_constDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(Dart2Parser.CONST)
            self.state = 347
            self.match(Dart2Parser.ID)
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==78:
                self.state = 348
                self.match(Dart2Parser.ASSIGN)
                self.state = 349
                self.expression(0)


            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 352
                self.match(Dart2Parser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedVarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(Dart2Parser.TypeContext,0)


        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def ASSIGN(self):
            return self.getToken(Dart2Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(Dart2Parser.SEMI, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_typedVarDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedVarDecl" ):
                listener.enterTypedVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedVarDecl" ):
                listener.exitTypedVarDecl(self)




    def typedVarDecl(self):

        localctx = Dart2Parser.TypedVarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_typedVarDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.type_()
            self.state = 356
            self.match(Dart2Parser.ID)
            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==78:
                self.state = 357
                self.match(Dart2Parser.ASSIGN)
                self.state = 358
                self.expression(0)


            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 361
                self.match(Dart2Parser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocalVariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def VAR(self):
            return self.getToken(Dart2Parser.VAR, 0)

        def FINAL(self):
            return self.getToken(Dart2Parser.FINAL, 0)

        def CONST(self):
            return self.getToken(Dart2Parser.CONST, 0)

        def ASSIGN(self):
            return self.getToken(Dart2Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(Dart2Parser.SEMI, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_localVariableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalVariableDeclaration" ):
                listener.enterLocalVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalVariableDeclaration" ):
                listener.exitLocalVariableDeclaration(self)




    def localVariableDeclaration(self):

        localctx = Dart2Parser.LocalVariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_localVariableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4295033088) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 365
            self.match(Dart2Parser.ID)
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==78:
                self.state = 366
                self.match(Dart2Parser.ASSIGN)
                self.state = 367
                self.expression(0)


            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 370
                self.match(Dart2Parser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def VAR(self):
            return self.getToken(Dart2Parser.VAR, 0)

        def FINAL(self):
            return self.getToken(Dart2Parser.FINAL, 0)

        def CONST(self):
            return self.getToken(Dart2Parser.CONST, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_declaredIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaredIdentifier" ):
                listener.enterDeclaredIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaredIdentifier" ):
                listener.exitDeclaredIdentifier(self)




    def declaredIdentifier(self):

        localctx = Dart2Parser.DeclaredIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_declaredIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4295033088) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 374
            self.match(Dart2Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(Dart2Parser.SEMI, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_exprStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStatement" ):
                listener.enterExprStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStatement" ):
                listener.exitExprStatement(self)




    def exprStatement(self):

        localctx = Dart2Parser.ExprStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exprStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.expression(0)
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 377
                self.match(Dart2Parser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(Dart2Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Dart2Parser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.StatementContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.StatementContext,i)


        def getRuleIndex(self):
            return Dart2Parser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = Dart2Parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(Dart2Parser.LBRACE)
            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3095846426872592) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2031715) != 0):
                self.state = 381
                self.statement()
                self.state = 386
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 387
            self.match(Dart2Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(Dart2Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(Dart2Parser.SEMI, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)




    def breakStatement(self):

        localctx = Dart2Parser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_breakStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(Dart2Parser.BREAK)
            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 390
                self.match(Dart2Parser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(Dart2Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(Dart2Parser.SEMI, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)




    def continueStatement(self):

        localctx = Dart2Parser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_continueStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(Dart2Parser.CONTINUE)
            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 394
                self.match(Dart2Parser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThrowStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THROW(self):
            return self.getToken(Dart2Parser.THROW, 0)

        def expression(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(Dart2Parser.SEMI, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_throwStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrowStatement" ):
                listener.enterThrowStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrowStatement" ):
                listener.exitThrowStatement(self)




    def throwStatement(self):

        localctx = Dart2Parser.ThrowStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_throwStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(Dart2Parser.THROW)
            self.state = 398
            self.expression(0)
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 399
                self.match(Dart2Parser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(Dart2Parser.LiteralContext,0)


        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def listLiteral(self):
            return self.getTypedRuleContext(Dart2Parser.ListLiteralContext,0)


        def ASSIGN(self):
            return self.getToken(Dart2Parser.ASSIGN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.ExpressionContext,i)


        def unaryOp(self):
            return self.getTypedRuleContext(Dart2Parser.UnaryOpContext,0)


        def LPAREN(self):
            return self.getToken(Dart2Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Dart2Parser.RPAREN, 0)

        def PLUSEQ(self):
            return self.getToken(Dart2Parser.PLUSEQ, 0)

        def MINUSEQ(self):
            return self.getToken(Dart2Parser.MINUSEQ, 0)

        def MULEQ(self):
            return self.getToken(Dart2Parser.MULEQ, 0)

        def DIVEQ(self):
            return self.getToken(Dart2Parser.DIVEQ, 0)

        def MODEQ(self):
            return self.getToken(Dart2Parser.MODEQ, 0)

        def binaryOp(self):
            return self.getTypedRuleContext(Dart2Parser.BinaryOpContext,0)


        def DOT(self):
            return self.getToken(Dart2Parser.DOT, 0)

        def argumentList(self):
            return self.getTypedRuleContext(Dart2Parser.ArgumentListContext,0)


        def unaryPostfixOp(self):
            return self.getTypedRuleContext(Dart2Parser.UnaryPostfixOpContext,0)


        def LBRACK(self):
            return self.getToken(Dart2Parser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(Dart2Parser.RBRACK, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Dart2Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 403
                self.literal()
                pass

            elif la_ == 2:
                self.state = 404
                self.match(Dart2Parser.ID)
                pass

            elif la_ == 3:
                self.state = 405
                self.listLiteral()
                pass

            elif la_ == 4:
                self.state = 406
                self.match(Dart2Parser.ID)
                self.state = 407
                self.match(Dart2Parser.ASSIGN)
                self.state = 408
                self.expression(10)
                pass

            elif la_ == 5:
                self.state = 409
                self.unaryOp()
                self.state = 410
                self.expression(4)
                pass

            elif la_ == 6:
                self.state = 412
                self.match(Dart2Parser.LPAREN)
                self.state = 413
                self.expression(0)
                self.state = 414
                self.match(Dart2Parser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 451
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 449
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                    if la_ == 1:
                        localctx = Dart2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 418
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 419
                        _la = self._input.LA(1)
                        if not(((((_la - 60)) & ~0x3f) == 0 and ((1 << (_la - 60)) & 31) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 420
                        self.expression(10)
                        pass

                    elif la_ == 2:
                        localctx = Dart2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 421
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 422
                        self.binaryOp()
                        self.state = 423
                        self.expression(6)
                        pass

                    elif la_ == 3:
                        localctx = Dart2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 425
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 426
                        self.match(Dart2Parser.DOT)
                        self.state = 427
                        self.match(Dart2Parser.ID)
                        pass

                    elif la_ == 4:
                        localctx = Dart2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 428
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 429
                        self.match(Dart2Parser.DOT)
                        self.state = 430
                        self.match(Dart2Parser.ID)
                        self.state = 431
                        self.match(Dart2Parser.LPAREN)
                        self.state = 433
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2392538384203776) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2031715) != 0):
                            self.state = 432
                            self.argumentList()


                        self.state = 435
                        self.match(Dart2Parser.RPAREN)
                        pass

                    elif la_ == 5:
                        localctx = Dart2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 436
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 437
                        self.match(Dart2Parser.LPAREN)
                        self.state = 439
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2392538384203776) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2031715) != 0):
                            self.state = 438
                            self.argumentList()


                        self.state = 441
                        self.match(Dart2Parser.RPAREN)
                        pass

                    elif la_ == 6:
                        localctx = Dart2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 442
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 443
                        self.unaryPostfixOp()
                        pass

                    elif la_ == 7:
                        localctx = Dart2Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 444
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 445
                        self.match(Dart2Parser.LBRACK)
                        self.state = 446
                        self.expression(0)
                        self.state = 447
                        self.match(Dart2Parser.RBRACK)
                        pass

             
                self.state = 453
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ListLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(Dart2Parser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(Dart2Parser.RBRACK, 0)

        def expressionList(self):
            return self.getTypedRuleContext(Dart2Parser.ExpressionListContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_listLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListLiteral" ):
                listener.enterListLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListLiteral" ):
                listener.exitListLiteral(self)




    def listLiteral(self):

        localctx = Dart2Parser.ListLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_listLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(Dart2Parser.LBRACK)
            self.state = 456
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2392538384203776) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2031715) != 0):
                self.state = 455
                self.expressionList()


            self.state = 458
            self.match(Dart2Parser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Dart2Parser.COMMA)
            else:
                return self.getToken(Dart2Parser.COMMA, i)

        def getRuleIndex(self):
            return Dart2Parser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)




    def expressionList(self):

        localctx = Dart2Parser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.expression(0)
            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 461
                self.match(Dart2Parser.COMMA)
                self.state = 462
                self.expression(0)
                self.state = 467
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetadataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self, i:int=None):
            if i is None:
                return self.getTokens(Dart2Parser.AT)
            else:
                return self.getToken(Dart2Parser.AT, i)

        def metadatum(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.MetadatumContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.MetadatumContext,i)


        def getRuleIndex(self):
            return Dart2Parser.RULE_metadata

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetadata" ):
                listener.enterMetadata(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetadata" ):
                listener.exitMetadata(self)




    def metadata(self):

        localctx = Dart2Parser.MetadataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_metadata)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==59:
                self.state = 468
                self.match(Dart2Parser.AT)
                self.state = 469
                self.metadatum()
                self.state = 474
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetadatumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def constructorDesignation(self):
            return self.getTypedRuleContext(Dart2Parser.ConstructorDesignationContext,0)


        def arguments(self):
            return self.getTypedRuleContext(Dart2Parser.ArgumentsContext,0)


        def getRuleIndex(self):
            return Dart2Parser.RULE_metadatum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetadatum" ):
                listener.enterMetadatum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetadatum" ):
                listener.exitMetadatum(self)




    def metadatum(self):

        localctx = Dart2Parser.MetadatumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_metadatum)
        try:
            self.state = 479
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
                self.match(Dart2Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 476
                self.constructorDesignation()
                self.state = 477
                self.arguments()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorDesignationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(Dart2Parser.TypeNameContext,0)


        def DOT(self):
            return self.getToken(Dart2Parser.DOT, 0)

        def typeArguments(self):
            return self.getTypedRuleContext(Dart2Parser.TypeArgumentsContext,0)


        def ID(self):
            return self.getToken(Dart2Parser.ID, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_constructorDesignation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorDesignation" ):
                listener.enterConstructorDesignation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorDesignation" ):
                listener.exitConstructorDesignation(self)




    def constructorDesignation(self):

        localctx = Dart2Parser.ConstructorDesignationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_constructorDesignation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.typeName()
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==74:
                self.state = 482
                self.typeArguments()


            self.state = 485
            self.match(Dart2Parser.DOT)
            self.state = 487
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==82:
                self.state = 486
                self.match(Dart2Parser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Dart2Parser.ID)
            else:
                return self.getToken(Dart2Parser.ID, i)

        def DOT(self):
            return self.getToken(Dart2Parser.DOT, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_typeName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeName" ):
                listener.enterTypeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeName" ):
                listener.exitTypeName(self)




    def typeName(self):

        localctx = Dart2Parser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_typeName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.match(Dart2Parser.ID)
            self.state = 492
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 490
                self.match(Dart2Parser.DOT)
                self.state = 491
                self.match(Dart2Parser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(Dart2Parser.LT, 0)

        def typeList(self):
            return self.getTypedRuleContext(Dart2Parser.TypeListContext,0)


        def GT(self):
            return self.getToken(Dart2Parser.GT, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_typeArguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeArguments" ):
                listener.enterTypeArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeArguments" ):
                listener.exitTypeArguments(self)




    def typeArguments(self):

        localctx = Dart2Parser.TypeArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_typeArguments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(Dart2Parser.LT)
            self.state = 495
            self.typeList()
            self.state = 496
            self.match(Dart2Parser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.TypeContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.TypeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Dart2Parser.COMMA)
            else:
                return self.getToken(Dart2Parser.COMMA, i)

        def getRuleIndex(self):
            return Dart2Parser.RULE_typeList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeList" ):
                listener.enterTypeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeList" ):
                listener.exitTypeList(self)




    def typeList(self):

        localctx = Dart2Parser.TypeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_typeList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.type_()
            self.state = 503
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 499
                self.match(Dart2Parser.COMMA)
                self.state = 500
                self.type_()
                self.state = 505
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(Dart2Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(Dart2Parser.RPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(Dart2Parser.ArgumentListContext,0)


        def COMMA(self):
            return self.getToken(Dart2Parser.COMMA, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = Dart2Parser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.match(Dart2Parser.LPAREN)
            self.state = 511
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2392538384203776) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 2031715) != 0):
                self.state = 507
                self.argumentList()
                self.state = 509
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==55:
                    self.state = 508
                    self.match(Dart2Parser.COMMA)




            self.state = 513
            self.match(Dart2Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Dart2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Dart2Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Dart2Parser.COMMA)
            else:
                return self.getToken(Dart2Parser.COMMA, i)

        def getRuleIndex(self):
            return Dart2Parser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)




    def argumentList(self):

        localctx = Dart2Parser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_argumentList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.expression(0)
            self.state = 520
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 516
                    self.match(Dart2Parser.COMMA)
                    self.state = 517
                    self.expression(0) 
                self.state = 522
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)

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

        def INT_LITERAL(self):
            return self.getToken(Dart2Parser.INT_LITERAL, 0)

        def DOUBLE_LITERAL(self):
            return self.getToken(Dart2Parser.DOUBLE_LITERAL, 0)

        def STRING(self):
            return self.getToken(Dart2Parser.STRING, 0)

        def TRUE(self):
            return self.getToken(Dart2Parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(Dart2Parser.FALSE, 0)

        def NULL(self):
            return self.getToken(Dart2Parser.NULL, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = Dart2Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1082163200) != 0) or ((((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 7) != 0)):
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


    class BinaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(Dart2Parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(Dart2Parser.MINUS, 0)

        def MUL(self):
            return self.getToken(Dart2Parser.MUL, 0)

        def DIV(self):
            return self.getToken(Dart2Parser.DIV, 0)

        def MOD(self):
            return self.getToken(Dart2Parser.MOD, 0)

        def EQ(self):
            return self.getToken(Dart2Parser.EQ, 0)

        def NEQ(self):
            return self.getToken(Dart2Parser.NEQ, 0)

        def LT(self):
            return self.getToken(Dart2Parser.LT, 0)

        def GT(self):
            return self.getToken(Dart2Parser.GT, 0)

        def LEQ(self):
            return self.getToken(Dart2Parser.LEQ, 0)

        def GEQ(self):
            return self.getToken(Dart2Parser.GEQ, 0)

        def AND(self):
            return self.getToken(Dart2Parser.AND, 0)

        def OR(self):
            return self.getToken(Dart2Parser.OR, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_binaryOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOp" ):
                listener.enterBinaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOp" ):
                listener.exitBinaryOp(self)




    def binaryOp(self):

        localctx = Dart2Parser.BinaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_binaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            _la = self._input.LA(1)
            if not(((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 57247) != 0)):
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


    class UnaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(Dart2Parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(Dart2Parser.MINUS, 0)

        def NOT(self):
            return self.getToken(Dart2Parser.NOT, 0)

        def INC(self):
            return self.getToken(Dart2Parser.INC, 0)

        def DEC(self):
            return self.getToken(Dart2Parser.DEC, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_unaryOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOp" ):
                listener.enterUnaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOp" ):
                listener.exitUnaryOp(self)




    def unaryOp(self):

        localctx = Dart2Parser.UnaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_unaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            _la = self._input.LA(1)
            if not(((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 65635) != 0)):
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


    class UnaryPostfixOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INC(self):
            return self.getToken(Dart2Parser.INC, 0)

        def DEC(self):
            return self.getToken(Dart2Parser.DEC, 0)

        def getRuleIndex(self):
            return Dart2Parser.RULE_unaryPostfixOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryPostfixOp" ):
                listener.enterUnaryPostfixOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryPostfixOp" ):
                listener.exitUnaryPostfixOp(self)




    def unaryPostfixOp(self):

        localctx = Dart2Parser.UnaryPostfixOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_unaryPostfixOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            _la = self._input.LA(1)
            if not(_la==70 or _la==71):
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
        self._predicates[32] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         




