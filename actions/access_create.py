import st2common.runners.base_action
import requests
import json


class AccessCreate(st2common.runners.base_action.Action):

    def __init__(self, config):
        super(AccessCreate, self).__init__(config=config)

    def run(self, url, basickey, action, protocol, source, destination,
            dest_port_op, src_port_op, dest_port_start, src_port_start,
            dest_port_end, src_port_end):

        dest_option = {
            "dest-port-op": dest_port_op,
            "dest-port-start": dest_port_start
        }

        src_option = {
            "src-port-op": src_port_op,
            "src-port-start": src_port_start
        }

        l4_options = dest_option if dest_port_op else src_option

        if dest_port_end:
            l4_options["dest-port-end"] = dest_port_end

        if src_port_end:
            l4_options["src-port-end"] = src_port_end

        access = {
            "kind": "object#acl",
            "rules": [
                {
                    "action": action,
                    "protocol": protocol,
                    "source": source,
                    "destination": destination,
                    "l4-options": l4_options
                }
            ]
        }

        access_json = json.dumps(access)

        response = requests.post(
            url=url,
            data=access_json,
            headers={
                "Authorization": "basic "+basickey
            }
        )

        return response.json()






