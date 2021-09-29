all: abstract boo govols kirby link mario sans wario

jgraph:
	./setup.sh

abstract: jgraph
	./makepdf.sh ./examples/abstract.png

boo: jgraph
	./makepdf.sh ./examples/boo.bmp

govols: jgraph
	./makepdf.sh ./examples/govols.png

kirby: jgraph
	./makepdf.sh ./examples/kirby.png

link: jgraph
	./makepdf.sh ./examples/link.png

mario: jgraph
	./makepdf.sh ./examples/mario.png

sans: jgraph
	./makepdf.sh ./examples/sans.bmp

wario: jgraph
	./makepdf.sh ./examples/wario.png

clean:
	rm *.pdf *.jpg