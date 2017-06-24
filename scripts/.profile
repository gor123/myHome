alias np="/c/Program\ Files\/Notepad++/notepad++.exe"
source git-completion.bash
alias gdiff="git difftool --tool=winmerge -y"
alias difm="'C:/Program Files (x86)/WinMerge/WinMergeU.exe'"
export HISTSIZE=100000
export HISTFILESIZE=100000
history -r /home/gil/history.txt
export PROMPT_COMMAND="history -w /home/gil/history.txt; history -c; history -r /home/gil/history.txt; ${PROMPT_COMMAND}"
