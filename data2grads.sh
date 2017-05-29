#/bin/bash

# download data
# e.g. yyyy=2017 mm=05 dd=25 hh=05 min=20
  
yyyy=${1}
mm=${2}
dd=${3}
hh=${4}
min=${5}

input="Z__C_RJTD_${yyyy}${mm}${dd}${hh}${min}00_RDR_JMAGPV__grib2.tar"

PDIR=${yyyy}/${mm}/${dd}/${hh}

mkdir -p $PDIR

url="http://database.rish.kyoto-u.ac.jp/arch/jmadata/data/jma-radar/synthetic/original/${yyyy}/${mm}/${dd}/"

wget ${url}$input

mv -v *.tar $PDIR

# unzip the data 
tar xvf ${PDIR}/Z__C_RJTD_${yyyy}${mm}${dd}${hh}${min}00_RDR_JMAGPV__grib2.tar
mv -v *.bin $PDIR

# jmaradar2grads
./jmaradar2bin  $PDIR/Z__C_RJTD_${yyyy}${mm}${dd}${hh}${min}00_RDR_JMAGPV_Ggis1km_Prr10lv_ANAL_grib2.bin $PDIR/${yyyy}${mm}${dd}${hh}${min}.dat

mkdir -p $PDIR/dat
mv -v $PDIR/*.dat $PDIR/dat
mv view_radar.ctl ${yyyy}${mm}${dd}${hh}${min}view_radar.ctl
mv ${yyyy}${mm}${dd}${hh}${min}view_radar.ctl $PDIR/dat