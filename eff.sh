#!/bin/bash

if [[ -d /home/$USER/Pictures/eff ]]; then
  echo "AWESOME! dir [~/Pictures/eff/] already exists."
else
  mkdir /home/$USER/Pictures/eff
  echo "dir [~/Pictures/eff/] has been created successfully!"
fi

if [[ -z $1 ]]; then
  effpy
else
  effpy $1
fi
