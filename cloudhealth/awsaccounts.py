from . import exceptions

class AwsAccountsClient():

    def __init__(self, client):
        self.client = client

    def enable(self, name, authentication, billing, cost_and_usage_report,
               cloudtrail, cloudwatch, tags, hide_public_fields=True,
               region='global', primary_aws_region='us-east-1', org_id=''):
        uri = '/v1/aws_accounts'
        params = [
            ('org_id', org_id),
        ]
        data = {
			"name": name,
		    "authentication": authentication,
			"billing": billing,
			"cost_and_usage_report" : cost_and_usage_report,
			"cloudtrail": cloudtrail,
			"tags": tags
        }

		account = self.client.query(
            uri, method='POST', data=json.dumps(data), params=params
        )

		return account


