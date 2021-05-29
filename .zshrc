# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
setopt appendhistory autocd nomatch
unsetopt beep
bindkey -e
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/ciga/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall


# Import colorscheme from 'wal' asynchronously
# &   # Run the process in the background.
# ( ) # Hide shell job control messages.
# Not supported in the "fish" shell.
#(cat ~/.cache/wal/sequences &)

# Alternative (blocks terminal for 0-3ms)
#cat ~/.cache/wal/sequences

# To add support for TTYs this line can be optionally added.
#source ~/.cache/wal/colors-tty

# alias
alias ls='exa'


# Import the colors.
#. "${HOME}/.cache/wal/colors.sh"

# Create the alias.
alias dmenu='dmenu_run -nb "$color0" -nf "$color15" -sb "$color1" -sf "$color15"'

# path
PATH=$PATH:/home/ciga/builds/qe-6.7/bin
PATH=$PATH:/home/ciga/.local/bin
PATH=$PATH:/snap/bin
PATH=$PATH:/var/lib/flatpak/exports/bin
fpath+=($fpath '/usr/local/lib/nodejs/lib/node_modules/purer-prompt/functions')

# prompt 
autoload -U promptinit; promptinit
prompt purer

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
source /home/ciga/builds/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# fix ranger
unset LINES
unset COLUMNS
