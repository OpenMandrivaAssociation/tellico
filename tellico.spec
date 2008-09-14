%define iconname %{name}.png

Summary:	A book collection manager
Name:		tellico
Version:	1.3.4
Release:	%mkrel 1
Epoch:		1
License:	GPLv2+
Group:		Databases
URL:		http://www.periapsis.org/tellico
Source:		http://www.periapsis.org/tellico/download/%{name}-%{version}.tar.gz
Source1:	admin.tar.bz2
Patch0:		tellico-1.3-releaseflaws.patch
Requires:	kdebase
Requires:	kdemultimedia-kscd
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:	kdelibs-devel 
BuildRequires:	libxslt-devel >= 1.0.19
BuildRequires:	imagemagick
BuildRequires:	icu-devel
BuildRequires:	chrpath
BuildRequires:	taglib-devel
BuildRequires:	kdemultimedia3-devel
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
%setup -q -a1
%patch0 -p0

%build
make -f admin/Makefile.common
%configure_kde3 --disable-final
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name} --with-html

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%update_mime_database
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%clean_mime_database
%endif

%clean 
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr (-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL TODO
%{_kde3_bindir}/%{name}
%{_kde3_datadir}/applications/kde/tellico.desktop
%{_kde3_datadir}/mimelnk/application/x-tellico.desktop
%{_kde3_datadir}/mime/packages/tellico.xml
%{_kde3_datadir}/apps/%{name}
%{_kde3_datadir}/apps/kconf_update/*
%{_kde3_datadir}/config.kcfg/tellico_config.kcfg
%{_kde3_datadir}/config/tellicorc
%{_kde3_iconsdir}/hicolor/*/*/*.png
%{_kde3_iconsdir}/hicolor/*/*/*/*.png
