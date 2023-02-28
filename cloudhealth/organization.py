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
        uri = f'/v2/organizations/{org_id}'
        data = { "description": description }

        organization = self.client.query(
            uri, method='PUT', data=json.dumps(data)
        )

        return organization


    def delete(self, org_id):
        uri = f'/v2/organizations/{org_id}'

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


    def assign_accounts(self, aws_accounts=None, azure_subscriptions=None, gcp_compute_projects=None, data_center_accounts=None, replace=False):
        if replace:
            uri = f'/v2/organizations/{org_id}'
        else:
            uri = f'/v2/organizations/{org_id}/accounts'

        data = { "accounts":"add" }

        if not (aws_accounts or 
                azure_subscriptions or 
                gcp_compute_projects or
                data_center_accounts):
            raise exceptions.CloudHealthError('You must pass at least one of the parameters.')

        if aws_accounts:
            data['aws_accounts'] = aws_accounts
        if azure_subscriptions:
            data['azure_subscriptions'] = azure_subscriptions
        if gcp_compute_projects:
            data['gcp_compute_projects'] = gcp_compute_projects
        if data_center_accounts:
            data['data_center_accounts'] = data_center_accounts

        organization = self.client.query(
            uri, method='PUT', data=json.dumps(data)
        )

        return organization


    def get_accounts(self, org_id, cloud_account, page=None, per_page=30, query=None, sort=None, is_down=False):
        uri = f'/v2/organizations/{org_id}/{cloud_account}'
        params = [
            ('per_page', per_page),
            ('is_down', is_down)
        ]

        if page:
            params.append(('page', page))
        if query:
            params.append(('query', query))
        if sort:
            params.append(('sort', sort))

        accounts = self.client.query(uri, method='GET', params=params)

        return accounts
