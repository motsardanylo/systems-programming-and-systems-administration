Name:           count_etc_files
Version:        1.0
Release:        1%{?dist}
Summary:        Script that counts files in /etc

License:        GPL
BuildArch:      noarch
Source0:        %{_sourcedir}/count_etc_files.sh

%description
Simple script that counts files in /etc.

%prep

%build

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/local/bin/count_etc_files

%files
/usr/local/bin/count_etc_files

%changelog
* Fri Dec 05 2025 Danylo <danylomotsar@mail.com> 1.0-1
- Initial build
