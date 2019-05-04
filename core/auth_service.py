from requests_oauthlib import OAuth2Session
from core.config import Config

config = Config()
config.parse()


class AuthService(object):

    def __init__(self):
        self.session = self.get_session()

    def authorization_url(self):
        if self.session is None:
            self.session = self.get_session()
        self.session.scope = 'public_repo'
        return self.session.authorization_url(config.get('oauth.url'))[0]

    def get_session(self):
        return OAuth2Session(config.get('client.id'))

    def fetch_token(self, code=None):
        return self.session.fetch_token(token_url=config.get('token.url'),
                                        client_secret=config.get('client.secret'),
                                        code=code)

    def forks(self, token_dict):
        self.session.token = token_dict
        response = self.session.post(
            f'{config.get("api.url")}/repos/{config.get("repo.owner")}/{config.get("repo.name")}/forks'
        )
        self.session = None
        return response


