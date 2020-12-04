help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

create_setup:
	poetry build
	tar -xvf dist/*.tar.gz --wildcards --no-anchored '*/setup.py' --strip=1
	rm -rf dist

.DEFAULT_GOAL := help
.PHONY: help
