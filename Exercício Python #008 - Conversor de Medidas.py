medida = float(input('Digite um valor em metros'))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 0.1
cm = medida * 0.1
mm = medida * 0.001
print('A medida de {}M, vale {} KM, {}HM, {}DAM, {}DM, {}CM e {}MM.'.format(medida, km, hm, dam, dm, cm, mm))
