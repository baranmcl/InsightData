chmod a+x ./code/runningmedian.py
chmod a+x ./code/wordcount.py

python ./code/wordcount.py ./wc_input ./wc_output/wc_result.txt &
python ./code/runningmedian.py ./wc_input ./wc_output/rm_result.txt
