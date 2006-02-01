%bcond_without  apidocs         # disable gtk-doc
Summary:	High-performance CORBA Object Request Broker
Summary(fr):	Requète d'Objects CORBA
Summary(pl):	Wysoko wydajny CORBA Object Request Broker
Name:		ORBit2
Version:	2.12.4
Release:	2
Epoch:		1
License:	GPL v2+/LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/ORBit2/2.12/%{name}-%{version}.tar.bz2
# Source0-md5:	aa2cae6e7957c369edccbd98ba78dea9
Patch0:		%{name}-pthread.patch
Patch1:		%{name}-popt.patch
URL:		http://www.labs.redhat.com/orbit/
BuildRequires:	autoconf >= 2.12
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	glib2-devel >= 1:2.6.3
%if %{with apidocs}
BuildRequires:	gtk-doc >= 1.3
%else
BuildRequires:	gtk-doc-automake
%endif
BuildRequires:	indent
BuildRequires:	libIDL-devel >= 0.8.5
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.14.0
BuildRequires:	popt-devel >= 1.5
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	glib2 >= 1:2.6.3
Requires:	libIDL >= 0.8.5
Requires:	popt >= 1.5
Provides:	linc = 1.1.1
Obsoletes:	libORBit2_0
Obsoletes:	linc
Conflicts:	libbonobo < 2.3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2-devel >= 1:2.6.3
Requires:	indent
Requires:	libIDL-devel >= 0.8.5
Provides:	linc-devel = 1.1.1
Obsoletes:	libORBit2_0-devel
Obsoletes:	linc-devel

%description devel
devel ORBit is a high-performance CORBA ORB with support for the C
language. It allows programs to send requests and receive replies from
other programs, regardless of the locations of the two programs.

This package includes the header files and utilities neecessary to
write programs that use CORBA technology.

%description devel -l fr
Librairies statiques et fichiers entête requis pour le development ou
la compilation de programmes utilisant ORBit.

%description devel -l pl
ORBit to wysokiej wydajno¶ci CORBA ORB ze wsparciem dla jêzyka C.
Pozwala na wysy³anie pró¶b i otrzymywanie odpowiedzi od innych
programów bez znajomo¶ci po³o¿enia tych dwóch programów.

Ten pakiet zawiera pliki nag³ówkowe oraz u¿ytki potrzebne do pisania
programów u¿ywaj±cych technologi CORBA.

%package static
Summary:	Static libraries for ORBit
Summary(pl):	Biblioteki statyczne dla ORBit
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	linc-static = 1.1.1
Obsoletes:	linc-static

%description static
ORBit is a high-performance CORBA ORB with support for the C language.
It allows programs to send requests and receive replies from other
programs, regardless of the locations of the two programs.

This package includes static libraries neecessary to write programs
statically linked that use CORBA technology.

%description static -l pl
ORBit to wysokiej wydajno¶ci CORBA ORB ze wsparciem dla jêzyka C.
Pozwala na wysy³anie pró¶b i otrzymywanie odpowiedzi od innych
programów bez znajomo¶ci po³o¿enia tych dwóch programów.

Ten pakiet zawiera biblioteki statyczne potrzebne do pisania programów
skonsolidowanych statycznie u¿ywaj±cych technologii CORBA.

%package automake
Summary:        Automake macros for ORBit2
Summary(pl):    Makra dla automake do ORBit2
Group:          Development/Tools
Requires:       automake
Conflicts:      ORBit2-devel < 1:2.12.4-2

%description automake
Automake macros for ORBit2.

%description automake -l pl
Makra dla automake do ORBit2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
# workaround a bug that prevents regenaration without gtk-doc, will need to fix it one day
%if %{with apidocs}
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%endif
%configure \
	%{?with_apidocs:--with-html-dir=%{_gtkdocdir}} \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc \
	--enable-http
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no static module - shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/orbit-2.0/Everything_module.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/ior-decode-2
%attr(755,root,root) %{_bindir}/linc-cleanup-sockets
%attr(755,root,root) %{_bindir}/orbit-idl-2
%attr(755,root,root) %{_bindir}/typelib-dump
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/orbit-2.0
%{_libdir}/orbit-2.0/*.so*
%{_datadir}/idl/orbit-*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/orbit2-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/libname-server-2.a
%{_pkgconfigdir}/*.pc
%{_includedir}/orbit-*
%{?with_apidocs:%{_gtkdocdir}/%{name}}

%files static
%defattr(644,root,root,755)
%{_libdir}/libORBit-2.a
%{_libdir}/libORBit-imodule-2.a
%{_libdir}/libORBitCosNaming-2.a

%files automake
%defattr(644,root,root,755)
%{_aclocaldir}/*
