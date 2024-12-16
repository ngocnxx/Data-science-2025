from diagrams import Diagram, Cluster
from diagrams.aws.mobile import APIGateway
from diagrams.aws.storage import S3
from diagrams.aws.security import IAMRole
from diagrams.aws.analytics import GlueDataCatalog
from diagrams.aws.management import Cloudformation

with Diagram(
    'Environments', direction='LR', show=False, filename='../content/assets/environments'
):
    with Cluster('DataHub Account (999999999999/ap-southeast-2)'):
        app = APIGateway('APIGateway')

    with Cluster('Environment1 (111111111111/ap-southeast-2)') as env1:
        role1 = IAMRole('AssumedRole')
        stack = Cloudformation('Stacks')
        bucket = S3('Dataset')
        cat = GlueDataCatalog('Catalog ')
        role1 >> stack >> [cat, bucket]

    with Cluster('Environment2 (222222222222/ap-southeast-2)') as env2:
        role2 = IAMRole('AssumedRole')
        stack = Cloudformation('Stacks')
        bucket = S3('Dataset')
        cat = GlueDataCatalog('Catalog ')
        role2 >> stack >> [cat, bucket]

    app >> [role1, role2]
