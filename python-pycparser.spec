#
# Conditional build:
%bcond_without  python2 # CPython 2.x module
%bcond_without  python3 # CPython 3.x module
#
Summary:	C Parser in Python 2
Summary(pl.UTF-8):	Parser języka C w Pythonie 2
Name:		python-pycparser
Version:	2.14
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/pypi/pycparser
Source0:	https://pypi.python.org/packages/source/p/pycparser/pycparser-%{version}.tar.gz
# Source0-md5:	a2bc8d28c923b4fe2b2c3b4b51a4f935
URL:		https://github.com/eliben/pycparser
%if %{with python2}
BuildRequires:	python >= 2
BuildRequires:	python-modules >= 2
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-devel >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.612
Requires:	python-modules
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
Requires:	python3-modules

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
%py_build \
	--build-base build-2
%endif
%if %{with python3}
%py3_build \
	--build-base build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build \
		--build-base build-2 \
	install \
		--root=$RPM_BUILD_ROOT \
		--optimize=2

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build \
		--build-base build-3 \
	install \
		--root=$RPM_BUILD_ROOT \
		--optimize=2
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
