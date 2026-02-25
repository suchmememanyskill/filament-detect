.PHONY: install-u1

install-u1:
ifndef DESTDIR
	$(error DESTDIR is required. Usage: make install-u1 DESTDIR=/path/to/destination)
endif
	mkdir -p $(DESTDIR)
	cp -r . $(DESTDIR)
