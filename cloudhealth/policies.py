from . import exceptions

class PoliciesClient():

    def __init__(self, client):
        self.client = client

    def list(self, client_api_id=None, page=1, per_page=30):
        uri = '/v1/policies'
        params = [
            ('page', page),
            ('per_page', per_page)
        ]

        if client_api_id:
            params.append(('api_key', client_api_id))

        policies = self.client.query(uri, method='GET', params=params)

        return policies
