from dynamics_utils import *
from math import pi, pow

fv1 = 0.7
fv2 = 0.7
fv3 = 0.7
fv4 = 0.7
fv5 = 0.7
fv6 = 0.7
fv7 = 0.7


m1 = 5.700440
m2 = 3.226980
m3 = 4.312720
m4 = 2.072060
m5 = 2.246650
m6 = 1.609790
# if not combining the hand
# m7 = 0.350930
# if combining the hand
m7 = 0.350930+0.191250

r1 = [ -0.051170000000000,    0.079080000000000,   0.000859999999999956]
r2 = [  0.00269000000000000, -0.00529000000000003, 0.0684499999999999]
r3 = [ -0.0717600000000000,   0.0814900000000001,  0.00131999999999994] 
r4 = [  0.00159000000000006, -0.0111700000000000,  0.0261799999999999]
r5 = [ -0.0116799999999999,   0.131110000000000,   0.00459999999999992]
r6 = [  0.00697000000000011,  0.00599999999999981, 0.0604800000000000]
# if not combining the hand
# r7 = [0.0019800, 0.001250050344661, 0.134594999936937];
# if combining the hand
r7 = [0.00513704655280540, 0.000957223615773138, -0.0668234671142425]


# %        Ixx     Iyy      Izz    Ixy     Iyz     Ixz
#I1 = [0.0471, 0.0377, 0.0360,  -0.0001,  -0.0008,  -0.0061]
#I2 = [0.0118, 0.0279, 0.0208, -0.0003, -0.0002,  0.0021]
#I3 = [0.0266, 0.0284, 0.0125,  0.0003,  0.0011,  0.0039]
#I4 = [0.0132, 0.0071, 0.0093, -0.0004, -0.0007, -0.0002]
#I5 = [0.0167, 0.0168, 0.0037,  0.0002, -0.0006,  0.0002]
#I6 = [0.0070, 0.0039, 0.0550,  0.0004,  0.0002,  0.0002]
#I7 = [0.0002529, 0.0002689, 0.0003074,  0.0000058, -0.0000052, -0.0000016]

# These values are from the Inerta Matrix so the cross terms are negated
# %        Ixx              Iyy              Izz                 Ixy                    Iyz                 Ixz
I1 = [0.0470910226200000,  0.0359598847800000,  0.0376697645500000,  -1*(0.00614870039000000),   -1*(0.000780868990000000),  -1*(-0.000127875560000001)]
I2 = [0.0278859752000000,  0.0207874929800000,  0.0117520941900000,  -1*(0.000188219930000000),  -1*(-0.00207675762000000),  -1*(0.000300963979999999)]
I3 = [0.0266173355700000,  0.0124800832200000,  0.0284435520700000,  -1*(0.00392189887000000),   -1*(0.00108389330000000),   -1*(-0.000292706340000000)]
I4 = [0.0131822787600000,  0.00926852064000000, 0.00711582686000000, -1*(0.000196634180000000),  -1*(-0.000745949600000000), -1*(-0.000360361730000000)]
I5 = [0.0166774282500000,  0.00374631150000000, 0.0167545726400000,  -1*(0.000186576290000000),  -1*(-0.000647323520000000), -1*(-0.000184037050000000)]
I6 = [0.00700537914000000, 0.00552755240000000, 0.00387607152000000, -1*(-0.000153480670000000), -1*(0.000211150380000000),  -1*(0.000443847840000000)]
# if not combining the hand
# I7 = [0.0002528915500000000, 0.0002688601005244859, 0.000307411799475514, 0.000005753109919612049, -0.00000519818194489434, -0.00000159345029023859]
# if combining the hand
I7 = [0.000816213583134714, 0.000873501275494573, 0.000549414879133963, -1*(-0.000128440101367341), -1*(-0.000105772659889993), -1*(-0.000189698911699243)]

L1 = I_to_matrix(I1)-m1*skew(r1)*skew(r1)
L2 = I_to_matrix(I2)-m2*skew(r2)*skew(r2)
L3 = I_to_matrix(I3)-m3*skew(r3)*skew(r3)
L4 = I_to_matrix(I4)-m4*skew(r4)*skew(r4)
L5 = I_to_matrix(I5)-m5*skew(r5)*skew(r5)
L6 = I_to_matrix(I6)-m6*skew(r6)*skew(r6)
L7 = I_to_matrix(I7)-m7*skew(r7)*skew(r7)

params = [L1[0,0], -L1[0,1], -L1[0,2], L1[1,1], -L1[1,2], L1[2,2], r1[0]*m1, r1[1]*m1, r1[2]*m1, m1, fv1,
          L2[0,0], -L2[0,1], -L2[0,2], L2[1,1], -L2[1,2], L2[2,2], r2[0]*m2, r2[1]*m2, r2[2]*m2, m2, fv2,
          L3[0,0], -L3[0,1], -L3[0,2], L3[1,1], -L3[1,2], L3[2,2], r3[0]*m3, r3[1]*m3, r3[2]*m3, m3, fv3,
          L4[0,0], -L4[0,1], -L4[0,2], L4[1,1], -L4[1,2], L4[2,2], r4[0]*m4, r4[1]*m4, r4[2]*m4, m4, fv4,
          L5[0,0], -L5[0,1], -L5[0,2], L5[1,1], -L5[1,2], L5[2,2], r5[0]*m5, r5[1]*m5, r5[2]*m5, m5, fv5,
          L6[0,0], -L6[0,1], -L6[0,2], L6[1,1], -L6[1,2], L6[2,2], r6[0]*m6, r6[1]*m6, r6[2]*m6, m6, fv6,
          L7[0,0], -L7[0,1], -L7[0,2], L7[1,1], -L7[1,2], L7[2,2], r7[0]*m7, r7[1]*m7, r7[2]*m7, m7, fv7]


#arams = [I1[0], -I1[3], -I1[5], I1[1], -I1[4], I1[2], r1[0]*m1, r1[1]*m1, r1[2]*m1, m1, 0., 0.,
#         I2[0], -I2[3], -I2[5], I2[1], -I2[4], I2[2], r2[0]*m1, r2[1]*m1, r2[2]*m1, m1, 0., 0.,
#         I3[0], -I3[3], -I3[5], I3[1], -I3[4], I3[2], r3[0]*m1, r3[1]*m1, r3[2]*m1, m1, 0., 0.,
 #        I4[0], -I4[3], -I4[5], I4[1], -I4[4], I4[2], r4[0]*m1, r4[1]*m1, r4[2]*m1, m1, 0., 0.,
  #       I5[0], -I5[3], -I5[5], I5[1], -I5[4], I5[2], r5[0]*m1, r5[1]*m1, r5[2]*m1, m1, 0., 0.,
#         I6[0], -I6[3], -I6[5], I6[1], -I6[4], I6[2], r6[0]*m1, r6[1]*m1, r6[2]*m1, m1, 0., 0.,
#         I7[0], -I7[3], -I7[5], I7[1], -I7[4], I7[2], r7[0]*m1, r7[1]*m1, r7[2]*m1, m1, 0., 0.]