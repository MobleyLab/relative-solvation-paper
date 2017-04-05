all: cycles.pdf dummies.pdf dummies2.pdf thermocycle.pdf

cycles.pdf: cycles.svg
dummies.pdf: dummies.svg
dummies2.pdf: dummies2.svg
thermocycle.pdf: thermocycle.svg

%.pdf: %.svg
	inkscape -z -A $@ $<

