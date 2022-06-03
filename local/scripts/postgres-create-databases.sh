#!/usr/bin/env bash

##  postgres-create-databases.sh
##
##  Script to be used to initialize the databases for the project. 
##  To use it we need to set $POSTGRES_CUSTOM_MULTI_DB with all the
##  databases we want to create separeted by ',' e.g.:
##
##  'export POSTGRES_CUSTOM_MULTI_DB=dev,test'.

# bash default parameters
set -o errexit  # make your script exit when a command fails
set -o pipefail # exit status of the last command that threw a non-zero exit code is returned
set -o nounset  # exit when your script tries to use undeclared variables

# check binaries
PSQL=$(which psql)
TR=$(which tr)

function create_user_and_database() {

	local database=$1

	# create db and grant privileges
	$PSQL -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
	    CREATE DATABASE $database;
	    GRANT ALL PRIVILEGES ON DATABASE $database TO $POSTGRES_USER;
EOSQL

}

if [ -n "$POSTGRES_CUSTOM_MULTI_DB" ]; then

	# need to create databases
	echo "Multiple database creation requested: $POSTGRES_CUSTOM_MULTI_DB"
	
	# create databases
	for db in $(echo $POSTGRES_CUSTOM_MULTI_DB | $TR ',' ' '); do
		create_user_and_database $db
	done
	echo "Multiple databases created"

fi
