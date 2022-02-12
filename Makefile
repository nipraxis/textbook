BUILD_DIR=_build/html
RMDS:=$(wildcard [!_]*/*.Rmd)
IPYNBS:=$(patsubst %.Rmd,%.ipynb,$(RMDS))

delete-ipynbs:
	# Delete modified ipynb files to force rebuild from .Rmd
	./_scripts/delete_modified.sh

%.ipynb: %.Rmd
	# Convert newer .Rmd file to ipynb file.
	jupytext --to ipynb $<

html: bibliography delete-ipynbs $(IPYNBS)
	# For ucb_pages module
	( export PYTHONPATH="${PYTHONPATH}:${PWD}" && jupyter-book build . )
	cp CNAME $(BUILD_DIR)


github: html
	ghp-import -n $(BUILD_DIR) -p -f
	./_scripts/check_pushed.sh

clean:
	rm -rf _build

rm-ipynb:
	rm -rf */*.ipynb

BIBLIOGRAPHIES = bib/course_refs.bib

bibliography: $(BIBLIOGRAPHIES)
	cat $(BIBLIOGRAPHIES) > _references.bib
