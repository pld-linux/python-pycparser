#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module
%bcond_without	tests	# unit tests
#
Summary:	C Parser in Python 2
Summary(pl.UTF-8):	Parser języka C w Pythonie 2
Name:		python-pycparser
Version:	2.21
Release:	5
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pycparser/
Source0:	https://files.pythonhosted.org/packages/source/p/pycparser/pycparser-%{version}.tar.gz
# Source0-md5:	48f7d743bf018f7bb2ffc5fb976d1492
URL:		https://github.com/eliben/pycparser
%if %{with python2}
BuildRequires:	python >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.4
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pycparser is a parser for the C language, written in pure Python. It
is a module designed to be easily integrated into applications that
need to parse C source code.

This package contains Python 2 module.

%description -l pl.UTF-8
pycparser to parser języka C napisany w czystym Pythonie. Jest to
moduł zaprojektowany tak, aby można go było łatwo zintegrować w
aplikacjach wymagających analizy kodu źródłowego w C.

Ten pakiet zawiera moduł Pythona 2.

%package -n python3-pycparser
Summary:	C Parser in Python 3
Summary(pl.UTF-8):	Parser języka C w Pythonie 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-pycparser
pycparser is a parser for the C language, written in pure Python. It
is a module designed to be easily integrated into applications that
need to parse C source code.

This package contains Python 3 module.

%description -n python3-pycparser -l pl.UTF-8
pycparser to parser języka C napisany w czystym Pythonie. Jest to
moduł zaprojektowany tak, aby można go było łatwo zintegrować w
aplikacjach wymagających analizy kodu źródłowego w C.

Ten pakiet zawiera moduł Pythona 3.

%prep
%setup -q -n pycparser-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} tests/test_c_parser.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} tests/test_c_parser.py
%endif
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
%doc CHANGES LICENSE README.rst
%dir %{py_sitescriptdir}/pycparser
%{py_sitescriptdir}/pycparser/*.py[co]
%{py_sitescriptdir}/pycparser/_c_ast.cfg
%dir %{py_sitescriptdir}/pycparser/ply
%{py_sitescriptdir}/pycparser/ply/*.py[co]
%{py_sitescriptdir}/pycparser-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pycparser
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%dir %{py3_sitescriptdir}/pycparser
%{py3_sitescriptdir}/pycparser/*.py
%{py3_sitescriptdir}/pycparser/_c_ast.cfg
%{py3_sitescriptdir}/pycparser/__pycache__
%dir %{py3_sitescriptdir}/pycparser/ply
%{py3_sitescriptdir}/pycparser/ply/*.py
%{py3_sitescriptdir}/pycparser/ply/__pycache__
%{py3_sitescriptdir}/pycparser-%{version}-py*.egg-info
%endif
