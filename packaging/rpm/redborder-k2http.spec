Name: redborder-k2http
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Package for redborder k2http initscripts and configuration.

License: AGPL 3.0
URL: https://github.com/redBorder/redborder-k2http
Source0: %{name}-%{version}.tar.gz

Requires: kafka2x
# the old k2http package ships the same unit file
Obsoletes: k2http

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build

%install
install -D -m 0644 resources/systemd/k2http.service %{buildroot}/usr/lib/systemd/system/k2http.service

%pre
getent group k2http >/dev/null || groupadd -r k2http
getent passwd k2http >/dev/null || \
    useradd -r -g k2http -d / -s /sbin/nologin \
    -c "User of k2http service" k2http
exit 0

%post
systemctl daemon-reload

%files
%defattr(0644,root,root)
/usr/lib/systemd/system/k2http.service
%doc

%changelog
* Fri Oct 30 2026 Juan Soto <jsoto@redborder.com> - 1.0.0-1
- first spec version
