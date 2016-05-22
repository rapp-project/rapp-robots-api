#!/bin/bash

cd pandoc
for f in classrapp*
do
    echo $f
    tmp=${f#*robot_1_1}
    clsn=${tmp%.*}
#    echo $tmp
#    echo $clsn
    pandoc -f docbook -t markdown_github $f \
    | sed 's/^|---|---|$/\n| Argument | Description |\n|---|---|/g' \
    | sed 's/^|---|---|---|---|---|$/\n|   |   |   |   |   |\n|---|---|---|---|---|/g' \
    | sed 's/^|---|---|---|---|---|---|$/\n|   |   |   |   |   |   |\n|---|---|---|---|---|---|/g' \
    | sed 's/-\\>/\n* /g' \
    | tr '\n' '\r' \
    | sed 's/\r\([^\r]*\)\r------*/\r#### \1/g' \
    | perl -pe 's|=====\r(.*?)####|=====\r\r####|g' \
    | tr '\r' '\n' \
    > ${clsn}.md
    cp ${clsn}.md ../includes/rapp-robots-api/{clsn}/README.md
done

