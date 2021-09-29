# image2picross

image2picross is a Python script intended to be used in conjunction with the graphing application jgraph. It converts images into picross (nonogram) puzzles.

## Setup

You can either run `setup.sh` or setup will be done automatically by `makejpg.sh` and `makepdf.sh`. How convenient!

## Usage

Running the makefile will automatically make the examples included with image2picross.

`image2picross.py` is the core script that does most of the work. It will convert an image into a picross puzzle in jgraph format and output it on stdout.
```
python3 image2picross.py [--solution | -s] path-to-image-file
```

`makepdf.sh` will automatically make two PDF files from the puzzle: one unsolved and the other being the solution.
```
sh makepdf.sh path-to-image-file
```

`makejpg.sh` will automatically make three JPG files from the puzzle: one unsolved, one being the solution, and one of them side-by-side.
```
sh makejpg.sh path-to-image-file
```

Make sure your working directory is the root directory of this repository. All image files should work. For maximum enjoyment, I highly recommend you use lossless formats as having homogeneous sections of color is important for this type of puzzle. Any image type supported by `convert` should work. I tested this with PNG and BMP. The alpha channel of your image will be turned white if you have one.

## Examples

#### Single-tone

Abstract `sh makejpg.sh ./examples/abstract.png`
![Abstract](/screenshots/abstract-merged.jpg)

Go Vols! `sh makejpg.sh ./examples/govols.png`
![Go Vols!](/screenshots/govols-merged.jpg)

Kirby `sh makejpg.sh ./examples/kirby.png`
![Kirby](/screenshots/kirby-merged.jpg)

sans. `sh makejpg.sh ./examples/sans.bmp`
![sans.](/screenshots/sans-merged.jpg)

#### Multi-tone

Mario `sh makejpg.sh ./examples/mario.png`
![Mario](/screenshots/mario-merged.jpg)

Link `sh makejpg.sh ./examples/link.png`
![Link](/screenshots/link-merged.jpg)

Wario `sh makejpg.sh ./examples/wario.png`
![Wario](/screenshots/wario-merged.jpg)

Big Boo `sh makejpg.sh ./examples/boo.bmp`
![Big Boo](/screenshots/boo-merged.jpg)

## What's a picross and how do I solve one?

One of the more popular terms is 'nonogram', but I grew up with Mario's Picross on the Game Boy. Each number corresponds to a group of boxes or pixels in a row or column. In the case of a single-tone puzzle, there's guaranteed to be a space between the group. In the case of multi-tone puzzles, the groups can be touching if they're different colors/shades. You should start out by crossing out every box in rows/columns labeled '0'. Fill out rows/columns with a number equal to the width/height of the puzzle (or if all numbers plus the spaces equal the width/height).