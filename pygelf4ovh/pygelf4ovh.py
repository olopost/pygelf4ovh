from pygelf import GelfTlsHandler,GelfTcpHandler, gelf


class GelfOVHHandler(GelfTcpHandler):
    """
    Class to adapt OVH Log management platform
    """
    def __init__(self, host, port, ovh_token, **kwargs):
        self.ovh_token = ovh_token
        GelfTcpHandler(host, port, **kwargs)

    def convert_record_to_gelf(self, record):
        l = gelf.make(record, self.domain, self.debug, self.version,
                    self.additional_fields, self.include_extra_fields)
        l.update({"_X-OVH-TOKEN": self.ovh_token})
        return gelf.pack(l,self.compress, self.json_default)

if __name__ == "__main__":
    pass