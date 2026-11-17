#!/bin/bash

echo "Entrez un caractère :"
read c

case "$c" in
    [a-z])
        echo "C'est une lettre minuscule."
        ;;
    [A-Z])
        echo "C'est une lettre majuscule."
        ;;
    [0-9])
        echo "C'est un chiffre."
        ;;
    *)
        echo "Ce n'est ni une lettre ni un chiffre."
        ;;
esac

