call plug#begin('~/.vim/plugged')

Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
Plug 'ryanoasis/vim-devicons'
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'dylanaraps/wal.vim'
" Plug 'yuttie/comfortable-motion.vim'

" Initialize plugin system
call plug#end()


" Nerd tree stuff
set encoding=UTF-8
nnoremap <C-n> :NERDTreeToggle<CR>
" Exit Vim if NERDTree is the only window left.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() |
    \ quit | endif

" Airline
let g:airline_powerline_fonts = 1
"let g:airline_theme='atomic'

" Ctrl-p (fork)
set runtimepath^=~/.config/nvim/ctrlp.vim

" General
colorscheme wal


