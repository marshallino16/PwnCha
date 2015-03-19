#!/bin/bash

declare count=0
declare maxLoop=100

for (( i=1; i<=maxLoop; ++i ))
do
   echo "[+] run $i"
   va=$(python capcap.py 2>&1)
   #echo $va
   if [[ $va == *"Success."* ]]
     then
        ((count ++))
        echo " --Success"
     else
        echo " --Fail"
   fi

done

let "percent = (count/maxLoop)*100"
let "failed = maxLoop - count"
echo "[+] Benchmark result : $percent %"
echo "Success : $count - Fail : $failed"
