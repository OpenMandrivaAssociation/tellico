Summary:	A collection manager
Name:		tellico
Version:	2.3.8
Release:	2
Epoch:		3
License:	GPLv2+
Group:		Databases
URL:		http://tellico-project.org/
Source0:	http://www.tellico-project.org/files/%{name}-%{version}.tar.bz2
Requires:	kdebase4-runtime
Requires:	kdelibs4-core
%if %{mdvver} < 201200
Requires:	kdemultimedia4
%endif
Requires:	kdepimlibs4-core
BuildRequires:	qjson
BuildRequires:	qjson-devel
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:	kdepimlibs4-devel
%if %{mdvver} < 201200
BuildRequires:	kdemultimedia4-devel
%else
BuildRequires:	libkcddb-devel
BuildRequires:	libkcompactdisc-devel
%endif
BuildRequires:	pkgconfig(libksane)
BuildRequires:	kdelibs4-devel
BuildRequires:	exempi-devel
BuildRequires:	pkgconfig(libexslt)
BuildRequires:	imagemagick
BuildRequires:	taglib-devel
BuildRequires:	pkgconfig(poppler-qt4)
BuildRequires:	yaz-devel >= 3.0
BuildRequires:  qimageblitz-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	kde4-macros
BuildRequires:	qt4-devel
Obsoletes:	bookcase
Provides:	bookcase

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
%makeinstall_std -C build

%find_lang %{name} --with-html

