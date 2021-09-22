from behave import *
import behave_direction

@given('I have a direction')
def step_impl(context):
    pass

@when('I check {num}')
def step_impl(context, num):
    context.result = behave_direction.direction(num)

@then('The result should be {result}')
def step_impl(context, result):
    assert context.result == result, "value returned: %s" % context.result