
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-dataclasses
Version:        0.7
Release:        lp152.1.1
Summary:        A backport of the dataclasses module for Python 3.6
License:        Apache-2.0
URL:            https://github.com/ericvsmith/dataclasses
Source:         https://files.pythonhosted.org/packages/source/d/dataclasses/dataclasses-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testsuite}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This is an implementation of PEP 557, Data Classes. It is a backport for Python 3.6.

%prep
%setup -q -n dataclasses-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python test/test_dataclasses.py -v

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*
