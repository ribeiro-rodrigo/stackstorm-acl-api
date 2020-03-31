import st2common.runners.base_action


class AccessCreate(st2common.runners.base_action.Action):

    def __init__(self, config):
        super(AccessCreate, self).__init__(config=config)

    def run(self, url, basickey, action, protocol, source, destination,
            destPortOp, srcPortOp, destPortStart, srcPortStart,
            destPortEnd, srcPortEnd):

        return [
            url,
            basickey,
            action,
            protocol,
            source,
            destination,
            destPortOp,
            srcPortOp,
            destPortStart,
            srcPortStart,
            destPortEnd,
            srcPortEnd,

        ]




