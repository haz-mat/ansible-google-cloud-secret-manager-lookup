.PHONY: test
test:
ifndef GOOGLE_CLOUD_PROJECT_ID
	$(error GOOGLE_CLOUD_PROJECT_ID must be defined)
endif
ifndef GOOGLE_CLOUD_SECRET_NAME
	$(error GOOGLE_CLOUD_SECRET_NAME must be defined)
endif
ifndef GOOGLE_CLOUD_SECRET_VERSION
	$(error GOOGLE_CLOUD_SECRET_VERSION must be defined)
endif
	OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES \
	ANSIBLE_LOOKUP_PLUGINS="./plugins/lookup" \
	pipenv run \
		ansible-playbook \
		-vvvv \
		-e google_cloud_project_id=$(GOOGLE_CLOUD_PROJECT_ID) \
		-e google_cloud_secret_name=$(GOOGLE_CLOUD_SECRET_NAME) \
		-e google_cloud_secret_version=$(GOOGLE_CLOUD_SECRET_VERSION) \
		test/playbook.yml
