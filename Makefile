projects = \
	visualizations/history_match\
	visualizations/morris_method\


.PHONY: build lint test dev-install install doc
build:
	for project in $(projects); do\
	    make build -C $$project || (echo 'error building' $$project; exit 1)\
	done

lint:
	for project in $(projects); do\
	    make lint -C $$project || exit 1;\
	done

dev-install: build
	make install ARGS=-e;\

test:
	for project in $(projects); do\
	    make test -C $$project || exit 1;\
	done

install: build
	for project in $(projects); do\
		make install ARGS="$(ARGS)" -C $$project || exit 1;\
	done

#doc:
#	cd docs && make html && cd ..
