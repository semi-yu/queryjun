set -e

apt-get update && apt-get install -y gettext

envsubst < /docker-entrypoint-initdb.d/init.sql > /docker-entrypoint-initdb.d/init_prepared.sql

# PostgreSQL 초기화 실행
exec docker-entrypoint.sh postgres
