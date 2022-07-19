Summary:       Nagios plugin which checks json for a given endpoint
Name:          nagios-plugins-http-json
Version:       2.0.1
Release:       1%{?dist}
Source0:       %{name}-%{version}.tar.gz
License:       ASL 2.0
Group:         Development/System
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:        %{_prefix}
BuildArch:     noarch

BuildRequires: python3-devel


%description
Nagios plugin which checks json for a given endpoint


%define _unpackaged_files_terminate_build 0


%prep
%setup -q


%build
%{py3_build}


%install
%{py3_install "--record=INSTALLED_FILES" }


%clean
rm -rf $RPM_BUILD_ROOT


%files -f INSTALLED_FILES


%changelog
* Mon Jul 18 2022 Katarina Zailac <kzailac@srce.hr> - 2.0.1-1
- Generic probe that checks json
