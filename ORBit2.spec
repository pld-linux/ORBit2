Summary:	High-performance CORBA Object Request Broker
Summary(fr.UTF-8):	Requète d'Objects CORBA
Summary(pl.UTF-8):	Wysoko wydajny CORBA Object Request Broker
Name:		ORBit2
Version:	2.14.14
Release:	1
Epoch:		1
License:	GPL v2+/LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/ORBit2/2.14/%{name}-%{version}.tar.bz2
# Source0-md5:	f288e9a4354fce14cf6bb35140ac5d9b
Patch0:		%{name}-pthread.patch
URL:		http://www.gnome.org/projects/ORBit2/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.9
BuildRequires:	flex
BuildRequires:	glib2-devel >= 1:2.14.1
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	indent
BuildRequires:	libIDL-devel >= 0.8.10
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.14.0
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	glib2 >= 1:2.14.1
Requires:	libIDL >= 0.8.10
Provides:	linc = 1.1.1
Obsoletes:	ORBit2-automake
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

%description -l fr.UTF-8
ORBit est un ORB CORBA avec support pour le language C. Il permet a
des programmes d'envoyer des requètes et recevoir de réponses d'autres
programmes, indépendement de l'endroit ou sont les deux programmes.

%description -l pl.UTF-8
ORBit to wysokiej wydajności CORBA (Common Object Request Broker
Architecture) ORB (object request broker). Pozwala na wysyłanie próśb
i otrzymywanie odpowiedzi od innych programów bez znajomości położenia
tych dwóch programów.

%package apidocs
Summary:	ORBit API documentation
Summary(pl.UTF-8):	Dokumentacja API ORBit
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
ORBit API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API ORBit.

%package devel
Summary:	Header files, and utilities for ORBit
Summary(fr.UTF-8):	Librairies statiques et fichiers entête pour ORBit
Summary(pl.UTF-8):	Pliki nagłówkowe i użytki dla ORBit
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	glib2-devel >= 1:2.14.1
Requires:	indent
Requires:	libIDL-devel >= 0.8.10
Provides:	linc-devel = 1.1.1
Obsoletes:	libORBit2_0-devel
Obsoletes:	linc-devel

%description devel
devel ORBit is a high-performance CORBA ORB with support for the C
language. It allows programs to send requests and receive replies from
other programs, regardless of the locations of the two programs.

This package includes the header files and utilities neecessary to
write programs that use CORBA technology.

%description devel -l fr.UTF-8
Librairies statiques et fichiers entête requis pour le development ou
la compilation de programmes utilisant ORBit.

%description devel -l pl.UTF-8
ORBit to wysokiej wydajności CORBA ORB ze wsparciem dla języka C.
Pozwala na wysyłanie próśb i otrzymywanie odpowiedzi od innych
programów bez znajomości położenia tych dwóch programów.

Ten pakiet zawiera pliki nagłówkowe oraz użytki potrzebne do pisania
programów używających technologi CORBA.

%package static
Summary:	Static libraries for ORBit
Summary(pl.UTF-8):	Biblioteki statyczne dla ORBit
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

%description static -l pl.UTF-8
ORBit to wysokiej wydajności CORBA ORB ze wsparciem dla języka C.
Pozwala na wysyłanie próśb i otrzymywanie odpowiedzi od innych
programów bez znajomości położenia tych dwóch programów.

Ten pakiet zawiera biblioteki statyczne potrzebne do pisania programów
skonsolidowanych statycznie używających technologii CORBA.

%prep
%setup -q
%patch0 -p1

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--enable-gtk-doc
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
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
%attr(755,root,root) %{_libdir}/libORBit-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libORBit-2.so.0
%attr(755,root,root) %{_libdir}/libORBit-imodule-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libORBit-imodule-2.so.0
%attr(755,root,root) %{_libdir}/libORBitCosNaming-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libORBitCosNaming-2.so.0
%dir %{_libdir}/orbit-2.0
%attr(755,root,root) %{_libdir}/orbit-2.0/Everything_module.so
%{_datadir}/idl/orbit-2.0

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/orbit2-config
%attr(755,root,root) %{_libdir}/libORBit-2.so
%attr(755,root,root) %{_libdir}/libORBit-imodule-2.so
%attr(755,root,root) %{_libdir}/libORBitCosNaming-2.so
%{_libdir}/libORBit-2.la
%{_libdir}/libORBit-imodule-2.la
%{_libdir}/libORBitCosNaming-2.la
%{_libdir}/libname-server-2.a
%{_includedir}/orbit-2.0
%{_pkgconfigdir}/ORBit-2.0.pc
%{_pkgconfigdir}/ORBit-CosNaming-2.0.pc
%{_pkgconfigdir}/ORBit-idl-2.0.pc
%{_pkgconfigdir}/ORBit-imodule-2.0.pc
%{_aclocaldir}/ORBit2.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libORBit-2.a
%{_libdir}/libORBit-imodule-2.a
%{_libdir}/libORBitCosNaming-2.a
