#/bin/bash

#GAMMA & IDC 需修改相应京东直投业务侧的mysql配置
master_jdztdb_host=10.191.250.123
slave_jdztdb_host=10.191.250.123
jdztdb_port=3306
jdztdb_user=myppdb
jdztdb_pass=Wy1gxy2boss!
jdztdb_cset=gbk
jdztdb_name=expressdb


#slave_db_host=10.187.130.57
#db_port=3306
#db_user=myppdb
#db_pass=Wy1gxy2boss!
#db_cset=gbk
#db_name=expressdb
tablenum=64
Uin=$1
dir=`pwd`
output=$dir/product.txt
SLAVE_MYSQL_JDZT="mysql -h${slave_jdztdb_host} -P${jdztdb_port} -u${jdztdb_user} -p${jdztdb_pass} ${jdztdb_name} --default-character-set=${jdztdb_cset} -A -N"
echo  "SELECT Uin,AdId FROM BossExpAds WHERE delflag=0 and AdType=6 and MediaType=1 and TargetType in (2,4,131074,262148,512,1024,131584,263168) and Uin=${Uin};" 
if [ -f "$output" ]; then
	rm $output
fi
	$SLAVE_MYSQL_JDZT -e "SELECT BossExpAds.Uin,BossExpUser.GdtUid,BossExpAds.GdtAId  FROM BossExpAds,BossExpUser WHERE BossExpAds.delflag=0 and BossExpAds.AdType=6 and BossExpAds.MediaType=1 and BossExpAds.TargetType in (2,4,131074,262148,512,1024,131584,263168) and BossExpAds.Uin= BossExpUser.Uin and BossExpAds.Uin in (4200309697,4200163416,4200137417,4200044647);" >> "$output"
wc -l $output

