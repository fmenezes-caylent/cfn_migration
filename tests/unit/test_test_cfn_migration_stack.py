import aws_cdk as core
import aws_cdk.assertions as assertions

from test_cfn_migration.test_cfn_migration_stack import TestCfnMigrationStack

# example tests. To run these tests, uncomment this file along with the example
# resource in test_cfn_migration/test_cfn_migration_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TestCfnMigrationStack(app, "test-cfn-migration")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
