from scapy.all import IP

def extract_features(packet):

    if packet.haslayer(IP):

        src_bytes = len(packet)
        dst_bytes = len(packet)

        count = 1
        srv_count = 1

        return [src_bytes,dst_bytes,count,srv_count]

    return None