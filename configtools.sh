#!/bin/sh
# pull the configurations files from the origin repository on git-hub.
git pull origin master
#put the config files in home folder where tools will expect to find them.
cp ./.vimrc $HOME/
cp ./.jrnl_config $HOME/
cp ./.emacs $HOME/
#Also update the .bashrc file for exports.
#I have put it here because it exports golang variables $GOPATH and updates $PATH
# to include $GOPATH/bin directory
# Bashrc also updates $PATH for dartlang. Although I might not use dartlang in future.

cp ./.bashrc $HOME/
