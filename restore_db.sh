#!/bin/bash

user=""
database=""

read -p "user: " user
read -p "database: " database

heroku pg:backups:capture
heroku pg:backups:download

pg_restore --verbose --clean --no-acl --no-owner -h localhost -U $user \
    -d $database latest.dump

rm latest.dump
