


call plug#begin()
Plug 'tpope/vim-sensible'
Plug 'fatih/vim-go'
call plug#end()

set number
if has('vim_starting')
	set nocompatible
	set runtimepath+=~/.vim/bundle/dart-vim-plugin
endif
filetype plugin indent on
