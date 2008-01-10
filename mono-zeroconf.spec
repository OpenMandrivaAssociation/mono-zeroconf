%define name mono-zeroconf
%define version 0.7.3
%define release %mkrel 1

Summary: Cross platform Zero Configuration Networking library 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: BSD
Group: System/Libraries
Url: http://mono-project.com/Mono_Zeroconf
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: mono-devel
BuildRequires: monodoc
BuildRequires: avahi-sharp

%description
Mono.Zeroconf is a cross platform Zero Configuration Networking library for
Mono and .NET. It provides a unified API for performing the most common
zeroconf operations on a variety of platforms and subsystems: all the
operating systems supported by Mono and both the Avahi and
Bonjour/mDNSResponder transports.

This package was built with support vor Avahi only.
%package doc
Summary: Development documentation for %name
Group: Development/Other
Requires(post): mono-tools >= 1.1.9
Requires(postun): mono-tools >= 1.1.9

%description doc
This package contains the API documentation for %name in
Monodoc format.

%prep
%setup -q

%build
./configure --prefix=%_prefix --disable-mdnsresponder
make

%install
rm -rf %{buildroot}
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig

%clean
rm -rf %{buildroot}

%post doc
%_bindir/monodoc --make-index > /dev/null
%postun doc
if [ "$1" = "0" -a -x %_bindir/monodoc ]; then %_bindir/monodoc --make-index > /dev/null
fi


%files
%defattr(-,root,root)
%doc README COPYING
%_bindir/mzclient
%_prefix/lib/%name
%_prefix/lib/mono/gac/Mono.Zeroconf
%_prefix/lib/mono/%name
%_datadir/pkgconfig/mono-zeroconf.pc

%files doc
%defattr(-,root,root)
%_prefix/lib/monodoc/sources/*


