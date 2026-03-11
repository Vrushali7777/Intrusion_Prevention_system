from scapy.all import sniff,IP
import joblib
from datetime import datetime
from feature_extractor import extract_features
from firewall import block_ip

ml_model = joblib.load("../models/ml_model.pkl")
anomaly_model = joblib.load("../models/anomaly_model.pkl")

logfile = "../logs/attacks.log"

def process_packet(packet):

    features = extract_features(packet)

    if features is None:
        return

    ml_prediction = ml_model.predict([features])[0]

    anomaly = anomaly_model.predict([features])[0]

    if ml_prediction != "normal" or anomaly == -1:

        ip = packet[IP].src

        print("Attack detected from",ip)

        block_ip(ip)

        with open(logfile,"a") as f:

            f.write(
            f"{datetime.now()} | {ip} | {ml_prediction} | anomaly={anomaly}\n"
            )

print("IPS running...")

sniff(prn=process_packet,store=False)