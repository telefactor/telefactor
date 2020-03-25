# tfr game exec-all -- bash -l $(get_absolute_path ./test_script.sh)
nvm version
npm install --silent --offline

test_out_dir=$(dirname $BASH_SOURCE)/stats/tests
mkdir -p "${test_out_dir}"
npm run test -- --json --outputFile "${test_out_dir}/$(basename $PWD).json"
