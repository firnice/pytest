#!/usr/bin/python
###dennis zhao  python script automatic deploy application server
###2013-08-01  python 2.6
###27202787@qq.com

import sys,os,time,shutil, filecmp
print ("start backup database .......");
oscommand = 'ver'
backup_sql_path="/data2/backup/sql2"
backup_war_path="/data2/backup/war2"
logs_path='/tmp/log.log'
current_date=time.strftime('%Y-%m-%d')
current_datetime=time.strftime('%Y%m%d%H%M%S')
db_name="laneige"
password="xxxx2011"
db_host="localhost"
mysql_user="root"

def writeLogs(filename,contents):
    f=open(filename,'a+');
    f.write(contents);
    f.close();

if not os.path.exists(backup_sql_path):
    Msg='-'*30+time.strftime('%Y-%m-%d %H:%M:%S')+'-'*30+'\n'
    if(os.mkdir(backup_sql_path))==None:
        Msg+='**succeed to create dir:'+backup_sql_path+'\n'
        writeLogs(logs_path,Msg)
    else:
        Msg+='!!create backup dir:'+backup_sql_path+'failed,check whether dir can write! nn'
        writeLogs(logs_path,Msg)

if not os.path.exists(backup_war_path):
    Msg='-'*30+time.strftime('%Y-%m-%d,%H:%M:%S')+'-'*30+'\n'
    if(os.mkdir(backup_war_path))==None:
        Msg+='**succeed to create dir:'+backup_war_path+'\n'
        writeLogs(logs_path,Msg)
    else:
        Msg+='!!create backup dir:'+backup_war_path+'failed,check whether dir can write! nn'
        writeLogs(logs_path,Msg)
    sys.exit()


param=raw_input("Please input deployment version(stress or staging or prod) :");
password="no password";
backup_name=backup_sql_path+"/" + current_datetime+".sql"
if (param == "stress" or param == "" or param == "local"):
    password="xxxx2012"
    bak_cmd='mysqldump -h%s -u%s -p%s %s  > %s  ' %(db_host,mysql_user,password,db_name,backup_name);
    os.system(bak_cmd);
    os.system("pwd");
    os.system("tar -zcvf %s.tar.gz %s --remove-files" %(backup_name,backup_name));
    Msg='-'*30+time.strftime('%Y-%m-%d %H:%M:%S')+'-'*30+'\n'
    writeLogs(logs_path,Msg+"Bacakup database finishded.\n");
elif (param == "staging" ):
    password="xxxx2011"
elif (param == "prod"):
    password="xxxx2014"
time.sleep(4);
print "#"*60;

print ("backup application war and update svn programme start..........");
resource="/data/src/laneige"
tomcat_home="/opt/app/tomcat"
webapps="/opt/app/tomcat/webapps"
backup_cmd="cp  %s/laneige_Web.war %s/laneige_Web_%s.war" %(webapps, backup_war_path,current_datetime);
os.system(backup_cmd);
time.sleep(6);
svn_cmd="cd %s;svn up" %(resource);
os.system(svn_cmd);
time.sleep(3);
print ("backup application war and update svn programme end ........");
print "#"*60;

print "compile class file.............begin............."
if (param == "stress" or param == "" or param == "local"):
    mvn_cmd="cd %s;mvn -U clean package -PSTRESS" %(resource);
    os.system(mvn_cmd);
    Msg='-'*30+time.strftime('%Y-%m-%d %H:%M:%S')+'-'*30+'\n'
    writeLogs(logs_path,Msg+"Complie all java files to generate war.\n");
elif (param == "staging" ):
    mvn_cmd="cd %s;mvn -U clean package -PSTAGING" %(resource);
    os.system(mvn_cmd);
    Msg='-'*30+time.strftime('%Y-%m-%d %H:%M:%S')+'-'*30+'\n'
    writeLogs(logs_path,Msg+"Complie all java files to generate war.\n");
elif (param == "prod"):
    mvn_cmd="cd %s;mvn -U clean package -PPROD" %(resource);
    os.system(mvn_cmd);
    Msg='-'*30+time.strftime('%Y-%m-%d %H:%M:%S')+'-'*30+'\n'
    writeLogs(logs_path,Msg+"Complie all java files to generate war.\n");
time.sleep(2);
print "compile class file.............end............."
print "="*60;

source_war="/data/src/laneige/laneige-web/target/laneige_Web.war"
target_path="/data/src/temp1";
print "start application server.............begin............."
if (param == "stress" or param == "" or param == "local"):
    kill_cmd="kill `ps -ef | grep tomcat | awk '{print $2,$8}' | grep 'java$'| awk '{print $1}'`";
    os.system(kill_cmd);
    time.sleep(3);
    os.system("rm -rf %s/laneige_Web*" %(webapps));
    time.sleep(3);
    os.system("cp -rf %s %s/" %(source_war,webapps));
    time.sleep(3);
    os.system("%s/bin/startup.sh " %(tomcat_home));
    time.sleep(3);
    Msg='-'*30+time.strftime('%Y-%m-%d %H:%M:%S')+'-'*30+'\n'
    writeLogs(logs_path,Msg+"Deploy finished.\n");
elif (param == "staging" ):
    scp_cmd="scp -P 1122 %s root@192.168.10.125:%s" %(source_war, target_path);
    os.system(scp_cmd);
    Msg='-'*30+time.strftime('%Y-%m-%d %H:%M:%S')+'-'*30+'\n'
    writeLogs(logs_path,Msg+"Copy to staging finished.\n");
elif (param == "prod"):
    scp_cmd="scp -P 60 %s root@192.168.11.185:%s" %(source_war,target_path);
    os.system(scp_cmd);
    Msg='-'*30+time.strftime('%Y-%m-%d %H:%M:%S')+'-'*30+'\n'
    writeLogs(logs_path,Msg+"Copy to prod finished.\n");
time.sleep(2);
print "start application server.............end............."

