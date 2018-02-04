BASEDIR=$(dir $(realpath $(firstword $(MAKEFILE_LIST))))

all: rpms
	

dirs:
	mkdir -p BUILD
	mkdir -p BUILDROOT
	mkdir -p RPMS
	mkdir -p SRPMS

rpms: | dirs
	rpmbuild --define '_topdir ${BASEDIR}' -ba SPECS/perl-Option.spec

clean:
	rm -rf BUILD
	rm -rf BUILDROOT
	rm -rf RPMS
	rm -rf SRPMS
