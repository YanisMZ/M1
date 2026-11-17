#!/bin/bash

tab=($(cat "$1"))

for ((i=0; i<${#tab[@]}; i++))
do
    for ((j=i+1; j<${#tab[@]}; j++))
    do
        if [ ${tab[i]} -gt ${tab[j]} ]
        then
            temp=${tab[i]}
            tab[i]=${tab[j]}
            tab[j]=$temp
        fi
    done
done

echo "${tab[@]}"
