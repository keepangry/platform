# web_platform
社交网络抽取算法展示平台

#用 root
# web服务器启动
web/
#在sudo nohup之前，使用一次sudo，并输入密码 
cd web/
nohup python manage.py runserver 104.131.134.29:80 &

#daemon
cd service/coae2008-car/ 
nohup python car_target_daemon.py &
