import configparser


def read_login_config(file_path, profile_name):
    config = configparser.ConfigParser()
    config.read(file_path)

    if profile_name in config:
        return config[profile_name]
    else:
        raise ValueError(
            f"Profile '{profile_name}' not found in the configuration file."
        )
