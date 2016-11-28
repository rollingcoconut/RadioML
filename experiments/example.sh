


ssh -o "StrictHostKeyChecking no" root@node19-2 'nohup python ~/RadioML/usrp_sample_generator.py  --args="addr=192.168.10.2" --freq 2.4e9 --samp-rate 2e6 --rx-gain 30 --ndata 1024 --ntrials=512 -N "example" > /tmp/example.txt 2>&1 &'

sleep 5

ssh -o "StrictHostKeyChecking no" root@node2-1 'nohup /usr/local/share/gnuradio/examples/digital/narrowband/benchmark_tx.py --freq=2.4e9 --bitrate=1e6 --args="type=usrp2" --tx-gain=25 -M 5 > /tmp/example.txt 2>&1 &'

sleep 60

ssh -o "StrictHostKeyChecking no" root@node19-2 bash <<'EOF' 
cat /tmp/example.txt |  awk -F', ' '{print $2}' | gnuplot -p -e "set terminal dumb; plot '<cat'" 
EOF
