import yaml
from box import ConfigBox

def read_yaml(path):
    with open(path) as yaml_file:
        content = yaml.safe_load(yaml_file)
        return ConfigBox(content)
    

res = read_yaml(r'E:\Projects\recommender_system\config\config.yaml')       
print(res)