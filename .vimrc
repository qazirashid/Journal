
map <unique> t lbi@<Esc> 

call plug#begin()
Plug 'tpope/vim-sensible'
Plug 'fatih/vim-go'
Plug 'rust-lang/rust.vim'
Plug 'tpope/vim-surround'
call plug#end()

set number
if has('vim_starting')
	set nocompatible
	set runtimepath+=~/.vim/bundle/dart-vim-plugin
endif

filetype plugin indent on
