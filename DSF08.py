m = float(input('Digite o valor em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('O valor de {} metros em km é {:.3f}km'.format(m,km))
print('O valor de {} metros em hm é {:.2f}hm'.format(m,hm))
print('O valor de {} metros em dam é {:.1f}dam'.format(m,dam))
print('O valor de {} metros em dm é {:.0f}dm'.format(m,dm))
print('O valor de {} metros em cm é {:.0f}cm'.format(m,cm))
print('O valor de {} metors em mm é {:.0f}mm'.format(m,mm))
