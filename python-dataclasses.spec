Name:           python-dataclasses
Version:        0.8
Release:        2
Summary:        A backport of the dataclasses module for Python 3.X
License:        Apache-2.0
URL:            https://github.com/ericvsmith/dataclasses
Source:         https://files.pythonhosted.org/packages/source/d/dataclasses/dataclasses-%{version}.tar.gz

BuildRequires: pkgconfig(python)
BuildRequires: python3dist(setuptools)

BuildArch:      noarch

%description
This is an implementation of PEP 557, Data Classes. It is a backport for Python 3.6.

%prep
%setup -q -n dataclasses-%{version}

%build
%py_build

%install
%py_install

%files
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*
