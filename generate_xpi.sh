
input_dir="$1"
cp -r $input_dir xpi_source_dir
cd xpi_source_dir
dt=`date +%Y%m%d%H%M%S`
zip -r /var/www/html/xpi/install_$dt.xpi * > /var/www/html/xpi/xpi.out
