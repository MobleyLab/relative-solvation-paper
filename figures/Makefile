all: cycles.pdf dummies.pdf dummies2.pdf thermocycle.pdf sire_histogram.pdf SI_sire_allbonds_relabs.pdf SI_sire_constraints.pdf amber-dist.pdf

cycles.pdf: cycles.svg
dummies.pdf: dummies.svg
dummies2.pdf: dummies2.svg
thermocycle.pdf: thermocycle.svg
sire_histogram.pdf : sire_histogram.svg
SI_sire_allbonds_relabs.pdf : SI_sire_allbonds_relabs.svg
SI_sire_constraints.pdf : SI_sire_constraints.svg
amber-dist.pdf: amber-dist.agr


%.pdf: %.svg
	inkscape -z -A $@ $<

%.pdf: %.agr
	xmgrace -hardcopy -hdevice EPS -printfile tmp.eps $<
	epstopdf tmp.eps $@
	rm tmp.eps
