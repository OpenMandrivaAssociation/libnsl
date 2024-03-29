%define major 3
%define libname %mklibname nsl %{major}
%define devname %mklibname nsl -d
%define static %mklibname -d -s nsl

Summary:	Public client interface library for NIS(YP) and NIS+
Name:		libnsl
Version:	2.0.1
Release:	1
License:	BSD and LGPLv2+
Group:		System/Libraries
Url:		https://github.com/thkukuk/libnsl
Source0:	https://github.com/thkukuk/libnsl/archive/v%{version}.tar.gz
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(libtirpc)

%description
This package contains the libnsl library. This library contains
the public client interface for NIS(YP) and NIS+.
This code was formerly part of glibc, but is now standalone to
be able to link against TI-RPC for IPv6 support.

%package -n %{libname}
Summary:	Public client interface library for NIS(YP) and NIS+
Group:		System/Libraries

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Development files for the libnsl library
Group:		Development/C
Requires:	%{libname} >= %{EVRD}

%description -n %{devname}
This package includes header files and libraries necessary for developing
programs which use the nsl library.

%package -n %{static}
Summary:	Static version of libnsl library
Group:		Development/C
Requires:	%{devname} >= %{EVRD}
Provides:	libnsl-static-devel = %{EVRD}

%description -n	%{static}
This package contains a static library version of the nsl library.

%prep
%autosetup -p1
autoreconf -fiv

%build
CONFIGURE_TOP="$PWD"
export CFLAGS="%{optflags} -fPIC"

%configure \
	--enable-shared \
	--enable-static

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libnsl.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING NEWS README
%{_includedir}/rpcsvc/*.h
%{_includedir}/rpcsvc/*.x
%{_libdir}/libnsl.so
%{_libdir}/pkgconfig/libnsl.pc

%files -n %{static}
%{_libdir}/libnsl.a
