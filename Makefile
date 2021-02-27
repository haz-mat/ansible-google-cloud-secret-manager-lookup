.PHONY: test
test:
	ANSIBLE_LOOKUP_PLUGINS="./plugins/lookup" pipenv run \
		ansible-playbook \
		-vvvv \
		test/playbook.yml
