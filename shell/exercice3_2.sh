#!/bin/bash


case "$1" in
    *[!0-9]*)
        echo "La chaîne contient autre chose que des chiffres."
        ;;
    *)
        echo "La chaîne est composée uniquement de chiffres."
        ;;
esac
