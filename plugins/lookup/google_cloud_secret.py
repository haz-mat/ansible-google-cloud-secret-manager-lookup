from ansible.errors import AnsibleError
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
                raise AnsibleError(e)

            ret.append(response)
        return ret
