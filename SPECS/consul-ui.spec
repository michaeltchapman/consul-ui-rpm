Name:           consul-ui
Version:        0.4.1
Release:        1%{?dist}
Summary:        Consul-UI is the web interface for consul, a tool for service discovery and configuration.

Group:          System Environment/Daemons
License:        MPLv2.0
URL:            http://www.consul.io
Source0:        https://dl.bintray.com/mitchellh/consul/%{version}_web_ui.zip
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:       consul >= 0.4.1

%description
Consul-UI is the web interface for consul, a tool for service discovery and configuration.

%prep
%setup -c

%install
mkdir -p %{buildroot}/%{_datarootdir}/%{name}
cp -r dist %{buildroot}/%{_datarootdir}/%{name}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_datarootdir}/%{name}

%doc

%changelog
* Sun Dec 21 2014 Michael Chapman <michael@aptira.com>
- Initial commit
