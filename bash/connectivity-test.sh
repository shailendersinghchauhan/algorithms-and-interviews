#!/bin/bash
for i in `cat host_list.txt`
#for((i=0;i<=$TOTAL_SERVER;i++))
do
SERVER=$(echo $i|cut -f '1' -d ",")
PORT=$(echo $i|cut -f '2' -d ",")
echo $SERVER and $PORT

STATUS=0
#STATUS=$(nc -v $SERVER $PORT)

if [ $STATUS -eq 0 ];then
        echo "Able to connect $SERVER on $PORT"
else
        echo "Unable to connect on $SERVER on $PORT"
fi
done
