.PHONY: install

install:
ifndef DESTDIR
	$(error DESTDIR is required. Usage: make install DESTDIR=/path/to/destination)
endif
	mkdir -p $(DESTDIR)
	cp -r ./src/* $(DESTDIR)
