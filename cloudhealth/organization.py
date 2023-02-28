from . import exceptions

class OrganizationClient():

    def __init__(self, client):
        self.client = client

    def list(self, page=None, per_page=None, org_id=None):
        uri = '/v2/organizations'
        params = []

        if page:
            params.append(('page', page))
        if per_page:
            params.append(('per_page', per_page))
        if org_id:
            params.append(('org_id', org_id))

        organizations = self.client.query(uri, method='GET', params=params)

        return organizations

