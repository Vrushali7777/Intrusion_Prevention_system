import pandas as pd
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.metrics import accuracy_score
import joblib
import os

columns = [
"duration","protocol_type","service","flag","src_bytes","dst_bytes",
"land","wrong_fragment","urgent","hot","num_failed_logins",
"logged_in","num_compromised","root_shell","su_attempted","num_root",
"num_file_creations","num_shells","num_access_files","num_outbound_cmds",
"is_host_login","is_guest_login","count","srv_count","serror_rate",
"srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
"diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
"dst_host_same_srv_rate","dst_host_diff_srv_rate",
"dst_host_same_src_port_rate","dst_host_srv_diff_host_rate",
"dst_host_serror_rate","dst_host_srv_serror_rate",
"dst_host_rerror_rate","dst_host_srv_rerror_rate",
"label","difficulty"
]

train = pd.read_csv("../dataset/KDDTrain+.txt", names=columns)
test = pd.read_csv("../dataset/KDDTest+.txt", names=columns)

train['label'] = train['label'].str.strip('.')
test['label'] = test['label'].str.strip('.')

features = ['src_bytes','dst_bytes','count','srv_count']

X_train = train[features]
X_test = test[features]

y_train = train['label']
y_test = test['label']

ml_model = RandomForestClassifier(n_estimators=100)
ml_model.fit(X_train, y_train)

pred = ml_model.predict(X_test)

print("Accuracy:", accuracy_score(y_test,pred))

anomaly_model = IsolationForest(contamination=0.02)
anomaly_model.fit(X_train)

os.makedirs("../models",exist_ok=True)

joblib.dump(ml_model,"../models/ml_model.pkl")
joblib.dump(anomaly_model,"../models/anomaly_model.pkl")

print("Models saved")