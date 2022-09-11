netstat /b /n 
sudo systemctl status postgres

#remove
dpkg -l | grep postgres

yannick@ubuntu:~$ sudo apt-get --purge remove  pgdg-keyring
#
service --status-all

#
https://www.liquidweb.com/kb/how-to-remove-postgresql/
https://www.liquidweb.com/kb/how-to-remove-postgresql/
#
anaconda removal
conda remove --force postgresql
#remove files
rm -rf folder
#
error
psql: could not connect to server: No such file or directory Is the server running locally and accepting connections on Unix domain socket "/var/run/postgresql/.s.PGSQL.5432"?

This error generally means that the server is not running. Based on dpkg -l output and the thread of comments, it was due to the postgresql-9.5 main package being somehow uninstalled. Since the uninstall hasn't been called with the --purge option to dpkg, the data and configuration files are still there, so apt-get install postgresql-9.5 can fix the problem
