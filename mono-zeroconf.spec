%define name mono-zeroconf
%define version 0.9.0
%define release %mkrel 8

Summary: Cross platform Zero Configuration Networking library 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://download.banshee-project.org/mono-zeroconf/%{name}-%{version}.tar.bz2
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

%package 1.0
Summary: Cross platform Zero Configuration Networking library 
Group: Development/Other
Conflicts: %name < 0.9.0-5
Requires: %name = %version

%description 1.0
Mono.Zeroconf is a cross platform Zero Configuration Networking library for
Mono and .NET. It provides a unified API for performing the most common
zeroconf operations on a variety of platforms and subsystems: all the
operating systems supported by Mono and both the Avahi and
Bonjour/mDNSResponder transports.

This package was built with support vor Avahi only.

This package contains a compatibility API for older applications.

%package 2.0
Summary: Cross platform Zero Configuration Networking library 
Group: Development/Other
Conflicts: %name < 0.9.0-5
Requires: %name = %version

%description 2.0
Mono.Zeroconf is a cross platform Zero Configuration Networking library for
Mono and .NET. It provides a unified API for performing the most common
zeroconf operations on a variety of platforms and subsystems: all the
operating systems supported by Mono and both the Avahi and
Bonjour/mDNSResponder transports.

This package was built with support vor Avahi only.

This package contains a compatibility API for older applications.

%package 3.0
Summary: Cross platform Zero Configuration Networking library 
Group: Development/Other
Conflicts: %name < 0.9.0-5
Requires: %name = %version

%description 3.0
Mono.Zeroconf is a cross platform Zero Configuration Networking library for
Mono and .NET. It provides a unified API for performing the most common
zeroconf operations on a variety of platforms and subsystems: all the
operating systems supported by Mono and both the Avahi and
Bonjour/mDNSResponder transports.

This package was built with support vor Avahi only.

This package contains a compatibility API for older applications.

%package 4.0
Summary: Cross platform Zero Configuration Networking library 
Group: Development/Other
Conflicts: %name < 0.9.0-5
Requires: %name = %version

%description 4.0
Mono.Zeroconf is a cross platform Zero Configuration Networking library for
Mono and .NET. It provides a unified API for performing the most common
zeroconf operations on a variety of platforms and subsystems: all the
operating systems supported by Mono and both the Avahi and
Bonjour/mDNSResponder transports.

This package was built with support vor Avahi only.

This package contains a compatibility API for older applications.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
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

%files 1.0
%defattr(-,root,root)
%_prefix/lib/mono/gac/policy.1.0.Mono.Zeroconf

%files 2.0
%defattr(-,root,root)
%_prefix/lib/mono/gac/policy.2.0.Mono.Zeroconf

%files 3.0
%defattr(-,root,root)
%_prefix/lib/mono/gac/policy.3.0.Mono.Zeroconf

%files 4.0
%defattr(-,root,root)
%_prefix/lib/mono/gac/policy.4.0.Mono.Zeroconf

%files devel
%defattr(-,root,root)
%_datadir/pkgconfig/mono-zeroconf.pc

%files doc
%defattr(-,root,root)
%_prefix/lib/monodoc/sources/*




%changelog
* Mon May 09 2011 Funda Wang <fwang@mandriva.org> 0.9.0-6mdv2011.0
+ Revision: 672865
- add conflicts to ease upgrade

* Mon May 09 2011 Götz Waschk <waschk@mandriva.org> 0.9.0-5
+ Revision: 672839
- split package to work around rpm5 provides bug

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-4
+ Revision: 666483
- mass rebuild

* Mon Aug 09 2010 Götz Waschk <waschk@mandriva.org> 0.9.0-3mdv2011.0
+ Revision: 567913
- split out devel package

* Fri Dec 11 2009 Götz Waschk <waschk@mandriva.org> 0.9.0-2mdv2010.1
+ Revision: 476299
- rebuild for new webkit-sharp

* Tue Jun 02 2009 Götz Waschk <waschk@mandriva.org> 0.9.0-1mdv2010.0
+ Revision: 382231
- new version
- update file list

* Tue Oct 21 2008 Götz Waschk <waschk@mandriva.org> 0.8.0-1mdv2009.1
+ Revision: 296086
- new version
- update source URL
- update file list

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 0.7.6-2mdv2009.0
+ Revision: 265175
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 08 2008 Götz Waschk <waschk@mandriva.org> 0.7.6-1mdv2009.0
+ Revision: 192419
- new version
- update file list

* Sun Jan 27 2008 Götz Waschk <waschk@mandriva.org> 0.7.5-1mdv2008.1
+ Revision: 158879
- new version
- update file list

* Thu Jan 24 2008 Götz Waschk <waschk@mandriva.org> 0.7.4-1mdv2008.1
+ Revision: 157426
- new version

* Thu Jan 10 2008 Götz Waschk <waschk@mandriva.org> 0.7.3-1mdv2008.1
+ Revision: 147504
- import mono-zeroconf


* Thu Jan 10 2008 Götz Waschk <waschk@mandriva.org> 0.7.3-1mdv2008.1
- initial package
