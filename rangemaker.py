def ip_to_int(ip):
    """Convert IP to integer."""
    a, b, c, d = map(int, ip.split('.'))
    return (a << 24) | (b << 16) | (c << 8) | d

def int_to_ip(val):
    """Convert integer back to IP."""
    return '.'.join(str((val >> shift) & 0xFF) for shift in (24, 16, 8, 0))

def get_ip_ranges(ips):
    """Group IPs into ranges."""
    ips = sorted(map(ip_to_int, ips))
    ranges = []
    start = ips[0]
    end = start

    for ip in ips[1:]:
        if ip == end + 1:
            end = ip
        else:
            ranges.append((start, end))
            start = end = ip
    ranges.append((start, end))
    return ranges

def valid_ip(ip):
    """Check if a given IP is valid."""
    octets = ip.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        try:
            num = int(octet)
        except ValueError:
            return False
        if num < 0 or num > 255:
            return False
    return True

def display_ranges(ip_ranges):
    """Write IP ranges to output file."""
    with open('outputmaker.txt', 'w') as out_file:
        for start, end in ip_ranges:
            if start == end:
                out_file.write(int_to_ip(start) + '\n')
            else:
                out_file.write(f"{int_to_ip(start)} - {int_to_ip(end)}\n")

if __name__ == '__main__':
    with open("ip_addresses.txt", "r") as file:
        raw_ips = [line.strip() for line in file]

    ips = []
    for ip in raw_ips:
        if valid_ip(ip):
            ips.append(ip)
        else:
            print(f"Warning: Skipped invalid IP address format: {ip}")

    ip_ranges = get_ip_ranges(ips)
    display_ranges(ip_ranges)
