SUBDIRS := figures

all: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@; \

.PHONY: all $(SUBDIRS)
