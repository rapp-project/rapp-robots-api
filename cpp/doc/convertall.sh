#!/bin/bash

cd docbook
for f in classrapp*
do
    echo $f
    tmp=${f#*robot_1_1}
    clsn=${tmp%.*}
#    echo $tmp
#    echo $clsn
    pandoc -f docbook -t markdown_github $f \
    | tr '\n' '\r' \
    | perl -pe 's|Classes.*?hpp||g' \
    | perl -pe 's|Private.*?hpp||g' \
    | sed 's/\r\([^\r]*\)\r------*/\r#### \1/g' \
    | perl -pe 's|=====\r(.*?)####|=====\r\r####|g' \
    | tr '\r' '\n' \
    | sed 's/\*\*\.\*\*//g' \
    > ${clsn}.md
#    | sed 's/^|---|---|$/\n| Argument | Description |\n|---|---|/g' \
#    | sed 's/^|---|---|---|---|---|$/\n|   |   |   |   |   |\n|---|---|---|---|---|/g' \
#    | sed 's/^|---|---|---|---|---|---|$/\n|   |   |   |   |   |   |\n|---|---|---|---|---|---|/g' \
#    | sed 's/-\\>/\n* /g' \
    cp ${clsn}.md ../../includes/rapp-robots-api/${clsn}/README.md
done

