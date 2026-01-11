import os

for root, _, files in os.walk("benchmarks"):
    for f in files:
        path = os.path.join(root, f)
        if os.path.getsize(path) == 0:
            print("EMPTY FILE:", path)
        else:
            print("OK:", path)