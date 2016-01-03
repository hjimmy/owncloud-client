#
# spec file for package neocloud-client
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           neocloud-client
Version:        1.6.2
Release:        21
License:        GPL-2.0+
Summary:        The ownCloud Client - Private file sync and share client based on Mirall
Url:            https://github.com/owncloud/mirall 
Group:          Productivity/Networking/Other
Source0:        mirall-%{version}.tar.bz2
%if 0%{?rhel_version} || 0%{?centos_version} || 0%{?suse_version} == 1110
#Source1:        neocloud.sh
#Patch1:         autostart_use_wrapper.diff
%endif
#Patch2:         man1.diff
#Patch3:		0001-add-owncloud-client-autologin.patch
#Patch4:		0001-translate-owncloud-client.patch
#Patch5:         0001-modify-OwnCloud-tags.patch
#Patch6:         0001-change-owncloud-tags-and-pictures-to-neocloud.patch 

%if 0%{?rhel_version} || 0%{?centos_version} || 0%{?suse_version} == 1110
%if 0%{?suse_version} == 1110
# SLES 11 calls make_install makeinstall
%define make_install %{makeinstall}
%endif
# We need a more recent, prefixed Qt for SLE11
%define qtprefix opt-
%define _prefix /opt/qt-4.8
%define cmake_args -DCMAKE_INCLUDE_PATH=%{_prefix}/include -DCMAKE_LIBRARY_PATH=%{_prefix}/%{_lib} -DNEON_INCLUDE_DIRS=/opt/neon-0.30.0/include/ -DNEON_LIBRARIES=/opt/neon-0.30.0/%{_lib}/libneon.so.27 -DCMAKE_INSTALL_SYSCONFDIR=/opt/etc/ownCloud -DSYSCONF_INSTALL_DIR=/opt/etc/ownCloud -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=TRUE
%else
%define qtprefix %{nil}
%define cmake_args -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} -DSYSCONF_INSTALL_DIR=%{_sysconfdir} 
%endif

# default to have no docs. Cannot be built with old distros.
%define have_doc 0

BuildRequires:  cmake >= 2.8.11
BuildRequires:  gcc gcc-c++
BuildRequires:  %{qtprefix}libqtkeychain-devel

%if 0%{?fedora_version}
BuildRequires:  qt qt-devel >= 4.7
BuildRequires:  inetd desktop-file-utils
BuildRequires:  qtwebkit >= 2.2
BuildRequires:  qtwebkit-devel >= 2.2
%endif

%if 0%{?suse_version}
BuildRequires:  libneon-devel
BuildRequires:  update-desktop-files
%endif

%if 0%{?fedora_version}
BuildRequires:  python-sphinx
%endif

%if 0%{?rhel_version} || 0%{?centos_version} || 0%{?suse_version} == 1110
BuildRequires:  oc-neon-devel
%else
BuildRequires:  neon-devel
%define have_doc 1
%endif

%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  sqlite-devel
BuildRequires:  inetd desktop-file-utils
%else
BuildRequires:  python-sphinx
BuildRequires:  sqlite-devel
BuildRequires:  neon-devel
#BuildRequires:  update-desktop-files
%endif

%if 0%{?suse_version} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  %{qtprefix}qt-devel >= 4.7
BuildRequires:  %{qtprefix}libQtWebKit-devel
BuildRequires:  %{qtprefix}libQtWebKit4
%else
BuildRequires:  qt-devel >= 4.7
%endif

%if 0%{?rhel_version} || 0%{?centos_version} || 0%{?suse_version} == 1110
Requires:       %{qtprefix}qt-x11
# libQtWebKit4 is implicitly pulled by libneocloudsync0
Requires:       %{qtprefix}libQtWebKit4		
# qt-sql is implicitly pulled by qt-sql-sqlite
Requires:       %{qtprefix}qt-sql		
Requires:       oc-neon
%endif

%if 0%{?suse_version}
Requires: 	%{qtprefix}qt-sql-sqlite
%endif

%if  0%{?fedora_version} 
Requires: 	%{qtprefix}qt-sqlite
%endif


Requires: %{name}-l10n
Requires: libneocloudsync0 = %{version}

Obsoletes: libocsync0
Obsoletes: libocsync-devel
Obsoletes: libocsync-plugin-neocloud
Obsoletes: libocsync-devel-doc
Obsoletes: libocsync-doc

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The ownCloud client based on Mirall - github.com/owncloud/mirall

ownCloud client enables you to connect to your private
ownCloud Server. With it you can create folders in your home
directory, and keep the contents of those folders synced with your
ownCloud server. Simply copy a file into the directory and the 
ownCloud Client does the rest.

ownCloud gives your employees anytime, anywhere access to the files
they need to get the job done, whether through this desktop application, 
our mobile apps, the web interface, or other WebDAV clients. With it, 
your employees can easily view and share documents and information 
critical to the business, in a secure, flexible and controlled 
architecture. You can easily extend ownCloud with plug-ins from the 
community, or that you build yourself to meet the requirements of 
your infrastructure and business.

ownCloud - Your Cloud, Your Data, Your Way!  www.owncloud.com

Authors
=======
Duncan Mac-Vicar P. <duncan@kde.org>
Klaas Freitag <freitag@owncloud.com>
Daniel Molkentin <danimo@owncloud.com>
 
%package -n %{name}-doc
Summary:        Documentation for ownCloud Client
Group:          Development/Libraries/C and C++
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}-doc
Documentation about the ownCloud Client desktop application.

%package -n %{name}-l10n
Summary:        Localisation for ownCloud Client
Group:          Development/Libraries/C and C++
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}-l10n
Localisation files for the ownCloud Client desktop application.

%package -n libneocloudsync0

Requires:       %{qtprefix}libqtkeychain0 >= 0.3

Summary:        The ownCloud sync library
Group:          Development/Libraries/C and C++

%description -n libneocloudsync0
The ownCloud client sync library.

%package -n libneocloudsync-devel
Summary:        Development files for ownClouds sync library
Group:          Development/Libraries/C and C++
Requires: libneocloudsync0 = %{version}

%description -n libneocloudsync-devel
Development files for the ownCloud client sync library.

%prep
%setup -q -n mirall-%{version}
%if 0%{?rhel_version} || 0%{?centos_version} || 0%{?suse_version} == 1110
# autostart_use_wrapper.diff
#%patch1 -p1
%endif
# man1.diff
#%patch2 -p0
#%patch3 -p2
#%patch4 -p2
#%patch5 -p2
#%patch6 -p2

%build
export LD_LIBRARY_PATH=%{_prefix}/lib64
export PATH=%{_prefix}/bin:$PATH

mkdir build
pushd build
# http://www.cmake.org/Wiki/CMake_RPATH_handling#Default_RPATH_settings
cmake .. -DCMAKE_INSTALL_PREFIX=%{_prefix:/usr} -DWITH_DOC=TRUE \
  -DCMAKE_C_FLAGS:STRING="%{-g -O2}" \
  -DCMAKE_CXX_FLAGS:STRING="%{-g -O2}" \
  -DCMAKE_SKIP_RPATH=OFF  \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DCMAKE_DOC_INSTALL_PATH=%{_docdir}/ocsync \
%if %{_lib} == lib64
  -DLIB_SUFFIX=64 \
%endif
  %cmake_args

# documentation here?
if [ -e conf.py ];
then
  # for old cmake versions we need to move the conf.py.
  mv conf.py doc/
fi

make %{?_smp_mflags} VERBOSE=1

make doc
popd

%install
pushd build
%make_install

if [ %{have_doc} != 0 ];
then
  mkdir -p ${RPM_BUILD_ROOT}%{_docdir}/%{name}
  mv ${RPM_BUILD_ROOT}/usr/share/doc/mirall/* ${RPM_BUILD_ROOT}%{_docdir}/%{name}
  rmdir ${RPM_BUILD_ROOT}/usr/share/doc/mirall
  rm ${RPM_BUILD_ROOT}%{_docdir}/%{name}/html/unthemed/.buildinfo
  mv ${RPM_BUILD_ROOT}%{_docdir}/%{name}/html/unthemed/* ${RPM_BUILD_ROOT}%{_docdir}/%{name}/html/
  rmdir ${RPM_BUILD_ROOT}%{_docdir}/%{name}/html/unthemed

  ## obsoleted by man1.diff -- we need the man pages at correct locations also for debianoid packages. 
  ## jw@owncloud.com
  # mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
  # mv ${RPM_BUILD_ROOT}/usr/share/man/man/* ${RPM_BUILD_ROOT}%{_mandir}/man1
fi
popd

if [ -d ${RPM_BUILD_ROOT}%{_mandir}/man1 ]; then
  gzip ${RPM_BUILD_ROOT}%{_mandir}/man1/*.1
fi
%if 0%{?rhel_version} || 0%{?centos_version} || 0%{?suse_version} == 1110

mkdir -p $RPM_BUILD_ROOT/usr/share/applications/
cat $RPM_BUILD_ROOT%{_datadir}/applications/neocloud.desktop |sed "s,Exec=.*,Exec=/usr/bin/neocloud," > $RPM_BUILD_ROOT/usr/share/applications/neocloud.desktop
# rm $RPM_BUILD_ROOT%{_datadir}/applications/owncloud.desktop
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor
mv $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/* $RPM_BUILD_ROOT/usr/share/icons/hicolor
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/usr/bin/neocloud
%endif

%if %{?suse_version:1}0
%suse_update_desktop_file -n neocloud
%endif

%if 0%{?fedora_version}
%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%post -n libneocloudsync0
/sbin/ldconfig

%postun -n libneocloudsync0
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/neocloud
%{_bindir}/neocloudcmd
%{_datadir}/applications/neocloud.desktop
%{_datadir}/icons/hicolor
%if 0%{have_doc}
%{_mandir}/man1/owncloud*
%endif

%if 0%{?suse_version} == 1110
# needed for SLES11 SP3. Not sure why all others can do without...
%{_prefix}/share/*
%dir /opt/etc
%endif

%if 0%{?rhel_version} || 0%{?centos_version} || 0%{?suse_version} == 1110
%config /opt/etc/neoCloud
%else
%config /etc/neoCloud
%endif

%if 0%{?rhel_version} || 0%{?centos_version} || 0%{?suse_version} == 1110
/usr/share/icons/hicolor
/usr/share/applications/neocloud.desktop
/usr/bin/neocloud
%endif

%files -n %{name}-doc
%defattr(-,root,root,-)
%doc README.md COPYING
%if 0%{have_doc}
%doc %{_docdir}/%{name}
%endif

%files -n %{name}-l10n
%defattr(-,root,root,-)
%{_datadir}/neocloud

%files -n libneocloudsync0
%defattr(-,root,root,-)
%{_libdir}/libneocloudsync.so.*
%dir %{_libdir}/neocloud
%{_libdir}/neocloud/libocsync.so.*

%files -n libneocloudsync-devel
%defattr(-,root,root,-)
%{_libdir}/libneocloudsync.so
%{_libdir}/libhttpbf.a
%{_libdir}/neocloud/libocsync.so
%{_includedir}/neocloudsync/
%{_includedir}/httpbf.h

%changelog
* Wed Dec 24 2014 jian.hou<jian.hou@cs2c.com.cn> - 1.6.2-21
- fix bug 37407,drop message box

* Fri Dec 19 2014 jian.hou<jian.hou@cs2c.com.cn> - 1.6.2-20
- avoid _reply =0x0 cause neocloud-client crash

* Wed Dec 17 2014 jian.hou<jian.hou@cs2c.com.cn> - 1.6.2-19
- change disconnect error info for avoid mess code

* Fri Dec 12 2014 jian.hou<jian.hou@cs2c.com.cn> - 1.6.2-18
- fix bug about button(next) and translation

* Tue Dec 02 2014 jian.hou<jian.hou@cs2c.com.cn> - 1.6.2-17
- translate remove all file translation

* Fri Nov 28 2014 jian.hou<jian.hou@cs2c.com.cn> - 1.6.2-16
- translate tags while error status

* Tue Nov 25 2014 jian.hou<jian.hou@cs2c.com.cn> - 1.6.2-15
- fix bug 36536,36900,36903,37069 translation and the neoCloud link wizard
  folder directory separator error

* Tue Nov 11 2014 jian.hou<jian.hou@cs2c.com.cn> - 1.6.2-14
- translate  english tags to chinese

* Tue Oct 28 2014 jian.hou<jian.hou@cs2c.com.cn> - 1.6.2-13
- fix bug 36540 add Quick Launch Shortcut

* Thu Oct 16 2014 jian.hou<jian.hou@cs2c.com.cn> - 1.6.2-12
- change owncloud desktop icon

* Thu Oct 16 2014 jian.hou<jian.hou@cs2c.com.cn> - 1.6.2-11
- change owncloud tags and pictures to neocloud

* Thu Oct 16 2014 jian.hou<jian.hou@cs2c.com.cn> - 1.6.2-10
- translate owncloud client

* Sat Oct 11 2014 jian.hou<jian.hou@cs2c.com.cn> - 1.6.2-9
- add owncloud client autologin

* Thu Sep 18 2014 jian.hou<jian.hou@cs2c.com.cn> - 1.6.2-8
- modify owncloud-client buildrequires and cmake parameters for nkwin.

* Tue Sep 09 2014 jian.hou <jian.hou@cs2c.com.cn> - 1.6.2-7
- modify OwnCloud tags

* Thu Jul 31 2014 jw@owncloud.com
- fixed specfile syntax
* Wed Jul 30 2014 jw@owncloud.com
- fixed https://github.com/owncloud/mirall/issues/1573 (again).
  Not sure why daniomo's original fix from obs revision 41 got lost.
* Wed Jul 30 2014 jw@owncloud.com
- Re-added lost dependency:
  Requires: qt-sql-sqlite
  This is apparently not detected by autoreqprov. Sigh.
- Compressing man pages with gzip.
- Summary always capitalized.
* Tue Jul 29 2014 jw@owncloud.com
- Fix build for SLE11-SP3
* Tue Jul 29 2014 jw@owncloud.com
- Fixed https://github.com/owncloud/mirall/issues/2004 (both, rpm and deb)
- added backport to make neon happy with only OpenSSL 1.0.0 available for xUbuntu 12.04 LTS
* Mon Jul 28 2014 freitag@owncloud.com
  Update to new release 1.6.2:
  * Limit the HTTP buffer size when downloading to limit memory consumption.
  * Another small mem leak fixed in HTTP Credentials.
  * Fix local file name clash detection for MacOSX.
  * Limit maximum wait time to ten seconds in network limiting.
  * Fix data corruption while trying to resume and the server does
  not support it.
  * HTTP Credentials: Read password from legacy place if not found.
  * Shibboleth: Fix the waiting curser that would not disapear (#1915)
  * Limit memory usage to avoid mem wasting and crashes
  * Propagator: Fix crash when logging out during upload (#1957)
  * Propagator_qnam: Fix signal slot connection (#1963)
  * Use more elaborated way to detect that the server was reconfigured (#1948)
  * Setup Wizard: Reconfigure Server also if local path was changed (#1948)
* Wed Jul  2 2014 freitag@owncloud.com
- Fix rpath setting for CentOS 6
* Tue Jul  1 2014 jw@owncloud.com
  * Fixed debian.control to require libqtchain >= 0.3 instead of
  >= 0.20140128, this should fix
  https://github.com/owncloud/mirall/issues/1907 and
  https://github.com/owncloud/mirall/issues/1910
  * Rename subpackage libowncloudsync-dev to owncloudsync-dev
* Thu Jun 26 2014 freitag@owncloud.com
  * Fix 'precondition failed' bug with broken upload
  * Fix openSSL problems for windows deployment
  * Fix syncing a folder with '#' in the name
  * Fix #1845: do not update parent directory etag before sub
  directories are removed
  * Fix reappearing directories if dirs are removed during its
  upload
  * Fix app version in settings dialog, General tab
  * Fix crash in FolderWizard when going offline
  * Shibboleth fixes
  * More specific error messages (file remove during upload, open
  local sync file)
  * Use QSet rather than QHash in SyncEngine (save memory)
  * Fix some memory leaks
  * Fix some thread race problems, ie. wait for neon thread to finish
  before the propagator is shut down
  * Fix a lot of issues and warnings found by Coverity
  * Fix Mac some settings dialog problems
* Tue Jun 17 2014 jw@owncloud.com
- +BuildRequires:  cmake >= 2.8.11
  This was an unversioned dependency, but failed on centos, which had 2.6.x.y
* Thu Jun  5 2014 freitag@owncloud.com
- Changed build dependency to use libneon not depending on gnutls
  but rather on openssl.
* Fri May 30 2014 danimo@owncloud.com
  version 1.6.0 (release 2014-05-30 )
  * Minor GUI improvements
  * Qt5 compile issues fixed
  * Ignore sync log file in filewatcher
  * Install libocsync to private library dir and use rpath to localize
  * Fix reconnect after server disconnect
  * Fix "unknown action" display in Activity window
  * Fix memory leaks
  * Respect XDG_CONFIG_HOME environment var
  * Handle empty fileids in the journal correctly
  * Add abilility to compile libowncloudsync without GUI dependendy
  * Fix SSL error with previously-expired CAs on Windows
  * Fix incorrect folder pause state after start
  * Fix a couple of actual potential crashes
  * Improve Cookie support (e.g. for cookie-based load-balancers)
  * Introduce a general timeout of 300s for network operations
  * Improve error handling, blacklisting
  * Job-based change propagation, enables faster parallel up/downloads
  (right now only if no bandwidth limit is set and no proxy is used)
  * Significantly reduced CPU load when checking for local and remote changes
  * Speed up file stat code on Windows
  * Enforce Qt5 for Windows and Mac OS X builds
  * Improved owncloudcmd: SSL support, documentation
  * Added advanced logging of operations (file .???.log in sync
  directory)
  * Avoid creating a temporary copy of the sync database (.ctmp)
  * Enable support for TLS 1.2 negotiation on platforms that use
  Qt 5.2 or later
  * Forward server exception messages to client error messages
  * Mac OS X: Support Notification Center in OS X 10.8+
  * Mac OS X: Use native settings dialog
  * Mac OS X: Fix UI inconsistencies on Mavericks
  * Shibboleth: Warn if authenticating with a different user
  * Remove vio abstraction in csync
  * Avoid data loss when a client file system is not case sensitive
* Mon Mar 10 2014 freitag@owncloud.com
  version 1.5.3 (release 2014-03-10 )
  * Fix usage of proxies after first sync run (#1502, #1524, #1459, #1521)
  * Do not wipe the credentials from config for reconnect (#1499, #1503)
  * Do not erase the full account config if an old version of the client stored
    the password (related to above)
  * Fix layout of the network tab (fixes #1491)
  * Handle authentication requests by a Shibboleth IdP
  * Shibboleth: If no connection is available, don't open the login window
  * [Packaging] Debian/Ubuntu: ship sync-exclude.lst
  * [Packaging] Fix issues with access to gnome keychain in Fedora and RHEL6
  * [Packaging] Ensure all sub packages get updated
  * [Packaging] Fix incorrect path in desktop file (RHEL6/CentOS6)
* Thu Mar  6 2014 freitag@owncloud.com
- Use proper qtprefix for libqtkeychain dependency
* Tue Mar  4 2014 freitag@owncloud.com
- Let the desktop file point to /usr/bin/owncloud
* Tue Mar  4 2014 freitag@owncloud.com
- Depend on explicit version of libqtkeychain for debian.
* Tue Mar  4 2014 freitag@owncloud.com
- Depend on explicit version numbers of libowncloudsync and
  libqtkeychain
* Wed Feb 26 2014 danimo@owncloud.com
- version 1.5.2 (release 2014-02-26 )
  * Fix behavior when attempting to rename Shared folder
  * Fix potential endless sync loops on Mac OS (#1463)
  * Fix potential crash when pausing during update phase (#1442)
  * Fix handing of shared directories
  * Fix online state handling (#1441, #1459)
  * Fix potential crash in c_iconv on Mac OS
  * Fix certificate chain display in SSLButton
  * Fix sporadicly appearing multiple auth prompts on sign-in
  * Show correct state icon in Account Settings right away
  * Re-fetch content that gets deleted from read only shared directories
  * Do not store the password in the config file, erase existing ones (#1469)
  * Shibboleth: Close browser window after login
  * Shibboleth: Proper invalidation if timeout during sync
  * Shibboleth: Do not pop up IdP login immediately when modifying account
  * Shibboleth: Avoid auth on restart by storing cookies in the wallet
  * Fix license headers
* Fri Feb 14 2014 danimo@owncloud.com
- version 1.5.1 (release 2014-02-14 )
  * Added an auto updater that updates the client if a
    more recent version was found automatically (Windows, Mac OS X)
  * Added a button to the account dialog that gives information
    about the encryption layer used for communication, plus a
    certificate information widget
  * Preserve the permission settings of local files rather than
    setting them to a default (Bug #820)
  * Handle windows lnk files correctly (Bug #1307)
  * Detect removes and renames in read only shares and
    restore the gone away files. (Bug #1386)
  * Fixes sign in/sign out and password dialog. (Bug #1353)
  * Fixed error messages (Bug #1394)
  * Lots of fixes for building with Qt5
  * Changes to network limits are now also applied during a
    sync run
  * Fixed mem leak after via valgrind on Mac
  * Imported the ocsync library into miralls repository.
    Adopted all build systems and packaging to that.
  * Introduce a new linux packaging scheme following the
    debian upstream scheme
  * Use a refactored Linux file system watcher based on
    inotify, incl. unit tests
  * Wizard: Gracefully fall back to HTTP if HTTPS connection
    fails, issuing a warning
  * Fixed translation misses in the propagator
  * Fixes in proxy configuration
  * Fixes in sync journal handling
  * Fix the upload progress if the local source is still
    changing when the upload begins.
  * Add proxy support to owncloud commandline client
  * NSIS fixes
  * A lot of other fixes and minor improvements
  * Improve Qt5 compatability
* Mon Jan 20 2014 freitag@owncloud.com
- Added /etc/ownCloud to file install list (debian builds)
* Thu Dec 12 2013 freitag@owncloud.com
- version 1.5.0 (release 2013-12-12 ), csync 0.91.4 required
  * New owncloud propagator that skips the vio abstraction layer
  * Add owncloudcmd to replace the ocsync command line tool
  * Localize Windows installer
  * Allow to sign in and out
  * Ask for password if missing
  * Introduce activity view
  * Introduce black list for files which could not be synced
  * Enabling accessbility by shipping accessibility enables on OS X (#736)
  * Toggle Settings window when clicking on systray icon on Win and KDE (#896)
  * FolderWizard: Sanitize error detection (#1201)
  * Set proper enable state of blacklist button after the dialog was opened
  * Set proper tooltips in blacklist
  * Translatable error messages for file errors
  * Add man page for owncloudcmd (#1234)
  * Don't close setup wizard when the initial sync run is started
  * Close the sync journal if a folder gets removed (#1252)
  * Activity: Avoid horizontal scrollbar (#1213)
  * Fix crash (#1229)
  * Resize wizard appropriately (#1130)
  * Fix account identity test (#1231)
  * Maintain the file type correctly
  * Display rename-target in sync protocol action column
  * Let recursive removal also remove the top dir
  * If item is a directory, remove its contents from the database as well (#1257)
  * Install headers for owncloudsync library
  * Fix opening the explorer with a selected file in Windows (#1249)
  * Add build number into versioning scheme
  * Windows: Fix rename of temporary files
  * Windows: Fix move file operation
* Mon Oct 21 2013 freitag@owncloud.com
  * Update to final 1.4.2 tarball
  * Do not show the warning icon in the tray (#944)
  * Fix manual proxy support when switching (#1016)
  * Add folder column to detailed sync protocol (#1037)
  * Fix possible endless loop in inotify (#1041)
  * Do not elide the progress text (#1049)
  * Fix high CPU load (#1073)
  * Reconnect if network is unavailable after startup (#1080)
  * Ensure paused folder stays paused when syncing with more than one folder (#1083)
  * Don't show desktop notification when the user doesn't want to (#1093)
  * System tray: Avoid quick flickering up of the ok-icon for the sync prepare state
  * Progress: Do not show progress if nothing is transmitted
  * Progress: Show number of deletes.
  * Fix pause/resume behaviour (#1105)
* Mon Oct  7 2013 danimo@owncloud.com
- RHEL/SLE: Add /usr/bin/owncloud as wrapper where needed, fix autostart
* Mon Oct  7 2013 danimo@owncloud.com
- Reintroduce support for SLE 11 SP2/3, RHEL/CentOS 6
* Thu Sep 26 2013 freitag@owncloud.com
- Removed not longer needed patch.
* Thu Sep 26 2013 freitag@owncloud.com
  * Update to final 1.4.1 tarball.
  * Fixed app name for ownCloud.
  * Translation and documentation fixes.
  * Fixed error display in settings/status dialog, displays multi
    line error messages now correctly.
  * Wait up to 30 secs before complaining about missing systray
    Fixes bug #949
  * Fixed utf8 issues with basic auth authentication, fixes bug #941
  * Fixed remote folder selector, avoid recursive syncing, fixes bug #962
  * Handle and display network problems at startup correctly.
  * Enable and disable the folder watcher during syncs correctly.
  * Fix setting of thread priority.
  * Fixed file size display.
  * Fixed various folder wizard issues, bug #992
  * Made "Sync started" message optional, fixes bug #934
  * Fixed shutdown, avoid crashed config on win32, fixes bug #945
  * Pop up config wizard if no server url is configured, fixes bug #1018
  * Settings: calculate sidebar width dynamically, fixes bug #1020
  * Fixed a crash if sync folders were removed, fixes bug #713
  * Do proper resync after network disconnect, fixes bug #1007
  * Various minor code fixes
* Thu Sep  5 2013 freitag@owncloud.com
- increment build number.
* Thu Sep  5 2013 freitag@owncloud.com
- Added fix translation patch for mirall.
* Thu Sep  5 2013 freitag@owncloud.com
- Fixed runtime dependency version for libocsync
* Wed Sep  4 2013 freitag@owncloud.com
- added some tweaks from the nightly build meta files.
* Wed Sep  4 2013 danimo@owncloud.com
- release of ownCloud Client 1.4.0
  * New Scheduler: Only sync when there are actual changes in the server
  * Add a Settings Dialog, move Proxy Settings there
  * Transform folder Status Dialog into Account Settings, provide feedback via
  * context menu
  * Add Bandwidth Control
  * Add a visual storage/quota indicator (context menu and account settings)
  * Add progress indication (context menu and account settings)
  * Introduce a sync history, persisting results across syncs
  * Move ability to switch to mono icons from a switch to a Settings option
  * Add "Launch on System Startup" GUI option
  * Add "Show Desktop Nofications"GUI option (enabled by default)
    top optionally disable sync notifications
  * Add Help item, pointing to online reference
  * Implement graphical selection of remote folders in FolderWizard
  * Allow custom ignore patterns
  * Add an editor for ingore patterns
  * ALlow to flag certain ignore patterns as discardable
  * Ensure to ship with all valid translations
  * Progress Dialog now preserves the last syncned items across sync runs
  * Split Setup Wizard into multiple pages again
  * Implement "--logfile -" to log to stdout
  * Add preliminary support for Shibboleth authentication
  * Linux: Provide more icon sizes
  * Linux: Do not trigger notifier on ignored files
  * Windows: Reduce priority of CSync thread
  * Documentation: Prem. updates to reflect UI changes
  * Significant code refactorings
  * Require Qt 4.7
  * Known issue: Under certain conditions, a file will only get uploaded after
    up to five minutes
* Tue Jun 25 2013 danimo@owncloud.com
- release of ownCloud Client 1.3.0
  * Default proxy port to 8080
  * Don't lose proxy settings when changing passwords
  * Support SOCKS5 proxy (useful in combination with ssh -D)
  * Propagate proxy changes to csync at runtime
  * Improve proxy wizard
  * Display proxy errors
  * Solved problems with lock files
  * Warn if for some reason all files are scheduled for removal on either side
  * Avoid infinite loop if authentication fails in certain cases
  * Fix reading the password from the config in certain cases
  * Do not crash when configured sync target disappears
  * Make --help work on windows
  * Make sync feedback less ambiguous.
  * Fix icon tray tooltip sometimes showing repeated content
  * More use of native directory separators on Windows
  * Remove journal when reusing a directory that used to have a journal before
  * Visual clean up of status dialog items
  * Wizard: When changing the URL or user name, allow the user to push his data
    to the new location or wipe the folder and start from scratch
  * Wizard: Make setting a custom folder as a sync target work again
  * Fix application icon
  * User-Agent now contains "Mozilla/5.0" and the Platform name (for
  * firewall/proxy compat)
  * Server side directory moves will be detected
  * New setup wizard, defaulting to root syncing (only for new setups)
  * Improved thread stop/termination
* Mon Apr 22 2013 danimo@owncloud.com
- release of ownCloud Client 1.2.5
  * [Fixes] NSIS installer fixes
  * [Fixes] Fix crash race by making certificateChain() thread safe
  * [Fixes] Build with older CMake versions (CentOS/RHEL 6)
  * [Fixes] Wording in GUI
  * [Fixes] Silently ignore "installed = true" status.php
  * Set log verbosity before calling csync_init.
  * GUI feedback for the statistics copy action
  * Safer approach for detecting duplicate sync runs
* Fri Apr 12 2013 danimo@owncloud.com
- Move debian files out of tar ball
* Thu Apr 11 2013 danimo@owncloud.com
- Force explicit dependency for RH/Fedora
* Thu Apr 11 2013 danimo@owncloud.com
- release of ownCloud Client 1.2.4
  * [Fixes] Clarify string in folder wizard
  * [Fixes] Fixed some valgrind warnings
  * [Fixes] Ensure that only one sync thread can ever run
  * [Fixes] Fix default config storage path
  * [Fixes] Skip folders with no absolute path
  * [Fixes] Allow setting the configuration directory on command line
* Tue Apr  2 2013 freitag@owncloud.com
- Fixed specfile, really use version 1.2.3
* Tue Apr  2 2013 freitag@owncloud.com
- release of ownCloud Client 1.2.3
  * [Fixes] Unbreak self-signed certificate handling
* Tue Apr  2 2013 freitag@owncloud.com
- release of ownCloud Client 1.2.2
  * [Fixes] Do not crash when local file tree contains symlinks
  * [Fixes] Correctly handle locked files on Windows
  * [Fixes] Display errors in all members of the SSL chain
  * [Fixes] Enable Accessibility features on Windows
  * [Fixes] Make setupFavLink work properly on Mac OS
  * [Fixes] Ignore temporary files created by MS Office
  * [Gui] Support Nautilus in setupFavLink
* Thu Feb 28 2013 freitag@owncloud.com
- specfile cleanup: Source1 removed, github url added.
* Tue Feb 26 2013 freitag@owncloud.com
- correct version in spec file.
* Tue Feb 26 2013 freitag@owncloud.com
- release of ownCloud Client 1.2.1
  * [Fixes] Leave configured folders on configuration changes.
  * [Fixes] Do not allow to finish the setup dialog if connection can't be established.
  * [Fixes] Better handling of credentials in setup dialog.
  * [Fixes] Do not leak fd's to /dev/null when using gnutls
  * [Fixes] Stop sync scheduling when configuration wizard starts.
  * [Fixes] Clear pending network requests when stepping back in config wizard.
  * [Fixes] User password dialog asynchronous issues.
  * [Fixes] Make folderman starting and stoping the scheduling.
  * [Fixes] Various minor fixes and cleanups.
  * [Fixes] Crash on pausing sync
  * [Fixes] Stale lock file after pausing sync
  * [App] Load translations from app dir or bundle as well.
  * [Platform] Build fixes and simplifications, ie. build only one lib.
  * [Platform] Added some getter/setters for configuration values.
  * [Platform] Added man pages.
  * [Platform] Simplified/fixed credential store usage and custom configs.
  * [Platform] Added soname version to libowncloudsync.
  * [Platform] Pull in Qt translations
  * [Gui]  Make sync result popups less annoyingq
  * [Gui] Fix for result popup
  csync version 0.70.4
  * [Win32] Ship with up-to-date openssl version to fix SSL problems we saw
  * [Fixes] Fix crash during mkdir
  * [Fixes] Added workaround for problem that server sometimes does not
    respond properly to PROPFIND (mirall#285)
  * [Fixes] Fix handling of deletion of non empty or locked directories.
  * [Fixes] Fixed some potential memory leaks
  * [Fixes] Files with filenames with unix extensions are ignored now.
* Thu Feb 21 2013 freitag@owncloud.com
- release of ownCloud Client 1.2.1RC1
* Wed Feb 20 2013 freitag@owncloud.com
- copy over from :devel to :devel:daily.
* Sun Feb  3 2013 freitag@owncloud.com
- Remved extra installed desktop file from deb packages, comes out
  of the source package now.
* Wed Jan 23 2013 freitag@owncloud.com
- Update to version 1.2.0, ocsync 0.70.3 required.
  * [GUI] New status dialog to show a detailed list of synced files.
  * [GUI] New tray notifications about synced files.
  * [GUI] New platform specific icon set.
  * [App] Using cross platform QtKeychain library to store credentials crypted.
  * [App] Use cross platform notification for changes in the local file system rather than regular poll.
  * [Fixes] Improved SSL Certificate handling and SSL fixes troughout syncing.
  * [Fixes] Fixed proxy authentication.
  * [Fixes] Allow brackets in folder name alias.
  * [Fixes] Lots of other minor fixes.
  * [Platform] cmake fixes.
  * [Platform] Improved, more detailed error reporting.
* Thu Jan 17 2013 freitag@owncloud.com
- Fix deb build.
* Thu Jan 17 2013 freitag@owncloud.com
- Fixed building with package desktop file.
* Thu Jan 17 2013 freitag@owncloud.com
- Update to second beta version of 1.2.0
* Fri Dec 21 2012 freitag@owncloud.com
- Update to first beta version of 1.2.0
* Thu Nov 22 2012 freitag@owncloud.com
  version 1.1.2rc (release 2012-11-22), csync 0.60.2 required
  * [Fixes] Allow to properly cancel the password dialog.
  * [Fixes] Share folder name correctly percent encoded with old Qt
    4.6 builds ie. Debian.
  * [Fixes] If local sync dir is not existing, create it.
  * [Fixes] lots of other minor fixes.
  * [GUI] Display error messages in status dialog.
  * [GUI] GUI fixes for the connection wizard.
  * [GUI] Show username for connection in statusdialog.
  * [GUI] Show intro wizard on new connection setup.
  * [APP] Use CredentialStore to better support various credential
    backends.
  * [APP] Handle missing local folder more robust: Create it if
    missing instead of ignoring.
  * [APP] Simplify treewalk code.
  * [Platform] Fix Mac building
* Thu Oct 18 2012 danimo@owncloud.com 
- /etc/owncloud -> /etc/ownCloud
* Thu Oct 18 2012 danimo@owncloud.com 
  version 1.1.1 (release 2012-10-18), csync 0.60.1 required
  * [GUI]   Allow changing folder name in single folder mode
  * [GUI]   Windows: Add license to installer
  * [GUI]   owncloud --logwindow will bring up the log window
    in an already running instance
  * [Fixes] Make sure SSL errors are always handled
  * [Fixes] Allow special characters in folder alias
  * [Fixes] Proper workaround for Menu bug in Ubuntu
  * [Fixes] csync: Fix improper memory cleanup which could
    cause memory leaks and crashes
  * [Fixes] csync: Fix memory leak
  * [Fixes] csync: Allow single quote (') in file names
  * [Fixes] csync: Remove stray temporary files
* Wed Oct 10 2012 freitag@owncloud.com
  version 1.1.0 (release 2012-10-10 ), ocsync 0.60.0 required
  * 
  * [GUI]   Added an about dialog
  * [GUI]   Improved themeing capabilities of the client.
  * [GUI]   Minor fixes in folder assistant.
  * [GUI]   Reworked tray context menu.
  * [GUI]   Users can now sync the server root folder.
  * [Fixes] Proxy support: now supports Proxy Auto-Configuration (PAC)
    on Windows, reliability fixes across all OSes.
  * [Fixes] Url entry field in setup assistant handles http/https correctly.
  * [Fixes] Button enable state in status dialog.
  * [Fixes] Crash fixed on ending the client, tray icon related.
  * [Fixes] Crash through wrong delete operator.
  * [MacOS] behave correctly on retina displays.
  * [MacOS] fix focus policy.
  * [MacOS] Packaging improvements.
  * [MacOS] Packaging improvements.
  * [Platform] Windows: Setup closes client prior to uninstall.
  * [Platform] Windows: ownCloud gets added to autorun by default.
  * [Platform] insert correct version info from cmake.
  * [Platform] csync conf file and database were moved to the users app data
    directory, away from the .csync dir.
  * Renamed exclude.lst to sync-exclude.lst and moved it to
    /etc/appName()/ for more clean packaging. From the user path,
    still exclude.lst is read if sync-exclude.lst is not existing.
  * Placed custom.ini with customization options to /etc/appName()
* Fri Oct  5 2012 freitag@owncloud.com
- Update to v1.1.0beta3 - ocsync 0.50.11 needed
* Thu Sep 20 2012 freitag@owncloud.com
- Update to v1.1.0beta2 - csync 0.50.10 needed
* Fri Aug 31 2012 msrex@owncloud.com
- Update to v1.1.0beta1 - csync 0.50.9 needed
  Required ownCloud v4.5 on the server side
* Tue Aug 14 2012 freitag@owncloud.com
- version 1.0.5 (release 2012-08-14), csync 0.50.8 required
  * [Fixes] Fixed setup dialog: Really use https if checkbox is activated.
* Mon Aug 13 2012 freitag@owncloud.com
- do not remove the unneeded libmirallsync.so to satisfy automatic
  dependency tracking.
* Fri Aug 10 2012 freitag@owncloud.com
- version 1.0.4 (release 2012-08-10), csync 0.50.8 required
  * [APP] ownCloud is now a single instance app, can not start twice any more.
  * [APP] Proxy support
  * [APP] Handle HTTP redirection correctly, note new url.
  * [APP] More relaxed handling of read only directories in the sync paths.
  * [APP] Started to split off a library with sync functionality, eg for KDE
  * [APP] Make ownCloud Info class a singleton, more robust.
  * [GUI] New, simplified connection wizard.
  * [GUI] Added ability for customized theming.
  * [GUI] Improved icon size handling.
  * [GUI] Removed Log Window Button, log available through command line.
  * [GUI] Proxy configuration dialog added.
  * [GUI] Added Translations to languages Slovenian, Polish, Catalan,
    Portuguese (Brazil), German, Greek, Spanish, Czech, Italian, Slovak,
    French, Russian, Japanese, Swedish, Portuguese (Portugal)
    all with translation rate >90%%.
  * [Fixes] Loading of self signed certs into Networkmanager (#oc-843)
  * [Fixes] Win32: Handle SSL dll loading correctly.
  * [Fixes] Many other small fixes and improvements.
* Wed Jul 18 2012 freitag@owncloud.com
- Fixed version in the desktop file
* Fri Jun 22 2012 freitag@owncloud.com
- version 1.0.3 (release 2012-06-19), csync 0.50.7 required
  * [GUI] Added a log window which catches the logging if required and
    allows to save for information.
  * [CMI] Added options --help, --logfile and --logflush
  * [APP] Allow to specify sync frequency in the config file.
  * [Fixes] Do not use csync database files from a sync before.
  * [Fixes] In Connection wizard, write the final config onyl if
    the user really accepted. Also remove the former database.
  * [Fixes] Allow special characters in the sync directory names
  * [Fixes] Win32: Fixed directory removal with special character dirs.
  * [Fixes] MacOS: Do not flood the system log any more
  * [Fixes] MacOS: Put app translations to correct places
  * [Fixes] Win32: Fix loading of csync state db.
  * [Fixes] Improved some english grammar.
  * [Platform] Added krazy2 static code checks.
* Wed May 16 2012 freitag@owncloud.com
- version 1.0.2 (release 18.5.2012), csync 0.50.6 required
  * [GUI] New icon set for ownCloud client
  * [GUI] No splashscreen any more (oC Bug #498)
  * [GUI] Russian translation added
  * [GUI] Added 'open ownCloud' to traymenu
  * [GUI] "Pause" and "Resume" instead of Enable/Disable
  * [Fixes] Long running syncs can be interrupted now.
  * [Fixes] Dialogs comes to front on click
  * [Fixes] Open local sync folder from tray and status for win32
  * [Fixes] Load exclude.lst correctly on MacOSX
* Fri May 11 2012 freitag@owncloud.com
- updated tarball to beta of next release 1.0.2
* Thu May 10 2012 msrex@owncloud.com
- updated debian dependencies around time syncing
* Tue May  1 2012 msrex@owncloud.com
- Correct installation of .desktop file in debian
* Fri Apr 20 2012 msrex@owncloud.com
- change dependencies again on non-SUSE platforms
* Thu Apr 19 2012 msrex@owncloud.com
- fix dependency for libiniparser on non-SUSE platforms
* Wed Apr 18 2012 freitag@opensuse.org
- version 1.0.1 (release 2012-04-18), csync 0.50.5 required
  * [Security] Support SSL Connections
  * [Security] SSL Warning dialog
  * [Security] Do not store password in clear text anymore
  * [Security] Restrict credentials to the configured host
  * [Security] Added ability to forbid local password storage.
  * [Fixes] Various fixes of the startup behaviour.
  * [Fixes] Various fixes in sync status display
  * [GUI] Various error messages for user display improved.
  * [GUI] fixed terms and Translations
  * [GUI] fixed translation loading
  * [Intern] Migrate old credentials to new format
  * [Intern] Some code refactorings, got rid of rotten QWebDav lib
  * [Intern] lots of cmake cleanups
  * [Platform] MacOSX porting efforts
  * [Platform] MacOSX Bundle creation added
  * [Platform] Enabled ranslations on Windows.
* Wed Apr 18 2012 msrex@owncloud.com
- fix typo in debian dependencies
* Wed Apr 18 2012 msrex@owncloud.com
- more debian / ubuntu packaging
* Wed Apr 18 2012 msrex@owncloud.com
- add debian / ubuntu packaging
* Tue Apr  3 2012 freitag@opensuse.org
- removed requirement on rubygem, not needed for this client.
* Mon Apr  2 2012 msrex@suse.de
- change minimum csync version required
* Mon Apr  2 2012 freitag@opensuse.org
- update to version 1.0.0
* Sun Apr  1 2012 msrex@owncloud.com
- renamed package mirall to owncloud-client
- new descriptions
