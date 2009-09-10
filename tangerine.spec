# create a server ?
# TODO missing icons 
%define name tangerine
%define release		%mkrel 5

Summary:    Application to publish music on lan, using DAAP	
Name:		%name
Version:	0.3.0
Release:	%release
Source0:	http://www.snorp.net/files//%name/%name-%version.tar.bz2
License:	GPL
Group:		Networking/File transfer
Url:		http://www.snorp.net/log/tangerine/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: muine avahi-sharp ipod-sharp glade-sharp2 
BuildRequires: mono beagle gtk-sharp2 
BuildRequires: desktop-file-utils
BuildRequires: libsm-devel 
Requires:  %name-daemon
# rhytmbox ?
%description
Tangerine is an application that allows you to publish music over the 
local network, using DAAP, based on Zeroconf. 

There are several clients that you can then use to connect to it, 
such as Apple's iTunes, Banshee, Rhythmbox or Amarok.


%package -n %name-daemon
Summary:     Application to publish music on lan, using DAAP, daemon part
Group:      Networking/File transfer

%description -n %name-daemon
Tangerine is an application that allows you to publish music over the 
local network, using DAAP, based on Zeroconf. 

There are several clients that you can then use to connect to it, 
such as Apple's iTunes, Banshee, Rhythmbox or Amarok.

This package only contains the daemon, suitable to be run without a 
graphical interface.

%prep
%setup -q

%build
%configure
# parallel build broken 
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="Network" \
  --add-category="X-MandrivaLinux-Internet-FileTransfer" \
  --add-category="FileTransfer" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

rm -f $RPM_BUILD_ROOT/%_libdir/%name/*.la
rm -f $RPM_BUILD_ROOT/%_libdir/%name/*.a
rm -f $RPM_BUILD_ROOT/%_libdir/pkgconfig/%name.pc

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root) 
%doc README AUTHORS  
%_bindir/%name-properties
%_prefix/lib/%name/%name-properties.exe*
%_datadir/applications/%name-properties.desktop
%_datadir/icons/hicolor/*/apps/%name.*

%files -n %name-daemon
%defattr(-,root,root) 
%_bindir/%name
%_prefix/lib/%name/
%_libdir/%name/
%exclude %_prefix/lib/%name/%name-properties.exe*


