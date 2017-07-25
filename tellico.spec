Summary:	A collection manager
Name:		tellico
Version:	3.0.2
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Databases
URL:		http://tellico-project.org/
Source0:	http://www.tellico-project.org/files/%{name}-%{version}.tar.xz
Requires:	kdebase5runtime
Requires:	kdelibs5-core
Requires:	libKF5Libkdepim
BuildRequires:	qjson
BuildRequires:	qjson-devel
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:	libKF5Libkdepim-devel
#BuildRequires:	libkcddb5-devel
BuildRequires:	libkcompactdisc-devel
BuildRequires:	pkgconfig(libksane)
BuildRequires:	libKF5KDELibs4Support-devel
BuildRequires:	exempi-devel
BuildRequires:	pkgconfig(libexslt)
BuildRequires:	imagemagick
BuildRequires:	taglib-devel
BuildRequires:	pkgconfig(poppler-qt5)
BuildRequires:	yaz-devel >= 3.0
BuildRequires:  qimageblitz-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	qt5-macros
BuildRequires:	qt5-devel
#BuildRequires:	libqt5test-devel
BuildRequires:	libKF5Html-devel
BuildRequires:	libKF5JS-devel
BuildRequires:	kjs
BuildRequires:	libKF5FileMetaData-devel
#BuildRequires:	libKF5NewStuff-devel
BuildRequires:	libKF5Sane-devel
BuildRequires:	libdiscid-devel

%description
Tellico is a collection manager for KDE. It includes default collections for
books, bibliographies, comic books, videos, music, coins, stamps, trading
cards, and wines, and also allows custom collections. Unlimited user-defined
fields are allowed. Filters are available to limit the visible entries by
definable criteria. Full customization for printing is possible through
editing the default XSLT file. It can import CSV, Bibtex, and Bibtexml and
export CSV, HTML, Bibtex, Bibtexml, and PilotDB. Entries may be imported
directly from different web services such as amazon.com.

%files -f %{name}.lang
%defattr (-,root,root)
%doc AUTHORS ChangeLog
%{_kde5_bindir}/%{name}
%{_kde5_sysconfdir}/xdg/*
%{_kde5_datadir}/applications/org.kde.tellico.desktop
%{_kde5_datadir}/mime/packages/tellico.xml
%{_kde5_datadir}/config.kcfg/tellico_config.kcfg
%{_kde5_iconsdir}/hicolor/*/*/*.png
%{_kde5_datadir}/tellico/*.xsl
%{_kde5_datadir}/tellico/*.png
%{_kde5_datadir}/tellico/*.xml
%{_kde5_datadir}/tellico/*.dtd
%{_kde5_datadir}/tellico/*.tips
%{_kde5_datadir}/tellico/*.cfg
%{_kde5_datadir}/tellico/*.html
%{_kde5_datadir}/tellico/*.js
%{_kde5_datadir}/tellico/pics/*
%{_kde5_datadir}/tellico/entry-templates/*
%{_kde5_datadir}/tellico/data-sources/*
%{_kde5_datadir}/tellico/report-templates/*
%{_kde5_datadir}/kconf_update/*
%{_kde5_xmlguidir}/tellico/tellicoui.rc
%{_kde5_datadir}/metainfo/org.kde.tellico.appdata.xml


#--------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --with-html

