Summary:	A tool for converting XML files to various formats
Summary(pl.UTF-8):	Narzędzie do konwersji plików XML do różnych formatów
Name:		xmlto
Version:	0.0.22
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://fedorahosted.org/releases/x/m/xmlto/%{name}-%{version}.tar.bz2
# Source0-md5:	12f297dc7051e4fef08339980f88a1dd
URL:		http://cyberelk.net/tim/software/xmlto/
BuildRequires:	autoconf
BuildRequires:	automake >= 1.6
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl >= 1.56.0
BuildRequires:	libxslt-progs
BuildRequires:	util-linux
Requires:	docbook-dtd42-xml
Requires:	docbook-style-xsl >= 1.56.0
Requires:	libxslt-progs
Requires:	mktemp >= 1.5-19
Requires:	passivetex >= 1.20
# for getopt
Requires:	util-linux
Obsoletes:	refentry2man
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a package for converting XML files to various formats using
XSL stylesheets.

%description -l pl.UTF-8
Jest to pakiet do konwersji plików w formacie XML do innych formatów
przy użyciu styli XSL.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

cat > refentry2man <<'EOF'
#!/bin/sh
XMLTO_TMPFILE=$(mktemp -t xmltoXXXXXX)
XMLTO_TMPDIR=$(mktemp -d -t xmltodirXXXXXX)
cat - > $XMLTO_TMPFILE
xmlto -o $XMLTO_TMPDIR man $XMLTO_TMPFILE >/dev/null
cat $XMLTO_TMPDIR/*
rm -f $XMLTO_TMPFILE
rm -rf $XMLTO_TMPDIR
EOF

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install refentry2man $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
