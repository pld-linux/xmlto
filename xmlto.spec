Summary:	A tool for converting XML files to various formats
Summary(pl):	Narzêdzie do konwersji plików XML do ró¿nych formatów
Name:		xmlto
Version:	0.0.18
Release:	1
Epoch:		0
License:	GPL
Group:		Applications/System
Source0:	http://cyberelk.net/tim/data/xmlto/stable/%{name}-%{version}.tar.bz2
# Source0-md5:	1a06471b70eb27a6aca5d1b3a144f9b0
URL:		http://cyberelk.net/tim/xmlto/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl >= 1.56.0
BuildRequires:	libxslt-progs
BuildRequires:	util-linux
Requires:	docbook-dtd42-xml
Requires:	docbook-style-xsl >= 1.56.0
Requires:	passivetex >= 1.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a package for converting XML files to various formats using
XSL stylesheets.

%description -l pl
Jest to pakiet do konwersji plików w formacie XML do innych formatów
przy u¿yciu styli XSL.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
