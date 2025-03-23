Name:           perl-Module-Filename
Version:        0.03
Release:        1%{?dist}
Summary:        Provides an object oriented, cross platform interface for getting a module's filename
License:        Distributable, see LICENSE
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-Filename/
Source0:        http://www.cpan.org/modules/by-module/Module/Module-Filename-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Simple) >= 0.44
BuildRequires:  perl(Path::Class)
Requires:       perl(Path::Class)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module returns the filename as a Path::Class::File object. It does not
load any packages as it scans. It simply scans @INC looking for a module of
the same name as the package passed.

%prep
%setup -q -n Module-Filename-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
