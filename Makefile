.PHONY: test
test:
	OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES \
	ANSIBLE_LOOKUP_PLUGINS="./plugins/lookup" \
	pipenv run \
		ansible-playbook \
		-vvvv \
		test/playbook.yml
