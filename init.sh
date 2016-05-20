sudo rm -r /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo rm -r /etc/gunicorn.d/*
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo ln -sf /home/box/web/etc/qa.py   /etc/gunicorn.d/qa.py
sudo /etc/init.d/gunicorn restart