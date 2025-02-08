set AIRFLOW_UID=50000
docker compose up -d
docker compose down



docker run --name phpmyadmin_container \
  --network airflow_default \
  -e PMA_HOST=mysql_container \
  -p 8087:80 \  # Map host port 8087 → container port 80
  -d phpmyadmin/phpmyadmin

docker run --name phpmyadmin_container --network airflow_default -e PMA_HOST=mysql_container -p 8087:80 -d phpmyadmin/phpmyadmin


docker stop mysql_container
docker rm mysql_container

docker run --name mysql_container --network airflow_default -e MYSQL_ROOT_PASSWORD=1234567890 -d mysql

# connect mysql
docker exec -it mysql_container mysql -u root -p
# Enter password: 1234567890

# Update Root User:
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '1234567890'; FLUSH PRIVILEGES;

----------------

docker-compose down -v

docker-compose up -d --build

--------
