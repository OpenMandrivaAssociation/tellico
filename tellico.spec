%define iconname %{name}.png

Summary:	A book collection manager
Name:		tellico
Version:	2.0
Release:	%mkrel 2
Epoch:		3
License:	GPLv2+
Group:		Databases
URL:		http://www.periapsis.org/tellico
Source:		http://www.tellico-project.org/files/%{name}-%{version}.tar.bz2
Requires:	kdebase4-runtime
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:	kdepimlibs4-devel
BuildRequires:	kdegraphics4-devel
BuildRequires:	kdemultimedia4-devel
BuildRequires:	libv4l-devel
BuildRequires:	exempi-devel
BuildRequires:	libxslt-devel >= 1.0.19
BuildRequires:	imagemagick
BuildRequires:	taglib-devel
BuildRequires:	libpoppler-qt4-devel
BuildRequires:	yaz-devel >= 3.0
BuildRequires:  qimageblitz-devel
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

%files -f %{name}.lang
%defattr (-,root,root)
%doc AUTHORS ChangeLog
%{_kde_bindir}/%{name}
%{_kde_datadir}/applications/kde4/tellico.desktop
%{_kde_datadir}/mimelnk/application/x-tellico.desktop
%{_kde_datadir}/mime/packages/tellico.xml
%{_kde_datadir}/apps/%{name}
%{_kde_datadir}/apps/kconf_update/*
%{_kde_datadir}/config.kcfg/tellico_config.kcfg
%{_kde_datadir}/config/*
%{_kde_iconsdir}/hicolor/*/*/*.png

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}

%makeinstall_std -C build

%find_lang %{name} --with-html

%clean 
rm -rf %{buildroot}
