Summary:	A tool for converting XML files to various formats
Summary(pl.UTF-8):	Narzędzie do konwersji plików XML do różnych formatów
Name:		xmlto
Version:	0.0.29
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	https://releases.pagure.org/xmlto/%{name}-%{version}.tar.bz2
# Source0-md5:	9d9e9b2ebfca1e453f5e1599b82c48cc
URL:		http://cyberelk.net/tim/software/xmlto/
BuildRequires:	autoconf
BuildRequires:	automake >= 1.6
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl-nons >= 1.56.0
BuildRequires:	libpaper
BuildRequires:	libxslt-progs
BuildRequires:	util-linux
Requires:	docbook-dtd42-xml
Requires:	docbook-style-xsl-nons >= 1.56.0
Requires:	libxslt-progs
Requires:	mktemp >= 1.5-19
Requires:	xmltex
# for getopt
Requires:	util-linux
# fop is required for --with-fop. It is quite rare usecase. Moreover fop is
# heavy dependency (written in Java, requires several Java libs, takes long time
# to execute %post), so we don't want user to force to install it.
Suggests:	fop
# for paperconf program
Suggests:	libpaper
# this is the default; links/lynx/text-www-browser is also possible
Suggests:	w3m
Obsoletes:	refentry2man < 0.5
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
%configure \
	FOP=/usr/bin/fop \
	PAPER_CONF=/usr/bin/paperconf \
	PDFXMLTEX=/usr/bin/pdfxmltex \
	XMLTEX=/usr/bin/xmltex
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
%doc AUTHORS.md ChangeLog NEWS.md README.md THANKS.md
%attr(755,root,root) %{_bindir}/refentry2man
%attr(755,root,root) %{_bindir}/xmlif
%attr(755,root,root) %{_bindir}/xmlto
%{_datadir}/%{name}
%{_mandir}/man1/xmlif.1*
%{_mandir}/man1/xmlto.1*
