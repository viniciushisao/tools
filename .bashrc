alias gitp="git checkout develop; git pull origin develop --rebase; git fetch --all"
alias gitm="git checkout master; git pull origin master --rebase; git fetch --all"
alias gits="git status"
alias gitd="git diff --color --color-words --abbrev --no-prefix "

parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
     }
export PS1="\u@\h \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "

export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad
alias l="ls -lah"
