Name:       waylandpp
Version:    0.2.4
Release:    1%{?dist}
Summary:    Wayland C++ bindings.

License:    BSD-2-Clause
URL:        https://github.com/NilsBrause/waylandpp
Source0:    ${name}-${version}.tar.bz2

BuildRequires: cmake
BuildRequires: wayland-egl-devel

%package devel
Summary: waylandpp development files
%description devel
waylandpp development files

%description
Wayland C++ bindings.
 
%prep
%autosetup -p1 -n ${name}-${version}/upstream

%build
%cmake
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/libwayland-cursor++.so.0.2
%{_libdir}/libwayland-egl++.so.0.2
%{_libdir}/libwayland-client-extra++.so.0.2
%{_libdir}/libwayland-client++.so.0.2

%files devel
%defattr(-,root,root,-)
%{_bindir}/wayland-scanner++
%{_libdir}/libwayland-egl++.so
%{_libdir}/libwayland-client-extra++.so
%{_libdir}/libwayland-client++.so
%{_libdir}/pkgconfig/wayland-client++.pc
%{_libdir}/pkgconfig/wayland-scanner++.pc
%{_libdir}/pkgconfig/wayland-egl++.pc
%{_libdir}/pkgconfig/wayland-cursor++.pc
%{_libdir}/pkgconfig/wayland-client-extra++.pc
%{_libdir}/libwayland-cursor++.so
%{_includedir}/wayland-cursor.hpp
%{_includedir}/wayland-client.hpp
%{_includedir}/wayland-version.hpp
%{_includedir}/wayland-client-protocol.hpp
%{_includedir}/wayland-util.hpp
%{_includedir}/wayland-client-protocol-extra.hpp
%{_includedir}/wayland-egl.hpp
%{_datadir}/waylandpp/protocols/input-timestamps-unstable-v1.xml
%{_datadir}/waylandpp/protocols/tablet-unstable-v1.xml
%{_datadir}/waylandpp/protocols/xdg-shell.xml
%{_datadir}/waylandpp/protocols/text-input-unstable-v1.xml
%{_datadir}/waylandpp/protocols/xdg-output-unstable-v1.xml
%{_datadir}/waylandpp/protocols/xdg-shell-unstable-v6.xml
%{_datadir}/waylandpp/protocols/primary-selection-unstable-v1.xml
%{_datadir}/waylandpp/protocols/input-method-unstable-v1.xml
%{_datadir}/waylandpp/protocols/linux-dmabuf-unstable-v1.xml
%{_datadir}/waylandpp/protocols/viewporter.xml
%{_datadir}/waylandpp/protocols/presentation-time.xml
%{_datadir}/waylandpp/protocols/tablet-unstable-v2.xml
%{_datadir}/waylandpp/protocols/idle-inhibit-unstable-v1.xml
%{_datadir}/waylandpp/protocols/pointer-constraints-unstable-v1.xml
%{_datadir}/waylandpp/protocols/fullscreen-shell-unstable-v1.xml
%{_datadir}/waylandpp/protocols/xwayland-keyboard-grab-unstable-v1.xml
%{_datadir}/waylandpp/protocols/wayland.xml
%{_datadir}/waylandpp/protocols/linux-explicit-synchronization-unstable-v1.xml
%{_datadir}/waylandpp/protocols/relative-pointer-unstable-v1.xml
%{_datadir}/waylandpp/protocols/keyboard-shortcuts-inhibit-unstable-v1.xml
%{_datadir}/waylandpp/protocols/xdg-decoration-unstable-v1.xml
%{_datadir}/waylandpp/protocols/xdg-foreign-unstable-v1.xml
%{_datadir}/waylandpp/protocols/xdg-foreign-unstable-v2.xml
%{_datadir}/waylandpp/protocols/pointer-gestures-unstable-v1.xml
%{_datadir}/waylandpp/protocols/text-input-unstable-v3.xml

