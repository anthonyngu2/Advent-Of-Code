##create list
#wire_1_route = '[R991,U77,L916,D26,R424,D739,L558,D439,R636,U616,L364,D653,R546,U909,L66,D472,R341,U906,L37,D360,L369,D451,L649,D521,R2,U491,R409,U801,R23,U323,L209,U171,L849,D891,L854,U224,R476,D519,L937,U345,R722,D785,L312,D949,R124,U20,R677,D236,R820,D320,L549,D631,R42,U621,R760,U958,L925,U84,R914,U656,R598,D610,R397,D753,L109,U988,R435,U828,R219,U583,L317,D520,L940,D850,R594,D801,L422,U292,R883,U204,L76,U860,L753,U483,L183,U179,R441,U163,L859,U437,L485,D239,R454,D940,R689,D704,R110,D12,R370,D413,L192,D979,R990,D651,L308,U177,R787,D717,R245,U689,R11,D509,L680,U228,L347,D179,R508,D40,L502,U689,L643,U45,R884,D653,L23,D918,L825,D312,L691,U292,L285,D183,R997,U427,L89,U252,R475,U217,R16,U749,L578,D931,L273,U509,L741,U97,R407,U275,L605,U136,L558,U318,R478,U505,R446,U295,R562,D646,R988,D254,L68,U645,L953,U916,L442,D713,R978,U540,R447,U594,L804,U215,R95,D995,R818,D237,R212,U664,R455,D684,L338,U308,R463,D985,L988,D281,R758,U510,L232,U509,R289,D90,R65,D46,R886,D741,L327,U755,R236,U870,L764,U60,R391,U91,R367,U587,L651,D434,L47,U954,R707,D336,L242,D387,L410,D19,R203,D703,L228,U292,L19,U916,R411,U421,L726,U543,L240,U755,R157,U836,L397,U71,L125,D934,L723,D145,L317,D229,R863,U941,L926,D55,L2,D452,R895,D670,L216,U504,R66,U696,L581,U75,L235,U88,L609,U415,L850,U21,L109,U416,R408,D367,R823,D199,L718,U136,L860,U780,L308,D312,R230,D671,R477,D672,L94,U307,R301,D143,L300,D792,L593,D399,R840,D225,R680,D484,L646,D917,R132,D213,L779,D143,L176,U673,L772,D93,L10,D624,L244,D993,R346]'
#wire_2_route = '[L997,U989,L596,U821,L419,U118,R258,D239,R902,D810,R553,D271,R213,D787,R723,D57,L874,D556,R53,U317,L196,D813,R500,U151,R180,D293,L415,U493,L99,U482,R517,U649,R102,U860,R905,D499,R133,D741,R394,U737,L903,U800,R755,D376,L11,U751,R539,U33,R539,U30,L534,D631,L714,U190,L446,U409,R977,D731,R282,U244,R29,D212,L523,D570,L89,D327,R178,U970,R435,U250,R213,D604,R64,D348,R315,D994,L508,D261,R62,D50,L347,U183,R410,D627,L128,U855,L803,D695,L879,U857,L629,D145,L341,D733,L566,D626,L302,U236,L55,U428,R183,U254,R226,D228,R616,U137,L593,U204,R620,U624,R605,D705,L263,D568,R931,D464,R989,U621,L277,U274,L137,U768,L261,D360,L45,D110,R35,U212,L271,D318,L444,D427,R225,D380,L907,D193,L118,U741,L101,D298,R604,D598,L98,U458,L733,U511,L82,D173,L644,U803,R926,D610,R24,D170,L198,U766,R656,D474,L393,D934,L789,U92,L889,U460,L232,U193,L877,D380,L455,D526,R899,D696,R452,U95,L828,D720,R370,U664,L792,D204,R84,D749,R808,U132,L152,D375,R19,U164,L615,D121,R644,D289,R381,U126,L304,U508,L112,D268,L572,D838,L998,U127,R500,D344,R694,U451,L846,D565,R158,U47,L430,U214,R571,D983,R690,D227,L107,U109,L286,D66,L544,U205,L453,U716,L36,U672,L517,U878,L487,U936,L628,U253,R424,D409,R422,U636,R412,U553,R59,D332,R7,U495,L305,D939,L428,D821,R749,D195,R531,D898,R337,D303,L398,D625,R57,D503,L699,D553,L478,U716,R897,D3,R420,U903,R994,U864,L745,U205,R229,U126,L227,D454,R670,U605,L356,U499,R510,U238,L542,D440,R156,D512,L237,D341,L439,U642,R873,D650,R871,D616,R322,U696,R248,D746,R990,U829,R812,U294,L462,U740,R780]'
##wire_1_route = '[R75,D30,R83,U83,L12,D49,R71,U7,L72]'
##wire_2_route = '[U62,R66,U55,R34,D71,R55,D58,R83]'
wire_1_route = '[R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51]'
wire_2_route = '[U98,R91,D20,R16,D67,R40,U7,R15,U6,R7]'
##wire_1_route = '[R8,U5,L5,D3]'
##wire_2_route = '[U7,R6,D4,L4]'
wire_1_route = wire_1_route.strip('][').split(',')
wire_2_route = wire_2_route.strip('][').split(',')

#initialize 2d list size
w1,h1 = 2, len(wire_1_route)
w2,h2 = 2, len(wire_2_route)
route_1_cords = [[0 for x in range(w1)] for y in range(h1)]
route_2_cords = [[0 for x in range(w2)] for y in range(h2)]

#populate 2d lists
for x in range (0,len(wire_1_route),1):
    route_1_cords[x][0] = wire_1_route[x][0]
    route_1_cords[x][1] = int(wire_1_route[x][1:4])

for x in range (0,len(wire_2_route),1):
    route_2_cords[x][0] = wire_2_route[x][0]
    route_2_cords[x][1] = int(wire_2_route[x][1:4])        
    
#determined route of wire from origin
def plot(route):
    origin = [0,0]
    final_cords = []
    final_cords.append(origin)
    for x in range(1,len(route)+1,1):
        
        if route[x-1][0] == 'U':
            old_x_cord = final_cords[x-1][0]
            new_y_cord = final_cords[x-1][1] + route[x-1][1] #determine new y cord
            new_point = [old_x_cord,new_y_cord]
            final_cords.append(new_point)

        if route[x-1][0] == 'D':
            old_x_cord = final_cords[x-1][0]
            new_y_cord = final_cords[x-1][1] - route[x-1][1] #determine new y cord
            new_point = [old_x_cord,new_y_cord]
            final_cords.append(new_point)

        if route[x-1][0] == 'R':
            new_x_cord = final_cords[x-1][0] +  route[x-1][1] #determine new x cord
            old_y_cord = final_cords[x-1][1]
            new_point = [new_x_cord, old_y_cord]
            final_cords.append(new_point)

        if route[x-1][0] == 'L':
            new_x_cord = final_cords[x-1][0] -  route[x-1][1] #determine new x cord
            old_y_cord =  final_cords[x-1][1]
            new_point = [new_x_cord,old_y_cord]
            final_cords.append(new_point)
            
    return (final_cords)

        

route_1 = plot(route_1_cords)
route_2 = plot(route_2_cords)

intersections = []
def calc_intercept (x1,x2,y1,y2,ua):
    x = x1 + ua*(x2-x1)
    y = y1 + ua*(y2-y1)
    return [x,y]

for x in range(1,len(route_1),1):
    for y in range(1,len(route_2),1):
        x1 = route_1[x-1][0] #line one x start
        y1 = route_1[x-1][1] #line one y start
        x2 = route_1[x][0] #line one x end
        y2 = route_1[x][1] #line one y end
        x3 = route_2[y-1][0] #line two x start
        y3 = route_2[y-1][1] #line two y start
        x4 = route_2[y][0] #line two x end
        y4 = route_2[y][1] #line two y end
        
        ua_num = (x4-x3)*(y1-y3)-(y4-y3)*(x1-x3)
        ua_den = (y4-y3)*(x2-x1)-(x4-x3)*(y2-y1)
        ub_num = (x2-x1)*(y1-y3)-(y2-y1)*(x1-x3)
        
##        ua_num = (y3-y4)*(x1-x3) - (x4-x3)*(y1-y3)
##        ua_den = (x4-x3)*(y1-y2) - (x1-x2)*(y4-y3)
##        ub_num = (y1-y2)*(x1-x3) - (x2-x1)*(y1-y3)
        
        ub_den = ua_den
##        if ua_den == 0: # coincident lines
##            intersections.append([min(),min()]
        if ua_den != 0 and ub_den != 0 :
            ua = ua_num / ua_den
            ub = ub_num / ub_den
        if ua_den == 0 or ub_den == 0 : #parallel lines
            continue 
        if ua > 0 and ua < 1: #check first intersection
##            print('intersect!')
##            print(x1,y1)
##            print(x2,y2)
##            print(x3,y3)
##            print(x4,y4)
##            print(ua_num)
##            print(ua_den)
##            print(ua)
            intersect = calc_intercept(x1,x2,y1,y2,ua)
            intersections.append(intersect)
        elif ub > 0 and ub < 1: #check second intersection
##            print('intersect!')
##            print(x1,y1)
##            print(x2,y2)
##            print(x3,y3)
##            print(x4,y4)
##            print(ub_num)
##            print(ub_den)
##            print(ub)
            intersect = calc_intercept(x1,x2,y1,y2,ub)
            intersections.append(intersect)
        

origin = [0,0]
distances = []
print(intersections)
# manhattan_equation = abs(origin[0] - endpoint[0]) + abs(origin[1] - endpoint[1])
for x in range(0,len(intersections),1):
    distance = abs(origin[0] - intersections[x][0]) + abs(origin[1] - intersections[x][1])
    distances.append(distance)

print(min(distances))
