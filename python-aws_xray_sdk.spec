#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	AWS X-Ray SDK for Python 2
Summary(pl.UTF-8):	SDK AWS X-Ray dla Pythona 2
Name:		python-aws_xray_sdk
# keep 2.12.0 here for python2 support
Version:	2.12.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/aws-xray-sdk/
Source0:	https://files.pythonhosted.org/packages/source/a/aws-xray-sdk/aws-xray-sdk-%{version}.tar.gz
# Source0-md5:	8a23112622f8e26e85ea134aad2bcfba
URL:		https://pypi.org/project/aws-xray-sdk/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-botocore >= 1.11.3
BuildRequires:	python-enum34
BuildRequires:	python-future
BuildRequires:	python-jsonpickle
BuildRequires:	python-wrapt
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-botocore >= 1.11.3
BuildRequires:	python3-jsonpickle
BuildRequires:	python3-wrapt
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray
service.

%description -l pl.UTF-8
AWS X-Ray SDK dla Pythona pozwala programistom Pythona zapisywać i
emitować z aplikacji informacje do usługi AWS X-Ray.

%package -n python3-aws_xray_sdk
Summary:	AWS X-Ray SDK for Python 3
Summary(pl.UTF-8):	SDK AWS X-Ray dla Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-aws_xray_sdk
The AWS X-Ray SDK for Python enables Python developers to record and
emit information from within their applications to the AWS X-Ray
service.

%description -n python3-aws_xray_sdk -l pl.UTF-8
AWS X-Ray SDK dla Pythona pozwala programistom Pythona zapisywać i
emitować z aplikacji informacje do usługi AWS X-Ray.

%prep
%setup -q -n aws-xray-sdk-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/aws_xray_sdk
%{py_sitescriptdir}/aws_xray_sdk-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-aws_xray_sdk
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/aws_xray_sdk
%{py3_sitescriptdir}/aws_xray_sdk-%{version}-py*.egg-info
%endif
