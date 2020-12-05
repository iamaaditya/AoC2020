cat data | sed 's/[F|L]/0/g' | sed 's/[B|R]/1/g' | xargs -n 1 -I {} echo 'ibase=2;obase=1010;{}' | bc | sort -n | tail -n 1
