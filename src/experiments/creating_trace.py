import sys

def generate_trace(rate_mbps, duration_secs, outfile):
    pkt_size_bytes = 1500
    bits_per_packet = pkt_size_bytes * 8
    packets_per_sec = (rate_mbps * 1e6) / bits_per_packet
    interval_ms = 1000.0 / packets_per_sec

    current_time = 0.0
    end_time = duration_secs * 1000  # millisecondss

    with open(outfile, 'w') as f:
        while current_time < end_time:
            f.write('%d\n' % int(current_time))
            current_time += interval_ms

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python2 make_trace.py <rate_mbps> <duration_secs> <outfile>")
        sys.exit(1)

    rate = float(sys.argv[1])
    duration = int(sys.argv[2])
    output_file = sys.argv[3]
    generate_trace(rate, duration, output_file)

