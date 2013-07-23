set backspace=indent,eol,start
:syntax on
:set autoindent
:set ignorecase
filetype indent on
filetype plugin on
:set hlsearch
:set incsearch
let g:neocomplcache_enable_at_startup = 1

" <TAB>: completion.
inoremap <expr><TAB>  pumvisible() ? "\<C-n>" : "\<TAB>"
" :highlight MatchParen ctermbg=white
" :highlight Normal ctermfg=grey ctermbg=white

set noswapfile
:set laststatus=2

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
