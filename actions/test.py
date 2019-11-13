from st2common.runners.base_action import Action

class TestAction(Action):
    def run(self, name):
        return {'message': 'hello {}'.format(name) }