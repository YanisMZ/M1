#!/bin/bash
function somme
{
	((s=$1+$2))
	echo $s
}

a=5
b=4
echo "la somme de $a et $b :"
somme $a $b

