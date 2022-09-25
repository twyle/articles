#!/bin/sh

rm -f .env


flask_app=$(curl  -H "X-Vault-Token: $VAULT_TOKEN" \
        -X GET http://127.0.0.1:8200/v1/kv/vault-secret-management/local/flask_app)

echo FLASK_APP=$(echo $flask_app | jq -r .data.FLASK_APP) >> .env

flask_env=$(curl  -H "X-Vault-Token: $VAULT_TOKEN" \
        -X GET http://127.0.0.1:8200/v1/kv/vault-secret-management/local/flask_environment)

echo FLASK_ENV=$(echo $flask_env | jq -r .data.FLASK_ENV) >> .env

secret_key=$(curl  -H "X-Vault-Token: $VAULT_TOKEN" \
        -X GET http://127.0.0.1:8200/v1/kv/vault-secret-management/local/secret_key)

echo SECRET_KEY=$(echo $secret_key | jq -r .data.SECRET_KEY) >> .env

postgres_host=$(curl  -H "X-Vault-Token: $VAULT_TOKEN" \
        -X GET http://127.0.0.1:8200/v1/kv/vault-secret-management/local/postgres_host)

echo POSTGRES_HOST=$(echo $postgres_host | jq -r .data.POSTGRES_HOST) >> .env

postgres_db=$(curl  -H "X-Vault-Token: $VAULT_TOKEN" \
        -X GET http://127.0.0.1:8200/v1/kv/vault-secret-management/local/postgres_db)

echo POSTGRES_DB=$(echo $postgres_db | jq -r .data.POSTGRES_DB) >> .env

postgres_port=$(curl  -H "X-Vault-Token: $VAULT_TOKEN" \
        -X GET http://127.0.0.1:8200/v1/kv/vault-secret-management/local/postgres_port)

echo POSTGRES_PORT=$(echo $postgres_port | jq -r .data.POSTGRES_PORT) >> .env

postgres_user=$(curl  -H "X-Vault-Token: $VAULT_TOKEN" \
        -X GET http://127.0.0.1:8200/v1/kv/vault-secret-management/local/postgres_user)

echo POSTGRES_USER=$(echo $postgres_user | jq -r .data.POSTGRES_USER) >> .env

postgres_password=$(curl  -H "X-Vault-Token: $VAULT_TOKEN" \
        -X GET http://127.0.0.1:8200/v1/kv/vault-secret-management/local/postgres_password)

echo POSTGRES_PASSWORD=$(echo $postgres_password | jq -r .data.POSTGRES_PASSWORD) >> .env