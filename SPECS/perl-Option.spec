%define debug_package %{nil}

Name:		perl-Option
Version:	1.0.0
Release:	1%{?dist}
Summary:	Perl Option parser

Group:		Development/Libraries
License:	MPLv2.0
URL:		http://www.edwinbuck.com/perl-Option
Source0:	perl-Option-%{version}.tgz

BuildRequires:	make
Requires:	perl-interpreter

%description

Perl Option is a library which performs command line parsing.

%package examples
Summary: Perl Option parser Examples

%description examples

Examples of how to use the  Perl Option library to perform command line
arugment parsing.

%prep
%setup -q


%build
make %{?_smp_mflags}
make check

%install
%make_install


%files
/usr/share/perl5/vendor_perl/Option/Parser.pm

%files examples
/usr/share/doc/perl-Option/samples/ExceptionExample
/usr/share/doc/perl-Option/samples/HelpFormatterExample
/usr/share/doc/perl-Option/samples/HelpExample
/usr/share/doc/perl-Option/samples/RequiredIfExample


%changelog

