%define iconname %{name}.png

Summary:	A book collection manager
Name:		tellico
Version:	1.2.12
Release:	%mkrel 1
Epoch:		1
License:	GPL
Group:		Databases
URL:		http://www.periapsis.org/tellico
Source:		http://www.periapsis.org/tellico/download/%{name}-%{version}.tar.bz2
Patch1:		%{name}-1.2.12-yaz.patch
Requires:	kdebase
Requires:	kdemultimedia-kscd
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:	kdelibs-devel 
BuildRequires:	libxslt-devel >= 1.0.19
BuildRequires:	imagemagick
BuildRequires:	chrpath
BuildRequires:	taglib-devel
BuildRequires:	libkdemultimedia-common-devel
BuildRequires:	kdepim-devel
BuildRequires:	libcdda-devel
BuildRequires:	yaz-devel >= 3.0
BuildRequires:	tcp_wrappers-devel 
Obsoletes:	bookcase
Provides:	bookcase
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot

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
%setup -q
%patch1 -p1 

%build 

%configure2_5x \
	--disable-debug \
	--disable-rpath \
	--with-xinerama \
	--enable-pch \
	--enable-new-ldflags \
	--enable-final \
	%if "%{_lib}" != "lib"
	--enable-libsuffix="%(A=%{_lib}; echo ${A/lib/})" \
	%endif
	--enable-nmcheck
	

%make

%install
rm -rf %{buildroot}

%makeinstall_std
chrpath -d %{buildroot}%{_bindir}/*

%find_lang %{name}

%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor

%clean 
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr (-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL TODO
%doc %dir %{_datadir}/doc/HTML/*/tellico/*
%{_bindir}/%{name}
%{_datadir}/applications/kde/tellico.desktop
%{_datadir}/mimelnk/application/x-tellico.desktop 
%{_datadir}/apps/%{name}/
%{_datadir}/apps/kconf_update/tellico-rename.upd
%{_datadir}/apps/kconf_update/tellico.upd
%{_datadir}/config.kcfg/tellico_config.kcfg
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/mimetypes/*.png
