Summary:	High-performance CORBA Object Request Broker
Summary(fr):	RequËte d'Objects CORBA
Summary(pl):	Wysoko wydajny CORBA Object Request Broker
Name:		ORBit2
Version:	2.3.104
Release:	1
Epoch:		1
License:	LGPL/GPL
Group:		Libraries
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}-Makefile.shared
Patch0:		%{name}-disable_test.patch
Patch1:		%{name}-am15.patch
URL:		http://www.labs.redhat.com/orbit/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1.3.13
BuildRequires:	linc-devel >= 0.1.16
BuildRequires:	libIDL-devel >= 0.7.4
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
des programmes d'envoyer des requËtes et recevoir de rÈponses d'autres
programmes, indÈpendement de l'endroit ou sont les deux programmes.

%description -l pl
ORBit to wysokiej wydajno∂ci CORBA (Common Object Request Broker
Architecture) ORB (object request broker). Pozwala na wysy≥anie prÛ∂b
i otrzymywanie odpowiedzi od innych programÛw bez znajomo∂ci po≥oøenia
tych dwÛch programÛw.

%package devel
Summary:	Header files, and utilities for ORBit
Summary(fr):	Librairies statiques et fichiers entÍte pour ORBit
Summary(pl):	Pliki nag≥Ûwkowe i uøytki dla ORBit
Group:		Development/Libraries
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Requires:	glib2-devel
Requires:	indent
Requires:	libIDL-devel
Requires:	linc-devel
Requires:	popt-devel

%description
devel ORBit is a high-performance CORBA ORB with support for the C
language. It allows programs to send requests and receive replies from
other programs, regardless of the locations of the two programs.

This package includes the header files and utilities neecessary to
write programs that use CORBA technology.

%description devel -l fr
Librairies statiques et fichiers entÍte requis pour le development ou
la compilation de programmes utilisant ORBit.

%description devel -l pl
ORBit to wysokiej wydajno∂ci CORBA ORB ze wsparciem dla jÍzyka C.
Pozwala na wysy≥anie prÛ∂b i otrzymywanie odpowiedzi od innych
programÛw bez znajomo∂ci po≥oøenia tych dwÛch programÛw.

Ten pakiet zawiera pliki nag≥Ûwkowe oraz uøytki potrzebne do pisania
programÛw uøywaj±cych technologi CORBA.

%package static
Summary:	Static libraries for ORBit
Summary(pl):	Biblioteki statyczne dla ORBit
Group:		Development/Libraries
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
ORBit is a high-performance CORBA ORB with support for the C language.
It allows programs to send requests and receive replies from other
programs, regardless of the locations of the two programs.

This package includes static libraries neecessary to write programs
statically linked that use CORBA technology.

%description static -l pl
ORBit to wysokiej wydajno∂ci CORBA ORB ze wsparciem dla jÍzyka C.
Pozwala na wysy≥anie prÛ∂b i otrzymywanie odpowiedzi od innych
programÛw bez znajomo∂ci po≥oøenia tych dwÛch programÛw.

Ten pakiet zawiera biblioteki statyczne potrzebne do pisania programÛw
zlinkowanych statycznie uøywaj±cych technologii CORBA.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

install %{SOURCE1} Makefile.shared

%build
rm -f missing
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

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/name-client-2
%attr(755,root,root) %{_bindir}/orbit-idl-2
%attr(755,root,root) %{_bindir}/orbit-name-server-2
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/idl/orbit-*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/orbit2-config
%attr(755,root,root) %{_libdir}/lib*.??
%{_libdir}/libname-server-2.a
%{_pkgconfigdir}/*.pc
%{_includedir}/orbit-*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libORBit-2.a
%{_libdir}/libORBitCosNaming-2.a
