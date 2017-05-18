RM = rm -f
SVG2PDF = inkscape -z -A $@
#SVG2PDF = cairosvg -f pdf -o $@
PDF := cycles.pdf dummies.pdf dummies2.pdf thermocycle.pdf sire_histogram.pdf \
       SI_sire_allbonds_relabs.pdf SI_sire_constraints.pdf amber-dist.pdf

all: ${PDF}

%.pdf: %.svg
	${SVG2PDF} $(realpath $<)

%.pdf: %.agr
	xmgrace -hardcopy -hdevice EPS -printfile tmp.eps $<
	epstopdf tmp.eps $@
	rm tmp.eps

clean:
	${RM} ${PDF}

.PHONY: all clean
