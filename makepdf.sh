#!/bin/sh

if [ ! -f jgraph ]; then
	./setup.sh
fi

FILE=$1

python image2picross.py $FILE | ./jgraph > temp.ps

newBB=$(awk '{
	if($1 == "%%BoundingBox:") {
		split($0, line, " ");
		line[4] += 5;
		line[5] += 5;
		printf("%s %d %d %d %d", line[1], line[2], line[3], line[4], line[5]);
	}
}' temp.ps)
sed -i "3s/.*/$newBB/" temp.ps

ps2pdf -dEPSCrop temp.ps $(basename "${FILE}" ".${FILE##*.}").pdf
rm temp.ps


python image2picross.py -s $FILE | ./jgraph > temp.ps

newBB=$(awk '{
	if($1 == "%%BoundingBox:") {
		split($0, line, " ");
		line[4] += 5;
		line[5] += 5;
		printf("%s %d %d %d %d", line[1], line[2], line[3], line[4], line[5]);
	}
}' temp.ps)
sed -i "3s/.*/$newBB/" temp.ps

ps2pdf -dEPSCrop temp.ps $(basename "${FILE}" ".${FILE##*.}")-solution.pdf
rm temp.ps