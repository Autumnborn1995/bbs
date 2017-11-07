初次部署应注意：

sudo apt-get install nginx
安装 uwsgi 的依赖包
sudo apt-get install libpcre3 libpcre3-dev
pip install uwsgi
pip install supervisor

bbs_nginx.conf 是 nginx 的配置文件，移到 /etc/nginx/conf.d 下面去
从 /etc/nginx 目录下复制一份 uwsgi_params 到 /home/bbs 下
bbs_uwsgi.ini 是 uwsgi 的配置文件，更改相应内容
bbs_supervisor.conf 是 supervisor 的配置文件，更改相应内容

在 /home/venv 下创建虚拟环境
在虚拟环境里用 pip install -r bbs_requirements.txt 安装依赖

创建数据库
更改 app.py 里 db_config 的相应内容

初始、迁移数据库
python3 app.py db init
python3 app.py db migrate
python3 app.py db upgrade

其他命令
测试 nginx 是否配置好了
sudo service nginx configtest
运行 uwsgi ，测试用
uwsgi --ini bbs_uwsgi.ini


启动
sudo service nginx start
supervisord -c bbs_supervisord.conf
