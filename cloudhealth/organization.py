import json
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


    def update(self, org_id, description):
        uri = '/v2/organizations/{org_id}'
        data = { "description": description }

        organization = self.client.query(
            uri, method='PUT', data=json.dumps(data)
        )

        return organization


    def delete(self, org_id):
        uri = '/v2/organizations/{org_id}'

        response = self.client.query(uri, method='DELETE')

        return response


    def create(self, name, description=None, parent_organization_id=None):
        uri = '/v2/organizations'
        data = { "name": name }

        if description:
            data['description'] = description
        if parent_organization_id:
            data['parent_organization_id'] = parent_organization_id

        organization = self.client.query(
            uri, method='POST', data=json.dumps(data)
        )

        return organization
