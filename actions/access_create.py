import st2common.runners.base_action


class AccessCreate(st2common.runners.base_action.Action):

    def __init__(self, config):
        super(AccessCreate, self).__init__(config=config)

    def run (self):

        return [
            self.config.get('url'),
            self.config.get('basickey'),
            self.config.get('action'),
            self.config.get('protocol'),
            self.config.get('source'),
            self.config.get('destination'),
            self.config.get('destPortOp'),
            self.config.get('srcPortOp'),
            self.config.get('destPortStart'),
            self.config.get('srcPortStart'),
            self.config.get('destPortEnd'),
            self.config.get('srcPortEnd'),

        ]




