.PHONY: test_thread_vs_corutine
test_thread_vs_corutine:
	@echo -n "Run Test thread vs corutine"
	@echo ""
	python -m test1.__init__

.PHONY: test_aiopg_vs_asyncpg
test_aiopg_vs_asyncpg:
	@echo -n "Run Test aioppg vs asyncpg"
	@echo ""
	python -m test2.__init__

.PHONY: test_aiopg_vs_asyncpg_2
test_aiopg_vs_asyncpg_2:
	@echo -n "Run Test aioppg vs asyncpg 2"
	@echo ""
	python -m test3.__init__

.PHONY: off_cpu
off_cpu:
	@echo -n "Off 7 cpu"
	@echo ""
	dmesg | grep CPU
	echo 0 | sudo tee  /sys/devices/system/cpu/cpu1/online
	echo 0 | sudo tee  /sys/devices/system/cpu/cpu2/online
	echo 0 | sudo tee  /sys/devices/system/cpu/cpu3/online
	echo 0 | sudo tee  /sys/devices/system/cpu/cpu4/online
	echo 0 | sudo tee  /sys/devices/system/cpu/cpu5/online
	echo 0 | sudo tee  /sys/devices/system/cpu/cpu6/online
	echo 0 | sudo tee  /sys/devices/system/cpu/cpu7/online
	dmesg | grep CPU

.PHONY: on_cpu
on_cpu:
	@echo -n "On 7 cpu"
	@echo ""
	dmesg | grep CPU
	echo 1 | sudo tee  /sys/devices/system/cpu/cpu1/online
	echo 1 | sudo tee  /sys/devices/system/cpu/cpu2/online
	echo 1 | sudo tee  /sys/devices/system/cpu/cpu3/online
	echo 1 | sudo tee  /sys/devices/system/cpu/cpu4/online
	echo 1 | sudo tee  /sys/devices/system/cpu/cpu5/online
	echo 1 | sudo tee  /sys/devices/system/cpu/cpu6/online
	echo 1 | sudo tee  /sys/devices/system/cpu/cpu7/online
	dmesg | grep CPU


.PHONY: clean
clean:
	@echo -n "Clear temp files"
	@echo -n "\n"
	@rm -rf `find . -name __pycache__`
	@rm -rf `find . -type f -name '*.py[co]' `
	@rm -rf `find . -type f -name '*~' `
	@rm -rf `find . -type f -name '.*~' `
	@rm -rf `find . -type f -name '@*' `
	@rm -rf `find . -type f -name '#*#' `
	@rm -rf `find . -type f -name '*.orig' `
	@rm -rf `find . -type f -name '*.rej' `
	@rm -rf .coverage
	@rm -rf coverage.html
	@rm -rf coverage.xml
	@rm -rf htmlcov
	@rm -rf build
	@rm -rf cover
	@python setup.py clean
	@rm -rf .develop
	@rm -rf .flake
	@rm -rf .install-deps
	@rm -rf *.egg-info
	@rm -rf .pytest_cache
	@rm -rf dist

.PHONY: help
help:
	@echo -n "Common make targets"
	@echo ":"
	@cat Makefile | sed -n '/^\.PHONY: / h; /\(^\t@*echo\|^\t:\)/ {H; x; /PHONY/ s/.PHONY: \(.*\)\n.*"\(.*\)"/  make \1\t\2/p; d; x}'| sort -k2,2 |expand -t 20
