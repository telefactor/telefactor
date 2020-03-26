# tfr game exec-all -- bash -l $(get_absolute_path ./cloc_script.sh)
test_out_dir=$(dirname $BASH_SOURCE)/stats/cloc
mkdir -p "${test_out_dir}"
cloc \
	--exclude-ext='.test.ts' \
	--json \
	--out "${test_out_dir}/$(basename $PWD).json" \
	./src
