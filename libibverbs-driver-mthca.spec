# NOTE: for version >= 17 see rdma-core.spec
Summary:	Userspace driver for the Mellanox InfiniBand HCAs
Summary(pl.UTF-8):	Sterownik przestrzeni użytkownika dla kart Mellanox InfiniBand HCA
Name:		libibverbs-driver-mthca
Version:	1.0.6
Release:	1.1
License:	BSD or GPL v2
Group:		Libraries
Source0:	http://www.openfabrics.org/downloads/mthca/libmthca-%{version}.tar.gz
# Source0-md5:	893b38bc498ca47ca094e48358aae507
URL:		http://openib.org/
BuildRequires:	libibverbs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmthca is a userspace driver for Mellanox InfiniBand HCAs. It works
as a plug-in module for libibverbs that allows programs to use
Mellanox hardware directly from userspace.

Currently the driver supports HCAs on PCI-X/PCI Express interface
based on MT23108/MT25208/MT25204 InfiniHost chips, using ib_mthca
kernel driver.

%description -l pl.UTF-8
libmthca to sterownik przestrzeni użytkownika dla kart Mellanox
InfiniBand HCA. Działa jako moduł ładowany przez libibverbs,
pozwalający programom na dostęp z przestrzeni użytkownika do sprzętu
Mellanox.

Obecnie sterownik obsługuje kontrolery HCA na szynie PCI-X/PCI Express
oparte na układach MT23108/MT25208/MT25204 InfiniHost poprzez
sterownik jądra ib_mthca.

%package static
Summary:	Static version of mthca driver
Summary(pl.UTF-8):	Statyczna wersja sterownika mthca
Group:		Development/Libraries
Requires:	libibverbs-static

%description static
Static version of mthca driver, which may be linked directly into
application.

%description static -l pl.UTF-8
Statyczna wersja sterownika mthca, którą można wbudować bezpośrednio
w aplikację.

%prep
%setup -q -n libmthca-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened by -rmav2.so name
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmthca.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libmthca-rdmav2.so
%{_sysconfdir}/libibverbs.d/mthca.driver

%files static
%defattr(644,root,root,755)
%{_libdir}/libmthca.a
