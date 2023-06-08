PREFIX = /usr

all:
	@echo Run \'make install\' to install eff.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p eff.sh $(DESTDIR)$(PREFIX)/bin/eff
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/eff
	@cp -p conv.py $(DESTDIR)$(PREFIX)/bin/effpy
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/effpy


uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/eff
	@rm -rf $(DESTDIR)$(PREFIX)/bin/effpy
