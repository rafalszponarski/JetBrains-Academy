import json

data_bus = {}
JSON = json.loads(input())
for block in JSON:
    if block['stop_name'] not in data_bus:
        data_bus[block['stop_name']] = [block['stop_type']]
    else:
        if block['next_stop'] != 0:
            data_bus[block['stop_name']].append(block['stop_type'])

bad = []
for key, value in data_bus.items():
    if len(set(value)) != 1:
        bad.append(key)

print("On demand stops test:")
if bad:
    print(f"Wrong stop type: {sorted(bad)}")
else:
    print("OK")
