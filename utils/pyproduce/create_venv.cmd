pushd %~dp0
call conda env create -p venv -f environment.yml || exit /B 1
popd