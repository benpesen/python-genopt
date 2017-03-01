from flame import Machine
import matplotlib.pyplot as plt


f = '../lattice/test_392.lat'

m = Machine(open(f))

s = m.allocState({})
ms = len(m)

r = m.propagate(s, 0, ms, range(ms))
z = [r[i][1].pos for i in range(ms)]
x = [r[i][1].moment0_env[0] for i in range(ms)]


opt_cor = {'LS1_CB10:DCH_D1849': {'config': {'theta_x': 5.0134431486e-05}, 'id': 619}, 'LS1_CB02:DCV_D1339': {'config': {'theta_y': 0.00036972498014}, 'id': 198}, 'FS1_CSS:DCH_D2275': {'config': {'theta_x': 6.5212371248e-05}, 'id': 921}, 'LS1_BTS:DCH_D1964': {'config': {'theta_x': 0.000104946827}, 'id': 698}, 'LS1_CB04:DCV_D1426': {'config': {'theta_y': 0.00023742733141}, 'id': 272}, 'LS1_CB11:DCH_D1872': {'config': {'theta_x': 6.6540904717e-06}, 'id': 642}, 'LS1_CA02:DCH_D1180': {'config': {'theta_x': -1.9620020032e-06}, 'id': 57}, 'FS1_CSS:DCV_D2367': {'config': {'theta_y': 2.1865043915e-05}, 'id': 1008}, 'LS1_BTS:DCV_D2114': {'config': {'theta_y': 0.00018137685288}, 'id': 787}, 'LS1_CB06:DCH_D1554': {'config': {'theta_x': 4.9725721656e-05}, 'id': 377}, 'LS1_CB09:DCV_D1765': {'config': {'theta_y': 0.00013291937205}, 'id': 552}, 'LS1_BTS:DCH_D2024': {'config': {'theta_x': 7.2029054264e-05}, 'id': 741}, 'LS1_CB01:DCV_D1275': {'config': {'theta_y': 0.00056114002756}, 'id': 146}, 'LS1_CA02:DCH_D1165': {'config': {'theta_x': -5.3982438406e-05}, 'id': 44}, 'FS1_CSS:DCH_D2367': {'config': {'theta_x': 9.4910367722e-05}, 'id': 1007}, 'FS1_CSS:DCV_D2381': {'config': {'theta_y': 4.6319871805e-05}, 'id': 1021}, 'LS1_CB05:DCV_D1530': {'config': {'theta_y': 0.00014084947479}, 'id': 355}, 'LS1_CB08:DCV_D1681': {'config': {'theta_y': 0.00013721779757}, 'id': 484}, 'LS1_CB03:DCH_D1403': {'config': {'theta_x': 4.6637378423e-05}, 'id': 249}, 'LS1_CB04:DCH_D1446': {'config': {'theta_x': 5.7908653916e-06}, 'id': 286}, 'LS1_CB01:DCH_D1235': {'config': {'theta_x': 0.00035875235677}, 'id': 115}, 'LS1_CB05:DCH_D1490': {'config': {'theta_x': 1.8008361628e-05}, 'id': 324}, 'FS1_BBS:DCH_D2476': {'config': {'theta_x': 0.00025833402592}, 'id': 1098}, 'LS1_CB07:DCH_D1618': {'config': {'theta_x': 6.8508276341e-05}, 'id': 430}, 'LS1_CB11:DCV_D1892': {'config': {'theta_y': 0.00012053805967}, 'id': 658}, 'LS1_CB03:DCH_D1363': {'config': {'theta_x': -3.3498296654e-05}, 'id': 219}, 'FS1_CSS:DCV_D2257': {'config': {'theta_y': 7.595700261e-05}, 'id': 906}, 'LS1_CB09:DCH_D1745': {'config': {'theta_x': 6.4360450799e-05}, 'id': 536}, 'LS1_CB03:DCV_D1383': {'config': {'theta_y': 0.00033538693678}, 'id': 235}, 'FS1_BMS:DCV_D2662': {'config': {'theta_y': 7.3950720611e-05}, 'id': 1207}, 'LS1_CB06:DCV_D1594': {'config': {'theta_y': 0.00014271584759}, 'id': 408}, 'LS1_CB10:DCH_D1829': {'config': {'theta_x': 4.5908706431e-05}, 'id': 604}, 'LS1_CB11:DCH_D1892': {'config': {'theta_x': -1.7836360964e-05}, 'id': 657}, 'FS1_CSS:DCH_D2351': {'config': {'theta_x': 7.0499582731e-05}, 'id': 994}, 'LS1_CB04:DCV_D1446': {'config': {'theta_y': 0.00024360815577}, 'id': 287}, 'FS1_BBS:DCH_D2412': {'config': {'theta_x': 0.00021066533055}, 'id': 1048}, 'FS1_CSS:DCV_D2351': {'config': {'theta_y': 8.1862681281e-05}, 'id': 995}, 'FS1_CSS:DCH_D2210': {'config': {'theta_x': -3.3538552161e-05}, 'id': 870}, 'LS1_BTS:DCV_D2024': {'config': {'theta_y': 8.2465751554e-05}, 'id': 742}, 'LS1_CB11:DCV_D1872': {'config': {'theta_y': 0.00011024538217}, 'id': 643}, 'LS1_CB07:DCV_D1657': {'config': {'theta_y': 0.0001637454682}, 'id': 461}, 'LS1_CA01:DCH_D1147': {'config': {'theta_x': 7.5578423135e-05}, 'id': 22}, 'FS1_BMS:DCH_D2640': {'config': {'theta_x': -8.9660638746e-05}, 'id': 1197}, 'FS1_BMS:DCH_D2585': {'config': {'theta_x': -3.1802563893e-05}, 'id': 1149}, 'LS1_CB10:DCV_D1849': {'config': {'theta_y': 0.00014360323669}, 'id': 620}, 'LS1_CA03:DCV_D1199': {'config': {'theta_y': -9.6435686108e-05}, 'id': 81}, 'LS1_CB04:DCH_D1426': {'config': {'theta_x': -6.7509443755e-06}, 'id': 271}, 'LS1_CB08:DCH_D1721': {'config': {'theta_x': 5.2539318601e-05}, 'id': 513}, 'LS1_BTS:DCV_D1937': {'config': {'theta_y': 4.7554162301e-05}, 'id': 690}, 'LS1_CA02:DCV_D1165': {'config': {'theta_y': 0.0001195123434}, 'id': 45}, 'LS1_BTS:DCH_D1997': {'config': {'theta_x': 0.00010498335929}, 'id': 732}, 'FS1_BMS:DCH_D2507': {'config': {'theta_x': 9.725917191e-05}, 'id': 1125}, 'LS1_CB06:DCH_D1594': {'config': {'theta_x': 8.7973816016e-05}, 'id': 407}, 'FS1_BMS:DCH_D2662': {'config': {'theta_x': 7.3092184446e-06}, 'id': 1206}, 'LS1_CB09:DCV_D1745': {'config': {'theta_y': 0.00014085012462}, 'id': 537}, 'LS1_CB02:DCV_D1319': {'config': {'theta_y': 0.00040654148644}, 'id': 183}, 'FS1_CSS:DCH_D2189': {'config': {'theta_x': 2.8426435411e-05}, 'id': 856}, 'LS1_CB07:DCH_D1637': {'config': {'theta_x': 4.7952104672e-05}, 'id': 445}, 'LS1_CB08:DCV_D1701': {'config': {'theta_y': 0.00013452696253}, 'id': 499}, 'LS1_CB02:DCH_D1299': {'config': {'theta_x': 1.3663423992e-05}, 'id': 167}, 'LS1_CB05:DCH_D1530': {'config': {'theta_x': 5.3575424342e-05}, 'id': 354}, 'LS1_CB09:DCH_D1765': {'config': {'theta_x': 6.0150086803e-05}, 'id': 551}, 'LS1_BTS:DCH_D2114': {'config': {'theta_x': 0.00012726974729}, 'id': 786}, 'LS1_CB10:DCH_D1809': {'config': {'theta_x': 3.9317189814e-05}, 'id': 589}, 'LS1_BTS:DCV_D2061': {'config': {'theta_y': 0.00011158418654}, 'id': 762}, 'LS1_CB04:DCV_D1466': {'config': {'theta_y': 0.00021908250875}, 'id': 302}, 'LS1_CA01:DCH_D1131': {'config': {'theta_x': 0.00013981587907}, 'id': 9}, 'LS1_CB01:DCH_D1275': {'config': {'theta_x': -8.8741586958e-05}, 'id': 145}, 'FS1_BBS:DCV_D2412': {'config': {'theta_y': 7.008359151e-05}, 'id': 1049}, 'LS1_CB05:DCV_D1490': {'config': {'theta_y': 0.00016016576782}, 'id': 325}, 'LS1_CB07:DCV_D1637': {'config': {'theta_y': 0.00014616748896}, 'id': 446}, 'LS1_CB08:DCH_D1681': {'config': {'theta_x': 7.1917724613e-05}, 'id': 483}, 'FS1_BMS:DCV_D2534': {'config': {'theta_y': 2.0182502319e-05}, 'id': 1135}, 'LS1_CA03:DCV_D1214': {'config': {'theta_y': 8.9829642345e-05}, 'id': 94}, 'FS1_BMS:DCV_D2507': {'config': {'theta_y': 2.6866920176e-05}, 'id': 1126}, 'LS1_CB01:DCV_D1235': {'config': {'theta_y': 0.00040875193663}, 'id': 116}, 'LS1_BTS:DCH_D1937': {'config': {'theta_x': 6.676941178e-05}, 'id': 689}, 'LS1_CB09:DCH_D1785': {'config': {'theta_x': 5.0041044241e-05}, 'id': 566}, 'LS1_BTS:DCH_D2061': {'config': {'theta_x': 9.5999598763e-05}, 'id': 761}, 'LS1_CB08:DCH_D1701': {'config': {'theta_x': 5.1412045624e-05}, 'id': 498}, 'LS1_CB03:DCH_D1383': {'config': {'theta_x': 2.6356604458e-05}, 'id': 234}, 'FS1_BMS:DCV_D2585': {'config': {'theta_y': 0.0001173634281}, 'id': 1150}, 'FS1_CSS:DCV_D2210': {'config': {'theta_y': 6.6262039524e-05}, 'id': 871}, 'FS1_BMS:DCH_D2689': {'config': {'theta_x': 8.5216269467e-05}, 'id': 1224}, 'LS1_CB07:DCH_D1657': {'config': {'theta_x': 6.8696124854e-05}, 'id': 460}, 'LS1_CA03:DCH_D1199': {'config': {'theta_x': 0.00017942079806}, 'id': 80}, 'LS1_CB06:DCV_D1554': {'config': {'theta_y': 0.00011589699457}, 'id': 378}, 'LS1_CB08:DCV_D1721': {'config': {'theta_y': 0.00014955610089}, 'id': 514}, 'LS1_CB11:DCV_D1912': {'config': {'theta_y': 0.00012705784249}, 'id': 673}, 'LS1_CB05:DCH_D1510': {'config': {'theta_x': 2.8394649914e-05}, 'id': 339}, 'LS1_CA02:DCV_D1180': {'config': {'theta_y': 1.4212262742e-05}, 'id': 58}, 'LS1_CA03:DCH_D1214': {'config': {'theta_x': 0.00022300571771}, 'id': 93}, 'FS1_BBS:DCV_D2476': {'config': {'theta_y': 6.5392728967e-05}, 'id': 1099}, 'FS1_CSS:DCH_D2257': {'config': {'theta_x': 1.4047339176e-05}, 'id': 905}, 'LS1_CB09:DCV_D1785': {'config': {'theta_y': 0.00013801167437}, 'id': 567}, 'LS1_CA01:DCV_D1131': {'config': {'theta_y': 0.00020016635618}, 'id': 10}, 'LS1_BTS:DCV_D1964': {'config': {'theta_y': 0.00010334899925}, 'id': 699}, 'LS1_CB02:DCV_D1299': {'config': {'theta_y': 0.00050820691963}, 'id': 168}, 'LS1_CB02:DCH_D1339': {'config': {'theta_x': -1.2059067075e-05}, 'id': 197}, 'LS1_CB06:DCH_D1574': {'config': {'theta_x': 5.8248055734e-05}, 'id': 392}, 'LS1_BTS:DCV_D1997': {'config': {'theta_y': 9.8650029113e-05}, 'id': 733}, 'LS1_CB07:DCV_D1618': {'config': {'theta_y': 0.0001209325297}, 'id': 431}, 'FS1_BMS:DCV_D2640': {'config': {'theta_y': 8.685656753e-05}, 'id': 1198}, 'FS1_CSS:DCH_D2381': {'config': {'theta_x': 0.00014210388376}, 'id': 1020}, 'LS1_CB10:DCV_D1809': {'config': {'theta_y': 0.00014904612487}, 'id': 590}, 'LS1_CB02:DCH_D1319': {'config': {'theta_x': 3.0533144808e-05}, 'id': 182}, 'LS1_CB05:DCV_D1510': {'config': {'theta_y': 0.00015625953366}, 'id': 340}, 'LS1_CB10:DCV_D1829': {'config': {'theta_y': 0.00015818440968}, 'id': 605}, 'LS1_CA01:DCV_D1147': {'config': {'theta_y': 0.00028005492237}, 'id': 23}, 'LS1_CB04:DCH_D1466': {'config': {'theta_x': 3.3075153588e-05}, 'id': 301}, 'FS1_BMS:DCV_D2689': {'config': {'theta_y': 8.2924283647e-05}, 'id': 1225}, 'FS1_CSS:DCV_D2189': {'config': {'theta_y': 7.5989512905e-05}, 'id': 857}, 'LS1_CB11:DCH_D1912': {'config': {'theta_x': 1.428158423e-06}, 'id': 672}, 'FS1_CSS:DCV_D2275': {'config': {'theta_y': 9.9827515567e-05}, 'id': 922}, 'FS1_BMS:DCH_D2534': {'config': {'theta_x': 2.0389373469e-05}, 'id': 1134}, 'LS1_CB01:DCH_D1255': {'config': {'theta_x': -1.6892169326e-05}, 'id': 130}, 'LS1_CB03:DCV_D1403': {'config': {'theta_y': 0.00028278723377}, 'id': 250}, 'LS1_CB03:DCV_D1363': {'config': {'theta_y': 0.00035444591542}, 'id': 220}, 'LS1_CB06:DCV_D1574': {'config': {'theta_y': 0.00013932249997}, 'id': 393}, 'LS1_CB01:DCV_D1255': {'config': {'theta_y': 0.0003313366176}, 'id': 131}}
for k,v in opt_cor.items():
    m.reconfigure(v['id'], v['config'])

r1 = m.propagate(s, 0, ms, range(ms))
x1 = [r1[i][1].moment0_env[0] for i in range(ms)]

plt.plot(z, x, 'r')
plt.plot(z, x1, 'b')
plt.show()


