from ansible.errors import AnsibleError
from ansible.module_utils._text import to_text, to_native
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display
from google.cloud import secretmanager

display = Display()
secrets = secretmanager.SecretManagerServiceClient()


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):

        self.set_options(var_options=variables, direct=kwargs)

        ret = []
        for term in terms:
            display.vvvv("google_cloud_secret looking up %s" % term)
            try:
                response = secrets.access_secret_version(
                    request={"name": term}
                ).payload.data.decode("utf-8")
            except Exception as e:
                raise AnsibleError("Error %s: %s" % (term, to_native(e)))

            if self.get_option("split_lines"):
                for line in response.read().splitlines():
                    ret.append(to_text(line))
            else:
                ret.append(to_text(response.read()))
        return ret
