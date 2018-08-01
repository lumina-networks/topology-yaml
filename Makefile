help:
	@echo "  clean     removes any unnecessary file"
	@echo "  package   creates a tar.gz file"
	@echo "  deploy    deploys pack on a remote machine, requires arguments user=<user>, host=<ip>, port=<port>, path=<path>"
	@echo "  documentation      render documentation" 

clean:
	rm -Rf topology-yaml.tar.gz topology_yaml.egg-info .pytest_cache .tox; find . -type f -name "*.pyc" -delete

package:
	make clean; tar -zcvf topology-yaml.tar.gz --exclude='.git' --exclude='Makefile' --exclude='.idea' --exclude='.venv' --exclude='.pytest_cache' --exclude='topology-yaml.tar.gz' -C .. ./topology-yaml

deploy:
	make package && \
	cat ./topology-yaml.tar.gz | ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no $(user)@$(host) -p $(port) \
	"tar -zxvf - -C $(path)"
	make clean;

documentation:
	cd docs && make html

