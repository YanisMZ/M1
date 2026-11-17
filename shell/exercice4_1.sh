#!/bin/bash

tab=("$@")

for ((i=0; i<$#; i++))
do
    for ((j=i+1; j<$#; j++))
    do
        if [ ${tab[i]} -lt ${tab[j]} ]
        then
            temp=${tab[i]}
            tab[i]=${tab[j]}
            tab[j]=$temp
        fi
    done
done

echo "${tab[@]}"
