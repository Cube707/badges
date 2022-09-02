.PHONY: tests build badges


# default target
all: tests pre-commit build


test tests:
	@pytest

pre-commit precommit:
	@pre-commit run -a

build pack badges:
	@python -m build .
