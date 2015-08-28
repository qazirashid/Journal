#!/bin/sh
# run this scirpt to push configuration files to git hub after making changes to any configuration files
# The tool will simply add all known config files irrespective of whetehre they were updated or not.

git add .vimrc .emacs .jrnl_config .bashrc
git commit -m "Bash: Auto updating the configs:"
git push origin master
