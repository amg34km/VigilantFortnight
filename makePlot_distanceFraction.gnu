#
set terminal pngcairo size 400, 350 enhanced font 'Verdana, 13'
set encoding iso_8859_1


# PLOT SET-UP
set output "distance_fraction.png"
set xlabel "Distance Fraction"
set ylabel "counts"
set boxwidth 0.5 absolute
set style fill transparent solid 0.45
set key right top spacing 1.0 font 'Verdana, 14'
bin_width = 1;
bin_number(x) = floor(x/bin_width)
rounded(x) = bin_width * ( bin_number(x) + 0.05 )

set label 1 "(A)" at 0.16, 38 font 'Verdana, 14'
plot [0:7.0][0:40]\
"dist.dat" u rounded(abs(1)):1 smooth frequency w boxes lc 1 t "100ns"
