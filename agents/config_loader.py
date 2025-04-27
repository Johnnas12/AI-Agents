import json
def load_config(config_path="config.json"):
    with open(config_path, "r") as f:
        return json.load(f)


def get_model_config(config, model_name):
    for conf in config:
        if conf["model"] == model_name:
            return conf
    raise ValueError(f"No config found for model {model_name}")

config = load_config("config.json")
model_config = get_model_config(config, "gemini-1.5-pro")
print(model_config)

