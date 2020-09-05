Name:       qt5-qtpim
Summary:    Qt PIM modules
Version:    5.12.7
Release:    1%{?dist}
Group:      System/Libraries
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
%if 0%{?fedora}
BuildRequires:  qt5-qtbase-private-devel
%endif
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt PIM module


%package -n qt5-qtpim-contacts
Summary:    Qt PIM Contacts
Group:      System/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-qtpim-contacts
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt PIM Contacts module


%package -n qt5-qtpim-contacts-devel
Summary:    Qt PIM - development files
Group:      Development/Libraries
Requires:   qt5-qtpim-contacts = %{version}-%{release}

%description -n qt5-qtpim-contacts-devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt PIM Contacts development files


%package -n qt5-qtdeclarative-pim-contacts
Summary:    Qt PIM Contacts import for QtDeclarative
Group:      System/Libraries
Requires:   qt5-qtdeclarative

%description -n qt5-qtdeclarative-pim-contacts
This package contains the PIM Contacts imports for QtDeclarative

%package -n qt5-qtpim-organizer
Summary:    Qt PIM Organizer
Group:      System/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-qtpim-organizer
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt PIM Organizer module


%package -n qt5-qtpim-organizer-devel
Summary:    Qt PIM - development files
Group:      Development/Libraries
Requires:   qt5-qtpim-organizer = %{version}-%{release}

%description -n qt5-qtpim-organizer-devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt PIM Organizer development files


%package -n qt5-qtdeclarative-pim-organizer
Summary:    Qt PIM Organizer import for QtDeclarative
Group:      System/Libraries
Requires:   qt5-qtdeclarative

%description -n qt5-qtdeclarative-pim-organizer
This package contains the PIM Organizer imports for QtDeclarative



%package -n qt5-qtpim-versit
Summary:    Qt PIM Versit
Group:      System/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-qtpim-versit
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt PIM Versit module


%package -n qt5-qtpim-versit-devel
Summary:    Qt PIM - development files
Group:      Development/Libraries
Requires:   qt5-qtpim-versit = %{version}-%{release}

%description -n qt5-qtpim-versit-devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt PIM Versit development files



%package -n qt5-qtpim-versitorganizer
Summary:    Qt PIM VersitOrganizer
Group:      System/Libraries
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description -n qt5-qtpim-versitorganizer
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt PIM VersitOrganizer module


%package -n qt5-qtpim-versitorganizer-devel
Summary:    Qt PIM - development files
Group:      Development/Libraries
Requires:   qt5-qtpim-versitorganizer = %{version}-%{release}

%description -n qt5-qtpim-versitorganizer-devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt PIM VersitOrganizer development files

%prep
%setup -q -n %{name}-%{version}/upstream

%build
export QTDIR=/usr/share/qt5
touch .git
%qmake5
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake_install
# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;
# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la
#Fixup modules name
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
-exec sed -i -e 's/Qt0/Qt5/' {} \;

# We don't need qt5/Qt/
rm -rf %{buildroot}/%{_includedir}/qt5/Qt

%fdupes %{buildroot}/%{_includedir}

%post -n qt5-qtpim-contacts
/sbin/ldconfig
%postun -n qt5-qtpim-contacts
/sbin/ldconfig

%post -n qt5-qtpim-organizer
/sbin/ldconfig
%postun -n qt5-qtpim-organizer
/sbin/ldconfig

%post -n qt5-qtpim-versit
/sbin/ldconfig
%postun -n qt5-qtpim-versit
/sbin/ldconfig

%post -n qt5-qtpim-versitorganizer
/sbin/ldconfig
%postun -n qt5-qtpim-versitorganizer
/sbin/ldconfig


%files -n qt5-qtpim-contacts
%defattr(-,root,root,-)
%{_libdir}/libQt5Contacts.so.0
%{_libdir}/libQt5Contacts.so.0.*
%{_libdir}/qt5/plugins/contacts/libqtcontacts_memory.so

%files -n qt5-qtpim-contacts-devel
%defattr(-,root,root,-)
%{_libdir}/libQt5Contacts.so
%{_libdir}/libQt5Contacts.prl
%{_libdir}/pkgconfig/Qt5Contacts.pc
%{_includedir}/qt5/QtContacts/
%{_libdir}/qt5/mkspecs/modules/qt_lib_contacts.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_contacts_private.pri
%{_libdir}/cmake/Qt5Contacts/

%files -n qt5-qtdeclarative-pim-contacts
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtContacts/

%files -n qt5-qtpim-organizer
%defattr(-,root,root,-)
%{_libdir}/libQt5Organizer.so.0
%{_libdir}/libQt5Organizer.so.0.*
%{_libdir}/qt5/plugins/organizer/libqtorganizer_memory.so

%files -n qt5-qtpim-organizer-devel
%defattr(-,root,root,-)
%{_libdir}/libQt5Organizer.so
%{_libdir}/libQt5Organizer.prl
%{_libdir}/pkgconfig/Qt5Organizer.pc
%{_includedir}/qt5/QtOrganizer/
%{_libdir}/qt5/mkspecs/modules/qt_lib_organizer.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_organizer_private.pri
%{_libdir}/cmake/Qt5Organizer/

%files -n qt5-qtdeclarative-pim-organizer
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtOrganizer/

%files -n qt5-qtpim-versit
%defattr(-,root,root,-)
%{_libdir}/libQt5Versit.so.0
%{_libdir}/libQt5Versit.so.0.*
%{_libdir}/qt5/plugins/versit/libqtversit_backuphandler.so
%{_libdir}/qt5/plugins/versit/libqtversit_vcardpreserver.so

%files -n qt5-qtpim-versit-devel
%defattr(-,root,root,-)
%{_libdir}/libQt5Versit.so
%{_libdir}/libQt5Versit.prl
%{_libdir}/pkgconfig/Qt5Versit.pc
%{_includedir}/qt5/QtVersit/
%{_libdir}/qt5/mkspecs/modules/qt_lib_versit.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_versit_private.pri
%{_libdir}/cmake/Qt5Versit/

%files -n qt5-qtpim-versitorganizer
%defattr(-,root,root,-)
%{_libdir}/libQt5VersitOrganizer.so.0
%{_libdir}/libQt5VersitOrganizer.so.0.*

%files -n qt5-qtpim-versitorganizer-devel
%defattr(-,root,root,-)
%{_libdir}/libQt5VersitOrganizer.so
%{_libdir}/libQt5VersitOrganizer.prl
%{_libdir}/pkgconfig/Qt5VersitOrganizer.pc
%{_includedir}/qt5/QtVersitOrganizer/
%{_libdir}/qt5/mkspecs/modules/qt_lib_versitorganizer.pri
%{_libdir}/qt5/mkspecs/modules/qt_lib_versitorganizer_private.pri
%{_libdir}/cmake/Qt5VersitOrganizer/

