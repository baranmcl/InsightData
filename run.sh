
apt-get install python-pandas

chmod a+x runningmedian.py
chmod a+x wordcount.py

python wordcount.py ./wc_input ./wc_output/wc_result.txt &
python runningmedian.py ./wc_input ./wc_output/rm_result.txt
