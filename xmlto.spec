Summary:	A tool for converting XML files to various formats.
Summary(pl):	Narz�dzie do konwersji plik�w XML do r�nych format�w.
Name:		xmlto
Version:	0.0.15
Release:	1
Epoch:		0
License:	GPL
Group:		Applications/System
Source0:	http://cyberelk.net/tim/data/xmlto/stable/%{name}-%{version}.tar.bz2
# Source0-md5:	c11226c3c0dabb245c191cbf39c6fcd8
URL:		http://cyberelk.net/tim/xmlto/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libxslt-progs
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl >= 1.56.0
Requires:	docbook-dtd42-xml
Requires:	docbook-style-xsl >= 1.56.0
Requires:	passivetex >= 1.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a package for converting XML files to various formats using
XSL stylesheets.

%description -l pl
Jest to pakiet do konwersji plik�w w formacie XML do innych format�w,
u�ywaj�c do tego celu styli XSL

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
