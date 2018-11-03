site:
	mkdir -p docs
	rm -f docs/*.html
	./make.py
	cp style.css docs
