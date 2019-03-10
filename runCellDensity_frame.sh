#!/bin/bash

python_path='/home/tsudo/works/programming/AnalyzingTool/GROtester.py'
frame_num=`ls frame* | wc -l`
num=71
new_name='101010calcdata'$num'.dat'
gro_name='101010HighDensity'$num'.gro'

#if [[ -a $gro_name ]]; then
#  rm -f $gro_name
#fi

#for i in `seq 1 $frame_num` ; do
for i in `seq $num $num` ; do
  gro_path="frame$i.gro"
  if [[ ! -a $gro_path ]]; then
    echo "$gro_pathが存在しません"
  else
    echo "$gro_path"
    echo "$new_nameを作成します"


### GROInfo.datの作成
    echo ';CellDensity' > GROInfo.dat
    echo '[ input ]' >> GROInfo.dat
    echo $gro_path >> GROInfo.dat
    echo '[ output dat ]' >> GROInfo.dat
    echo $new_name >> GROInfo.dat
    echo '[ output gro ]' >> GROInfo.dat
    echo $gro_name >> GROInfo.dat
    echo '[ colname ]' >> GROInfo.dat
    echo 'id_molecules particles id X Y Z VX VY VZ' >> GROInfo.dat
    echo '[ division number ]' >> GROInfo.dat
    echo '5 5 5' >> GROInfo.dat
    ###
    python3 $python_path
#    mv $new_name $gro_name $dir
  fi
done
