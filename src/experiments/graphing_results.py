import csv
import os

def parse_log(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        headers = next(reader)

        throughput = []
        rtt = []
        loss = []

        for row in reader:
                tput = float(row[1])  # Throughput (Mbps)
                delay = float(row[2])  # RTT (ms)
                loss_rate = float(row[4])  # Loss rate
                throughput.append(tput)
                rtt.append(delay)
                loss.append(loss_rate)

	if throughput:
	   	tput_avg = sum(throughput)/len(throughput)
	else:
		tput_avg = 0
	if rtt:
 		rtt_avg = sum(rtt)/len(rtt)
	else:
		rtt_avg = 0
	if loss:
		loss_avg = sum(loss)/len(loss)
	else:
		loss_avg = 0

    return tput_avg, rtt_avg, loss_avg

def save_summary(protocol, profile, tput, rtt, loss, filename='summary.csv'):
    file_exists = os.path.isfile(filename)
    with open(filename, 'a') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Protocol', 'Profile', 'Avg Throughput (Mbps)', 'Avg RTT (ms)', 'Avg Loss Rate'])
        writer.writerow([protocol, profile, tput, rtt, loss])

def run_summary():
    # Define combinations
    protocols = ['bbr', 'fillp', 'scream']
    profiles = {
        'profile1': '50mbps',  # low-latency, high-bandwidth
        'profile2': '1mbps'    # high-latency, low-bandwidth
    }

    for proto in protocols:
        for profile_name, trace_label in profiles.items():
            downlink_file = 'experiment_logs/{}_downlink_{}.log'.format(proto, trace_label)
            if os.path.exists(downlink_file):
                tput, rtt, loss = parse_log(downlink_file)
                save_summary(proto, profile_name, tput, rtt, loss)
            else:
                print('[!] Missing file: {}'.format(downlink_file))

if __name__ == "__main__":
    run_summary()
