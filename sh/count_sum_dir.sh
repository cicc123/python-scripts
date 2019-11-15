ls -lRk /usr/lib/python3.6/site-packages/pip|awk '/^-/{if($5>100){count++;sum+=$5}} END{print "count: " count," sum: " sum}'
 awk -F: 'BEGIN{count=0;}{account[count]=$1;count++;}; END{for(i=0;i<NR;i++) print account[i],i}' /etc/passwd
