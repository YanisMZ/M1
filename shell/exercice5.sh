
#!/bin/bash

calculer() {
    n=$1

    for ((i=0; i<nb; i++))
    do
        echo -n "$n "

        if [ $((n % 2)) -eq 0 ]
        then
            n=$((n / 2))
        else
            n=$((3 * n + 1))
        fi
    done
}


echo "Entrez le nombre N :"
read N

echo "Entrez le nombre de termes :"
read nb


calculer $N
