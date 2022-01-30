for i in {1..20}
do
   echo $i
   mv 10/* .
   cd ../..
   make run_send >> hecate/Final/nohecate_sx.txt
   cd hecate/Final/
   mv *.txt 10/
   cd ../..
   make run_sender_receive
   cd hecate/Final/
   rm nohecate_rx_end.txt nohecate_rx_start.txt
done
