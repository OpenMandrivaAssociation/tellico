Summary:	A collection manager
Name:		tellico
Version:	2.3.6
Release:	4
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
BuildRequires:	libpoppler-qt4-devel
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
BuildRequires:	libpoppler-qt4-devel
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


%changelog
* Tue Jul 24 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 3:2.3.6-1mdv2012.0
+ Revision: 810972
- update to 2.3.6

* Tue Jan 17 2012 Bruno Cornec <bcornec@mandriva.org> 3:2.3.5-1
+ Revision: 761852
- Update tellico to upstream 2.3.5

* Tue Oct 11 2011 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 3:2.3.4-2
+ Revision: 704140
- Remove kdegraphics4-devel to see the new header needed

  + Bruno Cornec <bcornec@mandriva.org>
    - Add a patch which fixes wrong booleans handling in 2.3.4 (from the 2.3.5 tree)
    - Update to upstream 2.3.4

* Mon Apr 11 2011 Funda Wang <fwang@mandriva.org> 3:2.3.3-1
+ Revision: 652614
- update to new version 2.3.3

* Tue Dec 14 2010 Bruno Cornec <bcornec@mandriva.org> 3:2.3.2-1mdv2011.0
+ Revision: 620686
- Update tellico to upstream 2.3.2

* Thu Nov 11 2010 Bruno Cornec <bcornec@mandriva.org> 3:2.3.1-2mdv2011.0
+ Revision: 596275
- Fix an upstream bug by backporting pach 1195446 - http://websvn.kde.org/trunk/extragear/office/tellico/src/detailedlistview.cpp?r1=1195446&r2=1195445&pathrev=1195446&view=patch

* Sun Nov 07 2010 Bruno Cornec <bcornec@mandriva.org> 3:2.3.1-1mdv2011.0
+ Revision: 594751
- Update to tellico upstream 2.3.1
- Update to tellico upstream 2.3.1

* Fri Aug 13 2010 Bruno Cornec <bcornec@mandriva.org> 3:2.3-5mdv2011.0
+ Revision: 569427
- Remove useless qjson dep

* Fri Aug 13 2010 Bruno Cornec <bcornec@mandriva.org> 3:2.3-4mdv2011.0
+ Revision: 569421
- Adds json as a build requirement
- Adds qjson support for tellico

* Mon Aug 09 2010 Funda Wang <fwang@mandriva.org> 3:2.3-2mdv2011.0
+ Revision: 567831
- those requires do not need to list, as it is satisfied through binary deps.

  + Bruno Cornec <bcornec@mandriva.org>
    - Updated to upstream 2.3
    - Dependencies increased to have most of the functions

* Sat Feb 20 2010 Funda Wang <fwang@mandriva.org> 3:2.2-2mdv2011.0
+ Revision: 508680
- update URL

* Sat Feb 20 2010 Funda Wang <fwang@mandriva.org> 3:2.2-2mdv2010.1
+ Revision: 508646
- rebuild

* Sun Feb 14 2010 Funda Wang <fwang@mandriva.org> 3:2.2-1mdv2010.1
+ Revision: 505858
- new version 2.2

* Sat Nov 21 2009 Funda Wang <fwang@mandriva.org> 3:2.1.1-1mdv2010.1
+ Revision: 467824
- new version 2.1.1

* Thu Nov 12 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3:2.1-2mdv2010.1
+ Revision: 465472
- rebuild

* Sun Nov 08 2009 Frederik Himpe <fhimpe@mandriva.org> 3:2.1-1mdv2010.1
+ Revision: 462842
- Update to new version 2.1
- Fix description and summary, based on Fedora's

* Tue Oct 20 2009 Funda Wang <fwang@mandriva.org> 3:2.0-2mdv2010.0
+ Revision: 458425
- add more BRs to fix bug#53964

* Mon Sep 21 2009 Funda Wang <fwang@mandriva.org> 3:2.0-1mdv2010.0
+ Revision: 446534
- New version 2.0 final

* Tue Sep 01 2009 Bruno Cornec <bcornec@mandriva.org> 2:2.0pre2-1mdv2010.0
+ Revision: 424040
- Fix Version string to allow for repsys/mdvsys to work
- Updated to 2.0pre2

* Sat Aug 22 2009 Funda Wang <fwang@mandriva.org> 2:2.0-0.pre1.1mdv2010.0
+ Revision: 419447
- adjust version schema
- add more BRs

* Fri Aug 21 2009 Bruno Cornec <bcornec@mandriva.org> 1:2.0pre1-1mdv2010.0
+ Revision: 418994
- Update to upstream 2.0pre1

* Wed Jul 01 2009 Bruno Cornec <bcornec@mandriva.org> 1:1.9-0.989364.2mdv2010.0
+ Revision: 391152
- Update to 1.9.989364 svn upstream (fix CD import)

* Mon Jun 29 2009 Bruno Cornec <bcornec@mandriva.org> 1:1.9-0.988370.2mdv2010.0
+ Revision: 390442
- Update to SVN rev 988370 (Fix Empty entries as first in the list)

* Sun Jun 14 2009 Bruno Cornec <bcornec@mandriva.org> 1:1.9-0.981656.2mdv2010.0
+ Revision: 385855
- Update to SVN version 981656 (fixes CD direct import via CDDB)

* Fri Jun 12 2009 Bruno Cornec <bcornec@mandriva.org> 1:1.9-0.980523.2mdv2010.0
+ Revision: 385318
- Update tellico to SVN 980523

* Fri May 29 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1:1.9-0.974359.2mdv2010.0
+ Revision: 380930
- increase release
- Remove merged patches
- New snapshot

* Sat Mar 07 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1:1.9-0.936109.4mdv2009.1
+ Revision: 351484
- Fix deps

* Sat Mar 07 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1:1.9-0.936109.3mdv2009.1
+ Revision: 350987
- Addd BuildRequire
- Fix patch
- Update to kde4 version

* Thu Nov 27 2008 Funda Wang <fwang@mandriva.org> 1:1.3.4-2mdv2009.1
+ Revision: 307201
- drop kde app dep

* Wed Sep 24 2008 Funda Wang <fwang@mandriva.org> 1:1.3.4-2mdv2009.0
+ Revision: 287687
- rebuild with poppler-qt3

* Sun Sep 14 2008 Funda Wang <fwang@mandriva.org> 1:1.3.4-1mdv2009.0
+ Revision: 284746
- update patch and file list
- update admin dir with kde 3.5.10
- add gentoo patch to fix building
- New version 1.3.4
- New version 1.3.3
- New version 1.3.2.1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Feb 01 2008 Funda Wang <fwang@mandriva.org> 1:1.3-1mdv2008.1
+ Revision: 161041
- BR poppler
- BR icu
- New version 1.3

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.2.14-1mdv2008.0
+ Revision: 93972
- fix file list
- new version

* Tue Jul 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.2.13-1mdv2008.0
+ Revision: 57018
- drop patch 1, as it is fixed upstream
- new version

* Sat Jul 14 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.2.12-1mdv2008.0
+ Revision: 52022
- new version
- provide patch 1 (compiles against yaz > 3)
- drop old menu style
- fix file list

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against new yaz libs


* Mon Feb 05 2007 Lenny Cartier <lenny@mandriva.com> 1.2.8-1mdv2007.0
+ Revision: 116501
- Update to 1.2.8

* Thu Dec 07 2006 Lenny Cartier <lenny@mandriva.com> 1:1.2.7-1mdv2007.1
+ Revision: 91931
- Update to 1.2.6

  + Nicolas LÃ©cureuil <neoclust@mandriva.org>
    - New version 1.2.6
    - import tellico-1.2.3-1mdv2007.0

* Tue Sep 26 2006 Charles A Edwards <eslrahc@mandriva.org> 1:1.2.3-1mdv2007.0
- 1.2.2

* Sat Sep 09 2006 Charles A Edwards <eslrahc@mandriva.org> 1:1.2.1-1mdv2007.0
- 1.2.2 (bugfix release for the bugfix release)

* Fri Sep 08 2006 Charles A Edwards <eslrahc@mandriva.org> 1:1.2.1-1mdv2007.0
- 1.2.1 (bugfix release)

* Sat Sep 02 2006 Charles A Edwards <eslrahc@mandriva.org> 1:1.2-1mdv2007.0
- 1.2 final

* Tue Aug 22 2006 Charles A Edwards <eslrahc@mandriva.org> 1:1.2-0.1pre3mdv2007.0
- 1.2pre3
- adjust BR and R
- add desktop patch to change exec
- don't rm buildroot in prep
- use  post postun database marco and icon cache

* Wed May 31 2006 Charles A Edwards <eslrahc@mandriva.org> 1.1.6-4mdv2007.0
- leave the major off the BR

* Tue May 30 2006 Charles A Edwards <eslrahc@mandriva.org> 1.1.6-3mdv2007.0
- fix requires
- add cddb support

* Tue May 30 2006 Charles A Edwards <eslrahc@mandriva.org> 1.1.6-2mdv2007.0
- use mkrel
- Put all collection mgrs Databases

* Wed May 10 2006 Lenny Cartier <lenny@mandriva.com> 1.1.6-1mdk
- 1.1.6

* Fri Apr 21 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.1.5-1mdk
- New release 1.1.5

* Wed Apr 05 2006 Lenny Cartier <lenny@mandriva.com> 1.1.4-1mdk
- 1.1.4

* Mon Mar 13 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.1.3-1mdk
- New release 1.1.3

* Mon Mar 06 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.1.2-1mdk
- New release 1.1.2

* Tue Feb 28 2006 Jerome quelin <jquelin@gmail.com> 1.1.1-1mdk
- 1.1.1

* Wed Feb 08 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.0.3-2mdk
- fix buildrequires (#19288)

* Wed Jan 25 2006 Lenny Cartier <lenny@mandriva.com> 1.0.3-1mdk
- 1.0.3

* Tue Oct 04 2005 Lenny Cartier <lenny@mandriva.com> 1.0.2-1mdk
- 1.0.2

* Mon Oct 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.13.8-2mdk
- BuildRequires fix

* Tue Jul 05 2005 Lenny Cartier <lenny@mandriva.com> 0.13.8-1mdk
- 0.13.8

* Tue May 31 2005 Lenny Cartier <lenny@mandriva.com> 0.13.7-1mdk
- 0.13.7

* Mon Apr 11 2005 Charles A Edwards <eslrahc@mandrake.org> 0.13.6-1mdk
- 0.13.6

* Wed Mar 09 2005 Charles A Edwards <eslrahc@mandrake.org> 0.13.5-1mdk
- 0.13.5

* Mon Feb 28 2005 Charles A Edwards <eslrahc@mandrake.org> 0.13.4-1mdk
- 0.13.4

* Sat Feb 05 2005 Charles A Edwards <eslrahc@mandrake.org> 0.13.2-1mdk
- 0.13.2
- buildrequires

* Tue Jan 11 2005 Charles A Edwards <eslrahc@mandrake.org> 0.13.1-1mdk
- 0.13.1

* Wed Oct 20 2004 Charles A Edwards <eslrahc@mandrake.org> 0.12-1mdk
- Renamed to Tellico because of trademark conflict. 
  Tellico 0.12 is identical to Bookcase 0.11, except for the name change.

* Sun Sep 05 2004 Charles A Edwards <eslrahc@mandrake.org> 0.11-1mdk
- 0.11
- update feature list
- add support for CDDB and audio file metadata
- buildrequires

* Wed Aug 25 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.10-1mdk
- 0.10

* Fri Jun 25 2004 Charles A Edwards <eslrahc@bellsouth.net> 0.9.3-1mdk
- 0.9.3
- reenable libtoolize
- patch for gcc3.4

* Sun May 16 2004 Charles A Edwards <eslrahc@bellsouth.net> 0.9.1-1mdk
- 0.9.1

* Wed Apr 21 2004 Charles A Edwards <eslrahc@bellsouth.net> 0.9-1mdk
- 0.9

* Tue Apr 20 2004 Charles A Edwards <eslrahc@bellsouth.net> 0.9-0.pre1.1mdk
- 0.9pre1

* Fri Apr 02 2004 Charles A Edwards <eslrahc@bellsouth.net> 0.8.5-1mdk
- 0.8.5

* Sun Feb 22 2004 Charles A Edwards <eslrahc@bellsouth.net> 0.8.4-1mdk
- 0.8.4

* Wed Feb 11 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.8.3-2mdk
- Fix menu entry

* Sat Feb 07 2004 Charles A Edwards <eslrahc@bellsouth.net> 0.8.3-1mdk
- 0.8.3

