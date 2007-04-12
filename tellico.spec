%define name    tellico
%define pre   %nil
%define version 1.2.8
%define release %mkrel 1
%define iconname %{name}.png


Summary: A book collection manager
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group:  Databases
Source: http://www.periapsis.org/tellico/download/%{name}-%{version}.tar.bz2
Patch0: tellico-1.2pre3-desktop.patch
URL: http://www.periapsis.org/tellico
Epoch: 1
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: kdebase
Requires: kdemultimedia-kscd
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires: kdelibs-devel libxslt-devel >= 1.0.19
BuildRequires: ImageMagick
BuildRequires: chrpath
BuildRequires: taglib-devel
BuildRequires: libkdemultimedia-common-devel kdepim-devel
BuildRequires: libcdda-devel
BuildRequires: yaz-devel
BuildRequires: tcp_wrappers-devel 
Obsoletes: bookcase
Provides: bookcase
 

%description
Tellico is a KDE application for keeping track of your book collection.

Features:

o Supports collections of books, bibliographic entries, videos, or music. 
o Supports any number of user-defined fields, of eight different types:
   o text, paragraph, list, checkbox, year, URL
   o tables of one or two columns.
o Handles books with multiple authors, genres, keywords, etc.
o Automatically formats titles and names
o Supports collection searching and view filtering
o Sorts and groups collection by various properties
o Automatically validates ISBN
o Allows customizable output through XSLT
o Imports Bibtex, Bibtexml, and CSV
o Exports to Bibtex, Bibtexml, CSV, and HTML
o Includes translations for more than nine languages, other than English
o Imports information directly from Amazon.com
   (US, Japan, Germany, and United Kingdom)
o Imports CDDB data
o Scans and imports audio file collections, such as mp3 or ogg
o Imports and exports to Alexandria libraries

%prep
 
%setup -q -n %{name}-%{version}
%patch0 -p1 

%build 

%configure2_5x --disable-debug --disable-rpath --with-xinerama 

%make

%install
rm -Rf %{buildroot} 
%makeinstall_std
chrpath -d $RPM_BUILD_ROOT/%{_bindir}/*

mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir},%{_menudir}}
convert icons/%{name}.png -geometry 48x48 %{buildroot}%{_liconsdir}/%{iconname}
convert icons/%{name}.png -geometry 32x32 %{buildroot}%{_iconsdir}/%{iconname} 
convert icons/%{name}.png -geometry 16x16 %{buildroot}%{_miconsdir}/%{iconname} 

kdedesktop2mdkmenu.pl tellico "More Applications/Databases" %buildroot/%_datadir/applications/kde/tellico.desktop                             %buildroot/%_menudir/tellico 
 
#rm  zero-length file
rm -f %buildroot/%{_datadir}/doc/HTML/*/tellico/customization.docbook

%find_lang %{name}

%post
%{update_menus}
%{update_desktop_database}
%{update_icon_cache hicolor}

%postun
%{clean_menus}
%{clean_desktop_database}
%{clean_icon_cache hicolor}

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr (-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL TODO
%doc %dir %{_datadir}/doc/HTML/*/tellico/*
%{_bindir}/* 
%{_datadir}/applications/kde/tellico.desktop
%{_datadir}/mimelnk/application/x-tellico.desktop 
%{_datadir}/apps/%{name}/
%{_datadir}/apps/kconf_update/tellico-rename.upd
%{_datadir}/apps/kconf_update/tellico.upd
%{_datadir}/config.kcfg/tellico_config.kcfg
%{_menudir}/%{name}
%{_miconsdir}/%{iconname}
%{_iconsdir}/%{iconname}
%{_liconsdir}/%{iconname}
%{_iconsdir}/*/*/*  



