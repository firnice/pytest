#!/usr/bin/python
###python script automatic deploy application server
###2015-06-04  python 2.7
###liyiliang

import sys, os, time, shutil, filecmp,commands,subprocess

print ("start   .......");
backup_war_path = "/usr/local/tomcat/bak"
logs_path = '/tmp/log.log'
current_date = time.strftime('%Y-%m-%d')
current_datetime = time.strftime('%Y%m%d%H%M%S')
tomcat_home = "/usr/local/tomcat"
filename = "gms"


(tmp,path) = commands.getstatusoutput('pwd')
source_war = "%s/%s.war" % (path,filename);
print ("source_war   .......");


def writeLogs(filename, contents):
    f = open(filename, 'a+');
    f.write(contents);
    f.close();

def backfile(sourcePath,backPath,fileName):
    if os.path.isfile("%s/%s.war" % (sourcePath, fileName)):
        backup_cmd = "cp  %s/%s.war %s/%s.%s.war" % (sourcePath, fileName,backPath, fileName,current_datetime);
        os.system(backup_cmd);
        time.sleep(6);
        print "#" * 60;
    else:
        print("%s.war not exists" % filename)

if not os.path.exists(backup_war_path):
    Msg = '-' * 30 + time.strftime('%Y-%m-%d,%H:%M:%S') + '-' * 30 + '\n'
    if (os.mkdir(backup_war_path)) == None:
        Msg += '** succeed to create dir:' + backup_war_path + '\n'
        writeLogs(logs_path, Msg)
    else:
        Msg += '!! create backup dir:' + backup_war_path + 'failed,check whether dir can write! nn'
        writeLogs(logs_path, Msg)
    sys.exit()

print ("backup application war..........");
backfile("%s/webapps" % (tomcat_home),backup_war_path,filename)
backfile(path,path,filename)


# if os.path.isfile("%s/webapps/%s.war" % (tomcat_home, filename)):
#     backup_cmd = "cp  %s/webapps/%s.war %s/%s.%s.war" % (tomcat_home, filename,backup_war_path, filename,current_datetime);
#     os.system(backup_cmd);
#     time.sleep(6);
#     print "#" * 60;
# else:
#     print("%s.war not exists" % filename)








print "start application server.............begin............."
print source_war
kill_cmd = "kill `ps -ef | grep tomcat |awk '{print $2,$8,$9}'|grep 'java'|grep 'tomcat'| awk '{print $1}'`";
os.system(kill_cmd);
time.sleep(3);
os.system("rm -rf %s/webapps/%s*" % (tomcat_home,filename));
time.sleep(3);
os.system("cp -rf %s %s/webapps" % (source_war, tomcat_home));
time.sleep(3);
os.system("%s/bin/startup.sh " % (tomcat_home));
time.sleep(3);
Msg = '-' * 30 + time.strftime('%Y-%m-%d %H:%M:%S') + '-' * 30 + '\n'
writeLogs(logs_path, Msg + "Deploy finished.\n");
time.sleep(2);
print "start application server.............end............."

