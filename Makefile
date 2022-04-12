BUILD_DIR=_build/html

html:
	# Check for ipynb files in source (should all be .Rmd).
	if compgen -G "*.ipynb" 2> /dev/null; then (echo "ipynb files" && exit 1); fi
	jupyter-book build .

clean:
	rm -rf _build

rm-ipynb:
	rm -rf */*.ipynb

github: html
	cp CNAME $(BUILD_DIR)
	ghp-import -n $(BUILD_DIR) -p -f
	./_scripts/check_pushed.sh
