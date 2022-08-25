from aws_cdk import (
    Stack,

)
from constructs import Construct
from aws_cdk.cloudformation_include import CfnInclude
import os

class TestCfnMigrationStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cfn_template = CfnInclude(self, "Template",
            template_file=os.path.join(os.getcwd(), "test_cfn_migration/templates/existing_stack.yaml")
        )