Summary:	A collection manager
Name:		tellico
Version:		4.2.1
Release:	1
Epoch:	3
License:	GPLv2+
Group:	Databases
Url:		https://tellico-project.org/
Source0:	https://tellico-project.org/download-tellico/%{name}-%{version}.tar.xz
Patch0: tellico-4.2-fix-shebangs.patch
BuildRequires:	cmake >= 3.16
BuildRequires:	make
BuildRequires:	extra-cmake-modules >= 5.19
BuildRequires:	gettext
BuildRequires:	imagemagick
BuildRequires:	qt6-cmake
BuildRequires:cmake(kcddb6)
BuildRequires:cmake(kcompactdisc6)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6ColorScheme)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6FileMetaData)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KSaneCore6)
BuildRequires:	cmake(KSaneWidgets6)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6Sonnet)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KPim6Libkdepim)
# Not provided yet
#BuildRequires:	yaz-devel
BuildRequires:	pkgconfig(cups)
BuildRequires:	pkgconfig(exempi-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libdiscid)
BuildRequires:	pkgconfig(libv4l1) >= 0.8.3
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(poppler-qt6)
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(Qt6Charts)
BuildRequires:	pkgconfig(Qt6Core) >= 6.4.0
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6PrintSupport)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6WebEngineWidgets)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Xml)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
#Requires:	kdebase5runtime
#Requires:	kdelibs5-core
#Requires:	libKF5Libkdepim
Requires(post,postun):	desktop-file-utils

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
%doc AUTHORS ChangeLog
%{_sysconfdir}/xdg/tellicorc
%{_bindir}/%{name}
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/config.kcfg/%{name}_config.kcfg
%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_datadir}/mime/packages/%{name}.xml
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/mimetypes/application-x-%{name}.png
%{_datadir}/tellico/*.xsl
%{_datadir}/tellico/*.png
%{_datadir}/tellico/*.xml
#{_kde5_datadir}/tellico/*.dtd
#{_kde5_datadir}/tellico/*.tips
%{_datadir}/tellico/*.cfg
%{_datadir}/tellico/*.html
%{_datadir}/tellico/*.js
%{_datadir}/tellico/pics/*
%{_datadir}/tellico/entry-templates/*
%{_datadir}/tellico/data-sources/*
%{_datadir}/tellico/report-templates/*
%{_datadir}/kconf_update/*
%{_datadir}/knsrcfiles/*.knsrc
#{_kde5_xmlguidir}/tellico/tellicoui.rc

#--------------------------------------------------------------------

%prep
%autosetup -p1


%build
%cmake -DBUILD_WITH_QT6=ON \
				-DENABLE_WEBCAM=ON \
				-DENABLE_BTPARSE=ON
%make_build


%install
%make_install -C build

%find_lang %{name} --with-html

