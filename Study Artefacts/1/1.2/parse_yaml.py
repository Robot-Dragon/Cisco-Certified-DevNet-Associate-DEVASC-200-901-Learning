import yaml

with open("yaml.yaml") as f:
    yaml_data = f.read()
    yaml_dict = yaml.load(yaml_data, Loader=yaml.FullLoader)

print('------raw YAML------')
print(yaml_data)
print('----YAML to dict----')
print(yaml_dict)