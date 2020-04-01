import st2common.runners.base_action


class AccessCreate(st2common.runners.base_action.Action):

    def __init__(self, config):
        super(AccessCreate, self).__init__(config=config)

    def run(self, url, basickey, action, protocol, source, destination,
            dest_port_op, src_port_op, dest_port_start, src_port_start,
            dest_port_end, src_port_end):

        return [
            url,
            basickey,
            action,
            protocol,
            source,
            destination,
            dest_port_op,
            src_port_op,
            dest_port_start,
            src_port_start,
            dest_port_end,
            src_port_end,
        ]




