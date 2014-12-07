Summary:	Cross platform Zero Configuration Networking library 
Name:		mono-zeroconf
Version:	0.9.0
Release:	15
License:	BSD
Group:		System/Libraries
Url:		http://mono-project.com/Mono_Zeroconf
Source0:	http://download.banshee-project.org/mono-zeroconf/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	monodoc
BuildRequires:	pkgconfig(avahi-sharp)
BuildRequires:	pkgconfig(mono)

%description
Mono.Zeroconf is a cross platform Zero Configuration Networking library for
Mono and .NET. It provides a unified API for performing the most common
zeroconf operations on a variety of platforms and subsystems:	all the
operating systems supported by Mono and both the Avahi and
Bonjour/mDNSResponder transports.

This package was built with support for Avahi only.

%package 1.0
Summary:	Cross platform Zero Configuration Networking library 
Group:		Development/Other
Conflicts:	%{name} < 0.9.0-5
Requires:	%{name} = %{version}-%{release}

%description 1.0
This package contains a compatibility API for older applications.

%package 2.0
Summary:	Cross platform Zero Configuration Networking library 
Group:		Development/Other
Conflicts:	%{name} < 0.9.0-5
Requires:	%{name} = %{version}-%{release}

%description 2.0
This package contains a compatibility API for older applications.

%package 3.0
Summary:	Cross platform Zero Configuration Networking library 
Group:		Development/Other
Conflicts:	%{name} < 0.9.0-5
Requires:	%{name} = %{version}-%{release}

%description 3.0
This package contains a compatibility API for older applications.

%package 4.0
Summary:	Cross platform Zero Configuration Networking library 
Group:		Development/Other
Conflicts:	%{name} < 0.9.0-5
Requires:	%{name} = %{version}-%{release}

%description 4.0
This package contains a compatibility API for older applications.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
This package was built with support for Avahi only.

%package doc
Summary:	Development documentation for %{name}
Group:		Development/Other
Requires(post,postun):	mono-tools >= 1.1.9

%description doc
This package contains the API documentation for %{name} in
Monodoc format.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	--disable-mdnsresponder
make

%install
%makeinstall_std pkgconfigdir=%{_datadir}/pkgconfig

%post doc
%{_bindir}/monodoc --make-index > /dev/null
%postun doc
if [ "$1" = "0" -a -x %{_bindir}/monodoc ]; then %{_bindir}/monodoc --make-index > /dev/null
fi

%files
%doc README COPYING
%{_bindir}/mzclient
%{_prefix}/lib/%{name}
%{_prefix}/lib/mono/gac/Mono.Zeroconf
%{_prefix}/lib/mono/%{name}

%files 1.0
%{_prefix}/lib/mono/gac/policy.1.0.Mono.Zeroconf

%files 2.0
%{_prefix}/lib/mono/gac/policy.2.0.Mono.Zeroconf

%files 3.0
%{_prefix}/lib/mono/gac/policy.3.0.Mono.Zeroconf

%files 4.0
%{_prefix}/lib/mono/gac/policy.4.0.Mono.Zeroconf

%files devel
%{_datadir}/pkgconfig/mono-zeroconf.pc

%files doc
%{_prefix}/lib/monodoc/sources/*

