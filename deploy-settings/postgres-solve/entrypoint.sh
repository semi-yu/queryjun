set -e

apt-get update && apt-get install -y gettext
envsubst < /docker-entrypoint-initdb.d/template > /docker-entrypoint-initdb.d/init.sql

exec docker-entrypoint.sh postgres
