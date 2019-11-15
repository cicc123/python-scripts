#!/bin/bash
for n in `seq 10`
do
        name=$(echo $RANDOM|md5sum|tr ["0-9"] ["a-j"] |cut -c 2-11)
        touch $(echo $name)
 
done
