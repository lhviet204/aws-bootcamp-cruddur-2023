#!/bin/bash

folder_names=("cicd" "cluster" "db" "frontend" "machine-user" "networking" "service" "sync")

for folder_name in "${folder_names[@]}"
do
    mkdir $folder_name

    touch $folder_name/template.yaml

    touch $folder_name/config.toml
done