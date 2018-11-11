site:
	mkdir -p docs
	rm -f docs/*.html
	pipenv run ./make.py
	cp style.css docs
	mkdir -p docs/img
	cp img/* docs/img
