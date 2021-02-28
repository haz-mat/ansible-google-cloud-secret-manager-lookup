# ansible-google-cloud-secret-manager-lookup
Ansible lookup plugin that can get the content of a secret from Google Secret
Manager.

## Requirements
- `python3`
- `ansible`
- The `google-cloud-secret-manager` pip package needs to be availabe in your
  python environment
- You need to have a Google Cloud service account with access to a secret
  available to the Google Cloud SDK. Doing `gcloud auth application-default
  login` will set-up one for local usage.

## Example Usage
```yaml
---
- hosts: localhost
  connection: local
  gather_facts: no
  tasks:
  - assert:
      that:
      - google_cloud_project_id is defined
      - google_cloud_secret_name is defined
      - google_cloud_secret_version is defined
  - name: Should succeed and print out secret.
    debug:
      var: lookup('google_cloud_secret', 'projects/'+google_cloud_project_id+'/secrets/'+google_cloud_secret_name+'/versions/'+google_cloud_secret_version)
```

It should also be possible to use as `with_google_cloud_secret` on a task and
provide a list.

## Known issues
- This plugin isn't well tested at all. The Makefile defines a test that should
  be improved.
- For some reason there's an error the author was getting that requires
  `OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES` to be set in order for this to work.
  I get this error otherwise:
  ```
  +[__NSCFConstantString initialize] may have been in progress in another thread
  when fork() was called. We cannot safely call it or ignore it in the fork()
  child process. Crashing instead. Set a breakpoint on
  objc_initializeAfterForkError to debug.
  ```
- Error handling inside the plugin is really minimal and could be improved.
