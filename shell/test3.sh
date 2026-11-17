#!/bin/bash
c=0
function carre
{
	c=$((a*a))
}

a=5
carre $a
echo "le carre de $a est : $c"

