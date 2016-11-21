#!/usr/bin/env bash

if [ -f intro.md ]; then
    cat intro.md
else
    echo -e "RAPP robots API\n\n"
fi

cd ../includes/rapp-robots-api/

for d in */
do
    dd="$(tr '[:lower:]' '[:upper:]' <<< ${d:0:1})${d:1}"
    dd=${dd::-1}
    cd $d
#    echo -e "$dd module\n\n"
    cat README.md
    cd ..
done
