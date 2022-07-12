Name: helloworld
Version: 1.0
Release: alt1

Summary: helloworld

License: license
Group: group

Source: helloworld.py

BuildArch: noarch

%description
description

%prep

%build

%install
mkdir -p %buildroot%_bindir
install -m755 %{SOURCE0} %buildroot%_bindir/

%files
%_bindir/helloworld.py
