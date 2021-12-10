# -*- coding: utf-8 -*-


def calculate_for_pos(position, data):
    crab_cost = 0
    for i in range(len(data)):
        simple_cost = abs(position - data[i])
        crab_cost += (simple_cost * (simple_cost + 1)) / 2 
    return crab_cost

def get_optimal(data):
    lowest_cost = 9999999999
    optimal_position = -1
    for i in range(len(data)):
        current_cost = calculate_for_pos(i, data)
        print(i, current_cost)
        if current_cost < lowest_cost:
            lowest_cost = current_cost
            optimal_position = i
    return (optimal_position, lowest_cost)

if __name__ == "__main__":
    test_positions = [16,1,2,0,4,2,7,1,2,14]
    prod_positions = [1101,1,29,67,1102,0,1,65,1008,65,35,66,1005,66,28,1,67,65,20,4,0,1001,65,1,65,1106,0,8,99,35,67,101,99,105,32,110,39,101,115,116,32,112,97,115,32,117,110,101,32,105,110,116,99,111,100,101,32,112,114,111,103,114,97,109,10,601,578,981,315,530,525,671,1501,616,214,724,1247,543,58,183,282,242,54,90,130,1788,360,1719,710,1165,1476,29,744,164,293,1360,274,47,119,16,387,134,547,72,48,77,416,863,39,65,144,500,678,430,160,1689,550,753,1478,480,56,583,85,206,93,335,990,174,276,1119,52,308,470,563,387,897,21,85,720,983,178,383,134,299,722,57,391,489,768,232,646,1312,1316,31,57,927,176,531,421,1162,369,934,7,172,237,340,169,261,1371,1351,1268,72,58,375,1570,1238,55,513,403,1462,141,263,419,1316,852,251,39,358,209,204,439,150,1667,344,205,1299,1226,992,967,536,1160,1503,1154,1323,486,1079,329,823,506,1252,387,28,69,649,296,233,62,219,344,464,1284,291,234,47,949,1126,935,1367,1450,1431,379,344,478,731,648,77,184,927,211,262,728,1093,381,140,239,332,1436,78,665,1486,601,1444,364,1057,753,488,127,1001,350,1016,357,638,309,40,333,136,655,779,821,414,275,140,149,185,445,1169,476,196,907,1570,193,161,43,204,1489,1125,1024,101,17,592,1378,338,1625,3,269,1568,254,803,25,776,109,52,291,1595,255,739,34,768,378,632,4,181,373,162,562,74,85,160,16,47,38,266,1610,9,7,1398,358,287,450,188,1390,37,98,80,685,1645,50,55,16,542,20,443,848,49,808,76,233,69,110,471,73,408,638,89,861,280,1062,75,314,808,237,96,401,57,48,1306,115,1164,1533,5,1032,1314,66,630,96,496,116,1558,438,13,182,1360,802,101,327,370,444,335,812,430,900,1259,1117,318,118,433,501,401,101,582,27,454,981,776,14,26,163,384,1652,87,788,474,588,155,845,207,33,200,622,840,1360,432,11,525,86,296,481,200,529,95,924,431,40,846,220,285,14,66,755,111,647,643,1201,81,483,555,125,426,1499,29,115,48,39,92,316,434,217,218,116,9,33,496,358,1106,736,1181,1153,117,20,1719,1113,1620,26,581,407,114,1559,6,1918,964,909,340,630,817,473,111,1485,434,262,1702,651,11,182,1043,1904,633,336,252,677,1238,637,1008,82,327,171,185,19,141,395,1209,53,798,836,1378,598,262,298,265,287,85,21,249,848,162,89,1050,108,34,41,25,291,918,28,1234,139,351,867,146,79,995,1173,635,24,31,81,214,1114,155,1256,159,206,586,426,452,650,1653,47,42,264,240,500,864,893,1308,1249,853,286,62,592,102,77,1082,91,120,625,211,978,319,655,200,152,86,396,52,308,1479,38,41,53,179,648,216,41,641,659,1556,226,1421,291,33,1461,1095,529,309,1100,314,1695,505,1200,150,946,53,124,139,1506,52,33,463,613,33,1264,386,678,563,564,318,273,912,60,31,150,1321,133,1333,302,1243,49,421,808,1399,555,195,611,268,39,1302,1154,92,664,117,92,124,332,561,1436,865,198,71,271,909,40,1185,664,251,422,306,122,814,158,1676,122,217,312,952,845,104,572,1796,392,651,176,714,44,757,111,56,489,333,738,369,304,1239,105,297,277,674,213,938,2,681,336,171,1252,166,88,489,273,260,565,231,319,1085,650,211,510,12,511,325,46,107,980,1136,16,95,308,935,514,469,20,44,209,345,467,1310,500,75,594,166,199,741,193,28,52,106,1437,366,575,1200,609,678,534,573,723,325,8,386,268,690,321,186,375,2,104,657,1341,601,175,0,745,146,508,180,426,811,7,215,300,86,25,372,233,900,276,1625,808,1941,510,234,813,131,334,58,783,992,236,244,174,609,1581,1767,204,187,208,1340,347,803,146,299,140,142,339,60,118,300,809,276,413,267,946,77,154,466,425,193,187,852,674,2,17,1006,1007,166,195,137,97,41,407,65,1072,20,789,311,1227,20,132,1536,995,194,506,635,115,1500,529,93,72,950,208,944,1177,476,207,1228,5,974,226,225,290,690,581,218,401,49,361,1408,242,254,24,313,441,635,126,513,994,299,1722,52,1123,44,1332,628,534,789,298,692,45,596,1583,77,15,38,1293,1181,1498,772,148,297,49,692,87,594,49,148,170,54,1079,7,468,847,336,421,34,1108,406,892,689,245,298,85,1187,1142,286,310,207,34,660,549,39,1172,97,1,750,47,0,77,1632,135,54,18,22,1292,230,1031,11,225,820,461,1208,108,1443,274,1134,41,287,166,274,1032,585,1491,75,549,1231,1314,443,212,395,386,698,58,644,395,81,905,366,233,716,656,799,643,1011,173,790,360,269,930,13,606,488,387,1206,51]

    print(get_optimal(test_positions))
    
    print(get_optimal(prod_positions))
    
