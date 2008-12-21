%define name xmms-musepack
%define version 1.2.1
%define filename %name-%version
%define release %mkrel 1
%define inst_dir %_libdir/xmms/

Summary:	XMMS plugin which plays musepack encoded audio files
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD
Group:		Sound
Source:		http://musepack.origean.net/files/linux/plugins/%{filename}.tar.bz2
Url:		http://www.musepack.net/
Buildroot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	xmms-devel >= 1.2.10
BuildRequires:	libmpcdec-devel
BuildRequires:	taglib-devel

%description
This plugin for XMMS can play audio files which are encoded with Andree
Buschmann's encoder Musepack. These files have the filename postfixes mpc,
mp+ or mpp.

%prep
%setup -q -n %filename
rm -f configure
libtoolize --copy --force
aclocal
autoconf
automake

%build
%define _disable_ld_no_undefined 1
%configure2_5x
%make

%install
%makeinstall_std
rm -f %buildroot%inst_dir/Input/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc ChangeLog 
%defattr(0755,root,root,0755)
%inst_dir/Input/*.so


