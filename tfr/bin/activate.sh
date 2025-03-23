export PYTHONBREAKPOINT=ipdb.set_trace

alias pe='pipenv'
alias ped='PIPENV_DEV=1 pe'

tfr() {
	pe run tfr "$@"
}

cli() {
	pe run python -m tfr.cli "$@"
}

tests() {
	pe run pytest "$@"
}

console() {
	pe run ipython
}

refresh() {
	source $BASH_SOURCE;
}
