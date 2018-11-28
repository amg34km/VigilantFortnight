version 1.1.0
 Tsudo Yamanaka

XVGDensityCalculation.py
  xvgファイルのcumulateから Radial Mass Density を計算し出力するプログラム
SystemInfo.datを以下のように設定してください

[ input ]
xvgFileName.xvg
[ output ]
newFileName.xvg
[ colname ]
xvgFileColumnNames
[ atoms ]
一行目に atom num ,二行目以降 Atom_XX  int


特殊な原子を使っている場合は Calculation/ChemistItem.pyのdictionaryに原子名と原子量を直接加えてください



XVGEccentricityCalculation.py
  moi.xvgからEccentricityを計算し出力するプログラム

SystemInfo.dataはinput,output,colnameのみ設定してください
colname time Imin Imid Imaj
