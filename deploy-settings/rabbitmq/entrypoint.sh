set -e

apt-get update && apt-get install -y gettext
envsubst < /etc/rabbitmq/definitions.template.json > /etc/rabbitmq/definitions.json

exec docker-entrypoint.sh rabbitmq-server
