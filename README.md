# image2picross

image2picross is a Python script intended to be used in conjunction with the graphing application jgraph. It converts images into picross (nonogram) puzzles.

### Setup

You can either run `setup.sh` or setup will be done automatically by `makejpg.sh` and `makepdf.sh`. How convenient!

### Usage

Running the makefile will automatically make the examples included with image2picross.

`image2picross.py` is the core script that does most of the work. It will convert an image into a picross puzzle in jgraph format and output it on stdout.
```
python3 image2picross.py [--solution | -s] image
```

`makepdf.sh` will automatically make two PDF files from the puzzle: one unsolved and the other being the solution.
```
sh makepdf.sh image-file
```

`makejpg.sh` will automatically make three JPG files from the puzzle: one unsolved, one being the solution, and one of them side-by-side.
```
sh makejpg.sh image-file
```

Make sure your working directory is the root directory of this repository. All image files should work. For maximum enjoyment, I highly recommend you use lossless formats and keep the dimensions of the image sane (remember: this is a *puzzle*).

### Examples

##### Single-tone

Abstract
![Abstract](/screenshots/abstract.png)