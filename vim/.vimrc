:set hlsearch
:set incsearch

:set autoindent
:set ignorecase
:set tabstop=4
:set shiftwidth=4
:set expandtab

:syntax on
set backspace=indent,eol,start

filetype indent on
filetype plugin on

let g:neocomplcache_enable_at_startup = 1
" <TAB>: completion.
inoremap <expr><TAB>  pumvisible() ? "\<C-n>" : "\<TAB>"
" :highlight MatchParen ctermbg=white
" :highlight Normal ctermfg=grey ctermbg=white

set noswapfile
:set laststatus=2 " Status bar

set statusline=%t       "tail of the filename
set statusline+=[%{strlen(&fenc)?&fenc:'none'}, "file encoding
set statusline+=%{&ff}] "file format
set statusline+=%h      "help file flag
set statusline+=%m      "modified flag
set statusline+=%r      "read only flag
set statusline+=%y      "filetype
set statusline+=%=      "left/right separator
set statusline+=%c,     "cursor column
set statusline+=%l/%L   "cursor line/total lines
set statusline+=\ %P    "percent through file

" colorscheme solarized
" set term=xterm-256color
" let g:solarized_termcolors=256
" set background=light

:nnoremap <s-tab> :tabprevious<cr>
:nnoremap <tab> :tabnext<cr>
:nnoremap <c-t> :tabnew<cr>
:nnoremap <leader>w :tabclose<cr>
:nnoremap <leader>s :w<cr>
:nnoremap <c-n> :set invrelativenumber<cr>
:nnoremap <s-down> :m+1<cr>
:nnoremap <s-up> :m-2<cr>

" :nnoremap <leader>ff :let ln=line('.')<cr>:%!~/Documents/js-beautify/python/js-beautify -i<cr>:<c-r>=ln<cr><cr>:unlet ln<cr>
