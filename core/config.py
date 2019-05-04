import os
import json


class Config(object):
    _configs = None
    _env = 'default'
    _cache = dict()

    def __init__(self):
        env_file_path = "./.env"

        if os.path.isfile(env_file_path):
            with open(env_file_path) as env_file:
                env = env_file.readline().strip('\t\n\r')
                if os.path.exists('./properties/%s.json' % env):
                    self._env = env

    def parse(self):

        if Config._configs is None:
            with open('./properties/%s.json' % self._env) as config_file:
                Config._configs = json.load(config_file)

    def get(self, key):
        self.parse()
        return self._configs[key]

    def get_cache(self):
        return Config._cache
