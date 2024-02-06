from sklearn.metrics import classification_report, f1_score
import pandas as pd

folder_name = "output_supervised_100"

try: 
    with open(f"{folder_name}/final/p0-i0/eval_logits.txt") as f:
        logits = f.read()
except FileNotFoundError:
    with open(f"{folder_name}/p0-i0/eval_logits.txt") as f:
        logits = f.read()

logits = [(float(i.split(" ")[0]), float(i.split(" ")[1])) for i in logits.split("\n")[:-1]]
y_pred = [0 if i[0] > i[1] else 1 for i in logits]
y_true = pd.read_csv("data/dev.csv", header=None)[1]
print(classification_report(y_true, y_pred, digits=3))