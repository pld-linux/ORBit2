Summary:	High-performance CORBA Object Request Broker
Summary(fr):	Requète d'Objects CORBA
Summary(pl):	Wysoko wydajny CORBA Object Request Broker
Name:		ORBit2
Version:	2.3.102
Release:	1
Epoch:		1
License:	LGPL/GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.gnome.org/pub/GNOME/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-disable_test.patch
Patch1:		%{name}-am.patch
URL:		http://www.labs.redhat.com/orbit/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	libIDL-devel
BuildRequires:	flex
BuildRequires:	indent
BuildRequires:	libtool
BuildRequires:	popt-devel >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
ORBit is a high-performance CORBA (Common Object Request Broker
Architecture) ORB (object request broker). It allows programs to send
requests and receive replies from other programs, regardless of the
locations of the two programs. CORBA is an architecture that enables
communication between program objects, regardless of the programming
language they're written in or the operating system they run on.

%description -l fr
ORBit est un ORB CORBA avec support pour le language C. Il permet a
des programmes d'envoyer des requètes et recevoir de réponses d'autres
programmes, indépendement de l'endroit ou sont les deux programmes.

%description -l pl
ORBit to wysokiej wydajno¶ci CORBA (Common Object Request Broker
Architecture) ORB (object request broker). Pozwala na wysy³anie pró¶b
i otrzymywanie odpowiedzi od innych programów bez znajomo¶ci po³o¿enia
tych dwóch programów.

%package devel
Summary:	Header files, and utilities for ORBit
Summary(fr):	Librairies statiques et fichiers entête pour ORBit
Summary(pl):	Pliki nag³ówkowe i u¿ytki dla ORBit
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	glib2-devel
Requires:	indent
Requires:	popt-devel

%description
devel ORBit is a high-performance CORBA ORB with support for the C
language. It allows programs to send requests and receive replies from
other programs, regardless of the locations of the two programs.

This package includes the header files and utilities neecessary to
write programs that use CORBA technology.

%description devel -l fr
Librairies statiques et fichiers entête requis pour le development ou
la compilation de programmes utilisant ORBit.

%description -l pl devel
ORBit to wysokiej wydajno¶ci CORBA ORB ze wsparciem dla jêzyka C.
Pozwala na wysy³anie pró¶b i otrzymywanie odpowiedzi od innych
programów bez znajomo¶ci po³o¿enia tych dwóch programów.

Ten pakiet zawiera pliki nag³ówkowe oraz u¿ytki potrzebne do pisania
programów u¿ywaj±cych technologi CORBA.

%package static
Summary:	Static libraries for ORBit
Summary(pl):	Biblioteki statyczne dla ORBit
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
ORBit is a high-performance CORBA ORB with support for the C language.
It allows programs to send requests and receive replies from other
programs, regardless of the locations of the two programs.

This package includes static libraries neecessary to write programs
statically linked that use CORBA technology.

%description -l pl static

ORBit to wysokiej wydajno¶ci CORBA ORB ze wsparciem dla jêzyka C.
Pozwala na wysy³anie pró¶b i otrzymywanie odpowiedzi od innych
programów bez znajomo¶ci po³o¿enia tych dwóch programów.

Ten pakiet zawiera biblioteki statyczne potrzebne do pisania programów
zlinkowanych statycznie u¿ywaj±cych technologii CORBA.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfigdir=%{_pkgconfigdir}


gzip -9nf TODO NEWS

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files devel
%defattr(644,root,root,755)
%doc *.gz
%{_pkgconfigdir}/*
%{_includedir}/*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
