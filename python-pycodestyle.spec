# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-pycodestyle
Epoch: 100
Version: 2.11.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Python style guide checker
License: MIT
URL: https://github.com/PyCQA/pycodestyle/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
pycodestyle is a tool to check your Python code against some of the
style conventions in PEP 8. It has a plugin architecture, making new
checks easy, and its output is parseable, making it easy to jump to an
error location in your editor.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pycodestyle
Summary: Python style guide checker
Requires: python3
Provides: python3-pycodestyle = %{epoch}:%{version}-%{release}
Provides: python3dist(pycodestyle) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pycodestyle = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pycodestyle) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pycodestyle = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pycodestyle) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pycodestyle
pycodestyle is a tool to check your Python code against some of the
style conventions in PEP 8. It has a plugin architecture, making new
checks easy, and its output is parseable, making it easy to jump to an
error location in your editor.

%files -n python%{python3_version_nodots}-pycodestyle
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-pycodestyle
Summary: Python style guide checker
Requires: python3
Provides: python3-pycodestyle = %{epoch}:%{version}-%{release}
Provides: python3dist(pycodestyle) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pycodestyle = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pycodestyle) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pycodestyle = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pycodestyle) = %{epoch}:%{version}-%{release}

%description -n python3-pycodestyle
pycodestyle is a tool to check your Python code against some of the
style conventions in PEP 8. It has a plugin architecture, making new
checks easy, and its output is parseable, making it easy to jump to an
error location in your editor.

%files -n python3-pycodestyle
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
